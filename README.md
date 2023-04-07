# homeassistant-climate

Questo progetto è utilizzabile in tre modalità diverse.
- [Card base per telecomando](#card-base-per-telecomando)
- [Card avanzata con pkg per gestione automazioni e statistiche](#card-avanzata-con-pkg-per-gestione-automazioni-e-statistiche)
- Blueperint per gestione automazione.

## Card base per telecomando:
### Requisiti: # aggiungere immagine
- [custom button card](https://github.com/custom-cards/button-card)
- [integrazione smart ir](https://github.com/smartHomeHub/SmartIR)
### Funzionamento
Questa card permette di simulare un telecomando per entità climate e non è vincolate all'utilizzo di altri file.
La card è realizzata con immagine svg e custom button-card
#### tastiiiiiiiiiiiiiiiiiiiii
### Installazione
Per eseguire la card basta copiare il file all'interno di una nuova card manuale e sostituire la variabile climate con la propria entità

``` 
type: custom:button-card
variables:
  climate: climate.condizionatore_salone
```

# Card avanzata con pkg per gestione automazioni e statistiche
### Requisiti: # aggiungere video
- [custom button card](https://github.com/custom-cards/button-card) con template abilitato
- [integrazione smart ir](https://github.com/smartHomeHub/SmartIR)
- dashboard in modalità yaml
- sensore finestra (non indispensabile)
- sensore allagamento (non indispensabile)
- sensore assorbimento in w (non indispensabile)
### Funzionamento
- **Modalità o periodo utilizzo:** È possibile scegliere 4 modalità di funzionamento:
  - [Estate Indice di thom:](https://indomus.it/progetti/definire-un-indicatore-di-benessere-estivo-sulla-domotica-home-assistant/) Viene valutata la differenza rilevata tra indice thom interno ed esterno per accendere o spegnere il condizionatore.
  - Estate Gradi Celsius: Viene valutato la differenza di umidità e temperatura impostata per accendere o spegne il condizionatore rispetto alla temperatura e umidità  rilevata
  - Inverno: Viene valutata solo la temperatura impostata per accendere o spegne il condizionatore rispetto alla temperatura rilevata
  - Umidità: Viene valutata solo l'umidità impostata per accendere o spegne il condizionatore rispetto all'umidità rilevata
Questo utilizzo è sicuramente il più complesso ma anche il più completo.
Prevede il funzionamento del condizionatore in modalità automatica tenendo in considerazione diversi fattori:
- **Temperatura interna rilevata:** in base alla modalità selezionata è possibile impostare una temperatura/umidità/thom rilevata per gestire l'accensione e lo spegnimento del condizionatore in modalita automatica
- **Velocità ventilazione:** e possibile impostare la velocita di ventilazione al condizionatore da utilizzare con l'accensione automatica
- **Modalità hvca:** e possibile impostare la modalità hvca (dry,cool,auto...) al condizionatore da utilizzare con l'accensione automatica
- **Temperatura condizionatore:** e possibile impostare la temperatura al condizionatore da utilizzare con l'accensione automatica
- **Fascia oraria:** è possibile scegliere una fascia oraria per l'attivazione e spegnimento 
- **Presenza in casa:** se abilitato le automazioni funzioneranno solo se lo stato del gruppo o della singola entità person si trova nello stato home. Nel caso le person o il gruppo passa nello stato not_home il condizionatore viene spento.
```
# Esempio di un gruppo famiglia
group:
  famiglia:
    name: Famiglia
    entities:
      - person.marco
      - person.serena
```
- **Stato Finestre:** viene eseguito un controllo sullo stato finestra:
    - Se condizionatore acceso e la finestra viene aperta si riceve inizialmente un avviso di chiudere la finestra, se non avviene entro 30 secondi il condizionatore viene spento.
    - Se condiziontore è spento e viene acceso manualmente con finestra aperta si riceve una notifica di avviso
    - Se accensione automatica attivo e ci sono i requisiti per accendere il condizionatore ma la finestra è aperta si riceve una notifica di avviso   
- **Temperatura esterna:** Viene eseguita in due modalità
   - Rispettando una sua fascia oraria è possibile impostare una differenza di temperatura istantanea rilevata tra interna ed esterne che consiglia di aprire o chiudere la finestra (se controllo finestra attivo ne verifica lo stato). 
   - Legata allo stato condizionatore:
      - Nel momento in cui il condizionatore si deve accendere in automatico ma la temperatura esterna è maggiore/minore (in base alla modalità impostata) di quella target. Non avviene l'accensione del condizionatore ma si riceve un notifica di avviso di aprire la finestra.
      - Se il condizionatore è acceso ma la temperatura esterna è maggiore/minore (in base alla modalità impostata) di quella target. Si riceve una notifica consigliando di aprire o chiudere la finestra e spegnere il condizionatore.
- **Livello acqua:** utilizzo un sensore allagamento aqara per controllare lo stato del serbatoio dove scarico l'acqua del condizionatore.
  - se il condizionatore è acceso ed il serbatoio si riempie ricevi una notifica per avvisarti di svuotarlo
  - se il condizionatore è acceso ed il serbatoio è pieno da 5 minuti il condizionatore si spegne con avviso del notifica
  - se il serbatoio è pieno e viene acceso il condizionatore, ricevi una notifica per svuotarlo
  - se accendi il condizionatore con serbatoio pieno e non viene svuotato entro 5 minuti il condizionatore si spegne con notifica.
