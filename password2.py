password = 'a123456'
count = 2
while count < 3 :
    code = input('請輸入密碼:')
    if code == password:
        print ('登入成功!')
        break
    elif count > 0 :
        print ('密碼錯誤! 還有',count,'次機會')
        count = count - 1
    elif count == 0 :
        print ('帳號鎖定')
        break