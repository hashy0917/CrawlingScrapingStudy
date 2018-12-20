import sys
from urllib.request import urlopen

f = urlopen("https://sample.scraping-book.com/dp")

# HTTPヘッダーからエンコーディングを取得する(明示されていない場合は"utf-8"とする)
encoding = f.info().get_content_charset(failobj="utf-8")

print("encoding:",encoding,file=sys.stderr)

text = f.read().decode(encoding)
print(text)
