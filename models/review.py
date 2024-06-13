from .base import Base

class Review(Base):
    def __init__(self, review_id, user_id, recipe_id, rating, comment):
        super().__init__(review_id=review_id, user_id=user_id, recipe_id=recipe_id, rating=rating, comment=comment)
        self.review_id = review_id
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.rating = rating
        self.comment = comment
