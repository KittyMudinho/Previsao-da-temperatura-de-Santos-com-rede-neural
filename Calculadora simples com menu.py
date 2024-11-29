print('Seja bem-vindo a calculadora em Python')
while 1:
    menu=int(input('\n Escolha o que deseja: \n 1-Soma \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n'))
    num1=float(input('Ótima escolha, agora diga o primeiro número: '))
    num2=float(input('Okay, agora o segundo: '))
    if(menu==1):
        print('Eis aqui sua soma {}' .format(num1+num2))
    if(menu==2):
        print('Eis aqui sua subtração {}' .format(num1-num2))
    if(menu==3):
        print('Eis aqui sua multiplicação {}' .format(num1*num2))
    if(menu==4):
        print('Eis aqui sua divisão {}' .format(num1/num2))
    confirmação=str(input('Deseja realizar mais alguma conta? '))
    if(confirmação=='n'):
        print('Muito obrigado!!')
        break