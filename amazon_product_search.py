import os

from amazon.api import AmazonAPI


AMAZON_ACCESS_KEY = os.environ["AMAZON_ACCESS_KEY"]
AMAZON_SECRET_KEY = os.environ["AMAZON_SECRET_KEY"]
AMAZON_ASSOCIATE_KEY = os.environ["AMAZON_ASSOCIATE_KEY"]

amazon = AmazonAPI(AMAZON_ACCESS_KEY,AMAZON_SECRET_KEY,AMAZON_ASSOCIATE_TAG,Region="JP")

products = amazon.search(Keywords="kindle",SearchIndex="All")

for product in products:
    print(product.title)
    print(product.offer_url)
    price, currency = product.price_and_currency
    print(price,currency)
