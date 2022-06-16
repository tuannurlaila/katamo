from turtle import rt
from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/parallel_series")
def paralle_series( r1:float, r2:float, r3:float ):
    parallel = (((1/r1) + (1/r2) + (1/r3))**-1)
    series = (r1 + r2 + r3)
    data = " parallel = {:.2f} = series = {:.2f}".format(parallel, series)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.43.118", port=8000)