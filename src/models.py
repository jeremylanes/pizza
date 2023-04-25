from dataclasses import dataclass

@dataclass
class Pizza:
    name: str = ""
    ingredients: str = ""
    price: float = 0.0
    vegetarian: bool = False

    def get_dictionary(self):
        return {'name': self.name, 'ingredients': self.ingredients, 'price': self.price, 'vegetarian':self.vegetarian}
