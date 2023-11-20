import zlib

original_text = "안녕하세요" *1000

utf8_encoded = original_text.encode('utf-8')
compressed = zlib.compress(utf8_encoded)

original_size = len(original_text)
encoded_size = len(utf8_encoded)
compressed_size = len(compressed)

print(f"Original Size: {original_size:,} bytes") # Original Size: 5,000 bytes
print(f"UTF-8 Encoded Size: {encoded_size:,} bytes") # UTF-8 Encoded Size: 15,000 bytes
print(f"Compressed Size: {compressed_size:,} bytes") # Compressed Size: 71 bytes



