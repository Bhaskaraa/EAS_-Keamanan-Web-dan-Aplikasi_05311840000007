# Gamer W

### Persoalan

Can you figure out how to [cheat](https://gamer_w.tjctf.org/) the system? Grab his hat to prove your victory!

____________________________________

### Penyelesaian
Sebelum mulai bermain, ada sebuah instruksi dalam game, tepatnya di bawah kata play seperti gambar berikut.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Web/Gamer%20W/Gamer1.PNG)

***Note*** : pada game tersebut, penulis diinstrusikan untuk menggunakan chrome extension **Cetus**. Penulis mengunduh ekstensi ini dalam Github [Qwokka](https://github.com/Qwokka/Cetus) dan sekaligus menggunakannya sebagai referensi. Cetus sendiri berfungsi untuk memanipulasi value dari suatu memory yang tersimpan.

- Langkah pertama, masuk ke dalam shop. Kemudian, penulis melakukan search ***value health point*** dengan comparison operator ***EQ*** dan value types ***F32***.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Web/Gamer%20W/GamerW-Cetus.png)

- Kemudian  penulis mencari musuh pada chapter 1 seperti di bawah ini.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Web/Gamer%20W/Gamer2.PNG)

- Biarkan musuh melakukan serangan terhadap karakter untuk mengurangi HP. Cari kembali value health point, namun comparison operator dalam cetus diubah menjadi LT. Setelah itu, pilih hasil search yang sesuai dengan value health point. Lalu, buka bookmarks dan freeze value health point tersebut. Setelah langkah ini, cheat untuk HP telah diaktifkan.
- Setelah mengalahkan musuh chapter 1, penulis dihadapkan dengan musuh chapter 2 seperti gambar berikut.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Web/Gamer%20W/Gamer3.PNG)

- Ketika musuh chapter 2 telah dikalahkan, pada chapter 3 akan muncul boss pemilik monster tersebut. Boss pada chapter 3 ini masih dapat penulis kalahkan hanya dengan menggunakan cheat HP.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Web/Gamer%20W/Gamer4.PNG)

- Chapter terakhir adalah seperti di bawah ini. Boss telah menggunakan Super Powernya dan meng-Upgrade Machine Gun-nya.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Web/Gamer%20W/Gamer5.PNG)

- Sebelum penulis melawan boss pada chapter ini, penulis melakukan cheat pada Gold terlebih dahulu. Cheat dapat dilakukan dengan cara yang sama saar penulis mengaktifkan cheat HP. Caranya yakni dengan pergi ke shop (ruangan bagian kiri), lalu cari/search value Gold saat ini dengan comparison operator ***EQ*** dan value type ***F32***. Kemudian, penulis membeli sesuatu sehingga Gold berkurang. Selanjutnya, cari kembali value gold namun comparison operator yang telah diubah menjadi ***LT***. Sama seperti cheat HP sebelumnya, kita akan mencentang ***freeze*** pada bookmarks value Gold. 
- Ketika cheat Gold telah diaktifkan, penulis meng-upgrade semua stat player hingga maksimal. Dan sebelum melawan boss, penulis mengaktifkan kembali cheat HP dengan cara mencentang freeze pada bookmarks value HP. 

Level 5 boss akan minum potion yang membuat lifenya regenerate jika terkena serangan. Disini manfaatkan lagi cheat untuk mengubah hp dari bossnya. Boss tersebut memiliki hp 300, dapat diketahui dengan cara menghitung :smirk: . Kode untuk hp boss adalah : `0x2112e4c`. Bookmark, freeze, dan ubah valuenya menjadi 0. 

Yeay menang!
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini `adalah tjctf{c3tus_del3tus_ur_m3ms_g0ne}`.
