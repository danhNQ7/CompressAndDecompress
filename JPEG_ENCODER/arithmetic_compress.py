import contextlib, sys
import arithmeticcoding
import time
import os
import tempfile
import arithmetic_decompress
import pickle
python3 = sys.version_info.major >= 3
DIR = os.path.dirname(os.path.realpath(__file__))+'/TMP/'
def arith_compress(inputstr):
	ip = tempfile.NamedTemporaryFile()
	inputstr=inputstr.encode('ascii')
	ip.write(inputstr) 
	ip.flush()
	inputfile=ip.name
	op = tempfile.NamedTemporaryFile()
	outputfile= op.name
	
	# Read input file once to compute symbol frequencies
	freqs = get_frequencies(inputfile)
	freqs.increment(256)  # EOF symbol gets a frequency of 1

	with open(inputfile, "rb") as inp, \
			contextlib.closing(arithmeticcoding.BitOutputStream(open(outputfile, "wb"))) as bitout:
		write_frequencies(bitout, freqs)
		compress(freqs, inp, bitout)
	output = open(outputfile, "rb") 
	return output.read()
# Command line main application function.
def main(args):
	# Handle command line arguments
	if len(args) != 2:
		sys.exit("Usage: python arithmetic-compress.py InputFile OutputFile")
	inputfile, outputfile = args
	
	# Read input file once to compute symbol frequencies
	freqs = get_frequencies(inputfile)
	freqs.increment(256)  # EOF symbol gets a frequency of 1
	
	# Read input file again, compress with arithmetic coding, and write output file
	with open(inputfile, "rb") as inp, \
			contextlib.closing(arithmeticcoding.BitOutputStream(open(outputfile, "wb"))) as bitout:
		write_frequencies(bitout, freqs)
		compress(freqs, inp, bitout)


# Returns a frequency table based on the bytes in the given file.
# Also contains an extra entry for symbol 256, whose frequency is set to 0.
def get_frequencies(filepath):
	freqs = arithmeticcoding.SimpleFrequencyTable([0] * 257)
	with open(filepath, "rb") as input:
		while True:
			b = input.read(1)
			if len(b) == 0:
				break
			b = b[0] if python3 else ord(b)
			freqs.increment(b)
	return freqs


def write_frequencies(bitout, freqs):
	for i in range(256):
		write_int(bitout, 32, freqs.get(i))


def compress(freqs, inp, bitout):
	enc = arithmeticcoding.ArithmeticEncoder(32, bitout)
	while True:
		symbol = inp.read(1)
		if len(symbol) == 0:
			break
		symbol = symbol[0] if python3 else ord(symbol)
		enc.write(freqs, symbol)
	enc.write(freqs, 256)  # EOF
	enc.finish()  # Flush remaining code bits


# Writes an unsigned integer of the given bit width to the given stream.
def write_int(bitout, numbits, value):
	for i in reversed(range(numbits)):
		bitout.write((value >> i) & 1)  # Big endian


# Main launcher
if __name__ == "__main__":
	tic = time.time()
	# main(sys.argv[1 : ])
	txt = arith_compress("Toi di hoc giua troi mua gio")
	with open("testt.pkl", "wb") as fp:   #Pickling
		pickle.dump(txt, fp)
	with open("testt.pkl", "rb") as fp:   #Pickling
		txt = pickle.load(fp)
	aaa= arithmetic_decompress.arith_decompress(txt)
	print(aaa)
	print("Time: " +str((time.time()-tic)) + "s")