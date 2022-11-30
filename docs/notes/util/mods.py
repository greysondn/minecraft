# Python 3.11, I think
from typing import Any
from typing import cast
from typing import Optional

# so the way this works is
# the mods kind of manage themselves as a data structure
# and I'll just output a document later

class SomeCollectible:
    def __init__(self, id:str, aliases:set[str]):
        self.id:str = id
        self.aliases:set[str] = aliases
        self.aliases.add(self.id)
    def answersTo(self, name:str):
        return name in self.aliases
    def addAlias(self, name:str):
        self.aliases.add(name)
    def canonize(self, name:str):
        return self.id

class SomeCollection:
    def __init__(self):
        self.contents:list[SomeCollectible] = []
    def add(self, collectible:SomeCollectible):
        self.contents.append(collectible)
    def get(self, name:str) -> Optional[SomeCollectible]:
        ret:Optional[SomeCollectible] = None
        found:bool                    = False
        
        for item in self.contents:
            if (not found):
                if item.answersTo(name):
                    found = True
                    ret = item
        
        return ret
    # I'm lazy, let's write a pair of operators for id lookup
    
    # conditional "in" support
    def __contains__(self, name:str) -> bool:
        ret:bool = False
        
        for item in self.contents:
            if (not ret):
                if item.answersTo(name):
                    ret = True
        
        return ret
    
    # dict key accessor - well, if you contain something, you can access it
    # via key
    def __getitem__(self, key:str):
        return self.get(key)

class User(SomeCollectible):
    # I've collected the entire class O.o
    pass

class UserList(SomeCollection):
    def get(self, name:str) -> Optional[User]:
        # literally the only change is a casting
        return cast(User,super().get(name))

class Vote(SomeCollectible):
    def __init__(self, user:User, vote:bool, notes:list[str]=[], reason:str=""):
        super().__init__(user.id, set())
        self.user:User = user
        self.notes:list[str] = notes
        self.vote:bool = vote
        self.reason:str = reason

class VoteCollection(SomeCollection):
    def get(self, userName:str) -> Optional[Vote]:
        # literally the only change is a casting
        return cast(Vote,super().get(userName))

class Status:
    def __init__(self, included:bool, reason:str=""):
        self.included = included
        self.reason = reason

class Version(SomeCollectible):
    def __init__(self, id:str):
        super().__init__(id, set())
        self.votes = VoteCollection()
    def addVote(self, vote:Vote):
        self.votes.add(vote)

class VersionCollection(SomeCollection):
    # oops, I did it again
    pass

class Mod(SomeCollectible):
    # right, this one at least has some unique properties
    pass