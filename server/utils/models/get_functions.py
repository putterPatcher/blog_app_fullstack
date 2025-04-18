def __get_type(item) -> str:return item.__class__.__name__

class Type:
    def __init__(self, item):
        self.type = item.__class__.__name__
        self.value = item if item not in data_types else None
        self.next = None

data_types = ['list', 'tuple', 'dict']

def get_record_type(item: any):
    ret = {}
    if __get_type(item) == 'dict':
        for i in item.keys():
            ret[i] = Type(item[i])
            val = item[i]
            key = i
            ret[key].next = get_record_type(val)       
        return ret
    elif (type:=__get_type(item)) == 'list' or type == 'tuple':
        ret = []
        for i in item:
            ret.append(type:=Type(i))
            if type in data_types:
                ret[-1].next = get_record_type(i)
        return ret
    else:
        Type(item)
    
def verify_data_type(data, *args, **kwargs):
    ret = {}
    try:
        if __get_type(data) == 'dict':
            for i, j in kwargs.items():
                if data[i].type != j[0]:raise Exception(data[i].type+" != "+j[0])
                if data[i].type == 'dict' and (val:=data[i].next):
                    verify_data_type(val, **j[1])
                if data[i].type == 'list' or 'tuple' and (val:=data[i].next):
                    verify_data_type(val, j[1])
        elif __get_type(data) == 'tuple' or __get_type(data.type) == 'list':
            for i in data:
                if i.type != args[0]:raise Exception(i.type+" != "+args[0])
                if i.type == 'dict' and (val:=data[i].next):
                    verify_data_type(val, **j[1])
                if i.type == 'list' or 'tuple' and (val:=data[i].next):
                    verify_data_type(val, j[1])
        else:
            if data.type != args[0]:raise Exception(data.type+" != "+args[0])
        return True
    except Exception as e:
        print(e)
        return False