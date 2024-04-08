import psycopg2
import os
from decouple import config
from app.entities.user import User 
from app.gateways.user_gateway_interface import UserGatewayInterface


class UserGateway(UserGatewayInterface):
    def __init__(self):
        self.connection_string = config("DATABASE_URL")

    def create(self, user):
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (name, email, date_of_birth, gender, id_number) VALUES (%s, %s, %s, %s, %s)",
                    (
                        user.name,
                        user.email,
                        user.date_of_birth,
                        user.gender,
                        user.id_number,
                    ),
                )

    def get_all(self):
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT name, email, date_of_birth, gender, id_number FROM users"
                )
                users = []
                for row in cur.fetchall():
                    name, email, date_of_birth, gender, id_number = row
                    users.append(User(name, email, date_of_birth, gender, id_number))
                return users
    
    def delete(self, id_number):
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM users WHERE id_number = %s",
                    (id_number,)
                )
    
    def get_by_number_id(self, id_number):
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT name, email, date_of_birth, gender, id_number FROM users WHERE id_number = %s",
                    (id_number,)
                )
                row = cur.fetchone()
                if row:
                    name, email, date_of_birth, gender, id_number = row
                    return User(name, email, date_of_birth, gender, id_number)
                else:
                    return None

             
