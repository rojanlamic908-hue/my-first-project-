fruit_name='orange'
result=fruit_name.maketrans('oR','AA')
print(fruit_name.translate(result))
  
  
Username='      laxman kc    '
step1=Username.split()
print(step1)
print(''.join(step1))
  #starts with function
phone_number="+977000000000"
print(phone_number.startswith('977+'))
#ends with function
image='heloo.png'
print(image.endswith('.png'))
