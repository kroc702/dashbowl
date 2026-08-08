import os
import markdown
from weasyprint import HTML

# Ordre d'assemblage des fichiers Markdown
FILES = [
    "docs/index.md",
    "docs/les-bases.md",
    "docs/actions.md",
    "docs/factions.md"
]

# CSS de style pour le PDF (A4, typographie, couleurs)
CSS_STYLE = """
@page {
    size: A4;
    margin: 20mm 15mm;
    background-color: #faf8f5;
    @bottom-center {
        content: counter(page);
        font-family: sans-serif;
        font-size: 9pt;
        color: #777;
    }
}

body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.5;
    color: #222;
    margin: 0;
    padding: 0;
}

h1 {
    font-size: 24pt;
    color: #8b0000;
    border-bottom: 2px solid #8b0000;
    padding-bottom: 5px;
    margin-top: 0;
}

h2 {
    font-size: 16pt;
    color: #111;
    border-left: 4px solid #8b0000;
    padding-left: 8px;
    margin-top: 1.5em;
    page-break-after: avoid;
}

h3 {
    font-size: 12pt;
    font-style: italic;
    color: #444;
    page-break-after: avoid;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
}

th, td {
    border: 1px solid #ccc;
    padding: 8px 10px;
    text-align: left;
}

th {
    background-color: #eee;
    font-weight: bold;
}

blockquote {
    background: #f0ede6;
    border-left: 3px solid #666;
    margin: 10px 0;
    padding: 8px 12px;
    font-style: italic;
}
"""

def generate_pdf():
    combined_md = ""
    for filepath in FILES:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                combined_md += f.read() + "\n\n"

    # Conversion MD -> HTML
    html_body = markdown.markdown(combined_md, extensions=['tables', 'fenced_code'])

    # Assemblage du document HTML
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>{CSS_STYLE}</style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    os.makedirs("output", exist_ok=True)
    pdf_path = "output/dashbowl_rules.pdf"
    
    # Generation PDF avec WeasyPrint
    HTML(string=full_html).write_pdf(pdf_path)
    print(f"PDF généré avec succès : {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
