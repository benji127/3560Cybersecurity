#! /usr/bin/env python3 

#make a script scanes the last availble host range in the 
    #subnet and tells me if the hosts are onloine. 
import math
import os
import time

#def makeRange():

#given a subnet mask and an ip tell me the:
    #network_id, first_host, last_host, broadcasting
    #network class A,B..



#get the mask host id 
#how many bits were borroed to make that host 
#what is the range of the networks?
    # make it dynamic class for ip building 

# ip1="10.3.0.0"
# mask="255.255.192.0"

# host_split=mask.split(".")
# host_index=0
# for a in host_split:
#     a=int(a)
#     if(a ==255):
#         host_index+=1
#     else:
#         break

# bit_borrowed=0
# ip_split=ip1.split(".")
# ip_host=int(ip_split[host_index])
# for _pow in range(7,0,-1):
#     pow_two=math.pow(2,_pow)

#     if(ip_host >= pow_two):
#         ip_host-=pow_two
#         bit_borrowed+=1
#         #---------------

# #build the tail.
# ranges=int(255/math.pow(2,bit_borrowed))

# print(bit_borrowed)
# for a in range(0,256,ranges):
#     # i want to build the message from the back 
#     # so that way i can have  255.x.0.0 wheer 0's


#     head_ip="" #add the network id parts of the ip 10:255 .0:255 ..
#     for boundrie in range(0,host_index+1):
#         head_ip+=ip_split[boundrie]
#         head_ip+="."
        
#     tail_ip=""
#     head_ip_split= head_ip.split(".")
#     for x in range(4,len(head_ip_split),-1):
#         tail_ip+=".0"
    
#     net_id=str(a) #0
#     first_host=str(a+1) #1
#     last_host=str(a+ranges-1)# 0+63-1
#     bast=str(a+ranges)    #0 +63

#     #last host is wrong since bits are not counted right. 
    

#     print(ip1)
#     print(mask)
#     print(f"{head_ip}{net_id}{tail_ip}")
#     print(f"{head_ip}{first_host}{tail_ip}")
#     print(f"{head_ip}{last_host}{tail_ip}")
#     print(f"{head_ip}{bast}{tail_ip}")
#     break




# def AreTwoIPSInTheSameSubnet():

#     #are 2 ips in the same network?
#         #are they one the same subnet?
#         #needs to be dynamic 

#     #are they on the same network?
#         #what is the bits borrowed?
#         #what is the range?
#         #is range-1 < ip1[host_index] <range 
#         #&& range-1  < ip2[host_index]  <range 
#             #range -1 is the previous in that series 0 < x <  63 

#     ip1="10.0.0.189"
#     ip2="10.0.0.190"
#     mask1="255.255.255.192"

#     host_index=0
#     _255=mask1.split(".")
#     for i in _255:
#         i=int(i) #"63" ->63
#         if(i == 255):
#             host_index+=1
#         else:
#             break


#     #need 192 in num of bits borrowed 
#         #4
#     host_num=int(_255[host_index])
#     bit_borrowed=0
#     for i in range(7,0,-1):
#         curr_pow=math.pow(2,i) #2^7, 2^6 ..
#         if(host_num >= curr_pow ):
#             bit_borrowed+=1
#             host_num-=curr_pow

#     # 63 127 191
#     network_ranges=int(255/math.pow(2, bit_borrowed))

#     ip_host1=int(ip1.split(".")[host_index])
#     ip_host2=int(ip2.split(".")[host_index])

#     old_range=0
#     for new_range in range (0, 256,network_ranges+1 ):
#         #+1 since need need to tip into next network for forrowing loop. 
#         if new_range==0:
#             continue

#         #0 <= 55 and 55 < new_range
#         if (
#             old_range <= ip_host1 and ip_host1 < new_range
#             and 
#             old_range <= ip_host2 and ip_host2 < new_range
#             ):

#             print("they are in the same range")        
#             break
#         old_range=new_range

def ScanLastSubNetWithPing():
    ip="10.13.13.3"
    mask="255.255.255.192" #/26

    host_index=0
    split_mask=mask.split(".")
    for a in split_mask:
        a=int(a)
        if(a== 255):
            host_index+=1
        else:
            break

    ip_host=int(split_mask[host_index])
    # get bits used

    num_bits_used=0
    for a in range(7,0,-1):
        curr_pow=math.pow(2,a)

        if(ip_host >= curr_pow ):
            ip_host-=curr_pow
            num_bits_used+=1

    #network ranges 
    host_ranges=int(255/math.pow(2,num_bits_used))

    #scan the last range
    at_least_one=False
    for i in range(254, 255-host_ranges, -1): #255 ->254 ->  292
        x=ip.split(".")
        x[host_index]=str(i)
        x=".".join(x)

        msg=f"ping -c 1 -w 3 {x} >/dev/null 2>&1"    
        output=os.system(msg)
        # print(msg)
        if output==0:
            print("the user is online ") 
            at_least_one=True
        else:
            print(f"{x} host is offline ")

    def getBitNum(start, end ):
        sum=0
        for a in range(start,end,-1): 
            sum+=(math.pow(2,a))
        print(sum)