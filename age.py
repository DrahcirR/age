driving = input('請問你有沒有開過車?')
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('你怎麼開過車 很奇怪')
elif driving =='沒有':
	if age >= 18:
		print('你可以考駕照怎麼不考')
	else:
		print('很好 再過幾年就能考駕照了')
else:
	print('只能輸入有或沒有')