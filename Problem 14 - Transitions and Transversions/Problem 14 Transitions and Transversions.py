import TransRatio
import FASTA_Reader

RosalindFile = FASTA_Reader.FASTA_Reader('rosalind_tran.txt')
RosalindFile.process_file()

Answer = RosalindFile.getFASTA_dict()

Ratio = TransRatio.TransRatio(Answer[Answer.keys()[0]], Answer[Answer.keys()[1]])

print Ratio
