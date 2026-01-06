from flask import Flask

app=Flask()

@app.get("/")
def greet():
    return {
        "message":"Hello User. Welcome to FastAPI!"
    }