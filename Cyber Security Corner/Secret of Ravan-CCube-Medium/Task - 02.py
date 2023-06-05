import pyzipper
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ';', ':', '"', "'", '<', '>', '?', ',', '.', '/', '`', '~']
known_password_dict = {'n':1, '_':2, '^':3, '`':5, 'W':6,'5':8}

known=list(known_password_dict)
known.insert(3,'')
known.insert(6,'')

for i in characters:
    known[3]=i
    for j in  characters :
        known[6]=j
        pw = ''.join(known)
        file_name = 'Cyber Security Corner\Secret of Ravan-CCube-Medium\The_secret.zip'
        try:
            with pyzipper.AESZipFile(file_name) as f:
                f.extractall(path='Cyber Security Corner\Secret of Ravan-CCube-Medium', pwd = bytes(pw, 'utf-8'))
                print("Correct password:",pw)
        except :
            print("failed:",pw)