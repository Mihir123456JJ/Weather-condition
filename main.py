weather=(1,0,0,0,1,1,0)
suncount=0
rainycount=0
for i in weather:
    if weather[i]==0:
        rainycount=rainycount+1
    else:
        suncount=suncount+1
if (suncount>rainycount ):
    print("Summer")
else:
    print('Winter')            
