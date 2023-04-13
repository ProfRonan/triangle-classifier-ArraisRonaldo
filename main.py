a = int(input("Digite um lado do triângulo: ")) 
b = int(input("Digite outro lado do triângulo: "))
c = int(input("Digite outro lado do triângulo: "))

if a+b > c and a+c > b and b+c > a:
    if a == b and b==c:
        print("Equilátero")
    elif a == b or b == c or c == a:
        print("Isósceles")
    else:
       print("Escaleno")
else:        
    print("Não é um triângulo")
