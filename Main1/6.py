#function

'''
To define the function we have to use
def for defining function
def function_name():
    body of the function

To call the function we have to use function_name()
'''

def name():
  print('Bitcoint to Rupees')

def bitcoin_to_rs(btc):
    amount = btc * 712343
    print(btc,' ',int(amount))
name()
bitcoin_to_rs(1)
bitcoin_to_rs(1.34)