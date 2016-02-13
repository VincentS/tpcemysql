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
Generate Test Data 
----------------------------------------
First you have to generate Test Data using `EGenLoader` in the bin directory supplying the path to the `flat_in` and `flat_out` directory. You can adjust the generator by supplying additional arguments to control the size of the generated dataset. 

```
./EGenLoader -i flat_in -o flat_out -c <number_of_customers> -t <active_customers> -f <number_of_customers_for_1TRTPS> -w <days_of_trade>
```


Concrete Example:
```
./EGenLoader -i flat_in -o flat_out -c 2000 -t 2000 -f 200 -w 50
```

After successfull generation of the benchmark data the generated data is located in the `flat_out` directory.

Prepare Database for Loading of the Flat Files
---------------------------------------------
First you have to create the tbales for the TPC-E like benchmark by executing the SQL script `1_create_table.sql` located in the directory `scripts/<your_database>`.

Load Flatfiles into SAP HANA with hdbsql
----------------------------------------

Before you execute can import the generated flat files you have to adjust the SQL script in the directory `scripts/<your_database>` you have to adjust the name of the schema and paths to the flat files in the file `2_load-data.sql` for the database you target.

We use the hdbsql command line tool supplied with the HANA ODBC driver to load the generated data into the SAP HANA database.
We load the flatfiles into the SAP HANA database by executing following command:
```
<path_to_hdbsql_executable>/hdbsql -n <IP_HANA_INSTANCE>:3<INSTANCE_ID>15 -u <USERNAME> -p <PASSWORD> -I <PATH_TO_IMPORT_SCRIPT>/hana_csv_import.sql -c ';'
```

**Please confirm that the User used for the import has the user rights to IMPORT / INSERT data into the SCHEMA/TABLE!**

Create FK / Indicies / ... in Database
-----------------------------------------
After successfully importing the previously generated flat_files you have to execute the remaining SQL scripts (3-6) in ascending order.
**The shell script `6_create_sequence.sql` has to be executed with the user account which executes the TPC-E benchmark **


Execute TPC-E like Benchmark
-----------------------------
To execute the Benchmark run the following command:
```
./EGenSimpleTest -c <number_of_customers> -a <active_customers> -f <number_of_customers_for_1TRTPS> -d <days_of_trade> -l <number_of_customer_load_unit> -e <path_to>/flat_in -D <name_of_data_source> -U <username> -P <password> -t <duration> -r <ramp_up> -u <number_of_users>
```
**The values <number_of_customers>,<active_customers>,<number_of_customers_for_1TRTPS>,<days_of_trade> have to be the same as used at the ./EGenLoader data generator !***

Known Issues
============
This project can be only compiled with CLANG / LLVM due to the usage of some deprecated C functions GCC seems to have an issue with.

Further Improvements
=====================
- Adjust the Benchmark using the TPC-E Changelog from 1.10 to 1.14 (Currently 1.9) and supplied Source
- Fix Compile Error when using GCC

Miscellaneous
===============
Debugging
---------
Compile the program with the argument -DDEBUG and execute the benchmark with the argument -o <directory_for_error_log> for additional debugging output.
  
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

