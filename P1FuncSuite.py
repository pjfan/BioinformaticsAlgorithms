def count(text, pattern):
    #iterate through a string 'text' and determine how many times the string 'pattern' appears
    text_length = len(text)
    pattern_length = len(pattern)
    count = 0
    for i in xrange(text_length-pattern_length+1):
        if text[i:i+pattern_length] == pattern:
            count+=1
    return count

def find_all_kmers(text, k):
    text_length = len(text)
    kmer_dict = dict()
    #Create a dictionary where all the words that are of length k are the keys and the number of times the word appears in the sequence are the values.
    for i in xrange(text_length-int(k)+1):
        if text[i:(i+int(k))] in kmer_dict:
            kmer_dict[text[i:(i+int(k))]] += 1
        else:
            kmer_dict[text[i:(i+int(k))]] = 1
    return kmer_dict

def freq_words(text, k):
    kmer_dict = find_all_kmers(text, k)
    #Iterate through the dictionary and determine which keys have the highest values. 
    freq_max = 0
    most_freq_words = []
    for key in kmer_dict.keys():
        if kmer_dict[key] < freq_max:
            continue
        if kmer_dict[key] > freq_max:
            freq_max = kmer_dict[key]
            most_freq_words = []
        most_freq_words.append(key)
    return most_freq_words  

def rev_comp(pattern):
    #Generates the reverse complement of a string 'pattern'.
    pattern_rev = []
    for base in pattern:
        if base == 'A':
            pattern_rev.append('T')
        if base == 'C':
            pattern_rev.append('G')
        if base == 'T':
            pattern_rev.append('A')
        if base == 'G':
            pattern_rev.append('C')
    pattern_rev = pattern_rev[::-1]
    return ''.join(pattern_rev)

def patt_match(pattern, genome):
    #Determines at which indices a sub-string 'pattern' occurs within a string 'genome.'
    genome_length = len(genome)
    pattern_length = len(pattern)
    pos_list = []
    for i in xrange(genome_length-pattern_length+1):
        if genome[i:(i+pattern_length)] == pattern:
            pos_list.append(i)
    return pos_list


def clump_check(sequence, k, t):
    #finds all kmers and the number of times they appear in a sequence, then checks if the k-mer appears 't' times or more.
    kmer_dict = find_all_kmers(sequence, k)
    lt_clump_kmers = []
    for key in kmer_dict.keys():
        if kmer_dict[key] >= t:
            lt_clump_kmers.append(key)
    return lt_clump_kmers

def clump_find(genome, k, L, t):
    #finds all k-mers that form '(L,t)-clumps' in a string genome.
    genome_length = len(genome)
    lt_clump_kmers = set([])
    #Iterates through genome using sliding window approach. Window is of size L. Runs clump_check to look for (L,t)-clumps in the window.
    #Uses sets to remove repeats
    for i in xrange(genome_length-int(L)+1):
        lt_clump_kmers = lt_clump_kmers.union(set(clump_check(genome[i:(i+int(L))], int(k), int(t)))-lt_clump_kmers)
    return lt_clump_kmers

def min_skew(genome):
    #Skew is defined as the difference between the number of G bp's and C bp's in the genome. 
    G_count = 0
    C_count = 0
    #The skew is always 0 to begin with.
    skew_list = [0]
    #Calculates the skew at every position.
    for base in genome:
        if base == 'G':
            G_count += 1
        if base == 'C':
            C_count += 1
        skew_list.append(G_count-C_count)
    #Finds the minimum value in the list of skews.
    min_value = skew_list[0]
    min_skew_list = []
    for i, skew in enumerate(skew_list):
        if skew > min_value:
            continue
        if skew < min_value:
            min_value = skew
            min_skew_list = []
        min_skew_list.append(i)
    return min_skew_list

def mismatch_detect(pattern1, pattern2):
    len_pattern = len(pattern1)
    mismatch = 0
    for i in xrange(len_pattern):
        if pattern1[i] != pattern2[i]:
            mismatch += 1
    return mismatch

def approx_patt_match(pattern, text, d):
    pattern_length = len(pattern)
    text_length = len(text)
    pos_list = []
    for i in xrange(text_length-pattern_length+1):
        if mismatch_detect(text[i:(i+pattern_length)], pattern) <= int(d):
            pos_list.append(i)
    return pos_list

#First approach to Problem 1G displayed below. Second approach is significantly faster.
#First approach:
    #First find all kmers in text.
    #Then generate a set containing all kmers in text + all kmers that have at most d mismatches with kmers that appear in the text.
    #Create a dictionary and iterate through text to find how many times each kmer appears with at most d mismatches.
    #Iterate through dictionary and determine which kmers appear the most.

