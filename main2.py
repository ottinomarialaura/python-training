#Per creare e stampare delle liste
unalista = ["mela", "avocado", "banana"]
print(unalista)
#Per stampare il numero di elementi presenti in una lista scrivere,inparentesi e prima del nome della lista, la scritta len
sport = ["tennis", "ping pong", "calcio", "pallavolo"]
print(len(sport))
#Dal punto di vista di Python, le liste sono definite come oggetti con il tipo di dati 'list': <class 'list'>. Infatti per verificare il tipo di classe di una lista bisogna scrivere la parola type in parentesi prima del nome della lista
unalista = ["mela", "avocado", "banana"]
print(type(unalista))
#Per stampare un unico elemento bisogna specificare il numero suo corrispondente nell'ordine
unalista = ["mela", "avocado", "banana"]
print(unalista[3]) #così stamperà la parola banana
#Nel caso si voglia stampare un elemento che,in ordine,è l'ultimo o tra gli ultimi basta mettere i - davanti 
thislist = ["mela", "avocado", "banana"]
print(thislist[-2]) #così stamperà la parola avocado
#Per specificare un intervallo di indici specificando da dove iniziare e dove terminare l'intervallo bisogna:
thislist = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]
print(thislist[3:7]) #cos' stamperà dal terzo al settimo elemento
#Per modificare il valore degli elementi all'interno di un intervallo specifico, definire un elenco con i nuovi valori e fare riferimento all'intervallo di numeri di indice in cui si desidera inserire i nuovi valori
unalista = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]

unalista[1:5] = ["mandarino", "anguria"]

print(unalista) #così stamperà ['mela', 'mandarino', 'anguria', 'mango', 'papaia']
#Inserisci "anguria" come terzo elemento bisogna
unalista = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]

unalista.insert(2, "anguria")

print(unalista)

