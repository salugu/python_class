
# replace
from itertools import count


s1="a-b-c-d"
print(s1.replace("-", "$"))
# join
s2="/"
s3="abcde"
print(s2.join(s3))
# split
s4="HLO I am saicharan"
print(s4.split(' ',1)) 
print(s4.rsplit(' ',1))
# splitlines
s6='''HI
HLO
HOW ARE YOU'''
print(s6.splitlines())
# prefix and suffix
s7="HLO I am saicharan"
print(s7.startswith("HLO"))
print(s7.endswith("saicharan"))

# remove prefix and suffix
s8="sai charan"
print(s8.removeprefix("sai"))
print(s8.removesuffix("charan"))
# partitions
s9="salugusaicharan@gmail.com"
print(s9.partition("@"))
# uppercase
s10="saicharan"
print(s10.upper())
# lowercase
s11="SAICHARAN"
print(s11.lower())
# title cases
s12="hello world"
print(s12.title())
# capitalize
s13="sai charan"
print(s13.capitalize())
# swapcase
s14="SaiChArAn"
print(s14.swapcase())
# csefold by default lowercase
s15="SaiChArAn"
print(s15.casefold())

# concatenate
s16="Sai"
s17 ="Charan"
print(s16+s17)

# length
s19="saicharan"
print(len(s19))

# count
s20="saicharan sai kumar sai charan"
print(s20.count("sai"))

# index
s21="saicharan"
print(s21.index("n"))
# print(s21.index("z")) # if not found throws error

# find
s22="saicharan"
print(s22.find("n"))
print(s22.find("z")) # if not found returns -1

