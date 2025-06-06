from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Générer la clé privée
private_key = ec.generate_private_key(ec.SECP256R1())

# Sérialiser la clé privée en PEM (base64)
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode('utf-8')

# Générer la clé publique
public_key = private_key.public_key()

# Sérialiser la clé publique en PEM
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode('utf-8')

print("Public Key (PEM):\n", public_key_pem)
print("Private Key (PEM):\n", private_key_pem)
