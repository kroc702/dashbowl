import os
import markdown
import sys
import frontmatter

# Ordre d'assemblage des fichiers Markdown
FILES = [
    "rules/index.md",
    "teams/index.md"
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
.cover-title {
    font-size: 48pt;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-weight: 900;
    letter-spacing: 4px;
    margin: 0;
    text-transform: uppercase;
}

.cover-title span {
    color: #c0392b; /* Rouge Dashbowl */
}

.cover-title img {
    height: 90px;
    position: relative;
    top: 20px;
    filter: invert(1);
}

.cover-subtitle {
    font-size: 16pt;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: grey;
    margin-top: 15px;
    margin-bottom: 40px;
    font-weight: 300;
}
"""

def generate_html():
    lang = '';
    if(len(sys.argv) == 2):
        lang = sys.argv[1]
    if(len(lang)>0):
        langpath = lang + '/'
    else:
        lang = 'en'
    if(lang == 'en'):
        langpath = ''

    combined_md = ""
    for filepath in FILES:
        if os.path.exists(langpath+filepath):
            print('read file '+langpath+filepath)
            page = frontmatter.load(langpath+filepath)
            combined_md += "# "+page['title']+" \n\n"
            combined_md += page['subtitle']+" \n\n"
            combined_md += page.content + "\n\n"
            # with open(langpath+filepath, "r", encoding="utf-8") as f:
            #     combined_md += f.read() + "\n\n"

    combined_md = combined_md.replace("* TOC\n{:toc}","")
    combined_md = combined_md.replace('\n-',"\n\n-")
    combined_md = combined_md.replace('\n -',"\n\n -")
    combined_md = combined_md.replace('\n  -',"\n\n  -")
    combined_md = combined_md.replace('\n    -',"\n\n    -")

    # Conversion MD -> HTML
    html_body = markdown.markdown(combined_md, extensions=['tables', 'fenced_code'])

    # Assemblage du document HTML
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <!-- meta charset="utf-8"-->
        <style>{CSS_STYLE}</style>
    </head>
    <body>
        <p class="cover-title">DASH<img src="../images/ball.png"/><span>BOWL</span></p>

        {html_body}
    </body>
    </html>
    """

    if(len(combined_md) == 0):
        print('nothing generated')
    else:
        filename = "release/dashbowl_"+lang+".html"
        print('generate '+filename)
        # os.rmdir("release")
        os.makedirs("release", exist_ok=True)
        if os.path.exists(filename):
            os.remove(filename)
        with open(filename, "x") as f:
            f.write(full_html)

if __name__ == "__main__":
    generate_html()
