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

#Per aggiungere elementi di un altro elenco all'elenco corrente, utilizzare il extend()
unalista = ["apple", "banana", "cherry"]
un.altra.lista = ["mango", "pineapple", "papaya"]

unalista.extend(un.altra.lista)

print(unalista)
#Il remove()metodo rimuove l'elemento specificato
unalista = ["apple", "banana", "cherry"]

unalista.remove(cherry)

print(unalista)
#Se non si specifica l'indice, il pop()metodo rimuove l'ultimo elemento.
unalista = ["apple", "banana", "cherry"]

unalista.popo(2)

print(unalista)

#La del parola chiave può eliminare completamente l'elenco, ma anche l'indice specificato
unalista = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]
del unalista[1] #eliminerà solo avocado
print(unalista) #oppure per eliminare tutta la lista:
unalista = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]
del unalista

#Il clear()metodo svuota l'elenco. L'elenco rimane ancora, ma non avrà alcun contenuto.
unalista = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]
thislist.clear()
print(unalista)

#Stampa tutti gli elementi, utilizzando un whileciclo per scorrere tutti i numeri di indice
unalista = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]
r = 0
while i < len(unalista):
  print(unalista[r])
  r = r + 1 #ora r=1 e così via

#Un breve forciclo manuale che stamperà tutti gli elementi in un elenco:
unalista = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]
[print(x) for x in unalista]

#Sulla base di un elenco, se si desidera un nuovo elenco, contenente solo elementi con la lettera "a" nel nome bisogna:
lista1 = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]
nuova_lista = [x for x in lista1 if "a" in x]

print(nuova_lista)

#La condizione if x != "apple"  ritornerà True per tutti gli elementi diversi da "mela", facendo in modo che il nuovo elenco contenga tutti i frutti tranne "mela".
unalista = ["mela", "avocado", "banana", "kiwi", "melone", "mango", "papaia"]

nuova_lista = [x for x in unalista if x != "kiwi" and "melone"]

print(nuova_lista) #così verranno stampati tutti gli elementi della prima lista senza kiwi e melone

