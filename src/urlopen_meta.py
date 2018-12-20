import re
import sys
from urllib.request import urlopen

f = urlopen("https://sample.scraping-book.com/dp")
bytes_content = f.read() # bytes型のレスポンスボディを一旦変数に格納する

# charsetはHTMLの最初の方に書いてあるはずなので
# レスポンスボディの先頭1024byteをASCII文字列としてdecodeする
# ASCII範囲外の文字は`U+FFFD(REPLACEMENT CHARACTER)`に置き換え例外を発生させない
scanned_text = bytes_content[:1024].decode('ascii',errors='replace')

match = re.search(r'charset=["\']?([\w-]+)',scanned_text)
if match:
    encoding = match.group(1)
else:
    encoding = "utf-8"

print('encoding:',encoding,file=sys.stderr)

text = bytes_content.decode(encoding)
print(text)
