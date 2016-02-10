Introduction
=============
This is a modified version based on the TPC-E version from Percona https://www.percona.com/blog/2010/02/08/introducing-tpce-like-workload-for-mysql/.
The package is based on the TPC-E workload described on http://www.tpc.org/tpce/default.asp
and uses EGen software provided by TPC. 

In this package SAP HANA Support was added to the TPC-E Percona version.

Installation
============
Before you can build the tool you need to install following dependencies:
- unixodbc driver
- ODBC driver for HANA (Linux)
- LLVM
- CLANG

First adjust the include path in the `makefile` in the directory `prj` to the directory with the unixodbc library / include files
on your system. Then execute the makefile by calling `make`.

Configure unixodbc
------------------
To be able to connect via ODBC to SAP HANA you have to configure unixodbc.
The default location of the `odbcinst.ini` and  `odbc.ini`  configuration files are the directory `/etc`.
Add following lines to odbcinst.ini:
```
[HDBODBC]
Description="HDBODBC Driver"
Driver=<path to HANA ODBC>/libodbcHDB.so
Setup=<path to HANA ODBC>/libodbcHDB.so
Threading = 2
```

Add following lines to odbc.ini:
```
[hana]
Description = "HANA"
Driver = HDBODBC
servernode = <IP of HANA Instance>:3<Instance Number>15
```

Usage
=====
Create Tables in SAP HANA
-------------------------
Before you execute the SQL Scripts in the directory `scripts/hana` to create the tables / foreign keys / indicies
of the TPC-E benchmark you have to adjust the name of the schema to your database. Then you can execute the SQL scripts.

Generate Test Data 
----------------------------------------
To generate Test Data you have to execute EGenLoader in the bin directory supplying the path to the `flat_in` and `flat_out` directory.
You can adjust the generator by supplying additional arguments to control the size of the generated dataset. 

Example:
```
./EGenLoader -i flat_in -o flat_out -c 2000 -t 2000 -f 200 -w 50
```

After successfull generation of the benchmark data the generated data is located in the `flat_out` directory.

Load Flatfiles into SAP HANA with hdbsql
----------------------------------------
We use the hdbsql command line tool supplied with the HANA ODBC driver to load the generated data into the SAP HANA database.
Before you can load the data into your database you have to adjust the schema name in the `scripts/hana/import_script` SQL file
and the path to the flat files accordingly.

Example:
```
SET SCHEMA <YOUR_SCHEMA_NAME>;
```

Now you can load the flatfiles into the SAP HANA database by executing following command:
```
<path_to_hdbsql_executable>/hdbsql -n <IP_HANA_INSTANCE>:3<INSTANCE_ID>15 -u <USERNAME> -p <PASSWORD> -I <PATH_TO_IMPORT_SCRIPT>/hana_csv_import.sql -c ';'
```

**Please confirm that the User used for the import has the user rights to IMPORT / INSERT data into the SCHEMA/TABLE!**

Execute TPC-E like Benchmark
-----------------------------

Known Issues
============
This project can be only compiled with CLANG / LLVM due to the usage of some deprecated system calls.


License
=======
This package based on tpc-e workload described  on http://www.tpc.org/tpce/default.asp
and uses EGen software provided by TPC.

The package is fully compatible with
TPC license
http://www.tpc.org/tpce/egen/TPC-E%20License%20Agreement.pdf

The results you get with this package
can't be named "TPC Benchmark Results"
and are not compatible or comparable with
TPC-E Benchmark results 

