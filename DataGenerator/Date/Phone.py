#https://randommer.io/free-valid-bulk-telephones-generator
# + vs
import random

Phone = "501773858 456577807 211358228 211310728 211140970 459748764 211190534 453113227 575470572 211358238 211135425 211346559 211184749 571282619 211359543 452412394 452441546 690254662 211342590 511711901 211120954 211332610 211310681 211351668 605509462 667211883 458971312 457051243 531732212 457338835 211313207 669635442 454210252 211327569 454518573 211350402 451619832 881638409 211339991 211339079 211336027 211354394 456445234 211356985 211172176 211320851 572656684 666251436 211327674 889053157 454085000 609434639 579677925 211145698 456773186 211342968 211334281 211105542 456716575 211135441 211355799 454900476 458345367 211148905 211337820 211344170 455511639 456190768 456731075 510190749 455985476 515508087 211331521 211166586 454010892 459386270 211313534 211310304 451849382 211141156 211351982 211347285 211337697 454824951 736214053 536583873 211332177 459343076 798845593 458073809 538245135 211343415 572866574 211330498 211324854 211336791 211336913 450277610 211177201 536625365"
PhoneList = []


def stringToList(stringText):
    result = stringText.split()
    return result

PhoneList = stringToList(Phone)
print(len(PhoneList))

def phoneGenerate():
    rndPhone = random.randint(0,len(PhoneList)-1)
    numberPhone = PhoneList[rndPhone]
    #PhoneList.remove(numberPhone)
    return numberPhone
