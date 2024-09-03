# Projetos Disciplina Data Science Using Python

## Projeto 1 - Decodificador Morse

Objetivo:

* Interceptar as mensagens de morse;
* Decodificar, sabendo que as letras estão espaçadas por um espaço;
* Salvar as mensagens em um arquivo em texto claro;
* Salvar o datetime da decodificação da mensagem;

Aspectos Obrigatórios do projeto:

* Recebe a mensagem como argumento;
* O "de-para morse" não deve estar hard coded;
* Path do arquivo não deve estar hard coded;
* Messagem deve ser passada através do keyboard.

Coniderações Finais:

* As letras devem ser separadas por um espaço
* As palavras devem ser separadas por dois espaços
* Executar com pelo menos 3 cenários diferentes, ou seja, 3 textos
* Você deve criar estes textos /frases de input

O projeto finalizado (arquivo .py e arquivo com as frases em texto claro) está [nesta pasta](Scripts) sendo:

* projeto_1_final.py = Script utilizando a estrutura de funções;
* projeto_1_v2.py = Script utilizando uma classe para o decodificador;
* frases_decod.csv = Arquivo com as frases traduzidas;

As frases que foram utilizadas como teste estão [nesta pasta](Docs) no arquivo de nome "Mensagens_morse.txt"

## Projeto 2 - Análise exploratória

Objetivo:

Realizar a análise exploratória da base de voos de new-york para entender como se comportam os atrasos dos voos.

A base a ser explorada contém a seguinte estrutura:

* year,month,day: Date of departure
* dep_time,arr_time: Departure and arrival times, format HMM or HHMM
* dep_delay,arr_delay: Departure and arrival delays, in minutes. Negative times represent early departures/arrivals.
* hour,minute : Time of departure broken in to hour and minutes
* carrier: Two letter carrier abbreviation
* tailnum: Plane tail number
* flight: Flight number
* origin,dest: Origin and destination.
* air_time: Amount of time spent in the air
* distance: Distance flown

O projeto de desenvolvimento pode ser encontrado [nesta pasta](Scripts), no arquivo de nome "projeto_2.ipynb"
