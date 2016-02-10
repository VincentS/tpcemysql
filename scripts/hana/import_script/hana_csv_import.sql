SET SCHEMA TPCE;

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/AccountPermission.txt' INTO "ACCOUNT_PERMISSION" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Address.txt' INTO "ADDRESS" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Broker.txt' INTO "BROKER" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/CashTransaction.txt' INTO "CASH_TRANSACTION" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Charge.txt' INTO "CHARGE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/CommissionRate.txt' INTO "COMMISSION_RATE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/CompanyCompetitor.txt' INTO "COMPANY_COMPETITOR" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Company.txt' INTO "COMPANY" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/CustomerAccount.txt' INTO "CUSTOMER_ACCOUNT" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/CustomerTaxrate.txt' INTO "CUSTOMER_TAXRATE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Customer.txt' INTO "CUSTOMER" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/DailyMarket.txt' INTO "DAILY_MARKET" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Exchange.txt' INTO "EXCHANGE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Financial.txt' INTO "FINANCIAL" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/HoldingHistory.txt' INTO "HOLDING_HISTORY" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/HoldingSummary.txt' INTO "HOLDING_SUMMARY" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Holding.txt' INTO "HOLDING" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Industry.txt' INTO "INDUSTRY" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/LastTrade.txt' INTO "LAST_TRADE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/NewsItem.txt' INTO "NEWS_ITEM" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/NewsXRef.txt' INTO "NEWS_XREF" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Sector.txt' INTO "SECTOR" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Security.txt' INTO "SECURITY" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Settlement.txt' INTO "SETTLEMENT" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/StatusType.txt' INTO "STATUS_TYPE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Taxrate.txt' INTO "TAXRATE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/TradeHistory.txt' INTO "TRADE_HISTORY" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/Trade.txt' INTO "TRADE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/TradeType.txt' INTO "TRADE_TYPE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/WatchItem.txt' INTO "WATCH_ITEM" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/WatchList.txt' INTO "WATCH_LIST" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';

IMPORT FROM CSV FILE '/mnt/tyros_01/TPCC/TPCE_Data/flat_out/ZipCode.txt' INTO "ZIP_CODE" WITH RECORD DELIMITED BY '\n' FIELD DELIMITED BY '|';