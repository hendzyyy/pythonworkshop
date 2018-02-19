countC=0
countG=0

DNA=open("yahyahyah.txt").read()
Length=len(DNA)

for i in range(len(DNA)):
    if DNA[i]=="C":
        countC=countC+1.00

    if DNA[i]=="G":
        countG=countG+1.00
        
print "Total number of C+G:",countC+countG
print "The percentage of C+G is:", ((countC+countG)/Length*100)
