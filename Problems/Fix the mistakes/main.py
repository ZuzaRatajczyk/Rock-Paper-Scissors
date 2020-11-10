text = input()
words = text.split()
web_address = ['www.', 'http://', 'https://']
for address in web_address:
    print('\n'.join(word for word in words if address in word.lower()))