DROP TABLE seq_trade_id CASCADE;

CREATE TABLE seq_trade_id (
id BIGINT NOT NULL
);

INSERT INTO seq_trade_id SELECT MAX(t_id) FROM trade;