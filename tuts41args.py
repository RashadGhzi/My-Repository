
def args(normal,*item,**item1):
    print(normal)
    for logic in item:
        print(logic)
    for key, value in item1.items():
        print(f"{key} marks is {value}")

n = ("Rashad", "Harryy", "Lucky", "Rocky")
key_value = {"Rashad":20,"Harry":50,"Rony":20,"Habib":40}
print(args("Logic",*n,**key_value))