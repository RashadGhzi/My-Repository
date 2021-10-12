a = [1,2,3,4,5]

revlist1 = a.copy()
revlist1.reverse()
print(f'The list of {a} item reverse 1 is {revlist1}')

revlist2 = a.copy()
itemrev = revlist2[::-1]
print(f'The list of {a} item reverse 2 is {itemrev}')

revlist3 = a.copy()
for item in range(len(revlist3)//2):
    revlist3[item],revlist3[len(revlist3)-item-1] = revlist3[len(revlist3)-item-1],revlist3[item]

print(f'The list of {a} item reverse 3 is {revlist3}')
