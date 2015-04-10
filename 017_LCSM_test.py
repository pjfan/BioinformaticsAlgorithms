import FindSharedMotif as Motif
import unittest

class TestFindMotif(unittest.TestCase):
    def runTest(self):
        self.test_compare_two_seqs_start_nuc()
        self.test_compare_two_seqs_end_nuc()
        self.test_is_it_in_here_true()
        self.test_is_it_in_here_false()
        self.test_check_matches_all_match()
        self.test_check_matches_no_match()
        self.test_check_matches_some_match()
        print 'Tests All Passed!'   
    def test_compare_two_seqs_start_nuc(self):
        self.assertEqual(Motif.CompareTwoSeqs('ATA', 'CATA'),['A', 'T', 'AT', 'TA', 'ATA'])
    def test_compare_two_seqs_end_nuc(self):
        self.assertEqual(Motif.CompareTwoSeqs('ATA', 'ATAC'),['A', 'T', 'AT', 'TA', 'ATA'])
    def test_is_it_in_here_true(self):
        self.assertTrue(Motif.IsItInHere('AT', 'CGATC'))
    def test_is_it_in_here_false(self):
        self.assertFalse(Motif.IsItInHere('AT', 'CGTAC'))
    def test_check_matches_all_match(self):
        self.assertEquals(Motif.CheckMatches(['ATA', 'TCG', 'GCC'], 'ATATCGCC'), ['ATA', 'TCG', 'GCC'])
    def test_check_matches_no_match(self):
        self.assertEquals(Motif.CheckMatches(['ATA', 'TAG', 'GCC'], 'ATTCCGTT'), [])
    def test_check_matches_some_match(self):
        self.assertEquals(Motif.CheckMatches(['ATA', 'TCG', 'GCC'], 'ATATCCTGT'), ['ATA'])
    def test_best_solution_multiple_best(self):
        self.assertEquals(Motif.BestSolution(['ATA', 'TCG', 'GCC']), 'ATA')
    def test_best_solution_one_best(self):
        self.assertEquals(Motif.BestSolution(['ATA', 'TCG', 'GCCA']), 'GCCA')

Tester = TestFindMotif()
Tester.runTest()

