class employee:
    like_marks = 100
    pass

rohan = employee()
rohan.name = "Rohan"
rohan.marks = 45

rakib = employee()
rakib.name = "Rakib"
rakib.marks = 50

print(rakib.name)
print(rohan.name)
print(rohan.like_marks)
rakib.like_marks = 90
print(rakib.like_marks)
print(rakib.__dict__)
print(rohan.__dict__)
