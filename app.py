from fastapi import FastAPI
import uvicorn
from models import SimpleModel
from fastapi.responses import JSONResponse

app = FastAPI()

# GET request example
@app.get("/")
async def root():
    sm = SimpleModel(id=1, name="randomname")
    return JSONResponse(content=sm.dict())


# POST request example
@app.post("/post")
async def post(simple_model: SimpleModel):
    return simple_model


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", reload=True, port=5001)
