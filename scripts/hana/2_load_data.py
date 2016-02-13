#!/usr/bin/env python

from __future__ import print_function
import sys
import os

sql_name = "1_load_data.sql"
sql_script = """--Select correct Schema

SET SCHEMA {1};

--Table: account_permission
IMPORT FROM CSV FILE '{0}/AccountPermission.txt' INTO "account_permission" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: customer
IMPORT FROM CSV FILE '{0}/Customer.txt' INTO "customer" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: customer_account
IMPORT FROM CSV FILE '{0}/CustomerAccount.txt' INTO "customer_account" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: customer_taxrate
IMPORT FROM CSV FILE '{0}/CustomerTaxrate.txt' INTO "customer_taxrate" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: holding
IMPORT FROM CSV FILE '{0}/flat_out/Holding.txt' INTO "holding" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: holding_history
IMPORT FROM CSV FILE '{0}/flat_out/HoldingHistory.txt' INTO "holding_history" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: holding_summary
IMPORT FROM CSV FILE '{0}/flat_out/HoldingSummary.txt' INTO "holding_summary" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: watch_item
IMPORT FROM CSV FILE '{0}/WatchItem.txt' INTO "watch_item" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: watch_list
IMPORT FROM CSV FILE '{0}/WatchList.txt' INTO "watch_list" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;


--Table: broker
IMPORT FROM CSV FILE '{0}/Broker.txt' INTO "broker" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: cash_transaction
IMPORT FROM CSV FILE '{0}/CashTransaction.txt' INTO "cash_transaction" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: charge
IMPORT FROM CSV FILE '{0}/Charge.txt' INTO "charge" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: comission_rate
IMPORT FROM CSV FILE '{0}/CommissionRate.txt' INTO "comission_rate" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: settlement
IMPORT FROM CSV FILE '{0}/Settlement.txt' INTO "settlement" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: trade
IMPORT FROM CSV FILE '{0}/Trade.txt' INTO "trade" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: trade_history
IMPORT FROM CSV FILE '{0}/TradeHistory.txt' INTO "trade_history" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: trade_request Was already commented out
--IMPORT FROM CSV FILE '{0}/TradeRequest.txt' INTO "trade_request" WITH
--RECORD DELIMITED BY '\\n'
--FIELD DELIMITED BY '|'
--FAIL ON INVALID DATA;

--Table: trade_type
IMPORT FROM CSV FILE '{0}/TradeType.txt' INTO "trade_type" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: company
IMPORT FROM CSV FILE '{0}/Company.txt' INTO "company" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: company_competitor
IMPORT FROM CSV FILE '{0}/CompanyCompetitor.txt' INTO "company_competitor" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: daily_market
IMPORT FROM CSV FILE '{0}/DailyMarket.txt' INTO "daily_market" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: exchange
IMPORT FROM CSV FILE '{0}/Exchange.txt' INTO "exchange" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: financial
IMPORT FROM CSV FILE '{0}/Financial.txt' INTO "financial" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: industry
IMPORT FROM CSV FILE '{0}/Industry.txt' INTO "industry" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: last_trade
IMPORT FROM CSV FILE '{0}/LastTrade.txt' INTO "last_trade" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: news_item
IMPORT FROM CSV FILE '{0}/NewsItem.txt' INTO "news_item" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: news_xref
IMPORT FROM CSV FILE '{0}/NewsXRef.txt' INTO "news_xref" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: sector
IMPORT FROM CSV FILE '{0}/Sector.txt' INTO "sector" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: security
IMPORT FROM CSV FILE '{0}/Security.txt' INTO "security" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: address
IMPORT FROM CSV FILE '{0}/Address.txt' INTO "address" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: status_type
IMPORT FROM CSV FILE '{0}/StatusType.txt' INTO "status_type" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: taxrate
IMPORT FROM CSV FILE '{0}/Taxrate.txt' INTO "taxrate" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: zip_code
IMPORT FROM CSV FILE '{0}/ZipCode.txt' INTO "zip_code" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;"""

def create_file(csv_file,schema):
	with open(sql_name,'w') as f:
		f.write(sql_script.format(csv_file,schema))
	
def main(argv):
	if not len(argv) == 2:
		print("Please supply the path to the directory with the files to be imported and the target schema name as parameter!\n E.g. python 1_load_data.py <path_to_folder> <schema_name>")
		sys.exit()
	csv_file = os.path.abspath(argv[0])
	print("Create SQL Script {} ...\n".format(sql_name))
	create_file(csv_file,argv[1])
	print("SQL Script {} successfull created!\n".format(sql_name))


if __name__ == "__main__":
	main(sys.argv[1:])
