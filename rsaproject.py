x = 1 
while x == 1:
    print ('would you like to encrypt, decrypt, or exit?')
    answer = raw_input('?: ')
    if answer == 'exit' or answer == 'Exit':
        print ('Goodbye')
        x = 2
    if answer == 'encrypt' or answer == 'Encrypt':
        print ('What would you like to encrypt?')
        message = raw_input('?: ')
        
    if answer == 'decrypt' or answer == 'Decrypt':
        print ('What would you like to decrypt?')
        