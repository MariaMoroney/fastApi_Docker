from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, mundo!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/usuarios/{usuario_id}")
def read_usuario(usuario_id: int):
    return {"usuario_id": usuario_id, "nombre": "Usuario de ejemplo"}