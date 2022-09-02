"""Module for Diffie-Hellman key exchange"""

import secrets


def private_key(p):
    """Return a private key less than p and greater than 1"""
    return secrets.randbelow(p)


def public_key(p, g, private):
    """Calculate a public key for a given private key"""
    return pow(g, private, p)


def secret(p, public, private):
    """Calculates a secret key given the public and private key"""
    return pow(public, private, p)
