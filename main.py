from fastapi import FastAPI, UploadFile
import uvicorn

from get_data.upload_csv import load_csv


app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello"}



@app.post("/assignWithCsv/")
def soldier_insert(file: UploadFile):
    data = load_csv(file)
    return data









if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)