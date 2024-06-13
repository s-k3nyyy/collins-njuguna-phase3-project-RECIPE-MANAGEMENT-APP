from .base import Base

class User(Base):
    def __init__(self, user_id, username, email, password):
        super().__init__(user_id=user_id, username=username, email=email, password=password)
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
