from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from contextlib import closing
import requests

app = FastAPI()

# Modelo de dados para criar um novo usuário


class UserCreate(BaseModel):
    email: str
    first_name: str
    last_name: str
    avatar: str


# Rota para criar um novo usuário
@app.post("/api/users", response_model=dict)
def create_user(user: UserCreate):
    try:
        with closing(sqlite3.connect("users.db")) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    avatar TEXT
                )
            """)
            conn.commit()

            # Armazenar informações do usuário no banco de dados local
            cursor.execute(
                "INSERT INTO users (email, first_name, last_name, avatar) "
                "VALUES (?, ?, ?, ?)",
                (user.email, user.first_name, user.last_name, user.avatar)
            )

            conn.commit()

            # Obter o ID gerado e criar um objeto com ID e outros campos
            new_user_with_id = {"id": cursor.lastrowid, **user.model_dump()}

            # Fazer a solicitação para a API externa
            reqres_response = requests.post(
                "https://reqres.in/api/users", json=new_user_with_id
            )
            reqres_response.raise_for_status()

            # Verificar o código de resposta da API externa
            print("Status Code da API Externa:", reqres_response.status_code)

            # Imprimir a resposta da API externa
            print("Resposta da API Externa:", reqres_response.json())

            # Retornar os dados do usuário criado localmente como resposta
            return new_user_with_id
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao criar usuário: {e}"
        )  # Imprimir detalhes do erro


@app.get("/api/user/{userId}")
def get_user(userId: int):
    try:
        response = requests.get(f'https://reqres.in/api/users/{userId}')
        response.raise_for_status()  # Verifica se há erros na resposta HTTP

        user_data = response.json()['data']
        return user_data  # Retorna os dados do usuário em um formato JSON
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=500, detail="Erro ao acessar a API externa"
        )


@app.delete("/api/user/{userId}")
def delete_user(userId: int):
    try:
        # Recuperar informações do usuário antes de excluir do banco de dados
        with closing(sqlite3.connect("users.db")) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (userId,))
            user_data = cursor.fetchone()
            # Obtém as informações do usuário antes de excluir
            if not user_data:
                raise HTTPException(
                    status_code=404, detail="Usuário não encontrado"
                )
            # Fazer a solicitação para a API
            response = requests.delete(f"https://reqres.in/api/users/{userId}")
            response.raise_for_status()

            # Excluir o usuário do banco de dados
            cursor.execute("DELETE FROM users WHERE id = ?", (userId,))
            conn.commit()

            # Verificar o código de resposta da API externa
            print("Status Code da API Externa:", response.status_code)
            return {
                'message': f"Usuário com ID {userId} deletado "
                "localmente e da API externa",
                'deleted_user_info': user_data
            }
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao excluir usuário: {e}"
        )  # Imprimir detalhes do erro
