INTRO
Questa repository fornisce script per elaborare ed analizzare i dati delle corse in taxy che hanno luogo nella città di New York City dal 2020.

OBIETTIVO
Analizzare per ogni distretto (Borough) le modalità di pagamento più comuni identificando il numero di pagamenti per ogni possibile metodo. 

FONTE DEI DATI
Per questo progetto utilizziamo i dati pubblici delle rotte dei Taxi a NYC disponibili su https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

STRUTTURA DEL FILE:
|-- Readme.md
|-- data		: directory dei dati di input
|-- documenti		: cartella contenente le richieste del progetto
|-- Main.py		: file principali contenente le classi da utilizzare
|-- taxy_zone.py	: prototipo iniziale dell'analisi, senza l'utilizzo di classi

PREREQUISITI
E' necessario aver installato i seguenti software e librerie sulla macchina prima di eseguire l'applicazione.
1. Python 3: https://www.python.org/downloads/
2. Anaconda: Installerà la maggior parte delle librerie necessarie https://www.anaconda.com/download/

LIBRERIE
- Pandas		:elemento fondamentale di alto livello per eseguire analisi pratiche e reali dei dati in Python
- Argparse		:il modulo argparse semplifica la scrittura della riga di comando. Il programma definisce quali	argomenti richiedere ed il modulo scoprirà come analizzarli
- tqdm			:indicatore di avanzamento veloce ed estensibile
- abstractmethod 	:modulo che fornisce le basi per la definizione di classi astratte 
- splitext		:modulo che implemanta alcune utili funzioni sui nomi di percorso, interagendo con il sistema operativo
- json			:il formato JSON è spesso usato per lo scambio di dati tra moduli di applicazioni web, nonché per la gestione di file di configurazione o, più semplicemente, per archiviare dati in formato testuale

ISTRUZIONI
1. Aprire il file "Main.py" ed installare le librerie
2. Scaricare i file delle corse dei taxi come indicato nella voce "FONTE DEI DATI" e salvarli nella cartella data.
3. Creare le classi implementate nel file "Main.py"
4. Istanziare uno o più oggetti della classe "file_list_features", a seconda del numero di analisi da svolgere
5. Utilizzare il metodo "list_features" che riceve i seguenti parametri d'ingresso: 
	- lista dei nomi dei file da analizzare (inseriti precedentemente nella cartella data) 
	- in maniera opzionale lista dei distretti di cui si vogliono estrapolare i dati (Manhattan, Queens, Bronx, Brooklyn, Staten Island, EWR, Unknown)
Se l'utente non inserisce il secondo parametro, il programma restituisce tutti i distretti.

OUTPUT
L'utente riceverà in output un Dataframe contenente:
- sugli indici il nome dei singoli distretti richiesti in input
- sulle colonne il conteggio associato ad ogni metodologia di pagamento identificata mediante l'apposito numero.

N.B. Il conteggio viene eseguito nel distretto dove inizia la corsa


LEGENDA TIPOLOGIA DI PAGAMENTO
Codice numerico associato alla tipologia di pagamento
1= Credit Card
2= Cash
3= No charge
4= Dispute
5= Unknown
6= Voided trip

AUTORI
- Camarda Nicola
- Di Noto Daniele
