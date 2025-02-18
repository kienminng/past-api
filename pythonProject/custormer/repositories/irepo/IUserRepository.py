from typing import Optional, List

from pythonProject.custormer.repositories.irepo.IBaseRepository import IBaseRepository
from pythonProject.custormer.entities.User import User

class IUserRepository(IBaseRepository[User]):
    def insert(self, entity: User) -> Optional[User]:
        pass

    def update(self, entity: User) -> Optional[User]:
        pass

    def delete(self, entity: User) -> Optional[User]:
        pass

    def deleteById(self, id: int) -> Optional[User]:
        pass

    def getAll(self) -> List[User]:
        pass

    def getById(self, id: int) -> Optional[User]:
        pass

    def getByName(self, name: str) -> Optional[User]:
        pass