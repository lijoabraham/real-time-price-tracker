mongo -u root -p root


use stock_data;

db.createCollection("prices", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["Symbol","time_added", "Open", "High", "Low", "Close", "Volume"],
      properties: {
        Symbol: {
          bsonType: "string",
          description: "Stock symbol (text)"
        },
        time_added: {
          bsonType: "date",
          description: "Date of the record creation"
        },
        Open: {
          bsonType: "double",
          description: "Opening price (double)"
        },
        High: {
          bsonType: "double",
          description: "Highest price during the day (double)"
        },
        Low: {
          bsonType: "double",
          description: "Lowest price during the day (double)"
        },
        Close: {
          bsonType: "double",
          description: "Closing price (double)"
        },
        Volume: {
          bsonType: "int",
          description: "Volume (integer)"
        }
      }
    }
  }
});

db.prices.insertOne({
  Symbol: "AAPL",
  time_added: new Date(),
  Open: 150.00,
  High: 155.00,
  Low: 148.50,
  Close: 153.25,
  Volume: NumberInt(10002)
})


db.prices.find()

