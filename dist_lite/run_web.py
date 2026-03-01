#!/usr/bin/env python3
"""MD → HWPX 웹 변환기 (Lite)

실행: python run_web.py
브라우저에서 http://localhost:8080 접속
"""

import http.server
import json
import os
import sys
import tempfile
import webbrowser
from pathlib import Path
from urllib.parse import parse_qs

# 경로 설정 (PyInstaller 호환)
# PyInstaller --onefile 모드에서는 sys._MEIPASS에 자원이 풀린다
if getattr(sys, 'frozen', False):
    SCRIPT_DIR = Path(sys._MEIPASS)
else:
    SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from converter.md_to_hwpx import convert_md_to_hwpx

PORT = 8080

HTML_PAGE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MD → HWPX 변환기</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Noto Sans KR', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }

  .container {
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    padding: 48px;
    max-width: 640px;
    width: 100%;
  }

  h1 {
    font-size: 28px;
    font-weight: 700;
    color: #1a1a2e;
    margin-bottom: 8px;
    text-align: center;
  }

  .subtitle {
    font-size: 14px;
    color: #888;
    text-align: center;
    margin-bottom: 36px;
  }

  .drop-zone {
    border: 2px dashed #c4c4c4;
    border-radius: 16px;
    padding: 48px 24px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    background: #fafafa;
    margin-bottom: 24px;
  }

  .drop-zone:hover, .drop-zone.dragover {
    border-color: #667eea;
    background: #f0f0ff;
    transform: scale(1.01);
  }

  .drop-zone .icon {
    font-size: 48px;
    margin-bottom: 12px;
  }

  .drop-zone p {
    color: #666;
    font-size: 15px;
  }

  .drop-zone .filename {
    font-weight: 700;
    color: #333;
    font-size: 16px;
    margin-top: 8px;
  }

  .btn {
    display: block;
    width: 100%;
    padding: 16px;
    font-size: 17px;
    font-weight: 700;
    color: white;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border: none;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.3s ease;
    letter-spacing: 1px;
  }

  .btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(102,126,234,0.5);
  }

  .btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
  }

  .status {
    margin-top: 16px;
    text-align: center;
    font-size: 14px;
    min-height: 20px;
  }

  .status.success { color: #27ae60; font-weight: 500; }
  .status.error { color: #e74c3c; font-weight: 500; }
  .status.loading { color: #667eea; }

  input[type="file"] { display: none; }

  .footer {
    margin-top: 32px;
    text-align: center;
    font-size: 12px;
    color: #aaa;
  }
</style>
</head>
<body>

<div class="container">
  <h1>📄 MD → HWPX</h1>
  <p class="subtitle">마크다운 파일을 한글(HWPX) 문서로 변환합니다</p>

  <div class="drop-zone" id="dropZone">
    <div class="icon">📁</div>
    <p>마크다운 파일(.md)을 여기에 끌어다 놓거나<br>클릭하여 선택하세요</p>
    <div class="filename" id="fileName"></div>
  </div>

  <input type="file" id="fileInput" accept=".md">

  <button class="btn" id="convertBtn" disabled>변환하기</button>

  <div class="status" id="status"></div>

  <div class="footer">
    MD → HWPX Converter Lite
  </div>
</div>

<script>
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const convertBtn = document.getElementById('convertBtn');
const fileName = document.getElementById('fileName');
const status = document.getElementById('status');

let selectedFile = null;

dropZone.addEventListener('click', () => fileInput.click());

dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
  dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('dragover');
  const file = e.dataTransfer.files[0];
  if (file && file.name.endsWith('.md')) {
    selectFile(file);
  } else {
    showStatus('⚠️ .md 파일만 지원됩니다', 'error');
  }
});

fileInput.addEventListener('change', (e) => {
  if (e.target.files[0]) selectFile(e.target.files[0]);
});

function selectFile(file) {
  selectedFile = file;
  fileName.textContent = '✅ ' + file.name;
  convertBtn.disabled = false;
  status.textContent = '';
}

function showStatus(msg, cls) {
  status.textContent = msg;
  status.className = 'status ' + (cls || '');
}

convertBtn.addEventListener('click', async () => {
  if (!selectedFile) return;

  convertBtn.disabled = true;
  showStatus('⏳ 변환 중...', 'loading');

  const formData = new FormData();
  formData.append('file', selectedFile);

  try {
    const response = await fetch('/convert', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const err = await response.text();
      throw new Error(err);
    }

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = selectedFile.name.replace('.md', '.hwpx');
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);

    showStatus('✅ 변환 완료! 다운로드를 확인하세요', 'success');
  } catch (e) {
    showStatus('❌ ' + e.message, 'error');
  }

  convertBtn.disabled = false;
});
</script>
</body>
</html>"""


class ConvertHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode("utf-8"))

    def do_POST(self):
        if self.path != "/convert":
            self.send_error(404)
            return

        content_type = self.headers.get("Content-Type", "")
        if "multipart/form-data" not in content_type:
            self.send_error(400, "multipart/form-data required")
            return

        # Parse multipart boundary
        boundary = content_type.split("boundary=")[-1].encode()
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        # Extract file content from multipart
        parts = body.split(b"--" + boundary)
        file_content = None
        original_name = "output"

        for part in parts:
            if b"filename=" in part:
                # Extract filename
                header_end = part.find(b"\r\n\r\n")
                if header_end == -1:
                    continue
                header = part[:header_end].decode("utf-8", errors="replace")
                if 'filename="' in header:
                    original_name = header.split('filename="')[1].split('"')[0]
                    original_name = original_name.rsplit(".", 1)[0]  # remove .md

                file_content = part[header_end + 4:]
                # Remove trailing boundary markers
                if file_content.endswith(b"\r\n"):
                    file_content = file_content[:-2]
                break

        if file_content is None:
            self.send_error(400, "No file uploaded")
            return

        try:
            # Write MD to temp file
            with tempfile.NamedTemporaryFile(
                mode="wb", suffix=".md", delete=False
            ) as tmp_md:
                tmp_md.write(file_content)
                tmp_md_path = Path(tmp_md.name)

            # Output path
            tmp_hwpx_path = tmp_md_path.with_suffix(".hwpx")

            # Convert
            convert_md_to_hwpx(tmp_md_path, tmp_hwpx_path)

            # Read result
            hwpx_bytes = tmp_hwpx_path.read_bytes()

            # Cleanup
            tmp_md_path.unlink(missing_ok=True)
            tmp_hwpx_path.unlink(missing_ok=True)

            # Send response
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header(
                "Content-Disposition",
                f'attachment; filename="{original_name}.hwpx"',
            )
            self.send_header("Content-Length", str(len(hwpx_bytes)))
            self.end_headers()
            self.wfile.write(hwpx_bytes)

        except Exception as e:
            # Cleanup on error
            try:
                tmp_md_path.unlink(missing_ok=True)
            except:
                pass
            try:
                tmp_hwpx_path.unlink(missing_ok=True)
            except:
                pass

            error_msg = f"변환 실패: {str(e)}"
            self.send_response(500)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(error_msg.encode("utf-8"))

    def log_message(self, format, *args):
        # Quieter logging
        if "POST /convert" in str(args):
            print(f"[변환 요청] {args[0]}")


def main():
    server = http.server.HTTPServer(("", PORT), ConvertHandler)
    url = f"http://localhost:{PORT}"
    print(f"🚀 MD → HWPX 변환기가 시작되었습니다!")
    print(f"   브라우저에서 {url} 에 접속하세요")
    print(f"   종료하려면 Ctrl+C 를 누르세요")
    print()

    # Auto-open browser
    try:
        webbrowser.open(url)
    except:
        pass

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n서버를 종료합니다.")
        server.server_close()


if __name__ == "__main__":
    main()
