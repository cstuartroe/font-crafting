import argparse
import os
from flask import Flask, render_template_string, send_from_directory

parser = argparse.ArgumentParser(description="Serve an HTML page to test a local font file.")
parser.add_argument("font_path", help="Path to the font file (.ttf, .otf, .woff, etc.)")
args = parser.parse_args()

font_path = os.path.abspath(args.font_path)
if not os.path.isfile(font_path):
    raise FileNotFoundError(f"Font file not found at: {font_path}")
font_dir, font_filename = os.path.split(font_path)

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Font Tester - {{ font_filename }}</title>
    <style>
        @font-face {
            font-family: 'TestFont';
            src: url('/font');
        }

        body {
            font-family: system-ui, -apple-system, sans-serif;
            max-width: 900px;
            margin: 2rem auto;
            padding: 0 1rem;
            background-color: #f8f9fa;
            color: #212529;
        }

        header {
            margin-bottom: 2rem;
            border-bottom: 2px solid #e9ecef;
            padding-bottom: 1rem;
        }

        .controls {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
            background: #ffffff;
            padding: 1rem;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .controls label {
            font-weight: 600;
        }

        .controls input[type="range"] {
            flex-grow: 1;
        }
        
        .preview-input-box {
            font-family: sans-serif;
            font-size: 16px;
            line-height: 1.4;
            width: 100%;
            min-height: 100px;
            padding: 1.5rem;
            border: 1px solid #ced4da;
            border-radius: 6px;
            background: #ffffff;
            box-sizing: border-box;
            resize: vertical;
            outline: none;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .preview-box-input:focus {
            border-color: #86b7fe;
            box-shadow: 0 0 0 0.25rem rgba(13,110,253,.25);
        }

        .preview-box {
            font-family: 'TestFont', sans-serif;
            font-size: 60px;
            line-height: 1;
            white-space: pre;
            width: 100%;
            min-height: 300px;
            padding: 1.5rem;
            border: 1px solid #ced4da;
            border-radius: 6px;
            background: #ffffff;
            box-sizing: border-box;
            resize: vertical;
            outline: none;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
    </style>
</head>
<body>
    <header>
        <h1>Font Tester</h1>
        <p>Testing file: <code>{{ font_filename }}</code></p>
    </header>

    <div class="controls">
        <label for="size-slider">Font Size:</label>
        <input type="range" id="size-slider" min="12" max="144" value="60">
        <span id="size-display">60px</span>
    </div>

    <textarea class="preview-input-box" id="preview-text-input" placeholder="Type text here to test your font..."></textarea>
    
    <div class="preview-box" id="preview-text"></div>

    <script>
        const slider = document.getElementById('size-slider');
        const inputarea = document.getElementById('preview-text-input');
        const display = document.getElementById('size-display');
        const preview = document.getElementById('preview-text');

        slider.addEventListener('input', (e) => {
            const size = e.target.value + 'px';
            preview.style.fontSize = size;
            display.textContent = size;
        });
        
        inputarea.addEventListener('input', (e) => {
            preview.textContent = e.target.value;
        });
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, font_filename=font_filename)


@app.route("/font")
def serve_font():
    return send_from_directory(font_dir, font_filename)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
