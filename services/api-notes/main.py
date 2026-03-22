from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running with UV"}

def main():
    print("Hello from api-notes!")


if __name__ == "__main__":
    main()
