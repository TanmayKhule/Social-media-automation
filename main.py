import instaautomate
import twitterautomate
import fbautomate

image_location = str(input())
caption = str(input())

instaautomate(image_location, caption)
fbautomate(image_location, caption)
twitterautomate(image_location, caption)
