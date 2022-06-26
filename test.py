class Test(object):
    def __init__(self,x):
        self.x = x
    def update(self):
        self.x = 5
    
kv_dict = {
    0:Test(x=0),
    1:Test(x=5),
    2:Test(x=10),
    3:Test(x=15),
}

for k,v in kv_dict.items():
    print(kv_dict[k].update())