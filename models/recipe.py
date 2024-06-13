from .base import Base

class Recipe(Base):
    def __init__(self, recipe_id, recipe_name, ingredients):
        super().__init__(recipe_id=recipe_id, recipe_name=recipe_name, ingredients=ingredients)
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.ingredients = ingredients
