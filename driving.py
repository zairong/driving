country = input('請問你是哪裡人?: ')
age = input('你今年幾歲?: ')
age = int(age)
if country == '台灣':
    if age >= 18 :
    	print('你可以考駕照了!')
    else:
    	print('你還不能考駕照!')
elif country == '美國':
    if age >= 16:
    	print('你可以考駕照了!')
    else:
    	print('你還不行考駕照!')