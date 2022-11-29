# Python 3.11, I think
from typing import Optional

# so the way this works is
# the mods kind of manage themselves as a data structure
# and I'll just output a document later
class User:
    def __init__(self, name:str, aliases:set[str]):
        self.name:str = name
        self.aliases:set[str] = aliases
        self.aliases.add(self.name)
    def answersTo(self, name:str):
        return name in self.aliases
    def addAlias(self, name:str):
        self.aliases.add(name)
    def canonize(self, name:str):
        return self.name

class UserList:
    def __init__(self):
        self.users:list[User] = []
    def addUser(self, user:User) -> None:
        self.users.append(user)
    def findUser(self, username:str) -> Optional[User]:
        ret:Optional[User] = None
        found:bool         = False
        
        for user in self.users:
            if (not found):
                if user.answersTo(username):
                    found = True
                    ret = user
        
        return ret

class Vote:
    def __init__(self, user:User, vote:bool, notes:str="", reason:str=""):
        self.user:User = user
        self.notes:str = notes
        self.vote:bool = vote
        self.reason:str = reason

class VoteCollection:
    def __init__(self):
        votes:list[Vote] = []
    def addVote(self, vote:Vote)
    

class Status:
    def __init__(self, included:bool, reason:str=""):
        self.included = included
        self.reason = reason



class Version:
    def __init__(self, id:str):
        self.id = id
        self.vot