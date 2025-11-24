from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="My CI/CD Demo App", version="1.0.0")

@app.get("/")
async def root():
    return {
        "message": "Hello from CI/CD Demo App!",
        "timestamp": datetime.now().isoformat(),
        "status": "healthy"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
