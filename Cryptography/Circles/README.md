

# Circles

### Persoalan

Some typefaces are mysterious, like this one - its origins are an enigma wrapped within a riddle, indeed.

[Circles.png](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Cryptography/Circles/Circles.png)
____________________________________

### Penyelesaian

![circle](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Cryptography/Circles/Circles.png)

- Gambar diatas menunjukan sebuah pola. 5 lingkaran paling kiri dapat penulis asumsikan sebagai awalan flag yakni ***tjctf***, sehingga penulis mencoba untuk mencari apakah yang digunakan pembuat soal untuk menyelimuti flag tersebut.
- Melihat pola pada lingkaran, penulis curiga bahwa lingkaran-lingkaran pada gambar adalah sebuah font. Oleh karena itu, penulis mencoba mengidentifikasinya dengan menggunakan [Font Identifier](https://www.whatfontis.com/).
- Penulis menemukan hasil dan font yang digunakan pada gambar adalah adalah [USF Circular Design](https://www.fonts.com/font/ultimate-symbol/usf-circular-designs/regular). 
- Penulis kemudian mengonversi font tersebut ke dalam plaintext dan didapatkan flag dari persoalan ini.
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{B3auT1ful_f0Nt}`
