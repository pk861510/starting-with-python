"""f=open("prince2.txt","w")#prince2.txt file not exist but they creat if already exist then replace their content
f.write("true love starts with self love\n")
f.write("kindness starts with self kindness")
f.close()"""

"""f=open("prince2.txt","a")# in apend mode we add more line in a file
f.write("\nfirst line\n")
f.write("second line")# jitna time run hoga utna time prince2.txt me add hote jayega line
f.close()"""

# Handle read and write both

f=open("prince3.txt","r+")
print(f.read())
f.write("\nthank you")
