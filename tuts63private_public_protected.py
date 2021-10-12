# Public
# Protected
# Private

class like():
    public = 50
    _protected = 60
    __private = 100

harry = like()
print(harry.public)                 # Thats how to access public value
print(harry._protected)             # Thats how to access protected value
print(harry._like__private)         # Thats how to acces private value