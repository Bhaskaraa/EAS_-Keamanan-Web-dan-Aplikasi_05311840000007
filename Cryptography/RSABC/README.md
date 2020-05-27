# RSABC

### Persoalan

I was just listening to some [relaxing ASMR](https://www.youtube.com/watch?v=J2g3lvNkAfI&feature=youtu.be) when a notification popped up with [this](https://static.tjctf.org/68f148e8d4b5ceb8f9fa6da568db024c28b80b55891fba49880b76b35d436114_rsa.txt). \
???
____________________________________

### Penyelesaian

Soal ini mirip dengan soal Easy as RSA pada TJCTF 2019. Langkah pertama dalah melakukan faktorisasi pada `n` menggunakan [website ini](factordb.com). Faktor dari `n` disimpan dalam `p` dan `q`

```
p = 202049603951664548551555274464815496697
q = 285934543893985722871321330457714807993
```
Masukkan `n`, `e`, `c`, `p` dan `q` ke **rsabc.rb**. Gunakan terminal untuk menjalankan program ruby dan flag akan muncul langsung
`$ruby rsabc.rb`
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{BOLm1QMWi3c}`.
