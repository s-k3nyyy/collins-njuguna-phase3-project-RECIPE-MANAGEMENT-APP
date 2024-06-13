class Base:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        raise NotImplementedError

    @classmethod
    def delete(cls, id):
        raise NotImplementedError

    @classmethod
    def get_all(cls):
        raise NotImplementedError

    @classmethod
    def find_by_id(cls, id):
        raise NotImplementedError
