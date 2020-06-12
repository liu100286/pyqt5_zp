import requests

setPageData = {
    'appid': '8pr0nphqcuh673kraxhdusk04lr723g8',
    'domain': "xxx",
    'pages': '["/lp2.html"]'
}
header = {
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9zc28ubHphZC5jY1wvYXBpXC9sb2dpbiIsImlhdCI6MTU5MTc1ODMxMywiZXhwIjoxNTkyMzYzMTEzLCJuYmYiOjE1OTE3NTgzMTMsImp0aSI6IktoeG5jbWFkWWtWWjgwa20iLCJzdWIiOjQ5NCwicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSIsIm5hbWUiOiJcdThkNzVcdTllNGYiLCJlbWFpbCI6IjkzMDA1NjM4MEBxcS5jb20ifQ.sfzXTua9Ochr_k229sKWWxowGC1CVqvLtCKG9Wcfslg; user={%22id%22:34%2C%22username%22:%22zhaopeng%22%2C%22emailid%22:%22930056380@qq.com%22%2C%22auth_key%22:%22hRZ-MUJ820ViKZZQHiBxAgBKiQaaNg5j%22%2C%22group%22:%22web%22%2C%22name%22:%22%E8%B5%B5%E9%B9%8F%22}',
}
setPage = 'http://127.0.0.1:5281/landpageManager/setPage'
putInfoOk = requests.post(url=setPage, headers=header, data=setPageData)
b = putInfoOk.json()
print(b)