from custormer.entities.BaseEntities import BaseEntity


class Product(BaseEntity) :
    name : str
    price : float

    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price

    def display(self):
        print(BaseEntity.display(self), self.name )