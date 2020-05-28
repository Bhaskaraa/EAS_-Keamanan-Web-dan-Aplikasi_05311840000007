# Censorship

**Soal**

My friend has some top-secret government intel. He left a message, but the government censored him! They didn't want the information to be leaked, but can you find out what he was trying to say?

`nc p1.tjctf.org 8003`
____________________________________

### Penyelesaian

Jalankan wireshark terlebih dahulu. <br>
Setelah wireshark dijalankan, maka buka terminal baru untuk menjalankan `nc p1.tjctf.org 8003`. Jawab pertanyaan penjumlahan sederhana yang diberikan. Akan muncul flag `tjctf{[CENSORED]}`.<br>

![](https://github.com/lumbricina/TJCTF-2020-05311840000044/blob/master/Miscellaneous/Censorship/run.PNG)

Buka wireshark dan cari di port 8003 akan terdapat flag asli yang tidak tersensor

![](https://github.com/lumbricina/TJCTF-2020-05311840000044/blob/master/Miscellaneous/Censorship/wireshark.PNG)
____________________________________


### Flag

Flag yang penulis dapatkan dari persoalan ini adalah tjctf{TH3_1llum1n4ti_I5_R3aL}
