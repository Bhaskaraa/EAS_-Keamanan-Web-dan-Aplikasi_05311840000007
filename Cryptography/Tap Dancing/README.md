# Tap Dancing

### Persoalan

My friend is trying to teach me to dance, but I am not rhythmically coordinated! They sent me a list of [dance moves](https://static.tjctf.org/518d6851c71c5482dbd5bbe812b678684238c8f4e9e9b3d95a188f7db83a0870_cipher.txt) but they're all numbers! Can you help me figure out what they mean so I can learn the dance?

NOTE: Flag is not in flag format.
____________________________________

### Penyelesaian
Berikut adalah bentuk dari persoalan ini.
`1101111102120222020120111110101222022221022202022211`
- Penulis curiga bahwa angka-angka diatas merupakan urutan sandi morse.
- Kemudian, dengan bantuan morse translator yakni [dcode.fr](https://www.dcode.fr/morse-code), penulis mencoba untuk menerjemahkan persoalan ini. Kemudian didapatkan beberapa hasil sebagai berikut.
```
(102)⇔ (-. )	�TEEA�ENEEM
(012)⇔ (-. )	�ETTN�TATTI
(120)⇔ (-. )	M0RSEN0TB4SE3
(210)⇔ (-. )	I5KOTA5EJ9OT8
(201)⇔ (-. )	EA�NEE��
(021)⇔ (-. )	TN�ATT��
```
- Penulis mencoba jawaban diatas satu-persatu untuk menemukan flag yang diinginkan oleh soal.
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `M0RSEN0TB4SE3`.
