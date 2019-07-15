



from array import array
class PythonArray():

    def __init__(self, type, data = []):
        self._array = array(type, data)
    
    def __count__(self):
        return len(self._array)


    

def generator(n, count):
    index = 0
    last = n
    r = []
    while index < count:
        last = last + index
        r.append(last)
        index += 1
    
    return r


g = generator(10, 10)
print(g)