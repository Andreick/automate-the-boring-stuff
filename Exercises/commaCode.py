#Program to add commas to strings with list items

def spam_func(spam):
    #Function that returns one single string with the values from the list followed by commas
    string = ''
    for itens in spam:
        if spam.index(itens) == len(spam) - 2:
            string += (itens + ', and ')
        elif spam.index(itens) == len(spam) - 1:
            string += (itens + '.')
        else:
            string += (itens + ', ')
    return string

spam = []        
while True:
    value = input('Enter list values (enter nothing to stop): ')
    if value == '':
        break
    spam.append(value)
string = spam_func(spam)
