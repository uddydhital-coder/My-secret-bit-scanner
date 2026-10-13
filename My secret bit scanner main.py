def bit_scanner(secret_code, access_key):
    print("--- Secret Code Bit Scanner ---")
    print(f"Secret Code: {secret_code} (Binary: {bin(secret_code)})")
    print(f"Access Key:  {access_key} (Binary: {bin(access_key)})")
    print("-" * 35)

    and_result = secret_code & access_key
    print(f"1. Bitwise AND (&): {and_result} -> Binary: {bin(and_result)}")

    or_result = secret_code | access_key
    print(f"2. Bitwise OR (|):  {or_result} -> Binary: {bin(or_result)}")

    xor_result = secret_code ^ access_key
    print(f"3. Bitwise XOR (^): {xor_result} -> Binary: {bin(xor_result)}")

    not_result = ~secret_code
    print(f"4. Bitwise NOT (~): {not_result} -> Binary: {bin(not_result)}")

    left_shift = secret_code << 1
    print(f"5. Left Shift (<< 1): {left_shift} -> Binary: {bin(left_shift)}")

    right_shift = secret_code >> 1
    print(f"6. Right Shift (>> 1): {right_shift} -> Binary: {bin(right_shift)}")

    set_bits_count = bin(secret_code).count('1')
    print(f"7. Count of Set Bits in Secret Code: {set_bits_count}")

bit_scanner(29, 12)
