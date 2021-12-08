def sum(x):
    s=0;
    while(x>0):
        s=s+x%10;
        x=int(x/10);
    return s;
x=int(input("Nhap 1 so ng.duong:"));
print('tong cac chu so:',sum(x));