import json


class StringHandler:
    def __init__(self, string):
        self.d_string = json.loads(str(string)) if not isinstance(string, dict) else string
        self.keys = []
        self.values = []

    def get_dict(self):
        return self.d_string

    def get_keys(self):
        return list(self.d_string.keys())

    def get_items(self, t_string=None, t_list=None, r_path=[]):
        if t_string:
            for key, value in t_string.items():
                if isinstance(t_string[key], dict):
                    r_path.append(key)
                    print('is dict')
                    self.get_items(t_string[key], r_path=r_path)
                elif isinstance(t_string[key], list):
                    r_path.append(key)
                    print('is list')
                    self.get_items(t_list=t_string[key], r_path=r_path)
                else:
                    print(f'key:{key}, value:{value}, path:{r_path}')
        elif t_list:
            for value in t_list:
                if isinstance(value, dict):
                    print('is dict')
                    self.get_items(t_string=value, r_path=r_path)
                elif isinstance(value, list):
                    print('is list')
                    self.get_items(t_list=value, r_path=r_path)
                else:
                    print(f'value:{value}, path:{r_path}')
        else:
            for key, value in self.d_string.items():
                # recover r_path
                r_path = []
                if isinstance(self.d_string[key], dict):
                    r_path.append(key)
                    print('is dict')
                    self.get_items(t_string=self.d_string[key], r_path=r_path)
                elif isinstance(self.d_string[key], list):
                    r_path.append(key)
                    print('is list')
                    self.get_items(t_list=self.d_string[key], r_path=r_path)
                else:
                    print(f'key:{key}, value:{value}, path:{r_path}')


if __name__ == "__main__":
    dict_string = {
        "dict": {"name": "dict1", "jd": {"j": "job", "d": "description"}},
        "list": [{"name": "dict2", "age": 5}, {"name": "dict3", "age": 7, "jd": {"j": "job", "d": "description"}}]
    }
    json_string = '''{
        "dict": {"name": "dict1", "jd": {"j": "job", "d": "description"}},
        "list": [{"name": "dict2", "age": 5}, {"name": "dict3", "age": 7, "jd": {"j": "job", "d": "description"}}]
    }'''
    sh = StringHandler(json_string)
    sh.get_keys()
    sh.get_items()
