using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SQLite;
using System.Data;
using System.Data.Common;
using System.Windows;
using System.Text.RegularExpressions;

namespace WpfApp1
{
    internal class SQLiteHelper
    {
        public SQLiteConnection connection;
        public SQLiteHelper(string dbPath)
        {
            //初始化SQLite数据库
            if (!System.IO.File.Exists(@"sqliteGis.db"))
            {
                SQLiteConnection.CreateFile(@"sqliteGis.db");//不存在就创建文件
                connection = new SQLiteConnection($"Data Source={dbPath};Version=3;");
                string sql = "create table user ('姓名' string(20), '年龄' int)";
                SQLiteCommand command = new SQLiteCommand(sql, connection);
                connection.Open();
                command.ExecuteNonQuery();
                connection.Close();
            }
            else
            {
                connection = new SQLiteConnection($"Data Source={dbPath};Version=3;");
            }
        }
        public void Close()
        {
            connection.Close();
        }
        public void Open()
        {
            connection.Open();
        }
        public void ExecuteNonQuery(string sql)
        {
            using (SQLiteCommand command = new SQLiteCommand(sql, connection))
            {
                command.ExecuteNonQuery();
            }
        }
        public object ExecuteScalar(string sql)
        {
            using (SQLiteCommand command = new SQLiteCommand(sql, connection))
            {
                return command.ExecuteScalar();
            }
        }
        public SQLiteDataReader ExecuteReader(string sql)
        {
            using (SQLiteCommand command = new SQLiteCommand(sql, connection))
            {
                return command.ExecuteReader();
            }
        }
        public DataTable ExecuteDataTable(string sql)
        {
            using (SQLiteCommand command = new SQLiteCommand(sql, connection))
            {
                using (SQLiteDataAdapter adapter = new SQLiteDataAdapter(command))
                {
                    DataTable dataTable = new DataTable();
                    adapter.Fill(dataTable);
                    return dataTable;
                }
            }
        }

        //Grid
        public static string ConnSqlLiteDbPath = string.Empty;
        public static string ConnString
        {
            get
            {
                return string.Format(@"Data Source={0}", ConnSqlLiteDbPath);
            }
        }
        //输出SQLite
        public int ExecuteMutliQuery(string commandText, DataTable dtData)
        {
            int res = 0;
            if (connection.State == ConnectionState.Closed)
                connection.Open();
            using (SQLiteTransaction dbTrans = connection.BeginTransaction())
            {
                try
                {
                    foreach (DataRow row in dtData.Rows)
                    {
                        res += ExecuteNonSqlQuery(dbTrans, commandText, row.ItemArray);
                    }
                    dbTrans.Commit();
                }
                catch (Exception ex)
                {
                    res = -1;
                    dbTrans.Rollback();
                    throw;
                }
                finally
                {
                    //Conn.Close();
                }
            }
            return res;
        }
        //调用方法
        public int ExecuteNonSqlQuery(SQLiteTransaction transaction, string commandText, params object[] paramList)
        {
            if (transaction == null) throw new ArgumentNullException("transaction is null");
            if (transaction != null && transaction.Connection == null) throw new ArgumentException("The transaction was rolled back or committed,please provide an open transaction.", "transaction");
            using (IDbCommand cmd = transaction.Connection.CreateCommand())
            {
                cmd.CommandText = commandText;
                AttachParameters((SQLiteCommand)cmd, cmd.CommandText, paramList);
                if (transaction.Connection.State == ConnectionState.Closed)
                    transaction.Connection.Open();
                int result = cmd.ExecuteNonQuery();
                return result;
            }
        }
        //SQLite事务
        #region AttachParameters(SQLiteCommand,commandText,object[] paramList)
        /// <summary>
        /// 增加参数到命令（自动判断类型）
        /// </summary>
        /// <param name="commandText">命令语句</param>
        /// <param name="paramList">object参数列表</param>
        /// <returns>返回SQLiteParameterCollection参数列表</returns>
        private SQLiteParameterCollection AttachParameters(SQLiteCommand cmd, string commandText, params object[] paramList)
        {
            if (paramList == null || paramList.Length == 0) return null;

            SQLiteParameterCollection coll = cmd.Parameters;
            string parmString = commandText.Substring(commandText.IndexOf("@"));
            // pre-process the string so always at least 1 space after a comma.
            parmString = parmString.Replace(",", " ,");
            // get the named parameters into a match collection
            string pattern = @"(@)\S*(.*?)\b";
            Regex ex = new Regex(pattern, RegexOptions.IgnoreCase);
            MatchCollection mc = ex.Matches(parmString);
            string[] paramNames = new string[mc.Count];
            int i = 0;
            foreach (Match m in mc)
            {
                paramNames[i] = m.Value;
                i++;
            }

            // now let's type the parameters
            int j = 0;
            Type t = null;
            foreach (object o in paramList)
            {
                t = o.GetType();

                SQLiteParameter parm = new SQLiteParameter();
                switch (t.ToString())
                {

                    case ("DBNull"):
                    case ("Char"):
                    case ("SByte"):
                    case ("UInt16"):
                    case ("UInt32"):
                    case ("UInt64"):
                        throw new SystemException("Invalid data type");


                    case ("System.String"):
                        parm.DbType = DbType.String;
                        parm.ParameterName = paramNames[j];
                        parm.Value = (string)paramList[j];
                        coll.Add(parm);
                        break;

                    case ("System.Byte[]"):
                        parm.DbType = DbType.Binary;
                        parm.ParameterName = paramNames[j];
                        parm.Value = (byte[])paramList[j];
                        coll.Add(parm);
                        break;

                    case ("System.Int32"):
                        parm.DbType = DbType.Int32;
                        parm.ParameterName = paramNames[j];
                        parm.Value = (int)paramList[j];
                        coll.Add(parm);
                        break;

                    case ("System.Int64"):
                        parm.DbType = DbType.Int32;
                        parm.ParameterName = paramNames[j];
                        parm.Value = Convert.ToInt32(paramList[j]);
                        coll.Add(parm);
                        break;

                    case ("System.Boolean"):
                        parm.DbType = DbType.Boolean;
                        parm.ParameterName = paramNames[j];
                        parm.Value = (bool)paramList[j];
                        coll.Add(parm);
                        break;

                    case ("System.DateTime"):
                        parm.DbType = DbType.DateTime;
                        parm.ParameterName = paramNames[j];
                        parm.Value = Convert.ToDateTime(paramList[j]);
                        coll.Add(parm);
                        break;

                    case ("System.Double"):
                        parm.DbType = DbType.Double;
                        parm.ParameterName = paramNames[j];
                        parm.Value = Convert.ToDouble(paramList[j]);
                        coll.Add(parm);
                        break;

                    case ("System.Single"):
                    case ("System.Decimal"):
                        parm.DbType = DbType.Decimal;
                        parm.ParameterName = paramNames[j];
                        parm.Value = Convert.ToDecimal(paramList[j]);
                        coll.Add(parm);
                        break;

                    case ("System.Guid"):
                        parm.DbType = DbType.Guid;
                        parm.ParameterName = paramNames[j];
                        parm.Value = (System.Guid)(paramList[j]);
                        coll.Add(parm);
                        break;

                    case ("System.Object"):

                        parm.DbType = DbType.Object;
                        parm.ParameterName = paramNames[j];
                        parm.Value = paramList[j];
                        coll.Add(parm);
                        break;

                    default:
                        throw new SystemException("Value is of unknown data type");

                } // end switch

                j++;
            }
            return coll;
        }
        #endregion

