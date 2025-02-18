from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class IBaseRepository(ABC, [T]):
    @abstractmethod
    def insert(self, entity: T) -> Optional[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, entity: T) -> Optional[T]:
        pass

    @abstractmethod
    def deleteById(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    def getAll(self) -> List[T]:
        pass

    @abstractmethod
    def getById(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    def getByName(self, name: str) -> Optional[T]:
        pass