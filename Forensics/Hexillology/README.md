# Hexollology

### Persoalan

I recently designed a new [flag](https://static.tjctf.org/af83861c918131864a4e3df24c49d9bad766ae701f02387ee0698593b44f3390_Hexillology.png) for my imaginary nation, Hexistan. Do you like it?
____________________________________

### Penyelesaian
Berikut adalah tampilan dari persoalan.
![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Forensics/Hexillology/Hexillology.png)

- Pada persoalan ini terdapat hint **hex** dimana penulis curiga persoalan ini mengajak penulis untuk bermain dengan kode warna. Untuk itu, penulis mencoba mencari nilai hexa dari setiap warna yang ada pada persoalan diatas. 
- Untuk mencari nilai hexadesimal dari setiap warna, penulis menggunakan bantuan website [Colour Picker](https://imagecolorpicker.com/en/).
- Kemudian didapatkan kode hexadecimal sebagai berikut. \
`746a63 70594a 4b3064 50477d 74667b 726651 626154`
Namun nilai hexadesimal diatas masih dalam pola yang salah.
- Kemudian penulis menggunakan pola nilai hexadesimal seperti di bawah ini.
`746a63 74667b 63306c 6f7266 75315f 666c34 67217d`
- Dengan batuan website converter online yakni [Rapid Tables](https://www.rapidtables.com/convert/number/hex-to-ascii.html) untuk mengonversi hexadesimal ke dalam bentuk ASCII, nilai hexadesimal dapat dikonversi menjadi text yang menunjukkan flag dari persoalan ini.
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{c0lorfu1_fl4g!}`
