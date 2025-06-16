class KMP:
    def __init__(self):
        self.text = ""
        self.pattern = ""

    def get_strings(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def compute_prefix(self):
        """Create longest prefix suffix array for the pattern"""
        m = len(self.pattern)
        lps = [0] * m
        length = 0  # Length of the previous longest prefix suffix
        
        i = 1
        while i < m:
            if self.pattern[i] == self.pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def kmp_algorithm(self):
        """Main KMP pattern matching algorithm"""
        n = len(self.text)
        m = len(self.pattern)
        
        if m == 0:
            return False
            
        lps = self.compute_prefix()
        i = j = 0  # Indexes for text and pattern

        while i < n:
            if self.pattern[j] == self.text[i]:
                i += 1
                j += 1
                
            if j == m:
                return True  # Pattern found
            elif i < n and self.pattern[j] != self.text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False


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
                   "individu differ sever way african "
                   "rel distinct physic differ.exampl asian eleph ear smaller compar larg fan shape ear african speci."
                   "male s herd reach puberti.forest eleph social group differ slightli may "
                   "compris adult femal offspr.howev may congreg larger group forest clear resourc abund.eleph need "
                   "extens land area surviv meet ecolog need includ food water space.averag eleph feed hour consum hundr "
                   "pound plant matter singl day.result lose habitat often come conflict peopl competit resource.")

# Tokenize database string by periods
database_tokens = [token.strip() for token in database_string.split('.') if token.strip()]

# Compare each input line with each database sentence
detector = set((ipt, dbs) for ipt in input_tokens for dbs in database_tokens)

kmp = KMP()
matched_lines = set()
print("\nMatched content:")
for input_str, db_str in detector:
    kmp.get_strings(db_str, input_str)
    if kmp.kmp_algorithm():
        matched_lines.add(input_str)
        print(input_str)

# Calculate plagiarism percentage
matched_count = len(matched_lines)
total_input_lines = len(input_tokens)
plagiarism_percentage = (matched_count / total_input_lines) * 100 if total_input_lines > 0 else 0

print(f"\nPlagiarism Detected: {plagiarism_percentage:.2f}%")
