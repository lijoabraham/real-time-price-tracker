CREATE KEYSPACE stock_data
WITH replication = {
   'class': 'SimpleStrategy'
};

USE stock_data;

CREATE TABLE stock_data.stock_data (
    Symbol text PRIMARY KEY,
    Date date,
    Time time,
    Open decimal,
    High decimal,
    Low decimal,
    Close decimal,
    Volume int
) WITH CDC = true;