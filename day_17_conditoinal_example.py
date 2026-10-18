import math
a,b,c=map(int,(input("enter value of a,b,and c: ").split()))
d=b**2-4*a*c
print(f"determinant={d}")



if d>0 :
    r1=(-b+math.sqrt(d))/(2*a)
    r1=(-b-math.sqrt(d))/(2*a)
elif d==0:
    r1=r2=-b/(2*a)
else:
    real=-b/(2*a)
    imag=math.sqrt(-d)/(2*a)
    print(f"r1=(real)+(imag)+j")
    print(f"r2=(real)-(imag)+j")
    


    