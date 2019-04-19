for i in range (10):
    print(i, end=" ")
    if i % 2 == 0:
        print("even");
    else:
        print("odd");
        
string = "TextInRandomOrder"
lst = set();
lst.add("T");
lst.add("I");
lst.add("R");
lst.add("O");
print(lst);
counter = 0;
for char in string:
    if char in lst:
        print("Found");
        counter += 1;
print(counter);