from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "from": "CI/CD"}

@app.get("/health")
def health():
    return {"status": "healthy"}
