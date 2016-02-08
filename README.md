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

Generate Test Data & Load into SAP HANA
----------------------------------------

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

