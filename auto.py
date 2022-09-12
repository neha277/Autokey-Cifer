import string
import argparse


# python auto.py --input_file out --output_file in1 --key l --type 0

# 

alpha = {v:k for k,v in enumerate(string.ascii_lowercase)}
print(alpha)
low_alphabet = string.ascii_lowercase
up_alphabet = string.ascii_uppercase

alphabet =  up_alphabet + low_alphabet

print(alphabet)




def read_file(filename):
    f = open(filename, "r")
    plain_text = f.read()

    return plain_text

def encrypt(plain_text,key_val,op):
    plain_text_value = []
    for i in plain_text:
        plain_text_value.append(alpha[i])


    key_text_value =  []
    for i in key_val:
        key_text_value.append(alpha[i])


    temp= key_text_value+plain_text_value
    key_stream = temp[:len(plain_text_value)]

    # print(key_stream)

    addition = [x+y  for x,y in zip(plain_text_value,key_stream)]
    mod = [s % 26 for s in addition]

    encrypted_list = []
    for i in mod:
        encrypted_list.append([k for k,v in alpha.items() if v == i][0])


    # print(''.join(encrypted_list))    

    with open(op, "w+") as f:
        f.write(''.join(encrypted_list))
        f.truncate()

    return encrypted_list,key_stream

def decrypt(input,op,key_val):


    print(plaintext)    
    plain_text_value =  []
    for i in input:
        plain_text_value.append(alpha[i])

    key_value = []
    for i in key_val.lower():
        key_value.append(alpha[i])


    temp = plain_text_value+key_value
    key_stream = temp[len(key_value):]

    cifer_value = [key_value[0]]
    for index,value in enumerate(key_stream):
        subs = plain_text_value[index] - cifer_value[index]
        if subs < 0:
            subs = (subs + 26) % 26
        else:
            subs = subs % 26
            
        cifer_value.append(subs)

    cifer_value =  cifer_value[-len(key_stream):]


    decrypted_list = []
    for i in cifer_value:
        decrypted_list.append([k for k,v in alpha.items() if v == i][0])
    with open(op, "w+") as f:
        f.write(''.join(decrypted_list))
        f.truncate()



if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--key', required=True, help='Enter the key')
    # parser.add_argument('--input_file', required=True, help='Enter the input file')
    # parser.add_argument('--output_file', required=True, help='Enter the output file')
    # parser.add_argument('--type', required=True, help='Enter 1 for encrypt/ 0 for decrypt ')

    # args = parser.parse_args()


    # # key_val = "m"
    # filename = args.input_file 
    # key_val = args.key.lower()
    # txt = read_file(filename)
    # # print(type(args.type))
    # if args.type == "1":
    #     enc,key_stream = encrypt(txt,key_val,args.output_file)
    #     # print(enc)

    # if args.type == "0":

    #     dec = decrypt(txt,args.output_file,key_val)

    


   
    filename = "out"
    key_val = "queenly".lower()
    txt = read_file(filename)
    # print(type(args.type))
    type = "0"
    if type == "1":
        enc,key_stream = encrypt(txt,key_val,"out")
        # print(enc)

    if type == "0":

        dec = decrypt(txt,"in1",key_val)     

 