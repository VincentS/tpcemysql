--Select correct Schema

SET SCHEMA TPCE

--Table: account_permission
IMPORT FROM CSV FILE '../../flat_out/AccountPermission.txt' INTO "account_permission" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: customer
IMPORT FROM CSV FILE '../../flat_out/Customer.txt' INTO "customer" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: customer_account
IMPORT FROM CSV FILE '../../flat_out/CustomerAccount.txt' INTO "customer_account" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: customer_taxrate
IMPORT FROM CSV FILE '../../flat_out/CustomerTaxrate.txt' INTO "customer_taxrate" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: holding
IMPORT FROM CSV FILE '../../flat_out/Holding.txt' INTO "holding" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: holding_history
IMPORT FROM CSV FILE '../../flat_out/HoldingHistory.txt' INTO "holding_history" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: holding_summary
IMPORT FROM CSV FILE '../../flat_out/HoldingSummary.txt' INTO "holding_summary" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: watch_item
IMPORT FROM CSV FILE '../../flat_out/WatchItem.txt' INTO "watch_item" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: watch_list
IMPORT FROM CSV FILE '../../flat_out/WatchList.txt' INTO "watch_list" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;


--Table: broker
IMPORT FROM CSV FILE '../../flat_out/Broker.txt' INTO "broker" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: cash_transaction
IMPORT FROM CSV FILE '../../flat_out/CashTransaction.txt' INTO "cash_transaction" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: charge
IMPORT FROM CSV FILE '../../flat_out/Charge.txt' INTO "charge" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: comission_rate
IMPORT FROM CSV FILE '../../flat_out/CommissionRate.txt' INTO "comission_rate" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: settlement
IMPORT FROM CSV FILE '../../flat_out/Settlement.txt' INTO "settlement" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: trade
IMPORT FROM CSV FILE '../../flat_out/Trade.txt' INTO "trade" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: trade_history
IMPORT FROM CSV FILE '../../flat_out/TradeHistory.txt' INTO "trade_history" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: trade_request Was already commented out
--IMPORT FROM CSV FILE '../../flat_out/TradeRequest.txt' INTO "trade_request" WITH
--RECORD DELIMITED BY '\n'
--FIELD DELIMITED BY '|'
--FAIL ON INVALID DATA;

--Table: trade_type
IMPORT FROM CSV FILE '../../flat_out/TradeType.txt' INTO "trade_type" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: company
IMPORT FROM CSV FILE '../../flat_out/Company.txt' INTO "company" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: company_competitor
IMPORT FROM CSV FILE '../../flat_out/CompanyCompetitor.txt' INTO "company_competitor" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: daily_market
IMPORT FROM CSV FILE '../../flat_out/DailyMarket.txt' INTO "daily_market" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: exchange
IMPORT FROM CSV FILE '../../flat_out/Exchange.txt' INTO "exchange" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: financial
IMPORT FROM CSV FILE '../../flat_out/Financial.txt' INTO "financial" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: industry
IMPORT FROM CSV FILE '../../flat_out/Industry.txt' INTO "industry" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: last_trade
IMPORT FROM CSV FILE '../../flat_out/LastTrade.txt' INTO "last_trade" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: news_item
IMPORT FROM CSV FILE '../../flat_out/NewsItem.txt' INTO "news_item" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: news_xref
IMPORT FROM CSV FILE '../../flat_out/NewsXRef.txt' INTO "news_xref" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: sector
IMPORT FROM CSV FILE '../../flat_out/Sector.txt' INTO "sector" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: security
IMPORT FROM CSV FILE '../../flat_out/Security.txt' INTO "security" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: address
IMPORT FROM CSV FILE '../../flat_out/Address.txt' INTO "address" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: status_type
IMPORT FROM CSV FILE '../../flat_out/StatusType.txt' INTO "status_type" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: taxrate
IMPORT FROM CSV FILE '../../flat_out/Taxrate.txt' INTO "taxrate" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;

--Table: zip_code
IMPORT FROM CSV FILE '../../flat_out/ZipCode.txt' INTO "zip_code" WITH
RECORD DELIMITED BY '\n'
FIELD DELIMITED BY '|'
FAIL ON INVALID DATA;