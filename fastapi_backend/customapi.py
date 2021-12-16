from fastapi import FastAPI

app = FastAPI()
candle = {
    "market": "KRW-ARDR",
    "candle_date_time_utc": "2021-12-16T00:00:00",
    "candle_date_time_kst": "2021-12-16T09:00:00",
    "opening_price": 293,
    "high_price": 297,
    "low_price": 286,
    "trade_price": 291,
    "timestamp": 1639638204057,
    "candle_acc_trade_price": 1327283886.9414957,
    "candle_acc_trade_volume": 4570641.92129976,
    "prev_closing_price": 292,
    "change_price": -1,
    "change_rate": -0.0034246575
}
#endpoint
@app.get("/")
def index():
    return{"name":"First Data"}


