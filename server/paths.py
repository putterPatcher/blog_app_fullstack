class Paths:
    home="/"
    blog="/blog/<id>"
    admin="/admin"

class AdminPaths:
    path = lambda s:Paths.admin + s
    login=path("/login")
    logout=path("/logout")
    add_blog=path("/add_blog")
    update_blog=path("/update_blog")
    delete_blog=path("/delete_blog")

