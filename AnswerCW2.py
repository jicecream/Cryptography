import numpy as np
import json
import random 



global A
global q
global b
global s

def computeM(u, v, q, s):
   
    res=(np.subtract(v, np.dot(s, u))) % q
    if q // 4 < res < 3 * q // 4:
        m = '1' 
    else:
        m = '0'
    return m





# retrieve u and v from JSON 

f = open('JiaQiEng_{190429166}_CO3326cw2.json')
data = json.load(f)


def getKeyValues():
    s = np.array(data['exercise']['alice']['sk'])
    q = np.array(data['exercise']['alice']['q'])
    A = np.array(data['exercise']['alice']['a'])
    b = np.array(data['exercise']['alice']['pk'])
    return s, q, A, b

def decrypt():
    m = ''
    u_list = [] 
    v_list =[]

    s, q, A, b = getKeyValues()

    # Extract the u and v values from the messages array
    u_json = []
    v_json = []

    for message in data['exercise']['messages'][0]['cipher']:
        u_json.append(message['u'])
        v_json.append(message['v'])  

    # store u and v in numpy array

    u_list = np.array(u_json)
    v_list = np.array(v_json)


    # compute each binary from u and v


    for i in range(len(u_list)):
        u = np.array(u_list[i])
        v = np.array(v_list[i])

        # print(v)
        m_bit = computeM(u, v, q, s)
        m += m_bit

    print("Decryption: ")
    print(m)
    return m 





def pickR():
    r = np.random.randint(low=0, high=2, size=7)
    return r 


def encrypt(binaryMessage):
    print()
    print("Encryption:")    
    m = ''
    u_list =[]
    v_list = []
    

    s, q, A, b = getKeyValues()

    binary_list = [int(bit) for bit in binaryMessage]


    print()
    i= 0
    for m_bit in binary_list:   

        # pick random r
        #r = np.array([0, 0, 1, 0, 0, 0, 1])
        r = pickR()
        
        c1 = np.dot(A.T, r)  %q
      
        c2 = round(np.add(np.dot(b, r.T),np.dot(m_bit, q/2))) % q


        u = c1
        v = c2       

        u_string = np.array2string(u, separator=", ") 
        print("{\"u\":%s,\"v\":%s}," % (u_string, v))

        u_list.append(u)
        v_list.append(v)

        # test u and v 
        m_bit = computeM(c1, c2, q, s)
        m += m_bit



    print(m)
    return  m




def checkSolution():
    
    m = ''
    u_list=[] 
    v_list = []
    s, q, A, b = getKeyValues()

    m = ''
    u_json = []
    v_json = []
    
    for message in data['solution']['messages'][1]['cipher']:
        u_json.append(message['u'])
        v_json.append(message['v'])


    # store u and v in numpy array

    u_list = np.array(u_json)
    v_list = np.array(v_json)
    u_json[0]


    # compute each binary from u and v


    for i in range(len(u_list)):
        u = np.array(u_list[i])
        v = np.array(v_list[i])
        # print(v)
        m_bit = computeM(u, v, q, s)
        m += m_bit

    print("Check: ")
    print(m)
    return m
    

def findMessageBinary(message):
    
    # Convert string to bytes
    encoded = message.encode('utf-8')

    #  # print bytes 
    # for byte in encoded: 
    #     print(byte)
 
    # Convert each byte to binary representation
    binary = ''.join(format(byte, '08b') for byte in encoded)
    # print(binary)
    return binary

def getPlaintextFromBinary(m):
    # Convert the bit stream to a byte array
    byte_array = bytes.fromhex('%x' % int(m, 2))
    # Convert the byte array to plaintext
    plaintext = byte_array.decode('utf-8')
    return plaintext
 



# run 
m = decrypt()
print(getPlaintextFromBinary(m))


m = encrypt(findMessageBinary("dock"))

print(getPlaintextFromBinary(m))



print()
print(getPlaintextFromBinary(checkSolution()))