from ldap3 import Server, Connection, ALL, SUBTREE
server = Server('ldap://DC-01.damopro.in', get_info=ALL)
conn = Connection(server, user='damopro\\administrator', password='Welcome@12345', auto_bind=True)
base_dn = 'OU=Lab,DC=damopro,DC=in'
search_filter = '(|(objectClass=user)(objectClass=group))'
attributes = ['cn', 'sAMAccountName','description','distinguishedName']
conn.search(search_base=base_dn, search_filter=search_filter, search_scope=SUBTREE, attributes=attributes)
with open('users.txt', 'w') as f:
    f.write("sAMAccountName , cn , description , distinguishedName\n")
    for entry in conn.entries:
        name = str(entry.sAMAccountName)
        cn = str(entry.cn)
        description = str(entry.description) if entry.description else 'none'
        dn = str(entry.distinguishedName)
        f.write(f"{name} , {cn} , {description} , {dn}\n")
print("Users saved to users.txt")
