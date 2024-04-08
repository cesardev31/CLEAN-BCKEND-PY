from app.gateways.user_gateway import UserGateway
from app.entities.user import User


class UserUseCase:
    def __init__(self, user_gateway: UserGateway):
        self.user_gateway = user_gateway

    def create_user(self, name, email, date_of_birth, gender, id_number):
        user = User(name, email, date_of_birth, gender, id_number)
        self.user_gateway.create(user)

    def get_user_id_number(self, id_number):
        return self.user_gateway.get_by_number_id(id_number)

    def get_all_users(self):
        return self.user_gateway.get_all()

    def delete_user(self, id_number):
        self.user_gateway.delete(id_number)
