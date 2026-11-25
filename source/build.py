# Génère ../index.html à partir du contenu FR + traductions EN/DE
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as fr
import content_en as en
import content_de as de
from ui import UI


def goals_html(goals):
    return "<ul class='goals'>" + "".join(f"<li>{g}</li>" for g in goals) + "</ul>"


def translate(base, tr, lang):
    mods = copy.deepcopy(base)
    assert len(mods) == len(tr), f"{lang}: module count"
    for m, tm in zip(mods, tr):
        for k in ("weeks", "title", "summary", "deliverable"):
            m[k] = tm[k]
        assert len(m["lessons"]) == len(tm["lessons"]), f"{lang}: lessons in {m['id']}"
        for l, tl in zip(m["lessons"], tm["lessons"]):
            l["title"] = tl["title"]
            where = f"{lang} / {m['id']} / {tl['title']}"
            assert len(l["slides"]) == len(tl["slides"]), f"{where}: slide count {len(l['slides'])} != {len(tl['slides'])}"
            for i, (s, ts) in enumerate(zip(l["slides"], tl["slides"])):
                ty = s["type"]
                if ty == "text":
                    if "goals" in ts:
                        s["title"], s["html"] = UI[lang]["goals"], goals_html(ts["goals"])
                    else:
                        assert "h" in ts, f"{where} #{i}: expected TX"
                        s["title"], s["html"] = ts["t"], ts["h"]
                elif ty == "code":
                    assert set(ts) == {"t", "n"}, f"{where} #{i}: expected CO"
                    if s["note"] and not ts["n"]:
                        print(f"WARN missing note {where} #{i}")
                    s["title"], s["note"] = ts["t"], ts["n"]
                elif ty == "quiz":
                    assert "q" in ts and len(ts["o"]) == len(s["options"]), f"{where} #{i}: expected QU"
                    s["question"], s["options"], s["explain"] = ts["q"], ts["o"], ts["x"]
                    s["title"] = UI[lang]["quiz"]
                elif ty == "exercise":
                    assert "k" in ts, f"{where} #{i}: expected EX"
                    s["title"], s["task"] = ts["t"], ts["k"]
                    if ts["s"]:
                        s["solution"] = ts["s"].strip("\n")
    return mods


course = {
    "fr": {"modules": fr.MODULES, "project": fr.PROJECT},
    "en": {"modules": translate(fr.MODULES, en.MODULES, "en"), "project": en.PROJECT},
    "de": {"modules": translate(fr.MODULES, de.MODULES, "de"), "project": de.PROJECT},
}

here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, "template.html"), encoding="utf-8").read()
js = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
out = t.replace("__DATA__", js(course)).replace("__UI__", js(UI))
open(os.path.join(here, "..", "index.html"), "w", encoding="utf-8").write(out)
n = sum(len(l["slides"]) for m in fr.MODULES for l in m["lessons"])
print("languages", list(course), "slides per language", n, "bytes", len(out))
