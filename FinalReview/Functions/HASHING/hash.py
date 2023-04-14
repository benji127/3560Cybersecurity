import hashlib
#hash function
def hash_epa_65(text_to_hash_epa_65):
    h_epa_65 = hashlib.new(hash_name_epa_65)
    h_epa_65.update(text_to_hash_epa_65.encode())

    return h_epa_65.hexdigest()