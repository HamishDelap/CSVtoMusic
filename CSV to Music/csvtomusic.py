import csv
import pysynth

#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    global Crimes
    Crimes = []
    
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        if line["Crime type"] not in Crimes:
            Crimes.append(line["Crime type"])
    
    print(Crimes)

def Maker(file_obj, Crimes):
    Notes = ["g2", "a#2", "b2", "c2", "d#2", "e2", "f#2", "g3", "a#3", "b3", "c3", "d#3", "e3", "f#3", "g4", "a#4", "b4", "c4", "d#4", "e4", "f#4"]
    Music = []
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        for y in range(0, len(Crimes)):
            if Crimes[y] == line["Crime type"]:
                ToAppend = [Notes[y], 16]
                Music.append(ToAppend)
                    
    pysynth.make_wav(Music, fn = "test.wav")
#----------------------------------------------------------------------

with open("2017-09-wiltshire-street.csv") as f_obj:
    csv_dict_reader(f_obj)
with open("2017-09-wiltshire-street.csv") as f_obj:
    Maker(f_obj, Crimes)

