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
Questa card permette di simulare il telecomando per entità climate e non è vincolato all'utilizzo di altri file.
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
Questo utilizzo è sicuramente il più complesso ma anche il più completo, perchè prevede il funzionamento del condizionatore in modalità automatica tenendo in considerazione diversi fattori:
- **Modalità o periodo utilizzo:** È possibile scegliere 4 modalità di funzionamento:
  - [Estate Indice di thom:](https://indomus.it/progetti/definire-un-indicatore-di-benessere-estivo-sulla-domotica-home-assistant/) Il condizionatore si accenderà o spegnerà se l'indice di thom rilevato è maggiore o inferiore a quello impostato
  - Estate Gradi Celsius: Il condizionatore si accenderà o spegnerà se la temperatura e l'umidità rilevata è maggiore o inferiore a quella impostata
  - Inverno: Il condizionatore si accenderà o spegnerà se la temperatura rilevata è maggiore o inferiore a quella impostata
  - Umidità: Il condizionatore si accenderà o spegnerà se l'umidità rilevata è maggiore o inferiore a quella impostata
- **Temperatura interna rilevata:** in base alla modalità selezionata è possibile impostare una temperatura/umidità/thom rilevata per gestire l'accensione e lo spegnimento del condizionatore in modalita automatica
- **Velocità ventilazione:** è possibile impostare la velocita di ventilazione del condizionatore da utilizzare con l'accensione automatica
- **Modalità hvca:** è possibile impostare la modalità hvca (dry,cool,auto...) del condizionatore da utilizzare con l'accensione automatica
- **Temperatura condizionatore:** e possibile impostare la temperatura del condizionatore da utilizzare con l'accensione automatica
- **Fascia oraria:** è possibile scegliere una fascia oraria per l'attivazione e per lo spegnimento automatico
- **Presenza in casa:** le automazioni funzioneranno solo se lo stato del gruppo o della singola entità person si trova nello stato home. Se si passa allo stato  not_home il condizionatore verrà spento.
```
# Esempio di un gruppo famiglia
group:
  famiglia:
    name: Famiglia
    entities:
      - person.marco
      - person.serena
```
- **Stato Finestre:** viene eseguito un controllo sullo stato finestre:
    - Se il condizionatore è acceso e la finestra viene aperta si riceve un avviso di chiudere la finestra, se questo non avviene entro 30 secondi il condizionatore verrà spento.
    - Se il condiziontore è spento e viene acceso manualmente con la finestra aperta si riceverà una notifica di avviso
    - Se l'accensione automatica è abilitata e ci sono i requisiti per accendere il condizionatore ma la finestra è aperta si riceverà una notifica
- **Temperatura esterna:** Viene eseguita in due modalità
   - Rispettando una sua fascia oraria: è possibile impostare una differenza di temperatura rilevata tra interna ed esterne che consiglia di aprire o chiudere la finestra se il controllo finestra è attivo ne verifica anche lo stato (es. quando rileva la temperatura esterna maggiore di 5° rispetto a quella interna)
   - Legata allo stato del condizionatore:
      - Nel momento in cui il condizionatore si deve accendere in automatico ma la temperatura esterna è maggiore/minore (in base alla modalità impostata) di quella target, non avviene l'accensione del condizionatore ma si riceverà un notifica per aprire la finestra.
      - Se il condizionatore è acceso ma la temperatura esterna è maggiore/minore (in base alla modalità impostata) di quella target, si riceverà una notifica per aprire o chiudere la finestra e spegnere il condizionatore.
- **Livello acqua:** utilizzo un sensore allagamento aqara per controllare lo stato del serbatoio dove scarica l'acqua il condizionatore.
  - se il condizionatore è acceso ed il serbatoio è pieno ricevi una notifica per svuotarlo
  - se il condizionatore è acceso ed il serbatoio è pieno da 5 minuti il condizionatore si spegnerà con notifica
  - se il serbatoio è pieno e verrà acceso il condizionatore, riceverai una notifica per svuotarlo
  - se accendi il condizionatore ed il serbatoio è pieno ma non verrà svuotato entro 5 minuti si spegnerà con notifica.
