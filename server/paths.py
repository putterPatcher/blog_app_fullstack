class Paths:
    home="/home"
    blog="/blog"
    admin="/admin"

class AdminPaths:
    path = lambda s:Paths.admin + s
    login=path("/login")
    logout=path("/logout")
    add_blog=path("/add_blog")
    update_blog=path("/update_blog")
    delete_blog=path("/delete_blog")

class HomePaths:
    path = lambda s:Paths.home + s
    get_blogs = path('/get_blogs')

class BlogPaths:
    path = lambda s:Paths.blog + s
    get_blog = path('/get_blog/<id>')

