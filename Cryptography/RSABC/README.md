# RSABC

### Persoalan

I was just listening to some [relaxing ASMR](https://www.youtube.com/watch?v=J2g3lvNkAfI&feature=youtu.be) when a notification popped up with [this](https://static.tjctf.org/68f148e8d4b5ceb8f9fa6da568db024c28b80b55891fba49880b76b35d436114_rsa.txt). \
???
____________________________________

### Penyelesaian

***Note*** : Persoalan ini mirip dengan soal [Easy as RSA](https://github.com/zst-ctf/tjctf-2019-writeups/tree/master/Writeups/Easy_as_RSA) pada TJCTF 2019 sehingga penulis menggunakannya sebagai referensi.

```
n=57772961349879658023983283615621490728299498090674385733830087914838280699121
e=65537
c=36913885366666102438288732953977798352561146298725524881805840497762448828130
```

- Langkah pertama adalah melakukan faktorisasi pada `n` menggunakan website [Factordb.com](factordb.com). Kemudian, hasil faktorisasi dari `n` disimpan dalam variabel`p` dan `q`. Didapatkan hasil dari faktorisasi adalah sebagai berikut.

```
p = 202049603951664548551555274464815496697
q = 285934543893985722871321330457714807993
```

- Kemudian input nilai dari variabel `n`, `e`, `c`, `p` dan `q` ke dalam program [RSABC.rb](). Gunakan terminal untuk menjalankan program ruby. Penulis mengeksekusinya dengan command berikut. \
`$ruby rsabc.rb`
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{BOLm1QMWi3c}`.
