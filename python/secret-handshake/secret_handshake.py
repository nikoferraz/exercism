"""Module for the secret handshake."""

actions = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str):
    """Return a list with the steps of the secret handshake."""
    secret_handshake = []
    binary_str = binary_str[::-1]
    for i, action in enumerate(actions):
        if binary_str[i] == "1":
            secret_handshake.append(action)
    return secret_handshake if binary_str[-1] == "0" else secret_handshake[::-1]
