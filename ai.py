import subprocess
import sys
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import string
from numpy.linalg import norm

# Step 2: Read preprocessed text from pre-processed.txt
with open("pre-processed.txt", "r", encoding="utf-8") as f:
    input_text = f.read()

# Step 3: Database string (tokenized per line as database_lines)
database_string = ("eleph largest land mammal earth distinctli massiv bodi larg ear long trunk use trunk pick object "
                   "trumpet warn greet eleph suck water drink bath among use male femal african eleph grow tusk "
                   "individu either left right tusk one use usual smaller wear tear eleph tusk serv mani purpos extend "
                   "teeth use protec eleph trunk lift move object gather food strip bark tree also use defens time "
                   "drought eleph even use tusk dig hole find water underground two genet differ african speci exist "
                   "savanna eleph forest eleph number characterist differenti african savanna eleph largest eleph speci "
                   "asian forest eleph african forest eleph compar smaller size asian eleph differ sever way african "
                   "rel distinct physic differ exampl asian eleph ear smaller compar larg fan shape ear african speci "
                   "male sian eleph tusk male femal african eleph grow tusk led matriarch eleph organ complex social "
                   "structur femal calv male eleph tend live isol small bachelor group singl calf born femal everi four "
                   "five year gestati period month longest mammal calv care entir herd relat femal femal calv may stay "
                   "matern herd rest live male leav herd reach puberti forest eleph social group differ slightli may "
                   "compris adult femal offspr howev may congreg larger group forest clear resourc abund eleph need "
                   "extens land area surviv meet ecolog need includ food water space averag eleph feed hour consum hundr "
                   "pound plant matter singl day result lose habitat often come conflict peopl competit resource.")

# Tokenize database string by sentences (simulate per line)
database_lines = [line.strip() for line in database_string.split('.') if line.strip()]

# Step 4: Feature extraction (using simple tokenizer for robustness)
def simple_tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    return tokens

def stylometric_features(text):
    words = simple_tokenize(text)
    avg_sentence_length = len(words)
    vocab_richness = len(set(words)) / len(words) if words else 0
    punctuation_freq = 0  # punctuation removed
    word_length_avg = np.mean([len(w) for w in words]) if words else 0
    return [avg_sentence_length, vocab_richness, punctuation_freq, word_length_avg]

# Step 5: Generate dataset (train on database_lines and original samples)
plagiarized_samples = database_lines
original_samples = [
    "this is an original paragraph written in a completely different style",
    "another authentic content with unique vocabulary and structure"
]

X = []
y = []
for text in plagiarized_samples:
    X.append(stylometric_features(text))
    y.append(1)
for text in original_samples:
    X.append(stylometric_features(text))
    y.append(0)
X = np.array(X)
y = np.array(y)

# Step 6: Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Step 7: Extract features from input text
input_features = np.array(stylometric_features(input_text)).reshape(1, -1)

# Step 8: Predict
prediction = model.predict(input_features)
print(f"\nPrediction: {'Plagiarized' if prediction == 1 else 'Original'}")

# Step 9: Find matching lines (if plagiarized)
if prediction == 1:
    matched_lines = []
    threshold = 0.5  # small threshold for similarity
    for line in database_lines:
        features = np.array(stylometric_features(line))
        dist = norm(features - input_features)
        if dist < threshold:
            matched_lines.append(line)
    print("\nPlagiarized content detected in lines:")
    for line in matched_lines:
        print(f"- {line}")
    matched_count = len(matched_lines)
    total_input_lines = 1  # since input is one block
    plagiarism_percentage = (matched_count / total_input_lines) * 100 if total_input_lines > 0 else 0
    print(f"\nPlagiarism Detected: {plagiarism_percentage:.2f}%")
else:
    print("\nNo plagiarism detected.")
