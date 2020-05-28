# Censorship

### Persoalan

My friend has some top-secret government intel. He left a message, but the government censored him! They didn't want the information to be leaked, but can you find out what he was trying to say?

`nc p1.tjctf.org 8003`
____________________________________

### Penyelesaian

***Note*** : pada soal dikatakan, bawa teman dari pembuat soal mengirimkan pesan namun pesan tersebut disensor, sehingga penulis memutuskan untuk melihat traffic dari pengiriman dan pengeksekusian program. Pada persoalan ini, penulis menggunakan bantuan tools Wireshark pada Linux. Jika pembaca belum memiliki Wireshark, dapat menginstallnya dengan command di bawah ini. 

`sudo apt-get install wireshark`

- Pertama, penulis menjalankan wireshark terlebih dahulu. Kemudian, buka terminal baru untuk menjalankan `nc p1.tjctf.org 8003`.
- Setelah itu akan muncul sebuah pertanyaan sederhana. Penulis mencoba menjawab pertanyaan tersebut dan didapatkan hasil seperti di bawah ini. Akan muncul flag `tjctf{[CENSORED]}`.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Censorship/Censored1.png)

Muncul sebuah flag namun masih dalam bentuk tersensor `tjctf{[CENSORED]}`.
- Kemudian, penulis membuka wireshark dan mencari di port 8003 sesuai dengan pernyataan pada persoalan. 
- Pada port tersebut, terdapat flag asli yang tidak tersensor dari persoalan ini seperti gambar dibawah ini.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Censorship/Censored3.png)
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini `adalah tjctf{TH3_1llum1n4ti_I5_R3aL}`.
