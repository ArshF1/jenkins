from flask import Flask
import uvicorn

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

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )