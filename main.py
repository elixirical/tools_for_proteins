file = open("protein.txt","r")
rArg = 0.0
hHis = 0.0
kLys = 0.0
dAsp = 0.0
eGlu = 0.0
sSer = 0.0
tThr = 0.0
nAsn = 0.0
qGln = 0.0
cCys = 0.0
gGly = 0.0
pPro = 0.0
aAla = 0.0
vVal = 0.0
iIle = 0.0
lLeu = 0.0
mMet = 0.0
fPhe = 0.0
yTyr = 0.0
wTrp = 0.0
charged = 0.0
positive = 0.0
negative = 0.0
polar = 0.0
hydrophobic = 0.0
total = 0.0
# positive = lys, rArg
# negative = apartate, glutamate
# polar = ser, thr, tyr, cys, asn, gln, his, gly
# hydrophobic = ala, val, phe, trp, leu, ile, met, pro
for line in file:
    for char in line:
        if char == "R":
            rArg += 1
            positive += 1
            charged += 1
        elif char == "H":
            hHis += 1
            polar += 1
        elif char == "K":
            kLys += 1
            positive += 1
            charged += 1
        elif char == "D":
            dAsp += 1
            negative += 1
            charged += 1
        elif char == "E":
            eGlu += 1
            negative += 1
            charged += 1
        elif char == "S":
            sSer += 1
            polar += 1
        elif char == "T":
            tThr += 1
            polar += 1
        elif char == "N":
            nAsn += 1
            polar += 1
        elif char == "Q":
            qGln += 1
            polar += 1
        elif char == "C":
            cCys += 1
            polar += 1
        elif char == "G":
            gGly += 1
            polar += 1
        elif char == "P":
            pPro += 1
            hydrophobic += 1
        elif char == "A":
            aAla += 1
            hydrophobic += 1
        elif char == "V":
            vVal += 1
            hydrophobic += 1
        elif char == "I":
            iIle += 1
            hydrophobic += 1
        elif char == "L":
            lLeu += 1
            hydrophobic += 1
        elif char == "M":
            mMet += 1
            hydrophobic += 1
        elif char == "F":
            fPhe += 1
            hydrophobic += 1
        elif char == "Y":
            yTyr += 1
            polar += 1
        elif char == "W":
            wTrp += 1
            hydrophobic += 1
        if char != "\n":
            total += 1

with open("data.txt","a") as dataFile:
    dataFile.write("Total:\t\t" + str(total) + "\n\n")
    dataFile.write("Charged:\t" + str(charged) + "\t(" + str((charged/total)*100) + "%)\n\n" )
    dataFile.write("Positive:\t" + str(positive) + "\t(" + str((positive/total)*100) + "%)\n\n" )
    dataFile.write("Lysine:\t\t" + str(kLys) + "\t(" + str((kLys/total)*100) + "%)\n" )
    dataFile.write("Arginine:\t" + str(rArg) + "\t(" + str((rArg/total)*100) + "%)\n\n" )
    dataFile.write("Negative:\t" + str(negative) + "\t(" + str((negative/total)*100) + "%)\n\n" )
    dataFile.write("Aspartate:\t" + str(dAsp) + "\t(" + str((dAsp/total)*100) + "%)\n" )
    dataFile.write("Glutamate:\t" + str(eGlu) + "\t(" + str((eGlu/total)*100) + "%)\n\n" )
    dataFile.write("Polar:\t\t" + str(polar) + "\t(" + str((polar/total)*100) + "%)\n\n" )
    dataFile.write("Serine:\t\t" + str(sSer) + "\t(" + str((sSer/total)*100) + "%)\n" )
    dataFile.write("Threonine:\t" + str(tThr) + "\t(" + str((tThr/total)*100) + "%)\n" )
    dataFile.write("Tyrosine:\t" + str(yTyr) + "\t(" + str((yTyr/total)*100) + "%)\n" )
    dataFile.write("Cysteine:\t" + str(cCys) + "\t(" + str((cCys/total)*100) + "%)\n" )
    dataFile.write("Asparagine:\t" + str(nAsn) + "\t(" + str((nAsn/total)*100) + "%)\n" )
    dataFile.write("Glutamine:\t" + str(qGln) + "\t(" + str((qGln/total)*100) + "%)\n" )
    dataFile.write("Histidine:\t" + str(hHis) + "\t(" + str((hHis/total)*100) + "%)\n" )
    dataFile.write("Glycine:\t" + str(gGly) + "\t(" + str((gGly/total)*100) + "%)\n\n" )
    dataFile.write("Hydrophobic:\t" + str(hydrophobic) + "\t(" + str((hydrophobic/total)*100) + "%)\n\n" )
    dataFile.write("Alanine:\t" + str(aAla) + "\t(" + str((aAla/total)*100) + "%)\n" )
    dataFile.write("Valine:\t\t" + str(vVal) + "\t(" + str((vVal/total)*100) + "%)\n" )
    dataFile.write("Phenylalanine:\t" + str(fPhe) + "\t(" + str((fPhe/total)*100) + "%)\n" )
    dataFile.write("Tryptophan:\t" + str(wTrp) + "\t(" + str((wTrp/total)*100) + "%)\n" )
    dataFile.write("Leucine:\t" + str(lLeu) + "\t(" + str((lLeu/total)*100) + "%)\n" )
    dataFile.write("Isoleucine:\t" + str(iIle) + "\t(" + str((iIle/total)*100) + "%)\n" )
    dataFile.write("Methionine:\t" + str(mMet) + "\t(" + str((mMet/total)*100) + "%)\n" )
    dataFile.write("Proline:\t" + str(pPro) + "\t(" + str((pPro/total)*100) + "%)\n" )
