text = input("Please, enter your text there: ")

qr = text[0]
qr_2 = text[-1]

text_2 = text.swapcase()

qs = input("Enter the symbol the quantity of which you want to khow(' ', '-', '/', ',', '.' and others): ")

qs_2 = text.count(qs)

print(f"first symbol: {qr}, \nlast symbol: {qr_2}, \ntext in different register: {text_2}, \nquantity of symbols: {qs_2}")