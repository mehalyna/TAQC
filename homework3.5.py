x = int (input ('Enter amount of money: ' ))
if x>0:
    a = int (x//200)
    a1 = (x%200)
    print ('It is possible to exchange into', a, 'banknotes by 200')
    a1>=100
    b = (a1//100)
    b1 = (a1%100)
    print ('It is possible to exchange into', b, 'banknotes by 100')
    b1>=10
    c = (b1//10)
    c1 = (b1%10)
    print ('It is possible to exchange into', c, 'banknotes by 10')
    c1>=1
    d = (c1//1)
    print ('It is possible to exchange into', d, 'banknotes by 1')
else:
    x<=0
    print ('Enter a positive amount of money: ' )
