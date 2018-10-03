

def Sound():
    sauti = ""
    sautii = sauti.lower()
    while(sautii!=("cat" and "dog" and "cow")):
        sauti = input('Enter the name of the animal: ')
        sautii = sauti.lower()
        if sautii == "dog":
            print("barks")
        elif sautii == "cat":
            print("meoow")
        elif sautii == "cow":
            print("MOOOOO")
        else:
            print("choose either dog,cat or cow")
            
Sound()
