import keep_alive
import urllib
import time

print("Hosted By Dhruv")
keep_alive.keep_alive()
while (True):
    urllib.request.urlopen("https://captcha-image-api.dhruvnation1.repl.co/gimme/some/captcha")
    time.sleep(500)
