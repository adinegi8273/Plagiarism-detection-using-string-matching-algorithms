const express = require('express');
const multer = require('multer');
const path = require('path');
const { execFile } = require('child_process');
const app = express();
const PORT = 3000;

// Middleware to serve static files like index.html
app.use(express.static('public'));
console.log("Hello1");
// Configure multer for file uploads
const upload = multer({ dest: 'uploads/' });

console.log("Hello2");
// Route to handle file upload and script execution
app.post('/check', upload.single('pdf'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded.');
  }

  const filePath = path.join(__dirname, req.file.path);
console.log("Hello3");
  // Step 1: Call bagofwords.py with file path
  execFile('python', ['bagofwords.py', filePath], (err1, stdout1, stderr1) => {
    if (err1) {
      console.error('bagofwords.py error:', err1, stderr1);
      return res.status(500).send('Error running bagofwords.py');
    }

    // Step 2: Call model.py
    execFile('python', ['model.py'], (err2, stdout2, stderr2) => {
      if (err2) {
        console.error('model.py error:', err2, stderr2);
        return res.status(500).send('Error running model.py');
      }

      // Send result back to frontend
      res.send(stdout2);
    });
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
