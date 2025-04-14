'''

Il classico modello di apprendimento SUPERVISIONATO è quello relativo al DATASET TITANIC.
Viene utilizzato per prevedere le percentuali di sopravvivenza dei passeggeri coinvolti nel naufragio del Titanic.

Il dataset Titanic è un set di dati classico utilizzato per problemi di apprendimento supervisionato, 
in particolare per la classificazione binaria. Il suo obiettivo principale è prevedere se un passeggero
del famoso transatlantico Titanic sia sopravvissuto o meno al suo tragico affondamento.

Ecco una descrizione dettagliata del dataset:

Obiettivo:

    Prevedere la sopravvivenza di un passeggero (variabile target: Survived). Questa è una variabile binaria:
        0 = Non sopravvissuto (Deceased)
        1 = Sopravvissuto

Caratteristiche (Features):

Il dataset contiene informazioni su diversi attributi di ciascun passeggero. Le caratteristiche più comuni includono:

    PassengerId: Un identificatore univoco per ciascun passeggero. (Solitamente non utilizzato come feature predittiva diretta).
    Survived: Indica se il passeggero è sopravvissuto (0 = No, 1 = Yes). Questa è la variabile target per l'apprendimento supervisionato.
    Pclass (Passenger Class): La classe del biglietto del passeggero. È una variabile ordinale che rappresenta lo stato socio-economico:
        1 = Prima classe (Upper)
        2 = Seconda classe (Middle)
        3 = Terza classe (Lower)
    Name: Il nome del passeggero. (Richiede spesso feature engineering per estrarre informazioni utili come il titolo).
    Sex: Il genere del passeggero. (Categorica: male, female).
    Age: L'età del passeggero in anni. (Numerica, può contenere valori mancanti).
    SibSp (Siblings/Spouses Aboard): Il numero di fratelli/sorelle o coniugi a bordo del Titanic. (Numerica).
    Parch (Parents/Children Aboard): Il numero di genitori/figli a bordo del Titanic. (Numerica).
    Ticket: Il numero del biglietto del passeggero. (Solitamente non utilizzato direttamente).
    Fare: La tariffa pagata dal passeggero. (Numerica).
    Cabin: Il numero della cabina del passeggero. (Categorica, contiene molti valori mancanti).
    Embarked: Il porto di imbarco. (Categorica):
        C = Cherbourg
        Q = Queenstown
        S = Southampton

Struttura del Dataset:

Il dataset Titanic è tipicamente suddiviso in due file csv principali per le attività di machine learning:

    train.csv: Contiene i dati di addestramento, inclusa la variabile target (Survived) per ciascun passeggero. Questo set di dati viene utilizzato
    per addestrare i modelli di machine learning.
    
    test.csv: Contiene i dati di test, che hanno le stesse caratteristiche del set di addestramento, ma non include la variabile target Survived.
    L'obiettivo è utilizzare il modello addestrato sul train.csv per prevedere la sopravvivenza dei passeggeri in questo set di dati.

Utilizzo per l'Apprendimento Supervisionato:

Il dataset Titanic è un ottimo punto di partenza per l'apprendimento supervisionato per diversi motivi:

    Problema di Classificazione Binaria Chiaro: L'obiettivo di prevedere la sopravvivenza (sì/no) è ben definito.

    Mix di Tipi di Dati: Contiene sia caratteristiche numeriche (Age, Fare, SibSp, Parch) che categoriche (Sex, Embarked, Pclass). 
    Questo permette di sperimentare diverse tecniche di pre-elaborazione dei dati e di feature engineering.

    Dimensione Relativamente Piccola: Il dataset è abbastanza piccolo da poter essere facilmente caricato e manipolato, rendendolo ideale
    per l'apprendimento e la sperimentazione.

    Disponibilità Diffusa: È un dataset molto popolare ed è facilmente reperibile su piattaforme come Kaggle e in molte librerie di machine
    learning (ad esempio, scikit-learn).

    Sfide Interessanti: Nonostante la sua semplicità apparente, il dataset presenta sfide come la gestione dei valori mancanti, la conversione
    di variabili categoriche in formato numerico e la selezione/ingegnerizzazione delle caratteristiche più predittive.

Il dataset Titanic è presente sul web in diverse forme. Si può scaricare da qui: https://calmcode.io/datasets/titanic/.


'''

import seaborn as sns
titanic = sns.load_dataset('titanic')
print(titanic.head())

