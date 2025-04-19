_Models = {}

class Type:
    def __init__(self, type, validation):
        self.__type = type
        self.__validation = validation
    @property
    def type(self):return self.__type;
    @property
    def validation(self):return self.__validation;

    def __str__(self):
        return "{}".format(self.__type)

class NP_Type:
    def __init__(self, type, value):
        self.__type = type
        self.__value = value
    @property
    def type(self):return self.__type;
    @property
    def value(self):return self.__value;


class Model:
    __Model_Schema = None

    @staticmethod
    def __get_type(item) -> str:return item.__class__.__name__
    
    @classmethod
    def __get_record_type(cls, schema: any, *args, **kwargs) -> NP_Type | bool:
        try:
            if (type:=cls.__get_type(schema)) == 'dict':
                ret = {}
                for i in schema.keys():
                    if (type:=cls.__get_type(data:=schema[i])) == 'tuple':
                        '''
                            data = (type), kwargs[i] = validation
                            data = ('list', type), kwargs[i] = validation
                            data = ('list', dict), kwargs[i] = dict
                            data = ('list', tuple), kwargs[i] = with something
                        '''
                        if i not in kwargs.keys():
                            raise Exception("validation for '{}' field does not exist.".format(i))
                        ret[i] = cls.__get_record_type(data, *(kwargs[i],))
                    elif type == 'dict':
                        '''
                            data = dict, kwargs[i] = dict
                        '''
                        ret[i] = cls.__get_record_type(data, **kwargs[i])
                    else:
                        '''
                            data = type, kwargs[i] = validation
                        '''
                        print(data, kwargs)
                        ret[i] = Type(data, kwargs[i])
                    if ret[i] == False:
                        raise Exception()
                return NP_Type('dict', ret)
            elif type == 'tuple':
                if schema[0] == 'list':
                    data = None
                    if (type:=cls.__get_type(data:=schema[1])) == 'dict':
                        '''
                            data = dict, args = (dict)
                        '''
                        data = cls.__get_record_type(data, **args[0])
                    elif type == 'tuple':
                        if (data[0]) == 'list':
                            if (type:=cls.__get_type(data[1])) == 'dict':
                                '''
                                    data[1] = dict, args = (dict)
                                '''
                                data = cls.__get_record_type(data[1], **args)
                            elif type == 'tuple':
                                '''
                                    data[1] = tuple, args = (with something)
                                '''
                                data = cls.__get_record_type(data[1], *args)
                            else:
                                '''
                                    data[1] = type, args = (validation)
                                '''
                                data = Type(data[1], args[0])
                        else:
                            '''
                                data = (type), args = (validation)
                            '''
                            data = cls.__get_record_type(data, *args)
                    else:
                        '''
                            data = type args = (validation)
                        '''
                        data = Type(data, args[0])
                    if data == False:
                        raise Exception()
                    return NP_Type('list', data)
                else:
                    '''
                        schema = (type), args = (validation)
                    '''
                    return Type(schema[0], args[0])
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    def __validate(data, validation):
        try:
            if validation:
                return validation(data)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def __check_data(cls, schema: NP_Type | Type, allow_extra=False, *data, **dict_data):
        try:
            def __check_dict(schema: dict, dic: dict):
                try:
                    schema_keys = list(schema.keys())
                    dic_keys = list(dic.keys())
                    if len(schema_keys) > len(dic_keys):raise Exception("fields {} not present in data.".format([i for i in schema_keys if i not in dic_keys]))
                    if not allow_extra:
                        if len(schema_keys) < len(dic_keys):raise Exception("fields {} not present in schema.".format([i for i in schema_keys if i not in dic_keys]))
                    for i in schema.keys():
                        if (type:=cls.__get_type(dic[i])) == 'dict':
                            cls.__check_data(schema[i], allow_extra, **dic[i])
                        elif type == "list":
                            cls.__check_data(schema[i], allow_extra, *dic[i])
                        else:
                            cls.__check_data(schema[i], allow_extra, *(dic[i],))
                except Exception as e:
                    raise Exception(e)
            def __check_list(schema, list: list[any]):
                try:
                    for i in list:
                        if schema.type != (type:=cls.__get_type(i)):raise Exception(error(type, schema.type))
                        else:
                            if type == 'dict':
                                cls.__check_data(schema.value, allow_extra, **i)
                            else:
                                cls.__check_data(schema.value, allow_extra, *i)
                except Exception as e:
                    raise Exception(e)
            def error(s1, s2):return "got type {}, expected {}".format(s1, s2)
            if (type:=cls.__get_type(schema)) == 'NP_Type':
                if schema.type == 'dict' and len(dict_data) != 0:
                    __check_dict(schema.value, dict_data)
                elif schema.type == 'list' and len(data) != 0:
                    __check_list(schema.value, data)
            elif type == 'Type':
                if (type:=cls.__get_type(data[0])) != schema.type or not cls.__validate(data[0], schema.validation):
                    raise Exception(error(type, schema.type))
            else:
                raise Exception("{} is not a valid type".format(type))
            return True
        except Exception as e:
            raise Exception(e)

    @classmethod
    def check_data(cls, data):
        try:
            return cls.__check_data(cls.__Model_Schema, **data)
        except Exception as e:
            print(e)
            return False

    @classmethod
    def generate(cls):
        '''
            generate the Schema Type object (NP_Type) for model
        '''
        def __generate_schema_object(model_name: str, Schema: dict, Validations: dict):
            try:
                if "_id" not in Schema.keys():
                    raise Exception("field '_id' is not present.")
                type_dict = None
                if type(Schema) == dict and type(Validations) == dict:
                    type_dict = cls.__get_record_type(Schema, **Validations)
                else:
                    raise Exception("Blog.Schema and Blog.Validations must have type dict.")
                if not type_dict:raise Exception("Object creation failed.")
                _Models[name:=model_name.capitalize()] = type_dict
                print("model {} generated successfully.".format(name))
                # print(type_dict.value)
                return type_dict
            except Exception as e:
                print("Error generating model {}".format(model_name.capitalize()))
                print(e)
                return None
        cls.__Model_Schema = __generate_schema_object(cls.name, cls.Schema, cls.Validations)
    
    @classmethod
    def print_schema(cls, schema:NP_Type | Type=None, tab=0):
        start = False
        if schema == None:schema = cls.__Model_Schema;start=True;
        if schema.type == 'dict':
            for _ in range(tab):print("  ", end="")
            print("{")
            for i, j in schema.value.items():
                for _ in range(tab+1 if start else tab+2):print("  ", end="")
                print("FIELD",i, end=" TYPE ");cls.print_schema(j)
            if not start:
                for _ in range(tab+1):print("  ", end="")
                print("},")
            else:print("}")
        elif schema.type == 'list':
            print("[")
            for _ in range(tab+1):print("  ", end="")
            cls.print_schema(schema.value, tab+1)
            for _ in range(tab+1):print("  ", end="")
            print("],")
        else:
            print(str(schema)+",")

