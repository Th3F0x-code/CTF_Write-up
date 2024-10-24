from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, current_app, Response
)
from flask_login import login_required, current_user

import os, math, base64
from Crypto.Cipher import DES
from . import auth 

bp = Blueprint('crypto', __name__, url_prefix='/crypto')

# dh params
G = 128
P = 3793

@bp.route('/get_params')
@login_required
def get_params():
    return jsonify({"status":"ok", "message":"dh params","params":{"g":str(G),"p":str(P)}})

@bp.route('/get_public/<int:uid>')
@login_required
def get_users_public(uid):
    public = get_public(auth.User.query.get_or_404(int(uid)).key)
    return jsonify({"status":"ok", "message":"public user {}".format(uid),"public":str(public)})

# my dh handshake functions
def get_public(private):
    # return ((G ** private) % P)
    return pow(G, private, P)

def get_symmetric(publicB, privateA):
    # return ((publicB ** privateA) % P)
    return pow(publicB, privateA, P)

# symmetric encr
def get_selected_cipher(symkey):
    # trim key to 16 bytes
    if ((len(bin(symkey))-2) > 56):
        symkey = symkey & 0xffffffffffffff
    return DES.new(symkey.to_bytes(8,byteorder='little'), DES.MODE_ECB)

def encrypt(cleartext, symkey):
    selected_cipher = get_selected_cipher(symkey)
    cleartext_length = len(cleartext)
    next_multiple_of_8 = 8 * math.ceil(cleartext_length/8)
    padded_cleartext = cleartext.ljust(next_multiple_of_8)
    raw_ciphertext = selected_cipher.encrypt(padded_cleartext)
    return base64.b64encode(raw_ciphertext).decode('utf-8')

def decrypt(ciphertext,symkey):
    selected_cipher = get_selected_cipher(symkey)
    raw_ciphertext = base64.b64decode(ciphertext)
    decrypted_message_with_padding = selected_cipher.decrypt(raw_ciphertext)
    return decrypted_message_with_padding.decode('utf-8').strip()