def gen_single_mismatch_set(kmer):
    #Takes a single kmer and generates a set containing itself and all kmers that are exactly 1 mismatch away from it.
    kmer_length = len(kmer)
    mismatch_set = set([])
    original_kmer = kmer
    kmer = list(kmer)
    for i in xrange(kmer_length):
        kmer[i] = 'A'
        mismatch_set = mismatch_set.union(set([''.join(kmer)])-mismatch_set)
        kmer[i] = 'G'
        mismatch_set = mismatch_set.union(set([''.join(kmer)])-mismatch_set)
        kmer[i] = 'C'
        mismatch_set = mismatch_set.union(set([''.join(kmer)])-mismatch_set)
        kmer[i] = 'T'
        mismatch_set = mismatch_set.union(set([''.join(kmer)])-mismatch_set)
        kmer = list(original_kmer)
    return mismatch_set


def gen_mismatch(kmers_all, d):
    mismatch_set = set([])
    for kmer in kmers_all:
        mismatch_set = mismatch_set.union(gen_single_mismatch_set(kmer)-mismatch_set)
    if d>1:
        mismatch_set = mismatch_set.union(gen_mismatch(mismatch_set,d-1)-mismatch_set)
    return mismatch_set


def freq_words_mismatches(text, k, d):
    d = int(d)
    k = int(k)
    #First find all kmers in text.
    kmers_all = find_all_kmers(text, k)
    #Then generate a set containing all kmers in text + all kmers that have at most d mismatches with kmers that appear in the text.
    mismatch_set = gen_mismatch(kmers_all, d)
    #Create a dictionary and iterate through text to find how many times each kmer appears with at most d mismatches.
    kmer_dict = dict()
    for kmer in mismatch_set:
        kmer_dict[kmer] = len(approx_patt_match(kmer, text, d))
    #Iterate through dictionary and determine which kmers appear the most.
    max_value = 0
    most_freq_words = []
    for key in kmer_dict.keys():
        if kmer_dict[key] < max_value:
            continue
        if kmer_dict[key] > max_value:
            max_value = kmer_dict[key]
            most_freq_words = []
        most_freq_words.append(key)
    return most_freq_words

#Second (and much much faster) approach:
#Iterate through text using sliding window approach, 
#Each time you add a kmer to the dicitonary also add all kmers that have at most d mismatches with that kmer to the dictionary.
#Iterate through dictionary at end to find out what kmers appeared most. 


def gen_mismatch_set(kmer,d):
    #Takes a single kmer and generates a set containing itself and all kmers that are exactly 1 mismatch away from it.
    kmer_length = len(kmer)
    mismatch_set = set([])
    original_kmer = kmer
    kmer = list(kmer)
    for i in xrange(kmer_length):
        kmer[i] = 'A'
        mismatch_set = mismatch_set.union(set([''.join(kmer)])-mismatch_set)
        kmer[i] = 'G'
        mismatch_set = mismatch_set.union(set([''.join(kmer)])-mismatch_set)
        kmer[i] = 'C'
        mismatch_set = mismatch_set.union(set([''.join(kmer)])-mismatch_set)
        kmer[i] = 'T'
        mismatch_set = mismatch_set.union(set([''.join(kmer)])-mismatch_set)
        kmer = list(original_kmer)
    #Recursive approach for if d>1, for each kmer in mismatch_set run gen_mismatch_set(kmer,(d-1)) on it to find all kmers exactly 1 mismatch away.
    #It works because a kmer 1 mismatch away from a kmer 1 mismatch away from the original is 2 mismatches away from the original. 
    if d > 1:
        for kmer in mismatch_set:
            mismatch_set = mismatch_set.union(gen_mismatch_set(kmer,(d-1))-mismatch_set)
    return mismatch_set

def find_all_kmers_mismatch(text, k, d, kmer_dict=None):
    text_length = len(text)
    if kmer_dict == None:
        kmer_dict = dict()
    #Create a dictionary where all the words that are of length k are the keys and the number of times the word appears in the sequence are the values.
    #Also include in the dictionary all kmers that are at most d-mismatches away from any kmer that appears in the sequence.
    for i in xrange(text_length-k+1):
        for kmer in gen_mismatch_set(text[i:(i+k)],d):
            if kmer in kmer_dict:
                kmer_dict[kmer] += 1
            else:
                kmer_dict[kmer] = 1
    return kmer_dict

def freq_words_mismatches_alt(text, k, d):
    k = int(k)
    d = int(d)
    kmer_dict = find_all_kmers_mismatch(text, k, d)
    #Iterate through dictionary and determine which kmers appear the most.
    max_value = 0
    most_freq_words = []
    for key in kmer_dict.keys():
        if kmer_dict[key] < max_value:
            continue
        if kmer_dict[key] > max_value:
            max_value = kmer_dict[key]
            most_freq_words = []
        most_freq_words.append(key)
    return most_freq_words

def freq_words_mismatches_rev(text,k,d):
    k = int(k)
    d = int(d)
    kmer_dict = find_all_kmers_mismatch(text, k, d)
    kmer_dict = find_all_kmers_mismatch(rev_comp(text), k, d, kmer_dict)    
    #Iterate through dictionary and determine which kmers appear the most.
    max_value = 0
    most_freq_words = []
    for key in kmer_dict.keys():
        if kmer_dict[key] < max_value:
            continue
        if kmer_dict[key] > max_value:
            max_value = kmer_dict[key]
            most_freq_words = []
        most_freq_words.append(key)
    return most_freq_words
