
scores = 1
stringItem = ["Python is a good", "This is snake",
                 "Harry is is is a good boy", "Subscribe to code with harry","We like to meet with Harry vai", "Harry vai is a good person"]
sorted_item = sorted(zip(scores,stringItem),reverse=True)
for serial, item in sorted_item:
        if serial > 0:
            print(f"\"{item}\"")