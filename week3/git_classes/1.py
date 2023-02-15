class String1():
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())

ans = String1()
ans.getString()
ans.printString()