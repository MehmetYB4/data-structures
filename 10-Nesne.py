class araba:
    hiz=0
    renk=""
    teker=4
    def hizlanma(self):
        self.hiz=self.hiz+1


x=araba()
x.hiz=100
x.hizlanma()
x.renk="siyah"
print(str(x.hiz) + " " + x.renk)



