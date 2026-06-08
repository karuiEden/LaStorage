import os, re, shutil, subprocess

QUESTIONS_DIR = "Вопросы"
TEX_DIR = "tex"
MAIN_TEX = "main.tex"


def find_pandoc():
    """Находит pandoc, не полагаясь на PATH (он бывает неполным в разных шеллах)."""
    p = shutil.which("pandoc")
    if p:
        return p
    for c in (os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe"),
              os.path.expandvars(r"%ProgramFiles%\Pandoc\pandoc.exe")):
        if os.path.isfile(c):
            return c
    raise FileNotFoundError("pandoc не найден ни в PATH, ни в стандартных каталогах")


PANDOC = find_pandoc()

os.makedirs(TEX_DIR, exist_ok=True)


def extract_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not m:
        return "", text
    fm, body = m.group(1), text[m.end():]
    # Ищем title: "..." или block scalar |-
    for i, line in enumerate(fm.splitlines()):
        if line.startswith("title:"):
            val = line[6:].strip().strip("\"'")
            if val and val not in ("|-", "|"):
                return val, body
            # block scalar — берём первую непустую следующую строку
            for nxt in fm.splitlines()[i+1:]:
                s = nxt.strip()
                if s:
                    return s, body
    return "", body


files = sorted(
    [f for f in os.listdir(QUESTIONS_DIR) if f.endswith(".md") and f[0].isdigit()],
    key=lambda x: int(re.match(r"^(\d+)", x).group(1))
)

tex_names = []

for fname in files:
    with open(os.path.join(QUESTIONS_DIR, fname), encoding="utf-8") as f:
        text = f.read()

    title, body = extract_frontmatter(text)
    if not title:
        title = fname.replace(".md", "")

    # ![[image.png]] → ![](Вопросы/media/image.png)
    body = re.sub(r"!\[\[(.+?)\]\]", r"![](Вопросы/media/\1)", body)

    md = f"# {title}\n\n{body.strip()}\n"

    num = re.match(r"^(\d+)", fname).group(1).zfill(2)
    tex_name = f"{num}.tex"
    # markdown передаём через stdin (без общего временного файла —
    # иначе на Windows pandoc может прочитать устаревший _tmp.md и продублировать вопрос)
    subprocess.run(
        [PANDOC, "-o", os.path.join(TEX_DIR, tex_name),
         "--from=markdown+lists_without_preceding_blankline", "--to=latex"],
        input=md.encode("utf-8"),
        check=True
    )
    tex_names.append(tex_name)
    print(f"  ✓ {fname} → {tex_name}")

# Строчки \input{tex/01.tex} ... с \newpage между ними
inputs = "\n\\newpage\n\n".join(f"\\input{{{TEX_DIR}/{n}}}" for n in tex_names)

main = rf"""\documentclass[12pt, a4paper]{{article}}

%% Кодировки и язык (для pdflatex)
\usepackage[utf8]{{inputenc}}
\usepackage[T2A]{{fontenc}}
\usepackage[russian, english]{{babel}}

%% Запасной вариант для отдельных Unicode-символов вне math-режима
\DeclareUnicodeCharacter{{2208}}{{\ensuremath{{\in}}}}
\DeclareUnicodeCharacter{{221E}}{{\ensuremath{{\infty}}}}
\DeclareUnicodeCharacter{{2282}}{{\ensuremath{{\subset}}}}

%% Математика
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\let\Bbbk\relax
\usepackage{{mathtools}}
\usepackage{{amsthm}}
\newtheorem*{{theorem}}{{Теорема}}
\newtheorem*{{lemma}}{{Лемма}}

%% Поля
\usepackage[top=25mm, bottom=25mm, left=25mm, right=20mm]{{geometry}}
\usepackage{{microtype}}
\setlength{{\parskip}}{{5pt plus 1pt}}
\setlength{{\parindent}}{{0pt}}

%% Картинки
\usepackage{{graphicx}}

%% Макросы, которые обычно даёт шаблон pandoc (нужны при --to=latex)
\makeatletter
\newsavebox\pandoc@box
\newcommand*\pandocbounded[1]{{%
  \sbox\pandoc@box{{#1}}%
  \Gscale@div\@tempa{{\textheight}}{{\dimexpr\ht\pandoc@box+\dp\pandoc@box\relax}}%
  \Gscale@div\@tempb{{\linewidth}}{{\wd\pandoc@box}}%
  \ifdim\@tempb\p@<\@tempa\p@\let\@tempa\@tempb\fi%
  \ifdim\@tempa\p@<\p@\else\gdef\@tempa{{1}}\fi%
  \scalebox{{\@tempa}}{{\usebox\pandoc@box}}%
}}
\makeatother
\providecommand{{\tightlist}}{{%
  \setlength{{\itemsep}}{{0pt}}\setlength{{\parskip}}{{0pt}}}}

%% Гиперссылки + оглавление
\usepackage{{hyperref}}
\hypersetup{{colorlinks=true, linkcolor=blue}}

\title{{Теория функций комплексного переменного\\[0.5em]
\large Вопросы к экзамену}}
\author{{karui}}
\date{{2025--2026}}

\begin{{document}}
\maketitle
\tableofcontents
\newpage

    {inputs}

\end{{document}}
    """

with open(MAIN_TEX, "w", encoding="utf-8") as f:
    f.write(main)

print(f"\n✓ {MAIN_TEX} готов")
print("Сборка PDF (latexmk сам прогонит нужное число раз для оглавления):")
print(f"  latexmk -pdf -interaction=nonstopmode {MAIN_TEX}")