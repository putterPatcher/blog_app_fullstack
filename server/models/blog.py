from nosql_schema_check.model import Model
from utils.connect import collection

class Blog(Model):
    '''
        name = name of model (capitalized)
    '''
    name = 'blog'
    '''
        Schema=dict[field_name, datatypes tuples]
    '''
    Schema={
        "heading": 'str',
        "image_urls": ('list', {"name": 'str', "age": 'int'}),
        "content": {"abc": 'int', "bcd": 'str'},
        "created_at": 'str',
        "deleted_at": 'str',
        "modified_at": 'str',
    }
    Validations={
        "content": {"abc":lambda i:i < 10, "bcd":lambda s:len(s) < 10},
    }
    Required=["heading", "image_urls", "content", "created_at", "modified_at"]
    blog=collection

Blog.generate()
