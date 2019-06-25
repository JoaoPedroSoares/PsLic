def (texto)
    for line in texto:
        linha = line
        lista = linha.split(',')
        c = len(lista)

        if c > 140:
            print(lista[1],'...')
        else:
            print (texto)


def conta(valor):
    a = len(valor)
    if a == 10:
        print (valor[0],',',valor[1:3],'Bilhões')
    elif a == 9:
        print (valor[0:3],'Milhões')
    elif a == 11:
        print (valor[0:2],',',valor[2],'Bilhões')





dic = {
    1997: {'filme':'Titanic','US$':2187463944},
    2009: {'filme':'Avatar','US$':2787965087},
    2011: {'filme':'Harry Potter and the Deathly Hallows - Part 2','US$':1341693157},
    2012: {'filme':'Marvels The Avengers','US$':1518812988},
    2013: {'filme':'Frozen','US$':1276480335},
    2015: {
            {'filme':'Avengers: Age of Ultron','US$':1405403694},
            {'filme':'Star Wars: The Force Awakens','US$':2068223624},
            {'filme':'Furious 7','US$':1516045911},
            {'filme':'Jurassic World','US$':1671713208}
            },
    2017: {
            {'filme':'Star Wars: The Last Jedi','US$':1332539889},
            {'filme':'Beauty and the Beast','US$':1263521126}
            },
    2018: {
            {'filme':'Black Panther','US$':1346913161},
            {'filme':'Avengers: Infinity War','US$':2048359754},
            {'filme':'Jurassic world: Fallen Kingdom','US$':1309484461}
            },
    2019: {'filme':'Avengers: Endgame','US$':2750667499}
    }





