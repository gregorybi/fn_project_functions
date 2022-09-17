import io
import json
import logging

from fdk import response


def handler(ctx, data: io.BytesIO = None):
    plaintext = ""
    cipher = None
    key = None
    ciphertext = ""
    err_msg = None
    try:
        body = json.loads(data.getvalue())
        ciphertext = text_cleanup(body.get("text"))
        cipher = body.get("cipher") if body.get("cipher") else None
        key = body.get("key") if body.get("key") else None
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))
    
    logging.getLogger().info("Inside Python encrypt function")
    
    # in case it's configured in app context
    if cipher == None and key == None:
        cipher = ctx.Config()["cipher"]
        key = ctx.Config()["key"]
    
    if cipher == "Caesar":
        plaintext = caesar_decrypt(ciphertext)
    elif cipher == "Shift Cipher":
        if type(key) == int:
            plaintext = shift_cipher_decrypt(ciphertext, key)
        else:
            err_msg = "Shift Cipher requires an Integer as key"
    elif cipher == "Vigenere":
        if key == None or len(text_cleanup(key)) != len(key):
            err_msg = "Vigenere cipher requires a word as key (without any special characters)"
        else:
            plaintext = vigenere_decrypt(ciphertext, key)
    else:
        err_msg = "Please pick a cipher from {\"Caesar\", \"Shift Cipher\", \"Vigenere\"}"

    return response.Response(
        ctx, response_data=json.dumps(
            {"plaintext": plaintext} if err_msg == None else {"err": err_msg}),
        headers={"Content-Type": "application/json"}
    )


# Turns out we can't place them in general file and import it in both functions -_-
def text_cleanup(text):
    return ''.join([c if (ord(c) >= ord('A') and ord(c) <= ord('Z')) else '' for c in str(text).upper()])


def shift_cipher_encrypt(text, n):
    n = n % 26
    return ''.join([chr((ord(c)-ord('A')-n)%26+ord('A')) for c in text])


def shift_cipher_decrypt(text, n):
    return shift_cipher_encrypt(text, -n)


def caesar_encrypt(text):
    return shift_cipher_encrypt(text, 3)


def caesar_decrypt(text):
    return shift_cipher_decrypt(text, 3)


def vigenere_encrypt(text, key):
    key = text_cleanup(key)
    return ''.join([chr((ord(text[i]) - ord(key[i % len(key)])) % 26 + ord('A')) for i in range(len(text))])


def vigenere_decrypt(text, key):
    key = ''.join([chr(-(ord(c) - ord('A')) % 26 + ord('A')) for c in text_cleanup(key)]) # shift to 0-24 (-65), then 26 - ord(c) and shift back to uppercase (+65)
    return vigenere_encrypt(text, key)