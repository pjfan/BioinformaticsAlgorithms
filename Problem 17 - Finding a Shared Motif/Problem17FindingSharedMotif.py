import FindSharedMotif as Motif
#import TestFindSharedMotif
import FASTA_Reader_faster 

RosalindFile = FASTA_Reader_faster.FASTA_Reader('rosalind_lcsm.txt')
RosalindFile.process_file()
Answers = sorted(RosalindFile.getFASTA_list())
print 'Answers'
matches = Motif.CompareTwoSeqs(Answers[0], Answers[1])
print 'Compared'
for seq in Answers[2:]:
	matches = Motif.CheckMatches(matches,seq)
print 'Checked'
print Motif.BestSolution(matches)

