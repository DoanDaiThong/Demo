import math
def InputData():
    print("Nhap 2 so a, b:\n")
    a = int(input("a="))
    b = int(input("b="))
    return a,b
def Tong(a,b):
    c=a+b
    return c
def Hieu(a,b):
    c=a-b
    return c
def Tich(a,b):
    c=a*b
    return c
def Thuong(a,b):
    if(b==0):
        print("Error!, Mau khac 0")
        exit()
    c=a/b
    return c
def main():
    a,b = InputData()
    c=Tong(a,b)
    print(a," + ",b," = ",c)
    c=Hieu(a,b)
    print(a," - ",b," = ",c)
    c=Tich(a,b)
    print(a," * ",b," = ",c)
    c=Thuong(a,b)
    print(a," / ",b," = ",c)
if __name__=="__main__":
    main()