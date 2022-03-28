def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy Smokes, Fermat was Wrong!")
    else:
        print("No, that doesn't work.")

a = int(input("Input a\n"))
b = int(input("Input b\n"))
c = int(input("Input c\n"))
n = int(input("Input n\n"))

check_fermat(a,b,c,n)