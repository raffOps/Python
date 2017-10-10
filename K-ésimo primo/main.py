x=0
y=1
quantidade=int(input("\nDigite quantos numeros primeiros vc  deseja ver: "))

while(quantidade>0):
    print("\n", x)
    z=x
    x=y
    y+=z
    quantidade-=1
