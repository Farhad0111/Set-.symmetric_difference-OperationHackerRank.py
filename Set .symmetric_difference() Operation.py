class Farhad:
    def __init__(self):
        self.i=int(input())
        self.a=set(input().split())
        self.j=int(input())
        self.b=set(input().split())
    def Faru(self):
        print(len(self.a.symmetric_difference(self.b)))
farhad=Farhad()
farhad.Faru()