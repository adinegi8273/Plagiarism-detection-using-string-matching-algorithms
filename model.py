class RabinCarb:
    hashCodes = {}

    def __init__(self):
        for i in range(97, 123):  # 'a' to 'z'
            char = chr(i)
            value = i - 96
            RabinCarb.hashCodes[char] = value

    def getStrings(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def rabinCarbAlgorithm(self):
        m = len(self.pattern)
        n = len(self.text)

        patternHashValue = self.calculateHashValue(self.pattern)
        l = 0
        r = m - 1
        while r < n:
            subString = ''
            for i in range(l, r + 1):
                subString += self.text[i]
            substringHashValue = self.calculateHashValue(subString)
            if patternHashValue == substringHashValue and self.checkCharacters(subString, self.pattern):
                return True
            l += 1
            r += 1
        return False

    def calculateHashValue(self, text):
        m = len(text)
        hashValue = 0
        for i in range(1, m + 1):
            ch = text[i - 1]
            hashValue += (26 ** (m - i)) * RabinCarb.hashCodes.get(ch, 0)
        return hashValue

    def checkCharacters(self, subString, pattern):
        length = len(pattern)
        for i in range(length):
            if subString[i] != pattern[i]:
                return False
        return True


# === Main logic ===

inputString = ""
try:
    with open("pre-processed.txt", "r") as inputFile:
        inputTokens = [line.strip() for line in inputFile.readlines()]
except FileNotFoundError:
    print("File not opened! Try again")
    exit()

databaseString = ("eleph largest land mammal earth distinctli massiv bodi larg ear long trunk."
"use trunk pick object trumpet warn greet eleph suck water drink bath among use."
"male femal african eleph grow tusk individu either left right tusk one use usual smaller wear tear."
"eleph tusk serv mani purpos."
"extend teeth use protec eleph trunk lift move object gather food strip bark tree. also use defens."
"time drought eleph even use tusk dig hole find water underground."
"two genet differ african speci exist savanna eleph forest eleph number characterist differenti."
"african savanna eleph largest eleph speci asian forest eleph african forest eleph compar smaller size."
"asian eleph differ sever way african rel distinct physic differ."
"exampl asian eleph ear smaller compar larg fan shape ear african speci."
"male sian eleph tusk male femal african eleph grow tusk."
"led matriarch eleph organ complex social structur femal calv male eleph tend live isol small bachelor group."
"singl calf born femal everi four five year gestati period month longest mammal."
"calv care entir herd relat femal."
"femal calv may stay matern herd rest live male leav herd reach puberti."
"forest eleph social group differ slightli may compris adult femal offspr."
"howev may congreg larger group forest clear resourc abund."
"eleph need extens land area surviv meet ecolog need includ food water space."
"averag eleph feed hour consum hundr pound plant matter singl day."
"result lose habitat often come conflict peopl competit resource.")

databaseTokens = []
pattern = ""
for ch in databaseString:
    if ch != '.':
        pattern += ch
    else:
        databaseTokens.append(pattern)
        pattern = ""

detector = set()
for iptToken in inputTokens:
    for dbsToken in databaseTokens:
        key = iptToken
        value = dbsToken
        detector.add((key, value))

rb = RabinCarb()
print("Matched content:")
for item in detector:
    rb.getStrings(item[0], item[1])
    if rb.rabinCarbAlgorithm():
        print(item[0])
