from Doubly_positional import PositionalList

plist= PositionalList()

for i in range(10):
    plist.add_last(i)

key=7
for i in plist.__iter__():
    if i ==key:
        print("Present")