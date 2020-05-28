# Rap God

### Persoalan

My rapper friend Big Y sent me his [latest track](https://raw.githubusercontent.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/master/Forensics/Rap%20God/RapGod.mp3) but something sounded a little off about it. Help me find out if he was trying to tell me something with it. Submit your answer as tjctf{message}
____________________________________

### Penyelesaian

- Point pertama adalah karena soal ini merupakan soal Forensics, penulis mengasumsikan persoalan ini berhubungan dengan audio forensic.
- Untuk mendapatkan flag dari persoalan ini, penulis menggunakan bantuan [Sonic Visualiser](https://www.sonicvisualiser.org/). Kemudian, perhatikan waveform dan spectogram yang ada. Akan didapatkan tampilan seperti ini :

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Forensics/Rap%20God/RapGod.jpg)

- Pembaca dapat melihat bahwa pada gambar terdapat wingdings character. Simbol-simbol yang terdapat pada Wingdings Character dapat dilihat pada gambar dibawah ini.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Forensics/Rap%20God/Wingdings.jpg)

- Kemudian, kita menerjemahkan wingdings character dari gambar tersebut. Dan terakhir, kita akan mendapatkan flag dari persoalan ini.
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{QUICKSONIC}`.
