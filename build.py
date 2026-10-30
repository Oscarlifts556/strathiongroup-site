"""Build the site: index.html (Claude artifact preview) and docs/ (standalone, for GitHub Pages)."""
import base64, shutil
from pathlib import Path

HERE = Path(__file__).parent
t = (HERE / "template.html").read_text(encoding="utf-8")
uri = "data:image/png;base64," + base64.b64encode((HERE / "mark.png").read_bytes()).decode()
(HERE / "index.html").write_text(t.replace("{{MARK}}", uri), encoding="utf-8")

# Standalone: a full document. The mark is a real file (cacheable) instead of a data URI.
head, body = t.split('<a class="skip"', 1)
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="icon" type="image/png" href="/mark.png">
<meta property="og:title" content="Strathion Group">
<meta property="og:description" content="A Wisconsin company building document, data and procurement systems for government.">
<meta property="og:image" content="https://strathiongroup.com/mark.png">
{head.replace("{{MARK}}", "/mark.png")}</head>
<body>
<a class="skip"{body}</body>
</html>
"""
dist = HERE / "docs"  # GitHub Pages serves /docs on main
dist.mkdir(exist_ok=True)
(dist / "index.html").write_text(page, encoding="utf-8")
shutil.copy(HERE / "mark.png", dist / "mark.png")
(dist / "CNAME").write_text("strathiongroup.com\n")
(dist / ".nojekyll").write_text("")
print("built index.html and docs/")
