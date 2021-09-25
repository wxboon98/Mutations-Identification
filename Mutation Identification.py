from Bio import SeqIO
alignments = list(SeqIO.parse("filename.fasta","fasta"))
refseq = alignments[0]
mutation = []

for sequence in alignments:
	for i in range(0,len(refseq)):
		nt1 = refseq[i]
		nt2 = sequence[i]
		if nt2 in ['a','t','c','g'] and nt1 != nt2:
			mutation.append([i+1, nt1, nt2])
count={}
for i in mutation:
	a = tuple(i)
	if a not in count:
		count[a] = 1
	else:
		count[a]+= 1

print i, count[i]
