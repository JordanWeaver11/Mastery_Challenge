#!/usr/bin/python
from random import randint

msg_raw = "This is the secret message";
print("Raw Message: ", msg_raw);

msgLen = len(msg_raw);

msg_list = [];
for i in range(msgLen):
	msg_list.append(msg_raw[i]);

key = [];
for i in range(msgLen):
	key.append(randint(0, 30));

msg_enc = [];
for i in range(msgLen):
	code = ord(msg_list[i]);
	#check for space
	if code == 32:
		code = 36;
	else:
		code = code - key[i];
	msg_enc.append(chr(code));

print("Encoded message: ", "".join(msg_enc));

msg_dec = [];
for i in range(msgLen):
	dec = ord(msg_enc[i]);
	if dec == 36:
		dec = 32;
	else:
		dec = dec + key[i];
	msg_dec.append(chr(dec));
print("Decoded message: ", "".join(msg_dec));
