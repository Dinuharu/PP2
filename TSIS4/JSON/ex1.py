import json
with open('C:\PP2\sample-data.json') as f:
    data = json.load(f)
interfaces = data['imdata']

print("Interface Status")
print("=" * 80)
print("{:<40} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interfaces:
    dn = interface['l1PhysIf']['attributes']['dn']
    descr = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')
    print("{:<40} {:<20} {:<10} {:<6}".format(dn, descr, speed, mtu))
