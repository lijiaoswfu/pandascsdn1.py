@echo off
cls
sqlite3 C:\carl\PythonExcel\pro\Geopy\arcgispro.sqlite<dboutput.sql
sqlite3 C:\carl\PythonExcel\QT\vs\ch1\WpfApp1\bin\Debug\net6.0-windows10.0.19041.0\sqliteGis.db<dbimport.sql
