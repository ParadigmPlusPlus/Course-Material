for i in range (10):
    print(i, end=", ");
print();

for i in range (10, 0, -1):
    print(i, end=", ");
print();

string = "String"
for char in string:
    print(char, end=" ");
print();

for i in range (len(string) - 1, -1, -1):
    print(string[i], end=" ");
print();


counter = 0;
while counter != 10:
    print(counter, end="");
    counter += 1;
print();

counter = 10;
while counter != 0:
    print(counter, end="");
    counter -= 1;