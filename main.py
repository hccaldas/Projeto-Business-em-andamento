from fastapi import FastAPI
from routes import usuarios, login

app = FastAPI()

# Registrando as rotas
app.include_router(usuarios.router)
app.include_router(login.router)

@app.get("/")
def home():
    return {"mensagem": "API do Dashboard de Vendas funcionando!"}

# Rodar o servidor com: uvicorn main:app --reload