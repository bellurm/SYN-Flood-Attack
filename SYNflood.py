import scapy.all as sc

# dst="" is must be a domain name (ex: www.blog-cyberworm.com) or an IP address.
sc.srloop(sc.IP(dst="")/sc.TCP(dport=80, flags="S"))
