import hashlib
import math

import random

import numpy as np


t1 = "vegetarian"
t2 = "television"
t3 = "toothpaste"
t4 = "providence"
t5 = "revelation"
t6 = "possession"
t7 = "laboratory"
t8 = "allegiance"
t9 = "enthusiast"
t10 = "gadolinium"

arr = []

arr.append(t1)
arr.append(t2)
arr.append(t3)
arr.append(t4)
arr.append(t5)
arr.append(t6)
arr.append(t7)
arr.append(t8)
arr.append(t9)
arr.append(t10)


# stringList = np.array(arr)
hash = ""
bigInt = 0

messageArr = []



def sha256(input_string):
    hash_object = hashlib.sha256(input_string.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig



for i in arr:
    hash = sha256(i)    
    bigInt = int.from_bytes(bytes(hash, 'utf-8'), "big")
    messageArr.append(bigInt)
  
print()





# store r list

r1 = 6639239524185765101
r2 = 7997103750559419825
r3 = 2807300125410466152
r4 = 16526574537075754551
r5 = 13112042454473672026
r6 = 11881214669873679340
r7 = 11070815852751191729
r8 = 16526574537075754551
r9 = 10428052768440187678
r10 = 6707840473249891091

rList = []

rList.append(r1)
rList.append(r2)
rList.append(r3)
rList.append(r4)
rList.append(r5)
rList.append(r6)
rList.append(r7)
rList.append(r8)
rList.append(r9)
rList.append(r10)



# store s list


sList = []

s1 = 3938252239699764786
s2 = 11043117593640282650
s3 = 16674534501237991620
s4 = 5176712809762123254
s5 = 15496635786824103714
s6 = 12753916073846954214
s7 = 2419018265908646477
s8 = 4029293089712725140
s9 = 1393740918527063389
s10 = 16735677713165379735

sList.append(s1)
sList.append(s2)
sList.append(s3)
sList.append(s4)
sList.append(s5)
sList.append(s6)
sList.append(s7)
sList.append(s8)
sList.append(s9)
sList.append(s10)





p = 17616640590392624387
g = 2
A = 9540710599828830739



correctMsgList = []
correctSList = []
correctRList = []

for i in range(len(messageArr)):
    T1 = pow(A, rList[i], p) * pow (rList[i], sList[i], p) % p
    T2 = pow(g, messageArr[i], p) # g ^ message mod p
    
    if (T1 == T2):
       print(arr[i])  # print the correct words 
       correctSList.append(sList[i])
       correctRList.append(rList[i])   
       correctMsgList.append(messageArr[i])
      
     

print()





# a = s2 - s1
# b = m2 - m1
# n = p -1

S1 = correctSList[0]
R1 = correctRList[0]
M1 = correctMsgList[0]

S2 = correctSList[3]
R2 = correctRList[3]
M2 = correctMsgList[3]


a = S1 - S2
b = M1 - M2
n = p - 1



r = 16526574537075754551
k = 235087545
# correct k = 17616640590627711931


x = 485897652
p = 17616640590392624387

if (pow(g, 235087545, p) == r):
    print("true")


import Crypto.Util.number as num


k = 17616640590627711931


ki = num.inverse(k, p-1)
s = ki * (M1 - x*r) % (p-1)



x = (pow(r, -1, p-1) * ((M1 - S1 * k) % (p-1))) % (p-1)


print(x== 485897652)

# x verified as true

t_list = []
m_list = []

t1 = 5247285421845087059140387699923700103986285229205296479476138331600546258380271833856861742724101495518137268812152047708294477265904690099019107925241955
t2 = 5152563136522592561092350557175874053674962986588514279854411864446071658320367263655899431781636200207470905206717797320426180298617820420292703273182053
t3 = 5100227224358248167837332187014767584604467962965024101489265394186424362868995087811060260568718863157512956959078748459498192124254378735438738510460473
t4 = 573412731067834962538251806503956334

t_list.append(t1)
t_list.append(t2)
t_list.append(t3)
t_list.append(t4)

m_list.append("data confidentiality")
m_list.append("data integrity")
m_list.append("authentication")
m_list.append("non-repudiation")



def gcd(a, b):
	if a == 0:
		return b

	return gcd(b % a, a)


import Crypto.Util.number as num

r_list = []
s_list = []

for t in t_list:
    r = pow(g, k, p)
    k = random.randint(1, p-1)
    while(not gcd(k, p-1) == 1):
        k = random.randint(1, p-1)

    
    ki = num.inverse(k, p-1)
    s = ki * (M1 - x*r) % (p-1)
    r = pow(g, k, p)
    r_list.append(r)
    s_list.append(s)
 

for i in range(len(r_list)):
    print(t_list[i])
    print(m_list[i])
    print("r: %s" % r_list[i])
    print("s: %s" % s_list[i])





