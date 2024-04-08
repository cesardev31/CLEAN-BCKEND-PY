from flask import Blueprint, request, jsonify
from app.use_cases.user_use_case import UserUseCase
from app.gateways.user_gateway import UserGateway
from utils.DateFormat import DateFormat
from app.gateways.user_gateway_interface import UserGatewayInterface

user_controller = Blueprint("user_controller", __name__)


@user_controller.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    # Convierte la fecha de nacimiento al formato correcto
    date_of_birth = DateFormat.convert_date(data["date_of_birth"])

    # Crea una instancia de UserGateway pasando la configuración de la base de datos
    user_gateway: UserGatewayInterface = UserGateway()

    # Crea una instancia de UserUseCase, pasándole el UserGateway
    user_use_case = UserUseCase(user_gateway)

    user_use_case.create_user(
        data["name"],
        data["email"],
        date_of_birth,
        data["gender"],
        data["id_number"],
    )
    return jsonify({"message": "User created successfully"}), 201


@user_controller.route("/users", methods=["GET"])
def get_users():
    # Crea una instancia de UserGateway pasando la configuración de la base de datos
    user_gateway: UserGatewayInterface = UserGateway()

    # Crea una instancia de UserUseCase, pasándole el UserGateway
    user_use_case = UserUseCase(user_gateway)

    # Obtiene todos los usuarios
    users = user_use_case.get_all_users()

    # Prepara los datos de los usuarios para la respuesta
    users_data = [
        {
            "name": user.name,
            "email": user.email,
            "date_of_birth": user.date_of_birth,
            "gender": user.gender,
            "id_number": user.id_number,
        }
        for user in users
    ]

    return jsonify({"users": users_data}), 200


@user_controller.route("/users/<string:id_number>", methods=["GET"])
def get_user_by_id_number(id_number):
    user_gateway: UserGatewayInterface = UserGateway()

    # Crea una instancia de UserUseCase, pasándole el UserGateway
    user_use_case = UserUseCase(user_gateway)

    # Obtiene todos los usuarios
    user = user_use_case.get_user_id_number(id_number)

    user_data = {
        "name": user.name,
        "email": user.email,
        "date_of_birth": user.date_of_birth,
        "gender": user.gender,
        "id_number": user.id_number,
    }

    return jsonify(user_data), 200


@user_controller.route("/users/<string:id_number>", methods=["DELETE"])
def delete_user(id_number):
    user_gateway: UserGatewayInterface = UserGateway()
    user_use_case = UserUseCase(user_gateway)
    user_use_case.delete_user(id_number)
    return jsonify({"message": "User deleted successfully"}), 201
