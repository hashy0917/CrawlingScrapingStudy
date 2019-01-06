import time

import requests

TEMPORARY_ERROR_CODES = (408,500,502,503,504) # 一時的なエラーを示すステータスコード

def main():
    """
    メインとなる処理
    """
    response = fetch("http://httpbin.org/status/200,404,503")
    if 200 <= response.status_code < 300:
        print("Success!")
    else:
        print("Error!?")

def fetch(url):
    """
    指定したURLを取得してResponseオブジェクトを返す。一時的なエラーが起きた場合は最大3回までリトライする。
    """
    max_retries = 3
    retries = 0
    while True:
        try:
            print("Retrieving {0}...".format(url))
            response = requests.get(url)
            print("Status: {0}".format(response.status_code))
            if response.status_code not in TEMPORARY_ERROR_CODES:
                return response # 一般的なエラーでなければresponseを返す

        except requests.exceptions.RequestException as ex:
            # ネットワークレベルのエラーの場合(RequestException)はリトライする
            print("Exception occured: {0}".format(ex))
            retries += 1
            if retries >= max_retries:
                raise Exception("Too many retries...") # リトライ回数の上限を超えた場合は例外を発生させる
            wait = 2**(retries - 1) # 指数関数的なリトライ間隔を求める
            print("Waitinf {0} secconds...".format(wait))
            time.sleep(wait)

if __name__ == '__main__':
    main()
