import pickle

with open("out.txt", "rb") as inputt:
    inputt=(inputt.read())
    with open(b"someobject.pickle", "wb") as output_file:
        pickle.dump([inputt,inputt],output_file)