import string
import re

class Openfile:
    def __init__(self): #inicializo la clase, defino argumentos
        """self.archivo = archivo #atributo inicial de la clase
        print("Esta clase abre y procesa archivos") #metodo inicial de la clase"""


    def file_lowercase(self,fileUsu):
        try:
            fhandle = open(fileUsu)
        except:
            print(">>> El archivo ingresado no fue encontrado")
            exit()
        for line in fhandle:
            line = line.rstrip()
            print(line.lower())
    

    def file_uppercase(self,fileUsu):
        try:
            fhandle = open(fileUsu)
        except:
            print(">>> El archivo ingresado no fue encontrado")
            exit()
        for line in fhandle:
            line = line.rstrip()
            print(line.upper())
        

    def file_countwords(self,fileUsu):
        wordsDict = {}
        try:
            fhandle = open(fileUsu)
        except:
            print(">>> El archivo ingresado no fue encontrado")
            exit()
        for lines in fhandle:
            lines = lines.rstrip()
            lines = lines.lower()
            lines = lines.translate(lines.maketrans("", "", string.punctuation))
            lines = lines.translate(lines.maketrans("", "", "1234567890"))
            wordsKeys = lines.split()
            #print(lines)
        
            for words in wordsKeys:
                wordsDict[words] = wordsDict.get(words, 0) + 1

        templist = []
        tuplist = wordsDict.items()

        for key, val in tuplist:
            nuevatup = (val, key)
            templist.append(nuevatup)

        ordenLista = sorted(templist, reverse = True)

        for val, key in ordenLista:
            print(key, val)


    def file_mailsfinder(self,fileUsu):
        mailsList = []
        contador = 0
        try:
            fhandle = open(fileUsu)
        except:
            print(">>> El archivo ingresado no fue encontrado")
            exit()
        
        for lines in fhandle:
            lines = lines.rstrip()
            mailsRe = "\s[^<](\S+@\S+[^;])\s"
            if re.search(mailsRe, lines):
                mails = re.findall("\s(\S+@\S+)\s", lines)
                #print(mails) #dbg
                
                if mails[0] not in mailsList:
                    mailsList.append(mails[0])
                    mailsList.sort()
                else:
                    continue
                
        if len(mailsList) == 0:
            print(">>> No se encontraron resultados")
            exit()
            
        else:   
            print(">>> Los correos detectados en el archivo", fileUsu, "fueron:\n") 
            while contador < len(mailsList):
                print(mailsList[contador])
                contador = contador + 1