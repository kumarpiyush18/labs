from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Quick Notes API")

@app.get("/")
def root():
    return {
        "message": "API running with UV",
        "status": "online",
        "docs": "/docs"
    }

def main():
    # Allow running directly via 'python main.py' or 'uv run main.py'
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
