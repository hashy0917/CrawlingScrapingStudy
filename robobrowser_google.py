from robobrowser import RoboBrowser

browser = RoboBrowser(parser="html.parser") 

browser.open("https://www.google.co.jp") # Open()メソッドでGoogleのトップページを開く

form = browser.get_form(action="/search") # フォームを取得
form["q"] = "python" # formの"q"という名前のフィールドに検索語を入力する
browser.submit_form(form, list(form.submit_fields.values())[0]) # 1つ目のボタンを押す

for a in browser.select("h3 > a"):
    print(a.text)
    print(a.get("href"))
