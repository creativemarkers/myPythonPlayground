def custom_hash(data):
    # Initialize hash value
    hash_value = 0
    
    # Process each byte of the input data
    for byte in data:
        # Update hash value using bitwise XOR operation
        hash_value ^= byte
        
        # Permute the hash value to introduce non-linearity
        hash_value = (hash_value << 1) | (hash_value >> 7)  # Example permutation operation
        
    return hash_value

# Test the custom hash function
data1 = b'helloWorldSuckerBitchOnthisDIck'
data2 = b'world'

hash1 = custom_hash(data1)
hash2 = custom_hash(data2)

print("Hash of 'hello':", hash1)
print("Hash of 'world':", hash2)