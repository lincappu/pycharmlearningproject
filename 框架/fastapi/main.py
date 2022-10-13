# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import uvicorn
from typing import Optional
from fastapi import FastAPI,Query,Path,Form,Depends,HTTPException,status
from fastapi.security import  OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pydantic import  BaseModel
import  jwt
from passlib.context import CryptContext

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int,item:Item):
#     return {"item_id": item_id, "name":item.name }

# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# @app.get("/items/")
# async def read_items(q: str = Query("fixedquery", min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# 路径参数和数值校验

# @app.get("/items/{item_id}")
# async def read_times(item_id:int=Path(...,title="The ID of the item to get"),
#                      q: Optional[str]=Query(None,alias="item-query")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# form 表单提交数据
# @app.post("/login")
# async def login(username: str=Form(...),password:str=Form(...)):
#     return username


# 额外的数据类型


# oauth2认证
# oauth=OAuth2PasswordBearer(tokenUrl='token')
# @app.get("/items")
# async def read(token: str=Depends(oauth)):
#     return {"token": token}



# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None
#
# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
#     )
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = fake_decode_token(token)
#     return user

# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user


# 例子 3
# SECRET_KEY =
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
#
# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     }
# }
#
#
# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None
#
# class UserInDB(User):
#     hashed_password: str
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
#
# def verify_password(plain_psssword,hashed_password):
#     return pwd_context.verify(plain_psssword,hashed_password)
#
# def get_password_hash(password):
#     return pwd_context.hash(password)
#
# def get_user(db,username:str):
#     if username in db:
#         user_dict=db.username
#         return UserInDB(**user_dict)










if __name__ == '__main__':
    uvicorn.run('main:app',reload=True,host='0.0.0.0',port=8000)