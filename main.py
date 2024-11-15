from fastapi import FastAPI
from starlette import responses, status


app = FastAPI()


@app.get('/')  # main page with menu
async def home_page():
    return responses.Response(status_code=status.HTTP_200_OK)

# page with list of currently available lots

# lot menu for buyer
    # post with new price
    # timer of newest price

# lot menu for seller

# page for seller with list of sellers lots and money raised

# list of pages for payments

# list of pages for authentication

