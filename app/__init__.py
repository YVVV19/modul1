from fastapi import FastAPI, Query

app = FastAPI(debug=True)

@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/greet/{name}/")
def read_greeting(name:str):
    return {"message":f"greeting:{name}"}

@app.get("/greet/")
def read_greeting(operation: str = Query(None, description="Input your name:")):
    return {"message":f"greeting:{operation}"}


@app.get("/calculate/")
def calculate(
    operation: str = Query(None, description="Input your name:"),
    num1: float = Query(None, description="Input your name:"),
    num2: float = Query(None, description="Input your name:")
            ):
    if operation == "-":
        division=num1-num2
        return {"message": f"{division}"}
    elif operation =="+":
        plus=num1+num2
        return{"message": f"{plus}"}
    else:
        return False
    
