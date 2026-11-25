import json, sys
sys.path.insert(0, ".")
from content import MODULES, PROJECT
t = open("template.html", encoding="utf-8").read()
data = json.dumps(MODULES, ensure_ascii=False).replace("</", "<\\/")
out = t.replace("__DATA__", data).replace("__PROJECT__", PROJECT)
open("../index.html", "w", encoding="utf-8").write(out)
n = sum(len(m["lessons"]) for m in MODULES); s = sum(len(l["slides"]) for m in MODULES for l in m["lessons"])
print("modules", len(MODULES), "lessons", n, "slides", s, "bytes", len(out))
