def showSecret(key, msg):
    key, n = key
    plain = [chr((char ** key) % n) for char in msg]
    return ''.join(plain)

my_secrect = [360, 4255, 1984, 360, 4791, 360, 2830, 4970, 4791, 4970, 3608, 1984, 2932, 1924, 3248, 1884, 3608, 1884, 691, 1850, 2701, 3608, 4590, 1268, 5120]

print('*'*29+'\n Wellcome To My Secret Vault \n'+'*'*29)

try:
    key1 = int(input('Please Input 1st Key : '))
    key2 = int(input('Please Input 2nd Key : '))
except:
    print('Opps.....')

final_key = (key1,key2)

try:
    print (f"Your Falg is : {showSecret(final_key,my_secrect)}")
except:
    print('Opps.....')