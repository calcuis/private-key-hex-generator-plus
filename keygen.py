import secrets

def generate_private_key():
    # Generate a random 32-byte (256-bit) private key
    private_key = secrets.token_bytes(32)
    return private_key

private_key = generate_private_key()
print("Generated Private Key:", private_key.hex())
