import os
import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))

def remove_line(s):
	# returns the header line, and the rest of the file
	return s[:s.index('\n') + 1], s[s.index('\n')+1:]


def parse_header_ppm(f):
	data = f.read()

	header = ""

	for i in range(3):
		header_i, data = remove_line(data)
		header += header_i

	return header, data

def to_bytes(n):
	s = hex(n)
	s_n = s[2:]
	if 'L' in s_n:
		s_n = s_n.replace('L', '')
	if len(s_n) % 2 != 0:
		s_n = '0' + s_n
	decoded = s_n.decode('hex')

	pad = (len(decoded) % BLOCK_SIZE)
	if pad != 0: 
		decoded = "\0" * (BLOCK_SIZE - pad) + decoded
	return decoded

def un_abc(ct):
	blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) / BLOCK_SIZE)]
	
	for i in range(1, len(blocks)):
		curr = int(blocks[len(blocks)-i].encode('hex'), 16)
		prev = int(blocks[len(blocks)-i-1].encode('hex'), 16)

		n_curr_blk = curr - prev
		while n_curr_blk < 0:
			curr += UMAX
			n_curr_blk = curr - prev


		blocks[len(blocks)-i] = to_bytes(n_curr_blk)
	iv = blocks[0]

	notabc = "".join(blocks)
 
	return iv, notabc

if __name__=="__main__":
	with open('body.enc.ppm', 'rb') as f:
		header, data = parse_header_ppm(f)
	
	iv, o_img = un_abc(data)

	with open('out.ppm', 'wb') as fw:
		fw.write(header)
		fw.write(o_img)
