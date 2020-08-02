class Weight:
    def __init__(self,gram,kilo=0):
        if(kilo==0):
            self.gram=gram%1000
            self.kilo=int(gram/1000)
        else:
            self.gram=gram
            self.kilo=kilo

#main
w=Weight(1500)
w1=Weight(700,1)
print(w.gram,w.kilo)
print(w1.gram,w1.kilo)