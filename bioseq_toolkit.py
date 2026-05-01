print("      WELCOME TO BIOSEQ TOOLKIT      ")

#Choice System
choice = input("Enter '1' for Manual Input or '2' to read from FASTA file: ")

sequence = ""
seq_id = "Manual Input"
is_valid = True
mutations = 0

if choice == '1':
    sequence = input("Enter DNA Sequence: ").upper().replace(" ", "").strip()
elif choice == '2':
    path_input = input("Paste the full file path: ").strip()
    filename = path_input.replace('"', '').replace("'", "")
   
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if lines:
                seq_id = "FASTA File Input"
                sequence = "".join(line.strip() for line in lines[1:]).upper()
            else:
                print("Error: File is empty.")
                is_valid = False
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        is_valid = False
    
#Character Validation
if is_valid:
    if not sequence:
        is_valid = False
    else:
        valid_bases = "ATGC"
        for base in sequence:
            if base not in valid_bases:
                is_valid = False
                break

if not is_valid:
    print("Analysis aborted: Invalid sequence or missing file.")   
else:
    print(f"\nSequence ID: {seq_id}")
    print("\n Valid DNA sequence confirmed.")

#GC Content length
    length = len(sequence)

    a_count, t_count = sequence.count('A'), sequence.count('T')
    g_count, c_count = sequence.count('G'), sequence.count('C')
    gc_content = ((g_count + c_count) / length) * 100

    print("\n     DNA ANALYSIS      ")
    print(f"Length: {length}")
    print(f"A: {a_count} | T: {t_count} | G: {g_count} | C:{c_count}")
    print(f"GC Content: {gc_content:.2f}%")

#Reverse Complement
    complement_map = str.maketrans("ATGC", "TACG")
    reverse_complement = sequence.translate(complement_map)[::-1]

    print("\n      REVERSE COMPLEMENT      ")
    print(reverse_complement)    

#Transcription & Translation
    rna = sequence.replace("T", "U")

    codon_table = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'*', 'UAG':'*',
        'UGC':'C', 'UGU':'C', 'UGA':'*', 'UGG':'W'
    }

    protein_sequence = ""

    for i in range(0, len(rna) -2, 3):
        codon = rna[i:i+3]
        amino_acid = codon_table.get(codon, "?")
        protein_sequence += amino_acid
    
    print("\n      TRANSCRIPTION & PROTEIN TRANSLATION      ")
    print(f"RNA Sequence: {rna}")
    print(f"\nProtein Sequence: {protein_sequence}")
    print("Note: '*' represents a stop codon.")

#Motif Searching
    motif = input("\nEnter motif to search (e.g., ATG): ").upper().strip()
    positions = []
    start = 0
    while True:
        pos = sequence.find(motif, start)
        if pos == -1: break
        positions.append(pos)
        start = pos + 1

    if positions:
        print(f"Motif '{motif}' found at positions: {positions}")
        print(f"Total occurrences: {len(positions)}")
    else:
        print(f"Motif '{motif}' not found.")

#Mutation Detection
    print("\n      MUTATION DETECTION      ")
    sequence2 = input("Enter second DNA sequence for comparison: ").upper().replace(" ", "").strip()

    if len(sequence) != len(sequence2):
        print("Error: Sequences must be of equal length for direct comparison.")
    else:
        mutations = 0
        for i in range(len(sequence)):
            if sequence[i] != sequence2[i]:
                print(f"Mutation at Position {i}: {sequence[i]} -> {sequence2[i]}")
                mutations += 1
        print("Total Mutations Found:", mutations)

#Report Export
    with open("bioseq_report.txt", "w") as f:
        f.write("=====================================================\n")
        f.write(f"               REPORT FOR: {seq_id}\n")
        f.write("=====================================================\n")
        f.write(f"Original DNA: {sequence}\n")
        f.write(f"Sequence Length: {length} bp\n")
        f.write(f"GC Content: {gc_content: .2f}%\n")
        f.write(f"RNA Sequence: {rna}\n")
        f.write(f"Protein Sequence: {protein_sequence}\n")
        f.write(f"Reverse Complement: {reverse_complement}\n")
        f.write(f"Total Mutations: {mutations if 'mutations' in locals()else 'N/A'}\n")
        f.write("-" * 53 + "\n")
        f.write("End of Report\n")

print("\n Analysis complete! A detailed report has been saved as 'bioseq_report.txt'.")
