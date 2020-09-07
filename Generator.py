from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha

image = ImageCaptcha()
audio = AudioCaptcha()



data = image.generate("abcd")
image.write('absfacd','1.png')