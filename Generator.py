from captcha.image import ImageCaptcha

image = ImageCaptcha()

data = image.generate("abcd")
image.write('abcd','1.png')