class LCSDetector:
    def __init__(self):
        self.text = ""
        self.pattern = ""

    def get_strings(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def lcs_algorithm(self, similarity_threshold=0.8):
        """Calculate LCS and return True if similarity exceeds threshold"""
        if not self.pattern:  # Empty pattern can't be matched
            return False
            
        m = len(self.pattern)
        n = len(self.text)
        
        # Create DP table (m+1 x n+1)
        dp = [[0]*(n+1) for _ in range(m+1)]

        # Build LCS matrix
        for i in range(1, m+1):
            for j in range(1, n+1):
                if self.pattern[i-1] == self.text[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        lcs_length = dp[m][n]
        similarity = lcs_length / m  # Ratio of LCS to input length
        return similarity >= similarity_threshold


# Read input string (user uploaded content) from file
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
                   "teeth use mmal.calv care entir herd relat femal.femal calv may stay "
                   "matern herd rest live male leav herd reach puberti.forest eleph social group differ slightli may "
                   "compris adult femal offspr.howev may congreg larger group forest clear resourc abund.eleph need "
                   "extens land area surviv meet ecolog need includ food water space.averag eleph feed hour consum hundr "
                   "pound plant matter singl day.result lose habitat often come conflict peopl competit resource.")

# Tokenize database string by periods
database_tokens = [token.strip() for token in database_string.split('.') if token.strip()]

# Compare each input line with each database sentence
detector = set((ipt, dbs) for ipt in input_tokens for dbs in database_tokens)

lcs = LCSDetector()
matched_lines = set()
print("\nMatched content:")
for input_str, db_str in detector:
    lcs.get_strings(db_str, input_str)
    if lcs.lcs_algorithm():  # Using default 80% similarity threshold
        matched_lines.add(input_str)
        print(input_str)

# Calculate plagiarism percentage
matched_count = len(matched_lines)
total_input_lines = len(input_tokens)
plagiarism_percentage = (matched_count / total_input_lines) * 100 if total_input_lines > 0 else 0

print(f"\nPlagiarism Detected: {plagiarism_percentage:.2f}%")
