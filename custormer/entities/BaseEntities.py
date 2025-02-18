from datetime import datetime


class BaseEntity:
    id : int
    created_at : datetime
    updated_at : datetime
    is_deleted : bool

    def display(self):
        print(self.id , self.created_at, self.updated_at, self.is_deleted)

