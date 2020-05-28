# Login

### Persoalan

Could you login into this [very secure site](https://login.tjctf.org/)? Best of luck!
____________________________________

### Penyelesaian

Untuk mendapatkan flag dari persoalan ini, penulis menggunakan langkah-langkah sebagai berikut.
- Poin pertama yakni seperti namanya, untuk dapat menemukan flag dari persoalan ini, kita harus masuk / ***Login*** ke dalamnya.
- Dalam halaman website, terdapat tulisan ***Can you log in?*** dengan dua space kosong untuk mengisi username dan password beserta tombol ***Login*** dibawahnya. 
- Untuk menemukan cara login ke website tersebut, kita dapat membuka inspect element atau dengan menekan tombol F12. Pada Sources dapat kita ketahui bahwa script yang digunakan menggunakan metode hashing md5 (ada file bernama md5.js). Pada file index, line ke 70 berisi seperti berikut :
```
var _0xb31c=['value','c2a094f7d35f2299b414b6a1b3bd595a','Sorry.\x20Wrong\x20username\x20o \x20password.','admin','tjctf{','getElementsByName','toString'];
``` 
- Dari sources diatas, kita dapat mengetahui bahwa username adalah admin dan `c2a094f7d35f2299b414b6a1b3bd595a` adalah hash md5 yang merupakan passwordnya. 
- Untuk mendapatkan message asli dari password, kita dapat menggunakan bantuan [MD5 Decoder](https://www.md5online.org/md5-decrypt.html) untuk melakukan decode digest tersebut. 

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Web/Login/Flag-Login2.PNG)

- Hasil decode merupakan password dari username admin yakni `inevitable`. 

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Web/Login/Flag-Login.PNG)

- Kemudian, masukkan username : Admin dan password : inevitable pada space kosong, dan klik Login. Flag akan muncul dalam bentuk Pop Up.
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{inevitable890898}`.
