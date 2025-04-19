from utils.models.model import Model

class Blog(Model):
    '''
        name = name of model (capitalized)
    '''
    name = 'blog'
    '''
        Schema=dict[field_name, datatypes tuples]
    '''
    Schema={
        "_id": 'str',
        "heading": 'str',
        "image_urls": ('list', {"name": 'str', "age": 'int'}),
        "content": {"abc": 'int', "bcd": 'str'},
        "created_at": 'str',
        "deleted_at": 'str',
        "modified_at": 'str',
    }
    '''
        Validations=dict[field_name, validations tuple]
    '''
    Validations={
        "_id": None,
        "heading": None,
        "image_urls": {"name": None, "age": None},
        "content": {"abc": 'int', "bcd": 'str'},
        "created_at": None,
        "deleted_at": None,
        "modified_at": None,
    }

Blog.generate()