# name of student: Maks Ratajczak
# number of student:99062843
# purpose of program: Change uit rekenen
# function of program: hoeveel munten moet je terug geven
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

if change > 0: #
  coinValue = 500 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below:
    euro5 = 0
    euro2 = 0
    euro1 = 0
    cent50 = 0
    cent20 = 0
    cent10 = 0
    cent5 = 0
    cent2 = 0
    if coinValue == 500:
      euro5 = nrCoinsReturned
      coinValue = 200
    elif coinValue == 200:
      euro2 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      euro1 = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      cent50 = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      cent20 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      cent10 = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      cent5 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      cent2 = nrCoinsReturned
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print(f"{euro5} : 5 euro munt,{euro2} : 2 euro munt,{euro1} : 1 euro munt,{cent50}: 50 cent munt,{cent20} : 20 cent munt,{cent10} : 10 cent munt,{cent5} : 5 cent munt,{cent2} : 2 cent munt terug gegeven")
  print('done')