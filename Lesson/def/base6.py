# サブジェネレータ

def sub_sub_generator():
    yield "sub subのyield"
    return "sub subのreturn"

def sub_generator():
    yield "subのyield"
    res = yield from sub_sub_generator()
    print("sub res = {}".format(res))
    return "subのreturn"

def genewrator():
    yield "generatorのyield"
    res = yield from sub_generator()
    print("gen res = {}".format(res))
    return "generatorのreturn"

gen = genewrator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
