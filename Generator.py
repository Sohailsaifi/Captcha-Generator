from captcha.image import ImageCaptcha

image = ImageCaptcha()
audio = AudioCaptcha()



data = image.generate("abcd")
image.write('abcd','1.png')