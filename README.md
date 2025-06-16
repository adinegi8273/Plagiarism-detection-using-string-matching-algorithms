# Plagiarism-detection-using-string-matching-algorithms

🧠 Plagiarism Detection Using String Matching Algorithms
A powerful and user-friendly plagiarism detection system that utilizes classical string matching algorithms and machine learning to identify and visualize content similarity in academic and textual documents.

📌 Project Overview
This project aims to develop a robust plagiarism detection tool that performs fast and accurate text similarity comparisons using algorithms like Rabin-Karp, Knuth-Morris-Pratt (KMP), Longest Common Subsequence (LCS), and Jaccard Similarity. It includes a responsive web interface for real-time document comparison and interactive result visualization.

👥 Team Information
Aditya Negi – Backend Developer, Frontend Designer

Sarthak Rawat – Algorithm Implementation, Analysis

Aman Singh – Machine Learning Integration

Anshika Singh – Web Interface Design

🏗️ System Architecture
📂 Backend
Document preprocessing: cleaning, tokenizing, and normalizing

String matching implementation: Rabin-Karp, KMP, LCS, Jaccard Similarity

Plagiarism scoring and result generation

ML model using Random Forest for advanced similarity analysis

🖥️ Frontend
Interactive web interface (login, registration, upload)

Result visualization (matching text, similarity percentage, graphs)

✅ Features
📄 Upload and compare text or CSV documents

⚙️ Real-time analysis of string similarity

📊 Visual comparison using graphs and metrics

🧠 Optional machine learning-based detection

📁 Report generation in CSV/JSON formats

🧪 Testing Status
Test Type	Status	Notes
Unit Tests (Algorithms)	✅ Pass	All core algorithms tested for accuracy
Web Functionality	✅ Pass	UI and backend integration works smoothly
ML Integration	🔄 In Progress	Basic similarity detection implemented

📈 Progress Overview
✅ Implemented: UI, core algorithms (Rabin-Karp, KMP, LCS), basic ML integration

⏳ In Progress: Performance comparison and speed analysis of algorithms

🔜 Pending: Semantic-level analysis with improved ML models

🚧 Challenges Faced
Integrating Node.js backend with Python ML modules

Displaying live results on the webpage from processed data

Structuring performance metrics into easy-to-understand graphs

🔍 Project Deliverables
✔️ Functional plagiarism detection tool

✔️ Interactive web interface

✔️ Comparative analysis of detection algorithms

📊 Future Enhancements
Advanced semantic detection using NLP models

Improved UI with dynamic graphs (bar, pie, histogram)

Speed optimization for large document comparisons

🔗 Repository Information
Repo URL: [Add your GitHub repository link here]

Branch: main

Main Technologies: JavaScript (Node.js), Python, HTML/CSS

📥 Installation & Run Instructions
bash
Copy
Edit
# Clone the repo
git clone https://github.com/your-username/plagiarism-detector.git

# Navigate into the project folder
cd plagiarism-detector

# Install dependencies
npm install

# Start the backend server
node app.js

# File structure

project-root/
├── index.html
├── ai.py
├── rabin_carp.py
├── lcs.py
├── kmp.py
├── app.js
└── public/
    ├── login.html
    ├── plag.html
    ├── register.html
    └── visualization.html



# Start frontend (if separate)
open index.html in browser or use live-server
📧 Contact
For any queries or contributions, reach out to:

📩 aditya.230114984@gehu.ac.in

📩 sarthakrawat.230112045@gehu.ac.in

📩 amankumar.230112444@gehu.ac.in

📩 anshikasingh.230122594@gehu.ac.in
