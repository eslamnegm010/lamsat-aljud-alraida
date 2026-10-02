import json, os, re
H = os.path.dirname(os.path.abspath(__file__))
SCR = "/private/tmp/claude-504/-Users-islamnegm-development-CampusX/93dff923-83e1-4b76-ad04-f903640c7981/scratchpad/lamsat"
meta = json.load(open(f"{H}/img/meta.json"))
photos = [[p["w"], p["h"], p["cx"], p["cy"]] for p in meta["photos"]]
src = open(f"{H}/src.html", encoding="utf-8").read()
src = src.replace("PHOTOS_JSON", json.dumps(photos, separators=(",", ":"))).replace("ORBIT_JSON", json.dumps(meta["orbit"]))
os.makedirs(SCR, exist_ok=True)
open(f"{SCR}/lamsat.html", "w", encoding="utf-8").write(src)
i = src.index('<div class="loader"')
head, body = src[:i], src[i:]
head = head.replace("<title>لمسة الجود الرائدة</title>", """<title>لمسة الجود الرائدة · أعمال الخرسانات المسلحة</title>
<meta name="description" content="لمسة الجود الرائدة: أعمال النجارة والحدادة للخرسانات المسلحة لصالح شركات المقاولات والاستثمار في مشاريع فندقية وصحية وتعليمية.">
<meta name="theme-color" content="#f4f3ee" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#070f0a" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:title" content="لمسة الجود الرائدة">
<meta property="og:description" content="أعمال النجارة والحدادة للخرسانات المسلحة.">
<meta property="og:image" content="https://eslamnegm010.github.io/lamsat-aljud-alraida/img/og.jpg?v=2">
<meta property="og:url" content="https://eslamnegm010.github.io/lamsat-aljud-alraida/">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="لمسة الجود الرائدة">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://eslamnegm010.github.io/lamsat-aljud-alraida/">
<link rel="apple-touch-icon" href="img/icon.png">
<link rel="icon" href="img/icon.png">
<style>[hidden]{display:none!important}body{margin:0}img{max-width:100%}</style>""")
html = '<!doctype html>\n<html lang="ar" dir="rtl">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + head + "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
open(f"{H}/index.html", "w", encoding="utf-8").write(html)
print("built", len(html) // 1024, "KB")
