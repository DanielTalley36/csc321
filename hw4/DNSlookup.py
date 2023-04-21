
'''## DNS look up program ##

author: Daniel Talley
Date 04-20-2023
'''
#libraries
import pandas as pd
import dns.resolver



#reading the domains.tsv file withe pandas and extractng the 2 column to a variable called domains
df_tsv = pd.read_csv('domains.tsv', delimiter='\t')
domains = df_tsv.iloc[:, 1]



ip_addr0=[]
#forward DNS lookup using dns.resolver query A
for i in range(len(domains)):
    ip = dns.resolver.query(domains[i], 'A')
    for val in ip:
        ip_addr0.append(val.to_text())

'''microsoftonline.com, and googleusercontent.com no longer exist, therefore were takin out of the list.

#printing hostnames-ipaddress to see visually
print("Domain Name:    ip Address:")
for i in range (len(domains)):
    print(f'{domains[i]} - {ip_addr0[i]}')



#Below is an attempt to get hostnames back from the ip address, I kept running into issues with hostnames not found errors
'''
hostnames=[]

#hostname = socket.gethostbyaddr(ip_addr0[1])
#print (hostname)
for i in range(11):
    hostname = socket.gethostbyaddr(ip_addr0[i])
    hostnames.append(hostname)

print(hostnames)
'''


'''baidu.com, live.com reverse dns lookup not found'''
