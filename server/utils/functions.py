from flask import Request, Response
from utils.connect import app, flask

__Error_Response = None

def setErrorResponse(response):__Error_Response = response;

def process_request(request: Request, controller, *middlewares, **kwargs):
    try:
        def __run_middlewares(request: Request, *middlewares, **kwargs):
            try:
                for i in middlewares:
                    res = i(request, **kwargs)
                    if type(res) == Response:
                        break;
            except:
                return __Error_Response
            
        def __run_controller(request: Request, controller, **kwargs):
            try:
                return controller(request, **kwargs)
            except Exception as e:
                return __Error_Response
        if type(res:=__run_middlewares(request, *middlewares, **kwargs)) == Response:
            return res
        elif res == None:
            return __run_controller(request, controller, **kwargs)
    except Exception as e:
        print(str(e)+" occured while processing request.")
        return __Error_Response
