#密碼重試程式
#密碼設定為 password = 'a123456'
#使用者最多嘗試3試密碼輸入
#輸入錯誤則印出"還有__次機會"
#輸入正確則印出"登入成功!"

password = 'a123456'
count = 2
while True:
    code = input('請輸入密碼:')
    if code == password:
        print ('登入成功!')
        break
    else:
        if count < 3 and count > 0:
            print ('密碼錯誤! 還有',count,'次機會')
            count = count - 1
        else :
            break 