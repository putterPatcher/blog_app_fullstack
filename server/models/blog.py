from utils.models.get_functions import get_record_type, verify_data_type

class Blog:
    Schema={
        "heading": ('str',),
        "image_urls": ('list', 'str'),
        "content": ('str',),
    }

blogs = {}

def verify_blog(record):
    data_dict = get_record_type(record)
    blogs["_id"] = data_dict
    return verify_data_type(data_dict, **Blog.Schema)
