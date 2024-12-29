list1=[0,1,2,3,4,5,6,7,8,9,"A","B"]
list2=[0,1,2,3,4]
list3=[0,1,2,3,4,5,6,7,8,9,"A","B"]
list4=[0,1,2,3,4]


def calculadora (entrada1, operacion, entrada2):
    #parte de valor 1:
    digito1_1=str(list2[int(entrada1//12)])
    digito1_2=str(list1[int(entrada1%12)])
    valor1=float(digito1_1+digito1_2)
    #parte de valor 2
    
    digito2_1=str(list2[int(entrada2//12)])
    digito2_2=str(list1[int(entrada2%12)])
    valor2=float(digito2_1+digito2_2)
    if operacion==str("suma") or "+":
        return float(valor1+valor2)
    
entrada1 = float(input("inserte primer valor"))
operacion=str(input("inserte operación"))
entrada2 = float(input("inserte segundo valor"))
print (calculadora(entrada1,operacion,entrada2))
