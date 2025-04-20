from flask import Request, Response

def __run_middlewares(request: Request, *middlewares, **kwargs):
    try:
        for i in middlewares:
            res = i(request, **kwargs)
            if type(res) == Request:
                request = res;
            elif type(res) == Response:
                return res
            else:
                raise Exception("{} is not Request".format(type(res)))
        return request
    except Exception as e:
        if type(request) != Request:
            raise Exception("{} is not Request.".format(type(request)))
        return None
    
def __run_controller(request: Request, controller, **kwargs):
    try:
        if type(request) != Request:
            raise Exception("{} is not Request.".format(type(request)))
        return controller(request, **kwargs)
    except Exception as e:
        if type(request) != Request:
            raise Exception("{} is not Request.".format(type(request)))
        return None
    
def process_request(request: Request, controller, *middlewares, **kwargs):
    try:
        if type(res:=__run_middlewares(request, *middlewares, **kwargs)) == Response:
            return res
        elif type(res) == Request:
            res = __run_controller(res, controller, **kwargs)
            if type(res) == Response:
                return res
            else:
                print("{} is not Response.".format(type(res)))
    except Exception as e:
        print(type(e)+"occured while processing request.")
        return request
