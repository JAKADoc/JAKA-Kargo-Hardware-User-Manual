# conf.py for Sphinx + LaTeX + PDF

import os
import sys
from docutils import nodes

# -- Project information -----------------------------------------------------

# MANUAL_LANGUAGE 可用于本地指定语言；在 Read the Docs 上则读取项目语言。
raw_language = (
    os.environ.get("MANUAL_LANGUAGE")
    or os.environ.get("READTHEDOCS_LANGUAGE")
    or "zh"
).strip().lower().replace("-", "_")

if raw_language.startswith("zh"):
    BUILD_LANG = "zh"
elif raw_language.startswith("ja"):
    BUILD_LANG = "ja"
elif raw_language.startswith("en"):
    BUILD_LANG = "en"
else:
    raise ValueError(f"Unsupported language: {raw_language}")

# Edit this block when reusing the configuration for another manual.
# Asset paths are relative to this Sphinx source directory. The header logo
# must refer to an entry in the images mapping below.
MANUAL_CONFIG = {
    # 项目元数据：改名称、版本或版权方时，只改此处相应字段。
    "project_titles": {
        "zh": "JAKA {product_name} 硬件用户手册",
        "en": "JAKA {product_name} Hardware User Manual",
        "ja": "JAKA {product_name} ハードウェアユーザーマニュアル",
    },
    "company_name": "JAKA Robotics",
    "copyright_year": "2026",
    "author": "JAKA",
    "release": "V02",
    "product_name": "Kargo",
    "software_name": "Coboπ Next",
    "latex_filename": "KargoManual.tex",

    # 品牌视觉资源：图片路径相对本 conf.py 所在的 source 目录。
    "html_css_files": ["custom.css"],
    # PDF 封面和封底按语言选择；尚未制作的语言设为 None，避免误用中文内容。
    "latex_covers": {
        "zh": "_static/cover.inc",
        "en": None,
        "ja": "_static/cover.ja.inc",
    },
    "latex_backcovers": {
        "zh": "_static/backcover.inc",
        "en": None,
        "ja": "_static/backcover.ja.inc",
    },
    # 每张图片只在这里登记一次；HTML 标志、PDF 页眉和 LaTeX 附件
    # 通过下面的资源名称引用它。
    "images": {
        "brand_logo": "../../images/00_封面/Logo.png",
        "disclaimer_qr": "../../images/01_免责声明/官网二维码.png",
        "product_image": "../../images/00_封面/Kargo.png",
    },
    "html_logo_asset": "brand_logo",
    "latex_header_logo_asset": "brand_logo",

    # 环境和样式选项：字体目录可通过 SOURCEHAN_FONT_DIR 环境变量覆盖。
    "sourcehan_font_dir": os.environ.get(
        "SOURCEHAN_FONT_DIR",
        os.path.join(
            os.path.expanduser("~"),
            "AppData/Local/Microsoft/Windows/Fonts",
        ).replace("\\", "/") + "/",
    ),
    "brand_color": "D80C1E",
    "merge_empty_table_cells": True,
    "localize_chinese_admonitions": True,
}

LANGUAGE_TEXT = {
    "zh": {
        "sphinx_language": "zh_CN",
        "search_language": "zh",
        "search_options": {"type": "jieba", "lang": "zh_CN"},
        "figure": "图",
        "table": "表",
        "code_block": "代码块",
        "section": "节",
        "list_figures": "图目录",
        "list_tables": "表目录",
        "version": "版本：",
        "release": "版本",
    },
    "en": {
        "sphinx_language": "en",
        "search_language": "en",
        "search_options": {},
        "figure": "Figure",
        "table": "Table",
        "code_block": "Code block",
        "section": "Section",
        "list_figures": "List of Figures",
        "list_tables": "List of Tables",
        "version": "Version:",
        "release": "Version",
    },
    "ja": {
        "sphinx_language": "ja",
        "search_language": "ja",
        "search_options": {},
        "figure": "図",
        "table": "表",
        "code_block": "コードブロック",
        "section": "節",
        "list_figures": "図目次",
        "list_tables": "表目次",
        "version": "バージョン：",
        "release": "バージョン",
    },
}

if BUILD_LANG not in LANGUAGE_TEXT:
    raise ValueError(
        f"Unsupported MANUAL_LANGUAGE={BUILD_LANG!r}; use 'zh', 'en', or 'ja'."
    )

