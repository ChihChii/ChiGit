# ChiGit

requests用法、上一頁參考 :
https://ithelp.ithome.com.tw/articles/10204709

find() :
https://www.jianshu.com/p/ef2f246cae46

正規表達式:


re.match(r'^https?://(i.)?(m.)?imgur.com' :
”^” 表示字串開頭，字元緊接著 “?” 表示該字元可出現 0 或 1 次，
所以 “^https?” 表示的是 “http” (s 出現 0 次) 或 “https” (s 出現 1 次) 開頭的字串，
同理 (i.)? 表示 “i.” 可以出現 0 或 1 次。


strip() : 用於移除頭尾字串，默認為空格或換行符號
參考:http://www.runoob.com/python/att-string-strip.html


os.makedirs():創建資料夾
http://www.runoob.com/python/os-makedirs.html


for img_url in img_urls:
1. 擷取了 imgur.com 網址的各種形式，但下載圖片時用的網址必須是 i.imgur.com 開頭，
因此要把 m.imgur.com 換成 i.imgur.com，或把 imgur.com 補成 i.imgur.com
2. 網址結尾不一定有 .jpg，為了順利下載，記得補上 .jpg。這些字串處理過程，就是資料淨化與清理的工作。


split():用指定的分隔符號，對字串進行分割
http://www.runoob.com/python/att-string-split.html


startswith(): 檢查字串是否為指定字串開頭
http://www.runoob.com/python/att-string-startswith.html


replace("old","new",max):把字符串中的old替换成new，如果指定第三個參數max，則替換不超過max次
http://www.runoob.com/python/att-string-replace.html
