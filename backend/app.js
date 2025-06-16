const http = require("http");
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");
const formidable = require("formidable");

function sendHtmlFile(response, filePath) {
  fs.readFile(filePath, "utf8", (error, data) => {
    if (error) {
      response.statusCode = 500;
      response.setHeader("Content-Type", "text/plain");
      response.end("Internal Server Error");
    } else {
      response.setHeader("Content-Type", "text/html");
      response.end(data);
    }
  });
}

function runPythonScript(script, args = []) {
  return new Promise((resolve, reject) => {
    const process = spawn("python", [script, ...args]);
    let output = "";
    let errorOutput = "";
    process.stdout.on("data", (data) => {
      output += data.toString();
    });
    process.stderr.on("data", (data) => {
      errorOutput += data.toString();
    });
    process.on("close", (code) => {
      if (code !== 0) {
        reject(errorOutput || `Script ${script} exited with code ${code}`);
      } else {
        resolve(output);
      }
    });
  });
}

function startServing(request, response) {
  if (request.url === "/" && request.method === "GET") {
    sendHtmlFile(response,"index.html");
    return;
  }
  if (request.url === "/plag.html" && request.method === "GET") {
    sendHtmlFile(response, path.join("public", "plag.html"));
    return;
  }
  if (request.url === "/visualization.html" && request.method === "GET") {
    sendHtmlFile(response, path.join("public", "visualization.html"));
    return;
  }
  if (request.url === "/register" && request.method === "GET") {
    sendHtmlFile(response, path.join("public", "register.html"));
    return;
  }
  if (request.url === "/login" && request.method === "GET") {
    sendHtmlFile(response, path.join("public", "login.html"));
    return;
  }
  if (request.url.startsWith("/assets/")) {
    const filePath = path.join(__dirname, request.url);
    fs.readFile(filePath, (err, data) => {
      if (err) {
        response.statusCode = 404;
        response.end("Asset not found");
      } else {
        const ext = path.extname(filePath);
        const contentType = {
          ".css": "text/css",
          ".jpg": "image/jpeg",
          ".jpeg": "image/jpeg",
          ".png": "image/png",
          ".gif": "image/gif"
        }[ext] || "application/octet-stream";
        response.setHeader("Content-Type", contentType);
        response.end(data);
      }
    });
    return;
  }
  if (request.url === "/upload-ai" && request.method === "POST") {
    const form = new formidable.IncomingForm();
    form.parse(request, async (err, fields, files) => {
      if (err) {
        response.statusCode = 500;
        response.end("Error processing file upload.");
        return;
      }
      if (!files.fileupload) {
        response.statusCode = 400;
        response.end("No file uploaded.");
        return;
      }
      const uploadedFilePath = files.fileupload.filepath;
      try {
        const aiResult = await runPythonScript("cnn_model.py", [uploadedFilePath]);
        response.setHeader("Content-Type", "text/html");
        response.end(`<pre>${aiResult}</pre><a href="/">Back to main page</a>`);
      } catch (err) {
        response.statusCode = 500;
        response.end("Error during AI analysis: " + err);
      }
    });
    return;
  }
  if (request.url === "/upload-string" && request.method === "POST") {
    const form = new formidable.IncomingForm();
    form.parse(request, async (err, fields, files) => {
      if (err) {
        response.statusCode = 500;
        response.end("Error processing file upload.");
        return;
      }
      if (!files.fileupload) {
        response.statusCode = 400;
        response.end("No file uploaded.");
        return;
      }
      const uploadedFilePath = files.fileupload.filepath;
      try {
        await runPythonScript("bagofwords.py", [uploadedFilePath]);
        const rabinResult = await runPythonScript("rabin_karp.py", ["preprocessed.txt"]);
        response.setHeader("Content-Type", "text/plain");
        response.end(rabinResult);
      } catch (err) {
        response.statusCode = 500;
        response.end("Error during analysis: " + err);
      }
    });
    return;
  }
  if (request.url === "/api/visualization" && request.method === "GET") {
    Promise.all([
      runPythonScript("rabin_karp.py", ["preprocessed.txt"]),
      runPythonScript("kmp.py", ["preprocessed.txt"]),
      runPythonScript("lcs.py", ["preprocessed.txt"])
    ]).then(([rk, kmp, lcs]) => {
      const toStr = (x) => (x === null || x === undefined) ? "" : String(x);
      rk = toStr(rk);
      kmp = toStr(kmp);
      lcs = toStr(lcs);
      const extractAccuracy = (output) => {
        const match = output.match(/Plagiarism Detected:\s*([\d.]+)%/i);
        return match ? parseFloat(match[1]) / 100 : 0;
      };
      response.setHeader("Content-Type", "application/json");
      response.end(JSON.stringify({
        rabinKarp: rk,
        kmp: kmp,
        lcs: lcs,
        accuracies: {
          rabinKarp: extractAccuracy(rk),
          kmp: extractAccuracy(kmp),
          lcs: extractAccuracy(lcs)
        }
      }));
    }).catch(err => {
      response.statusCode = 500;
      response.end("Error during visualization: " + err);
    });
    return;
  }
  response.statusCode = 404;
  response.end("Not Found");
}

const server = http.createServer(startServing);
server.listen(7070, () => {
  console.log("Server is listening on port 7070");
});
