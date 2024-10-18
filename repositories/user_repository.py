from models.user_models import User
from configurations.database import db

class UserRepository:
    @staticmethod
    def create_user(username, password):
        new_user = User(username, password)