        // 取datatable
        public static DataTable GetDataTable(out string sError, string sSQL)
        {
            DataTable dt = null;
            sError = string.Empty;
            try
            {
                SQLiteConnection conn = new SQLiteConnection(ConnString);
                conn.Open();
                SQLiteCommand cmd = new SQLiteCommand();
                cmd.CommandText = sSQL;
                cmd.Connection = conn;
                SQLiteDataAdapter dao = new SQLiteDataAdapter(cmd);
                dt = new DataTable();
                dao.Fill(dt);
            }
            catch (Exception ex)
            {
                sError = ex.Message;
                MessageBox.Show(sError, "数据库连接异常");
            }
            return dt;
        }
        // 取某个单一的元素
        public static object GetSingle(out string sError, string sSQL)
        {
            DataTable dt = GetDataTable(out sError, sSQL);
            if (dt != null && dt.Rows.Count > 0)
            {
                return dt.Rows[0][0];
            }
            return null;
        }
        // 取最大的ID
        public static Int32 GetMaxID(out string sError, string sKeyField, string sTableName)
        {
            DataTable dt = GetDataTable(out sError, "select ifnull(max([" + sKeyField + "]),0) as MaxID from [" + sTableName + "]");
            if (dt != null && dt.Rows.Count > 0)
            {
                return Convert.ToInt32(dt.Rows[0][0].ToString());
            }
            return 0;
        }
        // 执行insert,update,delete 动作，也可以使用事务
        public static bool UpdateData(out string sError, string sSQL, bool bUseTransaction = false)
        {
            int iResult = 0;
            sError = string.Empty;
            if (!bUseTransaction)
            {
                try
                {
                    SQLiteConnection conn = new SQLiteConnection(ConnString);
                    conn.Open();
                    SQLiteCommand comm = new SQLiteCommand(conn);
                    comm.CommandText = sSQL;
                    iResult = comm.ExecuteNonQuery();
                }
                catch (Exception ex)
                {
                    sError = ex.Message;
                    iResult = -1;
                }
            }
            else // 使用事务
            {
                DbTransaction trans = null;
                try
                {
                    SQLiteConnection conn = new SQLiteConnection(ConnString);
                    conn.Open();
                    trans = conn.BeginTransaction();
                    SQLiteCommand comm = new SQLiteCommand(conn);
                    comm.CommandText = sSQL;
                    iResult = comm.ExecuteNonQuery();
                    trans.Commit();
                }
                catch (Exception ex)
                {
                    sError = ex.Message;
                    iResult = -1;
                    trans.Rollback();
                }
            }
            return iResult > 0;
        }
    }
}
