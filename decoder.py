from pwn import * 

coded_key = "2366273d1d3924791d3923771d3970231d3978790a1d3925791d3920771f1d39"
message = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
encry_message = "5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b"

def de(a):
    ans=[]
    for i in a:
        ans.append(unhex(i))

    return ans


def de_ans(a):
    ans=[]
    for i in a:
        ans.append(str(unhex(i).decode('UTF-8')))

    return ans


def two_srt(a):
    x=0
    ans=[]
    temp=''
    for i in a:
        if x == 1:
            temp+=i
            ans.append(temp)
            temp=''
            x=0
        else:
            temp+=i
            x+=1
    return ans

coded_key=two_srt(coded_key)
encry_message= two_srt(encry_message)

# print(encry_message)
# print(coded_key)
coded_key= de(coded_key)
encry_message=de(encry_message)

key=list(map(lambda fla, ke: "{:02x}".format(ord(ke) ^ ord(fla)),message, encry_message))
key=''.join(de_ans(key))
# print(key)

flag=list(map(lambda fla, ke: "{:02x}".format(ord(ke) ^ ord(fla)),key, coded_key))
print(''.join(de_ans(flag)))