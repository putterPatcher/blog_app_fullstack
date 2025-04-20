from utils.models.model import Model

def num(n):
    if n < 10:
        return True
    return False

def string(s):
    if len(s) < 10:
        return True
    return False


class Test(Model):
    name = 'test'
    Schema={
        # "_id": "str",
        "abc": 'int',
        "bcd": ('list', 'str')
    }
    Validations={
        # "_id": None,
        "abc": num,
        "bcd": string
    }

Test.generate()
