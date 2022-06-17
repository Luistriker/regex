import re 
def Dna(sequencia):
    string = ""
    palavra = ""
    i = 0
    while i < (len(sequencia)):
        if((3+i) <= (len(sequencia))):
            palavra = sequencia[i:3+i]
            if(re.search("UUU",palavra) or re.search("UUC",palavra)):
                string += "Phenylalanina;"
            elif(re.search("AUU",palavra) or re.search("AUC",palavra) or re.search("AUA",palavra)):
                string += "Isoleucina;"
            elif(re.search("AUG",palavra)):
                string += "Methionina;"
            elif(re.search("GUU",palavra) or re.search("GUC",palavra) or re.search("GUA",palavra) or re.search("GUG",palavra)):
                string += "Valina;"
            elif(re.search("UCU",palavra) or re.search("UCC",palavra) or re.search("UCA",palavra) or re.search("UCG",palavra)):
                string += "Serina;"
            elif(re.search("CCU",palavra) or re.search("CCC",palavra) or re.search("CCA",palavra) or re.search("CCG",palavra)):
                string += "Prolina;"
            elif(re.search("ACU",palavra) or re.search("ACC",palavra) or re.search("ACA",palavra) or re.search("ACG",palavra)):
                string += "Threolina;"
            elif(re.search("GCU",palavra) or re.search("GCC",palavra) or re.search("GCA",palavra) or re.search("GCG",palavra)):
                string += "Alanina;"
            elif(re.search("UAU",palavra) or re.search("UAC",palavra)):
                string += "Tyrosina;"
            elif(re.search("UAA",palavra) or re.search("UAG",palavra)):
                string += "Stop(Ochre);"
            elif(re.search("CAU",palavra) or re.search("CAC",palavra)):
                string += "Stop(Amber);"
            elif(re.search("CAA",palavra) or re.search("CAG",palavra)):
                string += "Histidina;"
            elif(re.search("AAU",palavra) or re.search("AAC",palavra)):
                string += "Glutamina;"
            elif(re.search("AAA",palavra) or re.search("AAG",palavra)):
                string += "Asparagina;"
            elif(re.search("GAU",palavra) or re.search("GAC",palavra)):
                string += "Ácido Aspartico;"
            elif(re.search("GAA",palavra) or re.search("GAG",palavra)):
                string += "Ácido Glutaminico;"
            elif(re.search("UGU",palavra) or re.search("UGC",palavra)):
                string += "Cystina;"
            elif(re.search("UGA",palavra)):
                string += "Stop(Opal);"
            elif(re.search("UGG",palavra)): 
                string += "Tryptophan;"
            elif(re.search("CGU",palavra) or re.search("CGC",palavra) or re.search("CGA",palavra) or re.search("CGG",palavra)):
                string += "Arginina;"
            elif(re.search("AGU",palavra) or re.search("AGC",palavra)):
                string += "Serina;"
            elif(re.search("AGA",palavra) or re.search("AGG",palavra)):
                string += "Arginina;"
            elif(re.search("GGU",palavra) or re.search("GGC",palavra) or re.search("GGA",palavra) or re.search("GGG",palavra)):
                string += "Glycina;"
            else:#(re.search("UUA",palavra) or re.search("UUG",palavra) or re.search("CUU",palavra) or re.search("CUC",palavra) or re.search("CUA",palavra) or re.search("CUG",palavra)):
                string += "Leucina;"
        else:
            break
        i+=2
    return string

def toxins():
    path = input("Digite o nome do arquivo:")
    print("\n")
    string = ""
    header = []
    sequences53 = []
    sequences35 = []
    with open(path,"r") as pl:
        for l,line in enumerate(pl):
            if(re.search(">",line)):
                header.append(line)
                if(l != 0 ):
                    sequences53.append(string)
                    string = ""
            else:
                string += line
        sequences53.append(string)
        string = ""

    for i in sequences53:
        for y in i:
            if( y == "C"):
                string += "G"
            elif(y == "G"):
                string += "C"
            elif(y == "A"):
                string += "U"
            else:
                string += "A"
        sequences35.append(string)
        string = ""
    
    with open("toxins_3-5.txt","w") as pl:
        for i,j in zip(header,sequences35):
            pl.write(i)
            pl.write(j)
            pl.write("\n")
    
    with open("toxins-amino.txt","w") as pl:
        for i,line in enumerate(sequences35):
            x = "Sequencia - " + str(i)
            pl.write(x)
            pl.write("\n")
            pl.write(Dna(line))
            pl.write("\n\n")
    
   

        
                     
    
    

toxins()