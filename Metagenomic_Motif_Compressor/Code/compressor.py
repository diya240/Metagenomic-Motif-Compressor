def compress_dna(sequence):
    motif = "ATCG"
    compressed = sequence.replace(motif, "M1")

    dictionary = {
        "M1": motif
    }

    return compressed, dictionary


dna = "ATCGATCGATCGGGTATCGATCG"

compressed_data, dictionary = compress_dna(dna)

print("Original DNA:")
print(dna)

print("\nDictionary:")
print(dictionary)

print("\nCompressed DNA:")
print(compressed_data)