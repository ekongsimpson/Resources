#!/usr/bin/python3

import os
import sys
import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Variables
HOME = os.getenv("HOME")
now = datetime.datetime.now()
d = now.date()
#cn = "testing1.fwd365prodne.local"
HOLDER=[]
cn = input("Please, enter your fully qualified domain name. e.g. my.fqdn.com\n")


keypath = f"{HOME}/{cn}-{d}.key"
csrpath = f"{HOME}/{cn}-{d}.csr"
crtpath = f"{HOME}/{cn}-{d}.crt"


# Generate RSA Private Key
def generate_key():
    if os.path.exists(keypath):
        print("Certificate file exists, aborting.")
        print(keypath)
        sys.exit(1)
    else:
        print("Generating Key... Please standby.")
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
        with open(keypath, "wb") as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
        HOLDER.append("Key Stored Here:" + keypath)
    return private_key

# Generate CSR
def generate_csr(private_key):
    print("How would you like to generate CSR data?")
    print("1) Default values (Self-Signed Certs).")
    print("2) Specify your own.")
    option = input("Choose (1/2): ").strip()

    if option == "1":
        c = "IT"
        st = "Milan"
        l = "Milan"
        o = "Coreview Inc"
        ou = "Coreview"
    else:
        c = input("Enter your country (ex. US): ").strip()
        st = input("Enter your state (ex. Nevada): ").strip()
        l = input("Enter your location (City): ").strip()
        o = input("Enter your organization: ").strip()
        ou = input("Enter your organizational unit (ex. IT): ").strip()

    csr = (
        x509.CertificateSigningRequestBuilder()
        .subject_name(
            x509.Name(
                [
                    x509.NameAttribute(NameOID.COUNTRY_NAME, c),
                    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, st),
                    x509.NameAttribute(NameOID.LOCALITY_NAME, l),
                    x509.NameAttribute(NameOID.ORGANIZATION_NAME, o),
                    x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, ou),
                    x509.NameAttribute(NameOID.COMMON_NAME, cn),
                ]
            )
        )
        .sign(private_key, hashes.SHA256())
    )

    with open(csrpath, "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))

    HOLDER.append("CSR Stored Here:" + csrpath)
    return csr

# Generate Self-Signed Certificate
def generate_certificate(private_key, csr):
    reply = input("Is this a Self-Signed Cert (y/n): ").lower().strip()
    if reply[0] == "y":
        cert = (
            x509.CertificateBuilder()
            .subject_name(csr.subject)
            .issuer_name(csr.subject)  # Self-signed
            .public_key(csr.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.datetime.utcnow())
            .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365 * 10))  # 10 years
            .sign(private_key, hashes.SHA256())
        )

        with open(crtpath, "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))

        HOLDER.append("Certificate Stored Here:" + crtpath)
    else:
        print("Skipping certificate generation.")

# Main Execution
if __name__ == "__main__":
    private_key = generate_key()
    csr = generate_csr(private_key)
    generate_certificate(private_key, csr)

    print(', '.join(HOLDER))

