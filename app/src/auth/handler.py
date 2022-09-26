from auth.contracts import AuthModel

from database import db_users_data

def register(user: AuthModel):
    if user.login in db_users_data.keys():
        return {"Error" : "User is already registered"} 
    db_users_data.update({user.login : ([user.password, user.name], [])})
    return {"OK" : "User " + user.login + " has been succesfully registered"}