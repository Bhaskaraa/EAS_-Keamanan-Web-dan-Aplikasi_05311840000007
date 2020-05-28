# Censorship

### Persoalan

My friend has some top-secret government intel. He left a message, but the government censored him! They didn't want the information to be leaked, but can you find out what he was trying to say?

`nc p1.tjctf.org 8003`
____________________________________

### Penyelesaian

***Note*** : pada soal dikatakan, bawa teman dari pembuat soal mengirimkan pesan namun pesan tersebut disensor, sehingga penulis memutuskan untuk melihat traffic dari pengiriman dan pengeksekusian program. Pada persoalan ini, penulis menggunakan bantuan tools Wireshark pada Linux. Jika pembaca belum memiliki Wireshark, dapat menginstallnya dengan command di bawah ini. \

`sudo apt-get install wireshark`

- Pertama, penulis menjalankan wireshark terlebih dahulu. Kemudian, buka terminal baru untuk menjalankan `nc p1.tjctf.org 8003`. - Setelah itu akan muncul sebuah pertanyaan sederhana. Penulis mencoba menjawab pertanyaan tersebut dan didapatkan hasil seperti di bawah ini. Akan muncul flag `tjctf{[CENSORED]}`.<br>

![]()

Akan muncul flag `tjctf{[CENSORED]}`.<br>
Buka wireshark dan cari di port 8003 akan terdapat flag asli yang tidak tersensor

![](https://github.com/lumbricina/TJCTF-2020-05311840000044/blob/master/Miscellaneous/Censorship/wireshark.PNG)
____________________________________


### Flag

Flag yang penulis dapatkan dari persoalan ini adalah tjctf{TH3_1llum1n4ti_I5_R3aL}
