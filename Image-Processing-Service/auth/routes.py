from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth.jwt_utils import create_token, decode_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

mock_users_db = {"user1": {"username": "user1", "password": "1234"}}

@router.post("/register")
def register(form: OAuth2PasswordRequestForm = Depends()):
    if form.username in mock_users_db:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    mock_users_db[form.username] = {"username": form.username, "password": form.password}
    return {"msg": "Usuário registrado"}

@router.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = mock_users_db.get(form.username)
    if not user or user["password"] != form.password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_token({"sub": form.username})
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    if not username:
        raise HTTPException(status_code=403, detail="Token inválido")
    return username
