# Solving the reddit easteregg

I compared the images in a view different ways. One way was just XOR-ing them together. This results in [this image](xor.png). As you can see, there are some interesting lines between the noise. If you take a closer look at the noise, you'll see that it's quite dark and doesn't exceed a maximum value of 20. So let's remove that noise: [result](denoised.png). Now if you look at the remainging numbers, they seem to mean something. I tried converting them to ASCII, and it worked! The resulting text is `Bruh! Frohes neues Jahr!Bruh!Bruh! Du hast das Super-Easteregg gefunden, dafür bekommst du einen Preis: nichts!`. This is German and can be translated to something like `Bruh! Happy new Years!Bruh!Bruh! You found the Super-Easteregg, for this you get a prize: nothing!`.
