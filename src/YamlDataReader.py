from Types import DataType
from DataReader import DataReader
import yaml 
from yaml.loader import SafeLoader


class YamlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as yml_file:
            file = yaml.load(yml_file, Loader=yaml.FullLoader)
        for line in file:
            for name, subjects in line.items():
                self.key = name
                self.students[self.key] = []
                for subject, rating in subjects.items():
                    self.students[name].append((subject, int(rating)))
        return self.students
