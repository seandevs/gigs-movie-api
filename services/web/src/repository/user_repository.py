from src.entity.user import User


class UserRepository():
    def find_by_username(self, username):
        return User.query.filter_by(username=username).first()

