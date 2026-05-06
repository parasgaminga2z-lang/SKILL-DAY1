# store in dictionary
def display(**Kwargs):
    for key , value in Kwargs.items():
        print(f"{key} : {value}")
display(name='para',age= '23', city='sanwaer')

def student(**kwargs):
    print("detail",kwargs)
student(name ='apara',city='snawer',age='23')