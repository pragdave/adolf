progress = 0
cont = 1
multiplier = 1
clickmulti = 1


print("Press enter for progress or something!")

def theOnlyfunction():
    global progress
    global multiplier
    while progress < (50*clickmulti):
        doit = input()
        if doit == (''):
            progress += multiplier
            print (progress)
def Ilied():
    global multiplier
    global clickmulti
    global progress
    global multiplier
    print('')
    print ('CONGRATS! YOU GOT TO',(progress),'AND NOW YOU GET',(multiplier*2),'PER ENTER!')
    multiplier *= 2
    clickmulti *= 2.5

while cont == 1:
    theOnlyfunction()
    Ilied()
