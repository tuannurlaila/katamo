from fastapi import FastAPI
import uvicorn

from action import Action
a = Action

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my_name")
def my_name():
    data = "Tuannurlaila katamo"
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data


@app.get("/input_name_2")
def input_name_2(name, last_name):
    data = "{} {}".format(name, last_name)
    return data

@app.get("/physics")
def physics(s,t):
    v = float(s) / float(t)
    data = "v = {:.2f}".format(v)
    return data

@app.get("/get_hard_ware3")
def get_hard_ware3():
    data = a.gethard_ware3()
    return data

@app.get("/update_status_hard_ware3")
def update_status_hard_ware3(ID, status):
    data = a.updatehard_ware3(ID, status)
    return data

@app.get("/update_name_hard_ware3")
def update_name_hard_ware3(ID, name):
    data = a.updatehard_ware3(ID, name)
    return data

@app.get("/update_value_hard_ware3")
def update_value_hard_ware3(ID, value):
    data = a.updatehard_ware3(ID, value)
    return data

@app.get("/update_status_hard_ware3")
def update_status_hard_ware3(ID, status):
    data = a.updatehard_ware3(ID, status)
    return data

@app.get("/select_hard_ware3")
def select_hard_ware3(ID):
    data = a.gethard_ware3(ID)
    return data

@app.get("/insert_hard_ware3")
def inserthard_ware3(ID, name, hw_name):
    data = a.inserthard_ware3(ID, name, hw_name)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80)