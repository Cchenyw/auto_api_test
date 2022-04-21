import yaml


class YamlHandler:
    def __init__(self, file):
        self.file = file

    def read_yaml(self, encoding='utf-8'):
        """read from yaml"""
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, data, encoding='utf-8'):
        """write to yaml"""
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(f.write(data, stream=f, allow_unicode=True))


yaml_data = YamlHandler('../configs/config.yaml').read_yaml()
