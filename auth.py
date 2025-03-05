import jwt
import datetime

#chave secreta para assinar o token JWT
SECRET_KEY = "minha_chave_mais_que_secreta"

def criar_token(email, str):
    """Gera um token JWT para o usuário"""
    #cria o payload do token
    payload = {
        "sub": email,              #sub: assunto do token
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)  #exp: data de expiração, expira em 2 horas
    }
    
    #gera o token
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token