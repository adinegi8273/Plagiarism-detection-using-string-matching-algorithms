import math

class RabinKarp:
    def __init__(self):
        # Initialize character hash values: 'a' = 1, ..., 'z' = 26
        self.hash_codes = {chr(i): i - 96 for i in range(97, 123)}
        self.text = ""
        self.pattern = ""

    def get_strings(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def rabin_karp_algorithm(self):
        m = len(self.pattern)
        n = len(self.text)

        pattern_hash = self.calculate_hash(self.pattern)

        for i in range(n - m + 1):
            substring = self.text[i:i + m]
            substring_hash = self.calculate_hash(substring)
            if pattern_hash == substring_hash and self.check_characters(substring, self.pattern):
                return True
        return False

    def calculate_hash(self, s):
        m = len(s)
        hash_val = 0
        for i in range(m):
            ch = s[i]
            hash_val += (26 ** (m - i - 1)) * self.hash_codes.get(ch, 0)
        return hash_val

    def check_characters(self, s1, s2):
        return s1 == s2


# Read input string (user uploaded content) from a file
input_tokens = []
with open("pre-processed.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            input_tokens.append(line)

# Admin uploaded database paragraph (pre-processed)
database_string = ("eleph largest land mammal earth distinctli massiv bodi larg ear long trunk.use trunk pick object "
                   "trumpet warn greet eleph suck water drink bath among use.male femal african eleph grow tusk "
                   "individu either left right tusk one use usual smaller wear tear.eleph tusk serv mani purpos.extend "
                   "teeth use protec eleph trunk lift move object gather food strip bark tree. also use defens.time "
                   "drought eleph even use tusk dig hole find water underground.two genet differ african speci exist "
                   "savanna eleph forest eleph number characterist differenti.african savanna eleph largest eleph speci "
                   "asian forest eleph african forest eleph compar smaller size.asian eleph differ sever way african "
                   "rel distinct physic differ.exampl asian eleph ear smaller compar larg fan shape ear african speci."
                   "male sian eleph tusk male femal african eleph grow tusk.led matriarch eleph organ complex social "
                   "structur femal calv male eleph tend live isol small bachelor group.singl calf born femal everi four "
                   "five year gestati period month longest mammal.calv care entir herd relat femal.femal calv may stay "
                   "matern herd rest live male leav herd reach puberti.forest eleph social group differ slightli may "
                   "compris adult femal offspr.howev may congreg larger group forest clear resourc abund.eleph need "
                   "extens land area surviv meet ecolog need includ food water space.averag eleph feed hour consum hundr "
                   "pound plant matter singl day.result lose habitat often come conflict peopl competit resource.")

# Tokenize database string by periods
database_tokens = [token.strip() for token in database_string.split('.') if token.strip()]

# Compare each input line with each database sentence
detector = set((ipt, dbs) for ipt in input_tokens for dbs in database_tokens)

rk = RabinKarp()
matched_lines = set();
print("\nMatched content:")
for input_str, db_str in detector:
    rk.get_strings(db_str, input_str)
    if rk.rabin_karp_algorithm():
        matched_lines.add(input_str)
        print(input_str)

# Calculate plagiarism percentage
matched_count = len(matched_lines)
total_input_lines = len(input_tokens)
plagiarism_percentage = (matched_count / total_input_lines) * 100 if total_input_lines > 0 else 0

print(f"\nPlagiarism Detected: {plagiarism_percentage:.2f}%")
