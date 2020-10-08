class DataCollector(func,**kwargs):
    from generator import Generator
    from time import time
    def run(self, function, size_of_dataset, **kwargs):
        data = self.gen.generate(size_of_dataset)
        start = time.time()
        function(data)
        finish = time.time()
        return finish - start
    
    # def full_run(self):
        

    def __init__(self,generator_function):
        self.gen = Generator(generator_function)


# gen = Generator(gen_function= function_to_generate_sequences)
#            points = []
#            for i in range(sequence_min, sequence_max, step):
#                 data = gen.generate(i)
#                 start = time()
#                 function_to_decorate(data)
#                 t = time() - start
#                 points.append((i, t))
#             plt.plot(points[:][0], points[:][1])
#             plt.show()
#             return function_to_decorate(*function_to_decorate_args, **function_to_decorate_kwargs)
