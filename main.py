from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Hello World API", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>FastAPI Hello World</title>
        </head>
        <body>
            <h1>Hello World from FastAPI!</h1>
            <p>This is a simple FastAPI application deployed on AWS Amplify.</p>
        </body>
    </html>
    """

@app.get("/api/hello")
async def hello():
    return {"message": "Hello World!", "status": "success"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "FastAPI Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
