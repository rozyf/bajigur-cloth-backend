from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "admin": {
        "username": "admin",
        "full_name": "Admin 1",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
    "firmansyahrozy": {
        "username": "firmansyahrozy",
        "full_name": "Firmansyah Rozy",
        "email": "rozy@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class ItemField(BaseModel):
    sku: str
    name: str
    category: list[str]
    quantity: int 
    original_price: int
    discount: int
    discount_price: int

class Item(BaseModel):
    item: ItemField

class ItemLines(BaseModel):
    sku: str
    name: str
    categories: list[str]
    quantity: int 
    price: int

class OrderField(BaseModel):
    user_id: str
    total_amount: int
    status: str
    coupon_used: str
    items: list[ItemLines]
    shipping_price: int

class Order(BaseModel):
    order: OrderField

class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def routes(app):
    # Login & Register
    @app.post("/api/v1/login", response_model=Token, tags=['LOGIN & REGISTER'], summary='Login for Access Token')
    async def f(form_data: OAuth2PasswordRequestForm = Depends()):
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    @app.post("/api/v1/register", tags=['LOGIN & REGISTER'], summary='Register User')
    async def f(body: User):
        return { 'message': 'success' }


    # Highlight Feature
    @app.post("/api/v1/admin/coupons", tags=['HIGHLIGHT FEATURE'], summary='Create a coupon / voucher')
    async def f(body: Item, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.post("/api/v1/admin/coupons/share", tags=['HIGHLIGHT FEATURE'], summary='Give coupon to some / all of the users')
    async def f(body: Item, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.post("/api/v1/admin/coupons/share/{user_id}", tags=['HIGHLIGHT FEATURE'], summary='Give coupon to a user')
    async def f(body: Item, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }



    # Admin
    @app.get("/api/v1/admin/coupons", tags=['ADMIN'])
    async def get_a_list_of_coupons(current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.get("/api/v1/admin/coupons/{coupon_id}", tags=['ADMIN'])
    async def get_a_coupon(coupon_id, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.patch("/api/v1/admin/coupons/{coupon_id}", tags=['ADMIN'])
    async def update_status_order(coupon_id, order_id, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.delete("/api/v1/admin/coupons/{coupon_id}", tags=['ADMIN'])
    async def delete_an_order(coupon_id, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.get("/api/v1/admin/users", tags=['ADMIN'], summary='Get a List of Users')
    async def f(current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.get("/api/v1/admin/items", tags=['ADMIN'])
    async def get_a_list_of_products(current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.get("/api/v1/admin/items/{item_id}", tags=['ADMIN'])
    async def get_single_product(item_id, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.post("/api/v1/admin/items", tags=['ADMIN'])
    async def create_single_product(body: Item, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.post("/api/v1/admin/items/apply_discount", tags=['HIGHLIGHT FEATURE', 'ADMIN'], summary="Give discount on least sold product or old product to increase product's sales")
    async def f(body: Item, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.patch("/api/v1/admin/items/{item_id}", tags=['ADMIN'])
    async def edit_a_product(item_id, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.delete("/api/v1/admin/items/{item_id}", tags=['ADMIN'])
    async def delete_a_product(item_id, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.get("/api/v1/admin/orders", tags=['ADMIN'])
    async def get_a_list_of_orders(current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.post("/api/v1/admin/orders", tags=['ADMIN'])
    async def create_single_order(body: Order, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }


    # USERS
    @app.get("/api/v1/users/profile", response_model=User, tags=['USERS'])
    async def get_user_profile(current_user: User = Depends(get_current_active_user)):
        return current_user

    @app.get("/api/v1/users/orders", tags=['USERS'], summary="Get All User's Orders")
    async def f(current_user: User = Depends(get_current_active_user)):
        return [{"item_id": "Foo", "owner": current_user.username}]

    @app.get("/api/v1/users/orders/{order_id}", tags=['USERS'])
    async def get_single_order(order_id, current_user: User = Depends(get_current_active_user)):
        return { 'message': 'success' }

    @app.get("/api/v1/users/product_suggestions", tags=['HIGHLIGHT FEATURE', 'USERS'], summary="Show Product Based on User Order's History, Search History, Wishlist, etc.")
    async def f(current_user: User = Depends(get_current_active_user)):
        return [{"item_id": "Foo", "owner": current_user.username}]

    @app.get("/api/v1/users/product_discounts", tags=['HIGHLIGHT FEATURE', 'USERS'], summary="Show Product that is on sales discount")
    async def f(current_user: User = Depends(get_current_active_user)):
        return [{"item_id": "Foo", "owner": current_user.username}]

    @app.get("/api/v1/users/user_membership_level", tags=['HIGHLIGHT FEATURE', 'USERS'], summary="Get membership level. Level increased when user purchase a product. Higher level gets more benefits like coupons & discounts")
    async def f(current_user: User = Depends(get_current_active_user)):
        return [{"item_id": "Foo", "owner": current_user.username}]