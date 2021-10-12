class item():
    liker_boy = 50
    @classmethod
    def change_value(cls,value):
        cls.liker_boy = value


item.change_value(500)
lucky = item()
print(lucky.liker_boy)