class Paths:
    home="/home"
    blog="/blog"
    admin="/admin"

class AdminPaths:
    path = lambda s: s
    login=path("/login")
    logout=path("/logout")
    add_blog=path("/add_blog")
    update_blog=path("/update_blog/<id>")
    delete_blog=path("/delete_blog/<id>")

class BlogPaths:
    path = lambda s:s
    get_blog=path("/get_blog/<id>")

class HomePaths:
    path = lambda s:s
    get_blogs=path("/get_blogs")
