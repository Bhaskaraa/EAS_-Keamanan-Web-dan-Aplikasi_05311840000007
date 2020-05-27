

# Broken Button
**Soal**

This [site](https://broken_button.tjctf.org/) is telling me all I need to do is click a button to find the flag! Is it really that easy?
____________________________________

**Jawaban**

Inspect element dari website tersebut menunjukkan bahwa button tersebut tidak mengarah kemanapun. 

`<button>button</button>`

2 line dibawahnya terdapat button tersembunyi yang mengarah ke "find_the_flag!.html".

`<button class="hidden" href="find_the_flag!.html"></button>`

Ubah `button` yang pertama menjadi `a` dan tambahkan `href="find_the_flag!.html"` sehingga dapat diarahkan ke "find_the_flag!.html".

`<a href="find_the_flag!.html">button</a>`

Klik pada tulisan button yang mengarah ke [html](https://broken_button.tjctf.org/find_the_flag!.html) tersebut.
____________________________________
**Flag**

tjctf{wHa1_A_Gr8_1nsp3ct0r!}
