# Helpers for translation files: each mirrors the slide order of content.py
def G(goals): return {"goals": goals}
def TX(t, h): return {"t": t, "h": h}
def CO(t, n=""): return {"t": t, "n": n}
def QU(q, o, x): return {"q": q, "o": o, "x": x}
def EX(t, k, s=None): return {"t": t, "k": k, "s": s}
def M(weeks, title, summary, deliverable, lessons):
    return {"weeks": weeks, "title": title, "summary": summary, "deliverable": deliverable, "lessons": lessons}
def L(title, slides): return {"title": title, "slides": slides}
