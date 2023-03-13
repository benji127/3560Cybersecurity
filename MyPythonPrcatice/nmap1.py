def nmap(ip):
    var = f" nmap -A -p {ip} -sV -oN {ip}.txt"
    print(f"running nmap: {var}")
    
    
    
nmap(input("What is the IP address? "))
    
    