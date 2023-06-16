import dns.resolver
import sys

#DNS Record Resolver
#Following Tutorial by Joe Helle: https://www.youtube.com/watch?v=SLQrbjeVrk0

record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']


try:
    #Grabs the domain given after 'python3 demondns.py' 
    domain = sys.argv[1]
except IndexError:
    #If no domain given then let the user know they need to provide a domain
    print('Syntax Error - python3 demonDns.py <domain name>')
    quit()

#Grabs all the DNS records for the domain 
for records in record_types:
    try:
        answer = dns.resolver.resolve(domain, records)
        print(f'\n{records} Records')
        print('-'*30)

        for records in answer:
            print(records.to_text())

    #If the record type is not found then move on
    except dns.resolver.NoAnswer:
        print('No record found.')
        pass

    #If no DNS records are returned then let the user know
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist')
        quit()

    #If the user quits tell them goodbye
    except KeyboardInterrupt:
        print('See you, space cowboy.')
        quit()