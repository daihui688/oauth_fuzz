import random
import string
import base64
import hashlib


def gen_code_verifier_challenge():
    code_verifier = ''.join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
    code_verifier = base64.urlsafe_b64encode(code_verifier.encode('utf-8'))

    code_challenge = hashlib.sha256(code_verifier).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
    code_verifier = code_verifier.decode('utf-8')

    return code_verifier, code_challenge


