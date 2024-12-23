from fastapi import FastAPI
from starlette import responses, status
from models import User
import random, string


app = FastAPI()


@app.get('/')  # main page with menu
async def home_page():
    return responses.Response(status_code=status.HTTP_200_OK)


# page with list of currently available lots
@app.get('/lots')
async def lots_list():
    # queryset = request to db for queryset of not sold lots
    # variable content = queryset converted to JSON
    return responses.JSONResponse(content='{}', status_code=status.HTTP_200_OK)


# lot menu for buyer
    # post with new price
    # timer of newest price

# lot menu for seller

# page for seller with list of sellers lots and money raised

# list of pages for payments

# list of pages for authentication

@app.post("/auth/login")
def login(user: User):
    user.currentToken = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(128))
    return responses.JSONResponse({"token": f"{user.currentToken}"}, status_code=status.HTTP_202_ACCEPTED)

