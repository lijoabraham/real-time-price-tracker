# Real Time Price tracker


## 🛠 Setup

Clone project
```git clone https://github.com/lijoabraham/real-time-price-tracker.git```

### Launch containers
```
$ cd real-time-price-tracker/
$ docker-compose -f docker-compose.yml up -d
```

## 👣 Additional steps

### Create a price tracker table
- Connect to postgres DB using the below credentials
    ```
    host - localhost
    port - 5432
    username - postgres
    password- postgres
    ``` 
- Run the queries from the `postgres.sql` file.

### Create a price tracker connector in Debezium

- Create a connector entry by running the below API using the payload provided using postman or curl.

```
POST  http://localhost:8083/connectors

 {
   "name": "stock-price-connector",
   "config": {
     "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
     "database.hostname": "postgres",
     "database.port": "5432",
     "database.user": "postgres",
     "database.password": "postgres",
     "database.dbname": "postgres",
     "database.server.name": "stock-market",
     "table.include.list": "stock_prices.prices",
     "decimal.handling.mode": "string"
   }
 }
```
- Check the status of the connector by running the below command.
```
curl -X GET http://localhost:8083/connectors/stock-price-connector/status

```

### Check accesses
- UI: http://localhost:8000 
- kafdrop UI: http://localhost:9000

### For populating data in DB
```
  python price_generator.py
```
