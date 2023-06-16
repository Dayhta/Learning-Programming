import dns.resolver
import sys

#Subdomain Enumerator 
#Following tutorial by Joe Helle: https://www.youtube.com/watch?v=E5BklV9I2-4
subdomain_array = ['www','mail','accounts', 'cpanel']
domain = sys.argv[1]


def main():
    subdomain_store = []

    for subdoms in subdomain_array:

        try:
            ip_value = dns.resolver.resolve(f'{subdoms}.{domain}.com', 'A')
            if ip_value: 
                subdomain_store.append(f'{subdoms}.{domain}')
                if f'{subdoms}.{domain}' in subdomain_store:
                    print(f'{subdoms}.{domain} valid!')
                else:
                    pass
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            quit()

main()