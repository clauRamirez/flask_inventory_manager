from src.models.author import Author
from src.models.publisher import Publisher

class Book:
    def __init__(
        self,
        ISBN: int,
        title: str,
        genre: str,
        author: Author,
        illustrator: Author,
        publisher: Publisher,
        edition: int,
        cost: float,
        price: float,
        stock: int,
        id: int = None
    ):
    
        self.ISBN = ISBN
        self.title = title
        self.genre = genre
        self.author = author
        self.illustrator = illustrator
        self.publisher = publisher
        self.edition = edition
        self.cost = cost
        self.price = price
        self.stock = stock
        self.id = id
        
    def get_mark_up(self) -> float:
        return round(self.price - self.cost, 2)
    