TEXT = LANGUAGE_TEXT[BUILD_LANG]
LATEX_COVER = MANUAL_CONFIG["latex_covers"].get(BUILD_LANG)
LATEX_BACKCOVER = MANUAL_CONFIG["latex_backcovers"].get(BUILD_LANG)
MANUAL_IMAGES = MANUAL_CONFIG["images"]
HTML_LOGO_ASSET = MANUAL_CONFIG["html_logo_asset"]
LATEX_HEADER_LOGO_ASSET = MANUAL_CONFIG["latex_header_logo_asset"]
LATEX_HEADER_LOGO = (
    os.path.basename(MANUAL_IMAGES[LATEX_HEADER_LOGO_ASSET])
    if LATEX_HEADER_LOGO_ASSET
    else ""
)
LATEX_HEADER_LOGO_TEX = (
    r'\fancyhead[L]{\raisebox{0.05cm}{\includegraphics[height=0.5cm]{'
    + LATEX_HEADER_LOGO
    + r'}}}'
    if LATEX_HEADER_LOGO
    else ""
)

project = MANUAL_CONFIG["project_titles"][BUILD_LANG].format(**MANUAL_CONFIG)
copyright = f'{MANUAL_CONFIG["copyright_year"]}, {MANUAL_CONFIG["company_name"]}'
author = MANUAL_CONFIG["author"]
release = MANUAL_CONFIG["release"]
productname = MANUAL_CONFIG["product_name"]
CJK_SOURCEHAN_REGION = "JP" if BUILD_LANG == "ja" else "CN"
CJK_NOTO_REGION = "JP" if BUILD_LANG == "ja" else "SC"

# -- Substitution ------------------------------------------------------------

rst_epilog = f"""
.. |product_name| replace:: {MANUAL_CONFIG["product_name"]}
.. |company_name| replace:: {MANUAL_CONFIG["company_name"]}
.. |software_name| replace:: {MANUAL_CONFIG["software_name"]}
.. |软件| replace:: {MANUAL_CONFIG["software_name"]}

"""

# -- General configuration ---------------------------------------------------

locale_dirs = ['locale/']
gettext_compact = False

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
]

