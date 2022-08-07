import qrcode

img = qrcode.make("codingfizz.in")

img.save("mypng.png")

img.show()