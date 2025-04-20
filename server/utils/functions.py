def run_middlewares(*args):
    for i in args:
        res = i()
        if not res:
            continue
        else:
            return res
