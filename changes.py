#Algorithm Solution

def changeCoin ():
    total = int(input('Digite o valor a ser convertido: ')) #solicita a entrada do valor a ser analisado
    #abaixo, foram definidos os valores das moedas
    quarters = 25
    dimes = 10
    nickels = 5
    pennies = 1

    #nessa primeira parte, é analisado a quantidade de moeda começando em quarters
    subtotal = total
    possible1 = []
    nextCoin = quarters
    for i in range (4):
        possible1.append(subtotal // nextCoin)
        subtotal = subtotal - ((subtotal // nextCoin)*nextCoin)
        if nextCoin == quarters:
            nextCoin = dimes
        elif nextCoin == dimes:
            nextCoin = nickels
        elif nextCoin == nickels:
            nextCoin = pennies
    
    #nessa segunda parte, é analisado a quantidade de moeda começando em dimes (considera quarters = 0)
    subtotal = total
    possible2 = [0]
    nextCoin = dimes
    for i in range (3):
        possible2.append(subtotal // nextCoin)
        subtotal = subtotal - ((subtotal // nextCoin)*nextCoin)
        if nextCoin == dimes:
            nextCoin = nickels
        elif nextCoin == nickels:
            nextCoin = pennies
    
    #nessa terceira parte, é analisado a quantidade de moeda começando em nickels (considera quarters = 0, dimes = 0)
    subtotal = total
    possible3 = [0,0]
    nextCoin = nickels
    for i in range (2):
        possible3.append(subtotal // nextCoin)
        subtotal = subtotal - ((subtotal // nextCoin)*nextCoin)
        if nextCoin == nickels:
            nextCoin = pennies
    
    #a possibilidade 4 é constituída apenas de pennies (considera quarters = 0, dimes = 0, nickels = 0)
    possible4 = [0,0,0,total]

    output = [possible1,possible2,possible3,possible4]
    print(output)

changeCoin() #essa linha chama a execução da função criada


