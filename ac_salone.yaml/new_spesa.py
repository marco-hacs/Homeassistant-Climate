import os
hello_message = """
Benvenuti al programma Lista della Spesa !!!

Di seguito un elenco delle funzioni disponibili:

- Per Visualizzare la LISTA DELLA SPESA, premere 1;
- Per Aggiungere alimenti alla Lista della Spesa, premere 2;
- Per Rimuovere alimenti alla Lista della Spesa, premere 3;
- Per uscire dl programma digitare ESC;
"""
good_bye_message = """
GRAZIE per aver utilizzato LISTA DELLA SPESA V.0.1b

speriamo di rincontrarci presto

Buona Appetito
"""


def aggiungi_alimento():
    lista_spesa.setdefault(elemento, 0)


def rimuovi_alimento():
    del lista_spesa[del_elemento]


def add_quantità():
    quantità = input("Quantità: ")
    lista_spesa[elemento] = quantità
    os.system("cls")
    stato_lista()


def stato_lista():
    for k, v in lista_spesa.items():
        print(f"{k}: {v}")


os.system("cls")
lista_spesa = {}

while True:
  print(hello_message)
  print("\nLista spesa\n")
  scelta = input("Seleziona cosa vuoi fare !? \n ")

  if scelta == "1":
      print("\nEcco la tua lista della spesa!!! \n")
      os.system("cls")

  elif scelta == "2":
      elemento = input(f"\nQuale alimento vuoi aggiungere alla tua spesa???")
      aggiungi_alimento()
      add_quantità()

  elif scelta == "3":
      del_elemento = input(
          f"\nQuale alimento vuoi rimuovere dalla tua spesa???")
      rimuovi_alimento()

  elif scelta == "ESC":
      print(f"{good_bye_message}")
      break
