import json
import datetime
from google.protobuf.json_format import MessageToDict
from fastapi import FastAPI,Request, Response
from kafka import KafkaConsumer
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="/code/app/app")
app = FastAPI()

    
@app.get("/get_realtime_data")
def get_get_realtime_data():
    try:
        kafka_consumer = KafkaConsumer(
            'stock-market.stock_prices.prices',  
            bootstrap_servers='kafka1:29092,kafka2:29093',  
            group_id='realtime_data_consumer',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            auto_commit_interval_ms=1000,
        )

        try:
            for message in kafka_consumer:
                message_value = message.value.decode('utf-8')
                data = json.loads(message_value)['payload']['after']
                decoded_data = {
                    "id": data["id"],
                    "symbol": data["symbol"],
                    "timestamp": datetime.datetime.utcfromtimestamp(data["timestamp"] / 1000.0),  # Convert milliseconds to seconds
                    "open": float(data["open"]),
                    "high": float(data["high"]),
                    "low": float(data["low"]),
                    "close": float(data["close"]),
                    "volume": data["volume"]
                }
                decoded_data["timestamp"] = decoded_data["timestamp"].isoformat()
                # print(decoded_data)
                data = f"data: {json.dumps(decoded_data)}\n\n"
                return Response(data.encode("utf-8"), media_type="text/event-stream")

        except KeyboardInterrupt:
            print('Consumer interrupted by user')
        finally:
            kafka_consumer.close()
    except Exception as e:
        print(f"Unexpected error: {e}")

@app.get("/index", response_class=HTMLResponse)
async def read_root(request: Request):
    # Your data to be passed to the template
    data = {"title": "FastAPI Jinja2 Example", "content": "Hello, World!"}
    return templates.TemplateResponse("chart.html", {"request": request, "data": data})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
