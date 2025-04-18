from utils.middleware.get_functions import totalMiddlewares, check_processing

# 4 = total times the middleware is used
# 'verify_admin' = name of the middleware decorator
result = totalMiddlewares(4, 'verify_admin')
print("result: {}".format(result))
if not check_processing():
    pass
else:
    exit(1)