source_suffix = {
 '.rst': 'restructuredtext',
 '.txt': 'restructuredtext',
 '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = TEXT["sphinx_language"]
master_doc = 'index'

# 自动编号
numfig = True
numfig_secnum_depth = 1

# -- HTML -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = MANUAL_IMAGES.get(HTML_LOGO_ASSET) if HTML_LOGO_ASSET else None
html_show_sphinx = False
html_show_sourcelink = False
html_copy_source = False

html_css_files = MANUAL_CONFIG["html_css_files"]

numfig_format = {
    'figure': TEXT["figure"] + ' %s',
    'table': TEXT["table"] + ' %s',
    'code-block': TEXT["code_block"] + ' %s',
    'section': TEXT["section"] + ' %s',
}

html_search_language = TEXT["search_language"]
html_search_options = TEXT["search_options"]

# 生产版不加载评论组件。原 comments.js 绑定的是其他项目仓库，继续加载会
# 产生无效请求并把反馈提交到错误的位置。
html_js_files = []

# 查找图片偏好
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = ['image/svg+xml', 'image/png', 'image/gif', 'image/jpeg']

from sphinx.builders.latex import LaTeXBuilder
LaTeXBuilder.supported_image_types = ['application/pdf', 'image/png', 'image/jpeg']

# -- LaTeX -------------------------------------------------

latex_engine = "uplatex" if BUILD_LANG == "ja" else "xelatex"

latex_documents = [
    ('index', MANUAL_CONFIG["latex_filename"], project, author, 'manual'),
]

# standard 样式会生成全部横线和竖线；longtable 仍由 list-table 的
# :class: longtable 按需启用。booktabs 会主动省略竖线，不能满足全框线要求。
latex_table_style = ['standard']

latex_additional_files = [
    path for path in [
        LATEX_COVER,
        LATEX_BACKCOVER,
        *MANUAL_IMAGES.values(),
    ]
    if path
]

latex_cover_input = (
    rf'\input{{{os.path.basename(LATEX_COVER)}}}'
    if LATEX_COVER
    else None
)
latex_backcover_input = (
    rf'\input{{{os.path.basename(LATEX_BACKCOVER)}}}'
    if LATEX_BACKCOVER
    else ""
)
if latex_backcover_input:
    latex_backcover_input = r'''
    \cleardoublepage
    ''' + latex_backcover_input

# 日文目录的全角章节编号需要更宽的编号栏；其他语言沿用原宽度。
TOC_NUMBER_WIDTHS = (
    ("5.5em", "4.5em", "5.5em", "6.5em")
    if BUILD_LANG == "ja"
    else ("2.8em", "3.2em", "4.2em", "5.0em")
)

latex_elements = {

    'papersize': 'a4paper',
    'pointsize': '11pt',

    'figure_align': 'H',

    # 使用非 .tex 扩展名，避免 Read the Docs 的 latexmk 把封面误认为
    # 第二个主文档（latexmk + -jobname 要求构建目录中只有一个 .tex）。
    # 恢复原状，去除会导致??的锚点
    'atendofbody': r'''
    \cleardoublepage
    \phantomsection
    \addcontentsline{toc}{chapter}{''' + TEXT["list_figures"] + r'''}
    \begingroup
    \hypersetup{allcolors=black}
    \listoffigures
    \endgroup

    \cleardoublepage
    \phantomsection
    \addcontentsline{toc}{chapter}{''' + TEXT["list_tables"] + r'''}
    \begingroup
    \hypersetup{allcolors=black}
    \listoftables
    \endgroup

    % 总页数以最后一个实际显示页脚的页面为准，不计无页脚的封底。
    \phantomsection
    \label{LastNumberedPage}
    ''' + latex_backcover_input + r'''
    ''',

    'fncychap': r'\usepackage[Sonny]{fncychap}',

    'extraclassoptions': 'openany,oneside',

    'preamble': r'''

\usepackage{longtable}
\usepackage{booktabs}

''' + (
r'''
% ===== CJK 支持 =====
\usepackage{xeCJK}
\usepackage[fontset=none]{ctex}

% ===== PDF 正文字体 =====

% 英文字体：
% Windows 本地使用 Arial；
% Read the Docs/Linux 使用 Liberation Sans。
\IfFontExistsTF{Arial}{
    \setmainfont{Arial}[
        UprightFont = Arial,
        BoldFont = Arial Bold,
        ItalicFont = Arial Italic,
        BoldItalicFont = Arial Bold Italic
    ]
}{
    \setmainfont{Liberation Sans}[
        UprightFont = Liberation Sans,
        BoldFont = Liberation Sans Bold,
        ItalicFont = Liberation Sans Italic,
        BoldItalicFont = Liberation Sans Bold Italic
    ]
}

% CJK 字体按构建语言选择；中文使用 CN/SC 字体，日文使用 JP 字体。
\IfFileExists{''' + MANUAL_CONFIG["sourcehan_font_dir"] + r'''SourceHanSerif''' + CJK_SOURCEHAN_REGION + r'''-Regular.ttf}{
    \setCJKmainfont{SourceHanSerif''' + CJK_SOURCEHAN_REGION + r'''}[
        Path = ''' + MANUAL_CONFIG["sourcehan_font_dir"] + r''',
        UprightFont = *-Regular.ttf,
        BoldFont = *-Bold.ttf,
        ItalicFont = *-Regular.ttf,
        BoldItalicFont = *-Bold.ttf,
        ItalicFeatures = {FakeSlant=0.2},
        BoldItalicFeatures = {FakeSlant=0.2}
    ]
    \setCJKsansfont{SourceHanSerif''' + CJK_SOURCEHAN_REGION + r'''}[
        Path = ''' + MANUAL_CONFIG["sourcehan_font_dir"] + r''',
        UprightFont = *-Regular.ttf,
        BoldFont = *-Bold.ttf
    ]
    \setCJKmonofont{SourceHanSerif''' + CJK_SOURCEHAN_REGION + r'''}[
        Path = ''' + MANUAL_CONFIG["sourcehan_font_dir"] + r''',
        UprightFont = *-Regular.ttf,
        BoldFont = *-Bold.ttf
    ]
}{
    \setCJKmainfont{Noto Serif CJK ''' + CJK_NOTO_REGION + r'''}[
        UprightFont = Noto Serif CJK ''' + CJK_NOTO_REGION + r''',
        BoldFont = Noto Serif CJK ''' + CJK_NOTO_REGION + r''' Bold,
        AutoFakeSlant = 0.2
    ]
    \setCJKsansfont{Noto Sans CJK ''' + CJK_NOTO_REGION + r'''}[
        UprightFont = Noto Sans CJK ''' + CJK_NOTO_REGION + r''',
        BoldFont = Noto Sans CJK ''' + CJK_NOTO_REGION + r''' Bold
    ]
    \setCJKmonofont{Noto Sans Mono CJK ''' + CJK_NOTO_REGION + r'''}[
        UprightFont = Noto Sans Mono CJK ''' + CJK_NOTO_REGION + r''',
        BoldFont = Noto Sans Mono CJK ''' + CJK_NOTO_REGION + r''' Bold
    ]
}

% Arial/Liberation Sans 可能不包含这两个组合字符。
\XeTeXcharclass"2103=1 % ℃
\XeTeXcharclass"2109=1 % ℉
''' if BUILD_LANG != "ja" else r'''
% 日语版使用 upLaTeX，由 TeX Live 提供日文字体；不加载 XeLaTeX 专用字体设置。
'''
) + r'''

% ===== 页面边距与页眉空间分配 =====
\usepackage{geometry}
\geometry{
    left=14.5mm,
    right=14.5mm,
    top=24mm,
    bottom=20mm,
    headheight=25pt, % 留足页眉高度
    headsep=4mm,
    footskip=7mm
}

% ===== 图片路径 =====
\graphicspath{{images/}}

% ===== 禁止图表浮动 =====
\usepackage{float}
\usepackage{placeins}

\makeatletter
\def\fps@figure{H}
\def\fps@table{H}
\def\fps@sphinxfigure{H}
\def\fps@sphinxTable{H}
\makeatother

% ==== 强制图片后换行 ===
\usepackage{etoolbox}
\AtEndEnvironment{figure}{\par\noindent}
\AtEndEnvironment{sphinxfigure}{\par\noindent}

% ===== 代码高亮 =====
\usepackage{listings}

% ===== PDF书签 =====
\usepackage{bookmark}

% ===== 自定义变量 =====
\newcommand{\ProductName}{''' + productname + r'''}
\newcommand{\docversion}{''' + release + r'''}
\newcommand{\docname}{''' + project + r'''}

% ===== 页眉页脚 =====
\usepackage{fancyhdr}

% 1. 重定义 Sphinx 的正文页样式 (normal)
\fancypagestyle{normal}{
    \fancyhf{}
    ''' + LATEX_HEADER_LOGO_TEX + r'''
    \fancyhead[R]{\nouppercase{\leftmark}}
    \fancyfoot[L]{''' + TEXT["version"] + r''' \docversion}
    \fancyfoot[C]{\thepage/\pageref*{LastNumberedPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

% 2. 重定义 Sphinx 的章节起始页样式 (plain)
\fancypagestyle{plain}{
    \fancyhf{}
    ''' + LATEX_HEADER_LOGO_TEX + r'''
    \fancyhead[R]{\nouppercase{\leftmark}}
    \fancyfoot[L]{''' + TEXT["version"] + r''' \docversion}
    \fancyfoot[C]{\thepage/\pageref*{LastNumberedPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

% upLaTeX 的 ujbook 章节首页调用 jpl@in，单独定义为正文页眉页脚。
\fancypagestyle{jpl@in}{
    \fancyhf{}
    ''' + LATEX_HEADER_LOGO_TEX + r'''
    \fancyhead[R]{\nouppercase{\leftmark}}
    \fancyfoot[L]{''' + TEXT["version"] + r''' \docversion}
    \fancyfoot[C]{\thepage/\pageref*{LastNumberedPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

% 文档开始时，让 plain 页式沿用正文 normal 页式。
\makeatletter
\AtBeginDocument{
    \let\ps@plain\ps@normal
}
\makeatother

% 正文前目录页：只显示当前罗马页码，不显示总页数。
\fancypagestyle{frontmatter}{
    \fancyhf{}
    ''' + LATEX_HEADER_LOGO_TEX + r'''
    \fancyhead[R]{\nouppercase{\leftmark}}
    \fancyfoot[L]{''' + TEXT["version"] + r''' \docversion}
    \fancyfoot[C]{\thepage}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

% ===== 标题样式 =====
\usepackage{titlesec}
\usepackage{xcolor}

% chapter 至 subparagraph 共六级标题均显示编号。
\setcounter{secnumdepth}{5}

% 定义红色
\definecolor{TitleRed}{HTML}{''' + MANUAL_CONFIG["brand_color"] + r'''}

% 章节间距
\titlespacing*{\chapter}{0pt}{-30pt}{20pt}

% Chapter
\titleformat{\chapter}
{\Huge\bfseries\color{TitleRed}}
{\thechapter}{0.5em}{}

% Section
\titleformat{\section}
{\Large\bfseries\color{TitleRed}}
{\thesection}{0.5em}{}

% Subsection
\titleformat{\subsection}
{\large\bfseries\color{TitleRed}}
{\thesubsection}{0.5em}{}

% Subsubsection
\titleformat{\subsubsection}
{\normalsize\bfseries\color{TitleRed}}
{\thesubsubsection}{0.5em}{}

% ===== 超链接颜色 =====
\usepackage{hyperref}

\hypersetup{
colorlinks=true,
linkcolor=blue,
urlcolor=blue,
citecolor=blue
}

% ===== 主目录 =====

\renewcommand{\sphinxtableofcontents}{
    \cleardoublepage
    \pagenumbering{Roman}
    \pagestyle{frontmatter}
    \begingroup
      \parskip=0pt
      \hypersetup{linkcolor=black}
      \tableofcontents
    \endgroup
    \clearpage
    \pagenumbering{arabic}
    \pagestyle{normal}
}

% “目录”居中；一级标题也使用引导点连接页码。
\makeatletter
\renewcommand{\tableofcontents}{%
    \phantomsection
    \markboth{\contentsname}{\contentsname}%
    \begin{center}
      {\Huge\bfseries\color{TitleRed}\contentsname\par}
    \end{center}
    \vspace{1.5em}
    \@starttoc{toc}%
}
% 为三位数页码预留足够宽度，避免目录页码挤出右边界。
\renewcommand{\@pnumwidth}{2.2em}
\renewcommand{\@tocrmarg}{3.2em}
% 保留原目录的层级感：章标题加粗并增加段前间距；其余各级逐级缩进。
% LaTeX 原生 \@dottedtocline 会把首行拉回到左边界，导致编号看起来没有缩进。
% 这里仅回退编号宽度，使编号、标题及换行内容都从指定层级缩进处开始。
\newcommand*\Manualdottedtocline[5]{%
  \ifnum #1>\c@tocdepth\relax\else
    \vskip \z@ \@plus.2\p@
    {\leftskip #2\relax
     \rightskip \@tocrmarg
     \parfillskip -\rightskip
     \parindent \z@
     \@afterindenttrue
     \interlinepenalty\@M
     \leavevmode
     \@tempdima #3\relax
     % ujbook の \numberline は \@lnumwidth を参照する。
     \@ifundefined{@lnumwidth}{}{\@lnumwidth #3\relax}
     \advance\leftskip \@tempdima
     \null\nobreak\hskip -\@tempdima
     {#4}\nobreak
     \leaders\hbox{$\m@th
        \mkern \@dotsep mu\hbox{.}\mkern \@dotsep mu$}\hfill
     \nobreak
     \hb@xt@\@pnumwidth{\hfil\normalfont\normalcolor #5}%
     \par}%
  \fi
}
\renewcommand*\l@chapter[2]{%
  \addvspace{0.6em}%
  \begingroup
    \bfseries
    \@dottedtocline{0}{0em}{''' + TOC_NUMBER_WIDTHS[0] + r'''}{#1}{#2}%
  \endgroup
}
\renewcommand*\l@section[2]{\Manualdottedtocline{1}{1.8em}{''' + TOC_NUMBER_WIDTHS[1] + r'''}{#1}{#2}}
\renewcommand*\l@subsection[2]{\Manualdottedtocline{2}{5.0em}{''' + TOC_NUMBER_WIDTHS[2] + r'''}{#1}{#2}}
\renewcommand*\l@subsubsection[2]{\Manualdottedtocline{3}{9.2em}{''' + TOC_NUMBER_WIDTHS[3] + r'''}{#1}{#2}}
\renewcommand*\l@figure{\@dottedtocline{1}{1.5em}{3em}}
\renewcommand*\l@table{\@dottedtocline{1}{1.5em}{3em}}
\makeatother

% 2. 图目录
\let\origlistoffigures\listoffigures
\renewcommand{\listoffigures}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoffigures
    \endgroup
}

% 3. 表目录
\let\origlistoftables\listoftables
\renewcommand{\listoftables}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoftables
    \endgroup
}

% ===== 表格样式 =====
\usepackage{colortbl}
\usepackage{longtable}

% 表头 #D80C1E；边框 #9E9E9E、0.75 pt。
\definecolor{tableheader}{HTML}{''' + MANUAL_CONFIG["brand_color"] + r'''}
\definecolor{tableborder}{HTML}{9e9e9e}
\setlength{\arrayrulewidth}{0.75pt}
\arrayrulecolor{tableborder}

% Sphinx 会在每个表头单元格开头调用此命令。使用 cellcolor 比在
% varwidth 内调用 rowcolor 稳定，并且兼容 tabulary 与 longtable。
\renewcommand{\sphinxstyletheadfamily}{%
  \cellcolor{tableheader}\color{white}\bfseries%
}

% ===== 表格跨页与宽度控制 =====
\usepackage{tabularx}
\usepackage{ltablex}
\keepXColumns

% 表格自动换行
\renewcommand{\tabularxcolumn}[1]{m{#1}}

% 表格不要超出页边距
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}

% ===== 代码块分页优化 =====
\sphinxsetup{
verbatimwithframe=false,
div.note_box-decoration-break=clone,
div.hint_box-decoration-break=clone,
div.important_box-decoration-break=clone,
div.tip_box-decoration-break=clone,
div.warning_box-decoration-break=clone,
div.caution_box-decoration-break=clone,
div.attention_box-decoration-break=clone,
div.danger_box-decoration-break=clone,
div.error_box-decoration-break=clone
}

% ===== 图表名称按构建语言设置 =====
\AtBeginDocument{
    \renewcommand{\figurename}{''' + TEXT["figure"] + r'''}
    \renewcommand{\tablename}{''' + TEXT["table"] + r'''}
    \renewcommand{\listfigurename}{''' + TEXT["list_figures"] + r'''}
    \renewcommand{\listtablename}{''' + TEXT["list_tables"] + r'''}

}

''',
}

latex_keep_old_macro_names = True
latex_use_xindy = False
latex_toplevel_sectioning = 'chapter'

if latex_cover_input is not None:
    latex_elements['maketitle'] = latex_cover_input

latex_elements.update({
    'releasename': TEXT["release"],
})

# -- todo extension ---------------------------------------

todo_include_todos = True

# -- autodoc ----------------------------------------------

autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# -- list-table 空单元格自动合并 -------------------------------------------

def _table_entry_is_empty(entry):
    """含有图片或可见文字的单元格都不视为空。"""
    if any(entry.findall(nodes.image)):
        return False
    return not entry.astext().strip()


def _merge_empty_cells_horizontally(rows, grid, column_count):
    """把空单元格并入同一行左侧最近的非空单元格。

    已经跨行的单元格不再向右扩展，避免生成 HTML 能表示、但 LaTeX
    表格无法稳定表示的 L 形合并区域。
    """
    for row_index, row in enumerate(rows):
        anchor = None
        for column in range(column_count):
            cell = grid[row_index][column]
            if cell is None:
                anchor = None
                continue
            if (_table_entry_is_empty(cell) and anchor is not None
                    and not anchor.get('morerows', 0)):
                anchor['morecols'] = int(anchor.get('morecols', 0)) + 1
                row.remove(cell)
                grid[row_index][column] = None
            else:
                anchor = None if _table_entry_is_empty(cell) else cell


def _merge_empty_cells_vertically(rows, grid, column_count):
    """把空单元格并入同一列上方最近的非空单元格。

    已经跨列的单元格不再向下扩展，避免生成非矩形合并区域。
    """
    for column in range(column_count):
        anchor = None
        for row_index, row in enumerate(rows):
            cell = grid[row_index][column]
            if cell is None:
                anchor = None
                continue
            if (_table_entry_is_empty(cell) and anchor is not None
                    and not anchor.get('morecols', 0)):
                anchor['morerows'] = int(anchor.get('morerows', 0)) + 1
                row.remove(cell)
                grid[row_index][column] = None
            else:
                anchor = (
                    None
                    if _table_entry_is_empty(cell) or cell.get('morecols', 0)
                    else cell
                )


def _merge_empty_cells_in_table(table, logger):
    """安全合并规则表格中的空单元格。

    默认先横向合并，兼容规格表中有意留空的型号列。对于按类别纵向
    分组的表格，可添加 ``merge-empty-vertical`` 类，改为先纵向、再
    横向合并；也可用 ``merge-empty-horizontal`` 显式声明默认顺序。
    """
    tgroup = next(
        (child for child in table.children if isinstance(child, nodes.tgroup)),
        None,
    )
    if tgroup is None:
        return

    entries = list(tgroup.findall(nodes.entry))
    if any(entry.get('morerows', 0) or entry.get('morecols', 0)
           for entry in entries):
        logger.warning(
            '自动空单元格合并已跳过：该表格已经包含跨行或跨列单元格。',
            location=table,
        )
        return

    tbody = next(
        (child for child in tgroup.children if isinstance(child, nodes.tbody)),
        None,
    )
    if tbody is None:
        return

    rows = [child for child in tbody.children if isinstance(child, nodes.row)]
    if not rows:
        return

    column_count = int(tgroup.get('cols', 0)) or max(
        len(row.children) for row in rows
    )
    if any(len(row.children) != column_count for row in rows):
        logger.warning(
            '自动空单元格合并已跳过：该表格不是规则矩形。',
            location=table,
        )
        return

    # 保留原始坐标；被删除的单元格用 None 标记。
    grid = [list(row.children) for row in rows]

    if 'merge-empty-vertical' in table.get('classes', []):
        _merge_empty_cells_vertically(rows, grid, column_count)
        _merge_empty_cells_horizontally(rows, grid, column_count)
    else:
        _merge_empty_cells_horizontally(rows, grid, column_count)
        _merge_empty_cells_vertically(rows, grid, column_count)


def _merge_empty_table_cells(app, doctree, docname):
    """在输出 HTML/LaTeX 前转换 Docutils 表格节点。"""
    from sphinx.util import logging

    logger = logging.getLogger(__name__)
    for table in list(doctree.findall(nodes.table)):
        # LaTeX 的普通 tabulary 表格是不可分页的，会整体移到下一页并
        # 在前一页留下大块空白。统一改用 longtable，让表格按行跨页；
        # HTML 构建不受影响。
        if app.builder.format == 'latex':
            classes = table.setdefault('classes', [])
            if 'longtable' not in classes:
                classes.append('longtable')

        # 个别表格可用 :class: no-auto-merge 明确关闭自动合并。
        if (
            MANUAL_CONFIG["merge_empty_table_cells"]
            and 'no-auto-merge' not in table.get('classes', [])
        ):
            _merge_empty_cells_in_table(table, logger)

# Sphinx 当前环境未加载内置中文提示块翻译；在输出前统一本地化其标题。
_ADMONITION_TITLES_ZH = {
    'attention': '注意',
    'caution': '小心',
    'danger': '危险',
    'error': '错误',
    'hint': '提示',
    'important': '重要',
    'note': '注',
    'tip': '提示',
    'warning': '警告',
}


def _localize_admonition_titles(app, doctree, docname):
    """Replace automatic English admonition headings with Chinese labels."""
    for admonition in doctree.findall(nodes.admonition):
        kind = next(
            (
                name for name in _ADMONITION_TITLES_ZH
                if admonition.tagname == name
                or name in admonition.get('classes', [])
            ),
            None,
        )
        title = next(
            (child for child in admonition.children if isinstance(child, nodes.title)),
            None,
        )
        if kind and title is not None:
            title.clear()
            title += nodes.Text(_ADMONITION_TITLES_ZH[kind])


# -- 自定义 ------------------------------------------------

def setup(app):
    if MANUAL_CONFIG["merge_empty_table_cells"]:
        app.connect('doctree-resolved', _merge_empty_table_cells)
    if BUILD_LANG == "zh" and MANUAL_CONFIG["localize_chinese_admonitions"]:
        app.connect('doctree-resolved', _localize_admonition_titles)
    return {
        'version': '1.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

latex_elements['utf8extra'] = ''
