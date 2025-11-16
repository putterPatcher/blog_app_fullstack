from nosql_schema_check.model import Model

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
    '''
        use {} with fields for dict,
        use ('list', type) for list with type
        use 'type' for type
    '''
    Schema={
        # "_id": "str",
        "abc": 'int',
        "bcd": ('list', 'str'),
        "acd": {"abc": 'str'}
    }
    '''
        validations for schema: function that returns True or False.
    '''
    Validations={
        # "_id": None,
        "abc": num,
        "bcd": string
    }
    '''
        default fields: use function that returns value qas value for the field key.
    '''
    Default={
        "abc":lambda:25,
        "bcd":lambda:["Shantanu"],
        "extra":lambda:"Kor"
    }

Test.generate()
