from fastapi import FastAPI
from starlette import responses, status


app = FastAPI()


@app.get('/')
async def home_page():
    return responses.Response(status_code=status.HTTP_200_OK)
