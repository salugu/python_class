
import re
print(re.fullmatch(r'^[a-z]{15}\W{1}[a-z]{5}\W{1}[a-z]{3}$', 'salugusaicharan@gmail.com'))
print(re.fullmatch(r'^[A-Z]{5}\d{4}[A-Z]{1}$', 'ONPQS4542J')) 
print(re.fullmatch(r'^\d{12}$', '215990034179'))
print(re.fullmatch(r'^[A-Z]{1}\W{1}\d{3}[a-z]{1}\d{1}[a-z]\d{4}$','S@217r1a0549'))


#print(re.fullmatch(r'\d{12}', 215990034179))
#print(re.fullmatch{'^[A-Z]{5}\d{4}[A-Z]{1}$','ONPQS4542J'})
