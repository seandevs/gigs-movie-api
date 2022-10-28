class UserService():
    def __init__(self, repository):
        self.repository = repository

    def find_by_username(self, username):
        return self.repository.find_by_username(username)


