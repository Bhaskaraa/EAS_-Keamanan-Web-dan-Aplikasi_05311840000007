# Chord Encoder

### Persoalan

I tried creating my own [chords](https://static.tjctf.org/67be5bd036a4be8323314d1da6ad2e673963f76634a62ec47d53fb07a04a3722_chords.txt), but my [encoded sheet music](https://static.tjctf.org/c29857b8d4d1b2dfe502b5053d73844a08358ae681b2af8de6829b765dc2c28e_notes.txt) is a little hard to read. Please play me my song! \
[chord_encoder.py](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Chord%20Encoder/Chord%20Encoder.py)
____________________________________

### Penyelesaian

- Dalam persoalan ini, pertama kita harus mengonversi isi dari [encoded sheet music](https://static.tjctf.org/c29857b8d4d1b2dfe502b5053d73844a08358ae681b2af8de6829b765dc2c28e_notes.txt) ke dalam bentuk yang dapat kalian lihat dalam [song.txt](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Chord%20Encoder/song.txt). 
- Kemudian kita konversi kembali isi dari song.txt berdasarkan [chords.txt](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Chord%20Encoder/chords.txt), sehingga konversi akan menjadi seperti pada [song1.txt](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Chord%20Encoder/song1.txt). 
- Kemudian jalankan program [Python](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Chord%20Encoder/Chord%20Encoder.py) dan kita akan mendapatkan flag dari persoalan ini.
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah flag{zats_wot_1_call_a_meloD}
