#conjunto de localidades
V = [1,2,3,4,5]
#conjunto de arcos
A = [[2,4,5], [3], [1], [], [4]]
#distancia em KM
w = [ [4,5,1], [9], [2], [], [3] ]

V = [ {'localidades' : 1,
       'arcos' : [{ 'destino' : 2, 'peso' : 4 },
                  { 'destino' : 4, 'peso' : 5 }, 
                  { 'destino' : 5, 'peso' : 1 }] },
      {'localidades' : 2,
       'arcos' : [{ 'destino' : 3, 'peso' : 9 }] },
      {'localidades' : 3,
       'arcos' : [{ 'destino' : 1, 'peso' : 2 }] },
      {'localidades' : 4,
       'arcos' : [ {} ] },
      {'localidades' : 5,
       'arcos' : [{ 'destino' : 4, 'peso' : 3 }]} ]

def main():
    

if __name__ == "__main__":
    main()