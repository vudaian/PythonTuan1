a = [1,1,2,3,5,8,13,21,34,55,88]
a.sort();
b = [1,3,4,5,7,88,66,59,40,54]
b.sort();
c=[]
d=[]
e=[]
for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[i]==b[j]:
            c.append(a[i])
            break;
print('Ham trung nhau:', c);
k = int();
for i in range(0, len(a)):
    k=0
    for j in range(0, len(c)):
        if a[i]==c[j]:
            k=1;
    if k != 1:
        d.append(a[i]);
for i in range(0, len(b)):
    k=0
    for j in range(0, len(c)):
        if b[i]==c[j]:
            k=1
    if k != 1:
        e.append(b[i]);
print('Ham a duoc update ', d)
print('Ham b duoc update ', e)