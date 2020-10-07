#TODO: Тут всё падает, если попытаться создать словарь str с кастомной длиной. 

import random

class Generator:
    type_unit_gen = {
        'int': lambda data_values_min, data_values_max: random.randint(data_values_min, data_values_max),
        'float': lambda data_values_min, data_values_max: random.uniform(data_values_min, data_values_max),
        # оставил параметры, чтоб лишний раз не менять синтаксис
        'bool': lambda data_values_min, data_values_max: random.randint(0, 1),
        # string будет длины от dvm до dvM. Диапазон в chr - это латиница + часто используемые символы
        
        'string': lambda data_values_min=20, data_values_max=50: ''.join([chr(random.randint(32, 126)) for x in range(random.randint(data_values_min, data_values_max))]),
    }

    def generate_list(list_length, data_values_min=0, data_values_max=255, vartype='int'):
        return [Generator.type_unit_gen[vartype](data_values_min, data_values_max) for i in range(list_length)]
    
    def generate_set(set_length, data_values_min=0, data_values_max=255, vartype='int'):
        return {Generator.type_unit_gen[vartype](data_values_min, data_values_max) for i in range(set_length)}
    
    def generate_dict(dict_length, key_data_values_min=0, key_data_values_max=255, val_data_values_min=0, val_data_values_max=255, key_vartype='string', val_vartype='string'):
        kdvm, kdvM, vdvm, vdvM = key_data_values_min, key_data_values_max, val_data_values_min, val_data_values_max
        key = Generator.type_unit_gen[key_vartype]
        val = Generator.type_unit_gen[val_vartype]
        return {key(kdvm,kdvM):val(vdvm,vdvM) for k in range(dict_length)}
    
    def generate_string(string_length):
        return Generator.type_unit_gen['string'](string_length,string_length)

    def __init__(self, gen_function= generate_list):
            self.generate = gen_function


# x = Generator(Generator)

def test():
    print(Generator.generate_list(5,vartype='string'))
    list_generated = Generator(Generator.generate_list)
    print(list_generated.generate(50))
    
    custom_func_generated = Generator(lambda length: list(range(length)))
    z = custom_func_generated.generate(50)
    print(z)

    dict_generated = Generator(Generator.generate_dict)
    t = dict_generated.generate(20)
    print(t)

    string_generated = Generator(Generator.generate_string)
    q = string_generated.generate(250)
    print(q)
    print(len(q))
    
if __name__=="__main__":
    test()
