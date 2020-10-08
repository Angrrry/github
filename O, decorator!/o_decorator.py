#TODO: настройка количества циклов на одной длине датасета.
#TODO: полное удаление объектов из памяти.Вероятно, выбросы возникают из-за того, что что-то висит в памяти
import matplotlib.pyplot as plt
from generator import Generator
from time import time,sleep

def decorator_maker_with_arguments(function_to_generate_sequences, sequence_min, sequence_max, step, cycles_to_average_data, **decorator_extra_attributes):
    def actual_decorator(function_to_decorate):

        def perform_data_collection(function_to_generate_sequences, sequence_min, sequence_max, step, cycles_to_average_data,**decorator_extra_attributes):
                gen = Generator(gen_function= function_to_generate_sequences)
                X,Y = [],[]
                #Медиана нужна, чтоб убрать выбросы. Усреднение с этим справляется хуже.
                median = lambda list_of_data: sorted(list_of_data)[len(list_of_data)//2]
                for i in range(sequence_min, sequence_max, step):
                    for j in range(cycles_to_average_data):
                        y = []
                        data = gen.generate(i)
                        start = time()
                        function_to_decorate(data)
                        finish = time()
                        t = finish - start
                        y.append(t)
                    X.append(i)
                    Y.append(median(y))
                return X,Y

        def plot(X, Y, function_to_decorate=function_to_decorate):
            plt.plot(X,Y)
            plt.title(function_to_decorate.__name__)
            plt.xlabel("size of data")
            plt.ylabel("time")
            plt.show()

        return plot(
            *perform_data_collection(
                function_to_generate_sequences, 
                sequence_min, sequence_max, step,
                cycles_to_average_data,
                **decorator_extra_attributes)
            )

    return actual_decorator


#  ######## ########  ######  ########  ######
#     ##    ##       ##    ##    ##    ##    ##
#     ##    ##       ##          ##    ##
#     ##    ######    ######     ##     ######
#     ##    ##             ##    ##          ##
#     ##    ##       ##    ##    ##    ##    ##
#     ##    ########  ######     ##     ######


# @decorator_maker_with_arguments(Generator.generate_list,10,1000,1,10)
def max(seq):
    return max(seq)

# max([1,2,3])


# @decorator_maker_with_arguments(Generator.generate_list, 10, 1000, 1,100)
def stupid_max(seq):
    mx = seq[0]
    for i in seq:
        mx = i if i > mx else mx
    return mx

# @decorator_maker_with_arguments(lambda x:x,1,1000,1,10)
def base_math(x):
    return x**2


#TODO:Рекурсия сыпется. Что-то с пространством имён
#SOLVED: Если обернуть рекурсивную функцию, всё ок.
# @decorator_maker_with_arguments(lambda x:x,10,5000,2,5)
def rec_wrapped(n):
    import sys
    sys.setrecursionlimit(7000)
    def rec(n):
        return 1 if n==1 else rec(n-1)+n
    return rec(n)


# print(rec_wrapped(6))
## O(2^n)
# @decorator_maker_with_arguments(lambda x: x, 1, 20, 1, 3)
def rec2_wrapped(n):
    import sys
    sys.setrecursionlimit(7000)
    def rec(n):
        if n>0:
            rec(n-1)
            rec(n-1)
    rec(n)

@decorator_maker_with_arguments(Generator.generate_list,10,1000,5,10)
def sloooow_sorting(input_list):
    def get_min_with_index(input_list):
        miin, i = input_list[0],0
        for index, value in enumerate(input_list):
            if miin > value:
                i, miin= index,value
        return i
    
    sorted_list = []
    copy = input_list.copy()
    while len(copy)>0:
        sorted_list.append(
            copy.pop(get_min_with_index(copy)))
    return sorted_list


