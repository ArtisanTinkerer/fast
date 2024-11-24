import uvicorn

from model import Creature
from fastapi import FastAPI

app = FastAPI()


@app.get("/creatures")
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()


#so I can debug
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)