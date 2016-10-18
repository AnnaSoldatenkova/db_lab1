import pickle

class Model:

    def __init__ (self, file_name = ''):
        self.__comp = []
        self.__hard = []
        self.load(file_name)

    def get_hard (self):
        return self.__hard

    def get_comp (self):
        return self.__comp

    def load (self, file_name):
        try:
            with open(file_name, "rb") as stream:
                self.__comp, self.__hard = pickle.load(stream)
        except:
            self.__comp = []
            self.__hard = []

    def save (self, file_name):
        with open(file_name, "wb") as stream:
            pickle.dump([self.__comp, self.__hard], stream)

    def add_comp (self, name, series, pc_type):
        id = 0
        if self.__comp:
            id = self.__comp[-1]['id'] + 1
        self.__comp.append({'id': id, 'name': name,\
                            'series': series, 'pc_type': pc_type})

    def add_hard (self, id_comp, hdd, video_adapter, memory_module):
        id = 0
        if self.__hard:
            id = self.__hard[-1]['id'] + 1
        self.__hard.append({'id': id, 'id_comp': id_comp, 'hdd': hdd,\
                            'video_adapter': video_adapter, 'memory_module': memory_module})

    def del_hard (self, id, key = 'id'):
        self.__hard = filter (lambda x: x[key] != id, self.__hard)
        
    def del_comp (self, id):
        self.del_hard (id, 'id_comp')
        self.__comp = filter (lambda x: x['id'] != id, self.__comp)

    def update_hard (self, id, key, val):
        res = []
        for x in self.__hard:
            if x['id'] == id:
                x[key] = val
            res.append(x)
        self.__hard = res;
        
    def update_comp (self, id, key, val):
        res = []
        for x in self.__comp:
            if x['id'] == id:
                x[key] = val
            res.append(x)
        self.__comp = res;

    def find (self):
        res = set();
        res_comp = [];
        for el in self.__hard:
            if el['video_adapter'] != None:
                res.add(el['id_comp'])
        for el in self.__comp:
            if el['id'] in res:
                res_comp.append(el)
        return res_comp

    def hard_comp (self, id_comp):
        return filter(lambda x: x['id_comp'] == id_comp, self.__hard)

    
