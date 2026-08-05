''' class Pravi:
    def __init__(self):
        print("started")

pra= Pravi()
pra.name="pravinayak"
pra.add="bynepalli"
print(pra.name)
pra2=Pravi()
pra2.name="manivenkat"
pra2.add="nrp"
print(pra2.name) '''


class Pravi:
    def __init__(self,name,address):
        self.name=name
        self.adress=address
        self.fol=0

new1= Pravi("pravi","bynepali")
print(new1.name)
print(new1.fol)

new2= Pravi("mani","nrp")
print(new2.name)



