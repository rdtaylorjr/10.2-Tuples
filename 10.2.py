name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    spl = time.split(':')
    hour = spl[0]
    counts[hour] = counts.get(hour,0) + 1

hours = list()
#for hr, ct in counts.items():
    #newtup = (hr, ct)
    #hours.append(newtup)
#hours = sorted (hours)

hours = sorted( [ (hr,ct) for hr,ct in counts.items() ] )

for hr, ct in hours:
    print(hr,ct)





#print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
