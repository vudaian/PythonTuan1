a=[1,1,2,6,8,9,4,5,6,45,34,66,44,37,38];
a.sort();
b=[];
for i in range(0, len(a)):
    if a[i] < 30:
        b.append(a[i]);
    else:
        break;
print('list \n',b);
x = int(input(""));
print('Cac so lon hon gia tri vua nhap:');
for i in range(0, len(a)):
    if a[i] > x :
        print(' ',a[i]);
