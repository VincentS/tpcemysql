#!/usr/bin/env python

from __future__ import print_function
import sys
import csv
import operator as ops
import os

sql_name = "6_create_sequence.sql"


def find_max(csv_file):
	with open(csv_file) as f:
                return max(row[0] for row in csv.reader(f,delimiter='|',lineterminator='\n'))
def create_file(max_value):
	with open(sql_name,'w') as f:
		f.write("DROP SEQUENCE seq;")
		f.write("CREATE SEQUENCE seq START WITH %s NO MAXVALUE NO CYCLE;" % str(max_value))
	
def main(argv):
	if not len(argv) == 1:
		print("Please supply the path to the directory containing Trade.txt as parameter!\n E.g. python 6_create_sequence.py <path_to_folder>")
		sys.exit()
	csv_file = os.path.join( os.path.abspath(argv[0]),"Trade.txt")
	print("Create SQL Script {} ...\n".format(sql_name))
	max_value = find_max(csv_file)
	create_file(int(max_value)+1)
	print("SQL Script {} successfull created!\n".format(sql_name))


if __name__ == "__main__":
	main(sys.argv[1:])
