def betterCompression(s):
    char_freq = {}
    i = 0
    
    while i < len(s):
        char = s[i]
        i += 1
        freq = ""
        
        while i < len(s) and s[i].isdigit():
            freq += s[i]
            i += 1
        
        freq = int(freq)
        
        if char in char_freq:
            char_freq[char] += freq
        else:
            char_freq[char] = freq
    
    compressed_str = ""
    for char in sorted(char_freq.keys()):
        compressed_str += char + str(char_freq[char])
    
    return compressed_str

# Example usage
compressed_str = 'a12c56a1b5'
properly_compressed = betterCompression(compressed_str)
print(properly_compressed)  # Output: 'a3b2c10'





