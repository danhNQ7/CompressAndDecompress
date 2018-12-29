import sys
import arithmeticcoding
import time
import tempfile
import os
python3 = sys.version_info.major >= 3

def arith_decompress(inputstr):

	inp = tempfile.NamedTemporaryFile(delete=False)
	inp.write(inputstr) 
	inp.close
	op = tempfile.NamedTemporaryFile()
	outputfile= op.name
	
	# Perform file decompression
	with open(outputfile, "wb") as out,open(inp.name, "rb") as inp:
		bitin = arithmeticcoding.BitInputStream(inp)
		freqs = read_frequencies(bitin)
		decompress(freqs, bitin, out)
	os.unlink(inp.name)
	with open(outputfile, "r") as output:
		return output.read()
# Command line main application function.
def main(args):
	# Handle command line arguments
	if len(args) != 2:
		sys.exit("Usage: python arithmetic-decompress.py InputFile OutputFile")
	inputfile, outputfile = args
	
	# Perform file decompression
	with open(outputfile, "wb") as out, open(inputfile, "rb") as inp:
		bitin = arithmeticcoding.BitInputStream(inp)
		print(inp)
		freqs = read_frequencies(bitin)
		decompress(freqs, bitin, out)


def read_frequencies(bitin):
	def read_int(n):
		result = 0
		for _ in range(n):
			result = (result << 1) | bitin.read_no_eof()  # Big endian
		return result
	
	freqs = [read_int(32) for _ in range(256)]
	freqs.append(1)  # EOF symbol
	return arithmeticcoding.SimpleFrequencyTable(freqs)


def decompress(freqs, bitin, out):
	dec = arithmeticcoding.ArithmeticDecoder(32, bitin)
	while True:
		symbol = dec.read(freqs)
		if symbol == 256:  # EOF symbol
			break
		out.write(bytes((symbol,)) if python3 else chr(symbol))


# Main launcher
if __name__ == "__main__":
	tic = time.time()
	main(sys.argv[1 : ])
	print("Time: " +str((time.time()-tic)) + "s")
