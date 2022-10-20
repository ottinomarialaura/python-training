#creiamo delle variabili
x=4
y="laura" #sapendo che per inserire testi bisogna scrivere tra virgolette
#una volta definite le variabili si va a stamparle 
print(x)
print(y)
#se si vuole precisare il tipo di inserimento messo si deve scrivere: str(numero) se si vuole dare una valenza di testo, int(numero) inteso come numero intero e float(numero) per indicarlo in scala decimale e quindi con la virgola
x=str(4)
y=int(8)
z=float(12)
#dopodichè si va a stampare il tipo di variabile che si vuole
print(x)
print(y)
print(z)
#se si vuole stampare il tipo di variabile bisogna selezionare "type" tra le parentesi e poi scrivere la variabile desiderata 
x=4
y="laura"
print(type(x))
print(type(y))
#le doppie virgolette e quelle singole valgono alla stessa maniera senza dare errore
x="laura"
y='laura'
print(x)
print(y)
#CASI DA ESCLUDERE CHE CREA UN ERRORE: il nome di una variabile non può iniziare con un numeronnon può contenere trattini o spazi
#per aiutarsi a leggere meglio le parole lòunghe si può usare il trattino basso (_)
#in una sola riga possono essere inserite più variabili
x, y, z = "laura", "verde", "pallavolo"
print(x)
print(y)
print(z)
#in una sola riga possono essere inserite più variabili con lo stesso valore
x=y=z = "laura"
print(x)
print(y)
print(z)
#si piò anche decomprimere un elenco 
nomi = ["laura", "giorgia", "eleonora"]
x, y, z = nomi
print(x)
print(y)
print(z)
#Per i numeri(e solo con loro,quindi non tra parole e numeri o solo tra parole), il +carattere funziona come un operatore matematico
x = 4
y = 10
print(x + y)
#Per creare una variabile al di fuori di una funzione e usala all'interno della funzione
x = "fantastica"

def myfunc():
  print("Laura è " + x)

myfunc()
#Per creare una variabile all'interno di una funzione, con lo stesso nome della variabile globale
x = "fantastica"

def myfunc():
  x = "paziente"
  print("Laura è sempre " + x)

myfunc()

print("Laura è " + x)
#Per modificare il valore di una variabile globale all'interno di una funzione, fare riferimento alla variabile utilizzando la globalparola chiave
x = "paziente"

def myfunc():
  global x
  x = "fantastica"

myfunc()

print("Laura è " + x)
