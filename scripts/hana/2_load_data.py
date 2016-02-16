#!/usr/bin/env python

from __future__ import print_function
import sys
import os

sql_name = "2_load_data.sql"
sql_script = """--Select correct Schema

SET SCHEMA {1};

--Table: account_permission
IMPORT FROM CSV FILE '{0}/AccountPermission.txt' INTO "ACCOUNT_PERMISSION" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: customer
IMPORT FROM CSV FILE '{0}/Customer.txt' INTO "CUSTOMER" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: customer_account
IMPORT FROM CSV FILE '{0}/CustomerAccount.txt' INTO "CUSTOMER_ACCOUNT" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: customer_taxrate
IMPORT FROM CSV FILE '{0}/CustomerTaxrate.txt' INTO "CUSTOMER_TAXRATE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: holding
IMPORT FROM CSV FILE '{0}/Holding.txt' INTO "HOLDING" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: holding_history
IMPORT FROM CSV FILE '{0}/HoldingHistory.txt' INTO "HOLDING_HISTORY" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: holding_summary
IMPORT FROM CSV FILE '{0}/HoldingSummary.txt' INTO "HOLDING_SUMMARY" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: watch_item
IMPORT FROM CSV FILE '{0}/WatchItem.txt' INTO "WATCH_ITEM" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: watch_list
IMPORT FROM CSV FILE '{0}/WatchList.txt' INTO "WATCH_LIST" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;


--Table: broker
IMPORT FROM CSV FILE '{0}/Broker.txt' INTO "BROKER" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: cash_transaction
IMPORT FROM CSV FILE '{0}/CashTransaction.txt' INTO "CASH_TRANSACTION" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: charge
IMPORT FROM CSV FILE '{0}/Charge.txt' INTO "CHARGE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: comission_rate
IMPORT FROM CSV FILE '{0}/CommissionRate.txt' INTO "COMMISSION_RATE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: settlement
IMPORT FROM CSV FILE '{0}/Settlement.txt' INTO "SETTLEMENT" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: trade
IMPORT FROM CSV FILE '{0}/Trade.txt' INTO "TRADE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: trade_history
IMPORT FROM CSV FILE '{0}/TradeHistory.txt' INTO "TRADE_HISTORY" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: trade_request Was already commented out
--IMPORT FROM CSV FILE '{0}/TradeRequest.txt' INTO "TRADE_REQUEST" WITH
--RECORD DELIMITED BY '\\n'
--FIELD DELIMITED BY '|'
--FAIL ON INVALID DATA;

--Table: trade_type
IMPORT FROM CSV FILE '{0}/TradeType.txt' INTO "TRADE_TYPE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: company
IMPORT FROM CSV FILE '{0}/Company.txt' INTO "COMPANY" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: company_competitor
IMPORT FROM CSV FILE '{0}/CompanyCompetitor.txt' INTO "COMPANY_COMPETITOR" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: daily_market
IMPORT FROM CSV FILE '{0}/DailyMarket.txt' INTO "DAILY_MARKET" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: exchange
IMPORT FROM CSV FILE '{0}/Exchange.txt' INTO "EXCHANGE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: financial
IMPORT FROM CSV FILE '{0}/Financial.txt' INTO "FINANCIAL" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: industry
IMPORT FROM CSV FILE '{0}/Industry.txt' INTO "INDUSTRY" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: last_trade
IMPORT FROM CSV FILE '{0}/LastTrade.txt' INTO "LAST_TRADE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: news_item
IMPORT FROM CSV FILE '{0}/NewsItem.txt' INTO "NEWS_ITEM" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: news_xref
IMPORT FROM CSV FILE '{0}/NewsXRef.txt' INTO "NEWS_XREF" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: sector
IMPORT FROM CSV FILE '{0}/Sector.txt' INTO "SECTOR" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: security
IMPORT FROM CSV FILE '{0}/Security.txt' INTO "SECURITY" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: address
IMPORT FROM CSV FILE '{0}/Address.txt' INTO "ADDRESS" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: status_type
IMPORT FROM CSV FILE '{0}/StatusType.txt' INTO "STATUS_TYPE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: taxrate
IMPORT FROM CSV FILE '{0}/Taxrate.txt' INTO "TAXRATE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: zip_code
IMPORT FROM CSV FILE '{0}/ZipCode.txt' INTO "ZIP_CODE" WITH
RECORD DELIMITED BY '\\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;"""

def create_file(csv_file,schema):
	with open(sql_name,'w') as f:
		f.write(sql_script.format(csv_file,schema))
	
def main(argv):
	if not len(argv) == 2:
		print("Please supply the path to the directory with the files to be imported and the target schema name as parameter!\n E.g. python 2_load_data.py <path_to_folder> <schema_name>")
		sys.exit()
	csv_file = os.path.abspath(argv[0])
	print("Create SQL Script {} ...\n".format(sql_name))
	create_file(csv_file,argv[1])
	print("SQL Script {} successfull created!\n".format(sql_name))


if __name__ == "__main__":
	main(sys.argv[1:])
