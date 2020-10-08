def decorator(start,end):
    def actual_decorator(F):
        def cycle(start,end):
            for i in range(start,end):
                F()
                print(i)
        return cycle(start,end)
    return actual_decorator


@decorator(2,7)
def a():
    print("from a")
    