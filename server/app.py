from utils.middleware import generate_functions
from controllers import home, blog, admin
from utils.connect import app
from models import blog

blog.Blog.print_schema()
print(blog.Blog.check_data({"asdfs": 'fds'}))