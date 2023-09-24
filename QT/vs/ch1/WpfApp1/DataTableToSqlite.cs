using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WpfApp1
{
    internal class DataTableToSqlite
    {
        public class DataTableToSQLte

        {
            private string tableName;

            public string TableName
            {
                get { return tableName; }
                set { tableName = value; }
            }
            private string insertHead;

            public string InsertHead
            {
                get { return insertHead; }
            }

            private string[] separators;

            public string[] Separators
            {
                get { return separators; }
                set { separators = value; }
            }

            private string insertCmdText;

            private int colCount;
            private string[] fields;

            public DataTableToSQLte(DataTable dt)
            {
                List<string> myFields = new List<string>();
                List<string> mySeparators = new List<string>();
                List<string> valueVars = new List<string>();// insert command text
                colCount = dt.Columns.Count;

                for (int i = 0; i < colCount; i++)
                {
                    string colName = dt.Columns[i].ColumnName;
                    myFields.Add(colName);
                    mySeparators.Add(GetSeperator(dt.Columns[i].DataType.ToString()));
                    valueVars.Add("@" + colName);
                }
                insertHead = string.Format("insert into {0} ({1})"
                    , dt.TableName
                    , string.Join(",", myFields.ToArray()));
                separators = mySeparators.ToArray();

                insertCmdText = string.Format("{0} values ({1})", insertHead
                    , string.Join(",", valueVars.ToArray()));

                fields = myFields.ToArray();

            }

            private string GetSeperator(string typeName)
            {
                string result = string.Empty;
                switch (typeName)
                {
                    case "System.String":
                        result = "'";
                        break;

                    default:
                        result = typeName;
                        break;
                }

                return result;
            }


            public string GenInsertSql(DataRow dr)
            {
                List<string> strs = new List<string>();
                for (int i = 0; i < colCount; i++)
                {
                    if (DBNull.Value == dr[i])  //null or DBNull
                        strs.Add("null");
                    else
                        strs.Add(string.Format("{0}{1}{0}", separators[i], dr[i].ToString()));
                }
                return string.Format("{0} values ({1})", insertHead, string.Join(",", strs.ToArray()));
            }

            public void ImportToSqliteBatch(DataTable dt, string dbFullName)
            {
                string strConn = string.Format("data source={0}", dbFullName);
                using (SQLiteConnection conn = new SQLiteConnection(strConn))
                {
                    using (SQLiteCommand insertCmd = conn.CreateCommand())
                    {
                        insertCmd.CommandText = insertCmdText;
                        conn.Open();
                        SQLiteTransaction tranction = conn.BeginTransaction();
                        foreach (DataRow dr in dt.Rows)
                        {
                            for (int i = 0; i < colCount; i++)
                            {
                                object o = null;
                                string paraName = "@" + fields[i];
                                if (DBNull.Value != dr[fields[i]])
                                    o = dr[fields[i]];
                                insertCmd.Parameters.AddWithValue(paraName, o);
                            }
                            insertCmd.ExecuteNonQuery();
                        }
                        tranction.Commit();
                    }
                }
            }
        }
    }
}
