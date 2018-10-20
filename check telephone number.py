#coding:utf-8
"check the reality of a phone number"
import random
CN_mobile = \
[134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,
187,188,147,178,1705]
CN_union = [130,131,132,155,156,185,186,145,176,1709]
CN_telecom = [133,153,180,181,189,177,1700]
def main():
    while True:
        temp=raw_input('Enter your phone number:')
        if len(temp)<11:
            print ('invalid length, your number should be in 11 digits')
            continue
        elif (int(temp[:3]) not in CN_mobile+CN_union+CN_telecom)and (int(temp[:4]) not in CN_mobile+CN_union+CN_telecom):
            print ('No such a operator')
            continue
        else:
            print ('Operator:'),
            if (int(temp[:3]) in CN_mobile)or(int(temp[:4]) in CN_mobile):
                print ('China Mobile')
            elif (int(temp[:3]) in CN_union)or(int(temp[:4]) in CN_union):
                print ('China Unicom')
            else:
                print ('China Telecom')
            print ('We\'re sending verification code via text to your phone:'+temp)
            break


if __name__ == "__main__":
    main()

