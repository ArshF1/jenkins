from flask import Flask

app=Flask()

@app.get("/")
def greet():
    return {
        "message":"Hello User. Welcome to FastAPI!"
    }

@app.get("/test")
def test():
    return {
        "message":"Welcome to test"
    }