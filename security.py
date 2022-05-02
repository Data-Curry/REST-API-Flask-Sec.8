from models.user import UserModel


def authentication(username, password):
    user = UserModel.find_by_username(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    userid = payload['identity']
    return UserModel.find_by_id(userid, None)
