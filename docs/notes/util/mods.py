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
    def getUser(self, username:str) -> Optional[User]:
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
        self.votes:list[Vote] = []
    def addVote(self, vote:Vote):
        self.votes.append(vote)
    

class Status:
    def __init__(self, included:bool, reason:str=""):
        self.included = included
        self.reason = reason

class Version:
    def __init__(self, id:str):
        self.id = id
        self.votes = VoteCollection()
    def hasId(self, id:str):
        return id == self.id

class VersionCollection:
    def __init__(self):
        self.versions:list[Version] = []
    def getVersion(self, id:str) -> Optional[Version]:
        ret:Optional[Version] = None
        found:bool            = False
        
        for version in self.versions:
            if (not found):
                if version.hasId(id):
                    found = True
                    ret = version
        
        return ret

class Mod:
    def __init__(self, name:str, curseId:str):
        self.name = name
        self.curseId = curseId
    def hasName(self, name:str):
        return name == self.name
    def hasCurseId(self, curseId):
        return curseId == self.curseId