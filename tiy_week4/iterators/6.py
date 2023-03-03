class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration 
        
myclass = Mynumbers()
myit = iter(myclass)

for x in myit:
    print(x)