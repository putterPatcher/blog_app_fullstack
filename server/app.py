from utils.middleware import generate_functions
from controllers import home, blog, admin
from utils.connect import app
from models import blog, test

# blog.Blog.print_schema()
test.Test.print_schema()
# print(blog.Blog.check_data({"asdfs": 'fds'}))
print(test.Test.check_data({"dsf": "sf", "abc": 5, "bcd": "asdfg"}))
print(test.Test.check_data({"abc": 4, "bcd": "asdfgh"}))