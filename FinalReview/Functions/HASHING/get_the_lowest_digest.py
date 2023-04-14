import hashlib
 
# Print the shortest value
def get_the_lowest_digest_epa_65():
    new_hash_epa_65 = -1
    for alg_epa_65 in hashlib.algorithms_available:
        hash_epa_65 = hashlib.new(alg_epa_65)
        if hash_epa_65.digest_size == 0:
            continue
        elif new_hash_epa_65 == -1 or hash_epa_65.digest_size < new_hash_epa_65:
            new_hash_epa_65 = hash_epa_65.digest_size
            hash_name_epa_65 = alg_epa_65
    print(f"I am using : {hash_name_epa_65}, because it is the lowest digest with size {new_hash_epa_65}")    
    return hash_name_epa_65
