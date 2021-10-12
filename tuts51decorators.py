def func(func1):
    def executer():
        print("Executing time")
        func1()
        print("Executed")
        return like()
    def like():
        print("LIke")
    return executer

@func
def function_1():
    print("You are good boy")

#function_1 = func(function_1)
function_1()