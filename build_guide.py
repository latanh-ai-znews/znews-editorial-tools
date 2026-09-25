import re
import html
import os

with open('huong-dan-bai-dac-biet-znews-2.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
out = []
in_code = False
code_lang = ''
code_buf = []
in_ul = False
in_ol = False

def close_lists():
    global in_ul, in_ol
    res = ''
    if in_ul:
        res += '</ul>\n'
        in_ul = False
    if in_ol:
        res += '</ol>\n'
        in_ol = False
    return res

toc = []
slug_counts = {}

def make_slug(title):
    clean = re.sub(r'[*_`"\'\(\)\[\]]', '', title).lower()
    s = re.sub(r'[^\w\s-]', '', clean)
    s = re.sub(r'[\s_]+', '-', s).strip('-')
    if not s:
        s = 'muc'
    c = slug_counts.get(s, 0)
    slug_counts[s] = c + 1
    return s if c == 0 else f"{s}-{c}"

for line in lines:
    if line.startswith('```'):
        if in_code:
            code_text = html.escape('\n'.join(code_buf))
            out.append(f'''<div class="code-wrapper">
  <div class="code-header">
    <span class="code-badge">{code_lang or "mã nguồn"}</span>
    <button class="copy-btn" onclick="copySnippet(this)">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
      Sao chép
    </button>
  </div>
  <pre><code class="lang-{code_lang}">{code_text}</code></pre>
</div>''')
            code_buf = []
            in_code = False
            code_lang = ''
        else:
            out.append(close_lists())
            in_code = True
            code_lang = line[3:].strip()
        continue

    if in_code:
        code_buf.append(line)
        continue

    trimmed = line.strip()
    if not trimmed:
        out.append(close_lists())
        continue

    # Headings
    hm = re.match(r'^(#{1,3})\s+(.*)$', line)
    if hm:
        out.append(close_lists())
        level = len(hm.group(1))
        htext = hm.group(2).strip()
        slug = make_slug(htext)
        clean_title = re.sub(r'[*_`]', '', htext)
        toc.append({'level': level, 'title': clean_title, 'slug': slug})
        
        # Format inline marks in heading
        htext_fmt = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', htext)
        htext_fmt = re.sub(r'`(.*?)`', r'<code>\1</code>', htext_fmt)
        
        if level == 1:
            out.append(f'<h1 id="{slug}" class="heading-1">{htext_fmt}</h1>')
        elif level == 2:
            out.append(f'<h2 id="{slug}" class="heading-2"><a href="#{slug}" class="anchor-link">#</a> {htext_fmt}</h2>')
        else:
            out.append(f'<h3 id="{slug}" class="heading-3"><a href="#{slug}" class="anchor-link">#</a> {htext_fmt}</h3>')
        continue

    # Horizontal rule
    if re.match(r'^-{3,}$', trimmed):
        out.append(close_lists())
        out.append('<hr class="divider" />')
        continue

    # Unordered list
    ul_m = re.match(r'^[-*]\s+(.*)$', line)
    if ul_m:
        if in_ol:
            out.append(close_lists())
        if not in_ul:
            out.append('<ul class="doc-list">')
            in_ul = True
        item = ul_m.group(1)
        item = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item)
        item = re.sub(r'`(.*?)`', r'<code>\1</code>', item)
        out.append(f'<li>{item}</li>')
        continue

    # Ordered list
    ol_m = re.match(r'^\d+\.\s+(.*)$', line)
    if ol_m:
        if in_ul:
            out.append(close_lists())
        if not in_ol:
            out.append('<ol class="doc-ordered-list">')
            in_ol = True
        item = ol_m.group(1)
        item = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item)
        item = re.sub(r'`(.*?)`', r'<code>\1</code>', item)
        out.append(f'<li>{item}</li>')
        continue

    # Blockquote
    bq_m = re.match(r'^>\s*(.*)$', line)
    if bq_m:
        out.append(close_lists())
        b_text = bq_m.group(1)
        b_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', b_text)
        b_text = re.sub(r'`(.*?)`', r'<code>\1</code>', b_text)
        out.append(f'<blockquote class="doc-quote">{b_text}</blockquote>')
        continue

    # Normal paragraph
    out.append(close_lists())
    p_text = line
    p_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p_text)
    p_text = re.sub(r'`(.*?)`', r'<code>\1</code>', p_text)
    out.append(f'<p>{p_text}</p>')

out.append(close_lists())
rendered_body = '\n'.join(out)

# Build TOC HTML
toc_html = []
for item in toc:
    lvl = item['level']
    title = item['title']
    slug = item['slug']
    indent_class = f"toc-level-{lvl}"
    toc_html.append(f'<li class="{indent_class}"><a href="#{slug}">{title}</a></li>')

toc_rendered = '\n'.join(toc_html)

guide_html = f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cẩm nang quy chuẩn kỹ thuật CMS Znews</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #fbfaf7;
      --bg-subtle: #f5f2eb;
      --surface: #ffffff;
      --border: #e8e4dc;
      --border-subtle: #f0ece4;
      --text: #262421;
      --text-muted: #6e6a62;
      --text-soft: #4a4742;
      --primary: #c94a29;
      --primary-hover: #b33e1f;
      --code-bg: #f5f2eb;
      --radius: 12px;
    }}
    [data-theme="dark"] {{
      --bg: #161514;
      --bg-subtle: #1f1d1b;
      --surface: #242220;
      --border: #363330;
      --border-subtle: #2d2b28;
      --text: #f2eee8;
      --text-muted: #9e988f;
      --text-soft: #c7c1b7;
      --primary: #e0603f;
      --primary-hover: #ea7051;
      --code-bg: #1f1d1b;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Be Vietnam Pro', -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.75;
      font-size: 15px;
      transition: background .2s ease, color .2s ease;
      -webkit-font-smoothing: antialiased;
    }}
    /* Topbar */
    .topbar {{
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(14px);
      background: rgba(251, 250, 247, 0.92);
      border-bottom: 1px solid var(--border);
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    [data-theme="dark"] .topbar {{
      background: rgba(22, 21, 20, 0.92);
    }}
    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }}
    .brand-badge {{
      background: var(--primary);
      color: #fff;
      font-weight: 700;
      font-size: 12.5px;
      padding: 4px 9px;
      border-radius: 6px;
    }}
    .brand-title {{
      font-size: 15px;
      font-weight: 600;
    }}
    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 13px;
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 500;
      text-decoration: none;
      cursor: pointer;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text);
      transition: all .18s;
    }}
    .btn:hover {{
      border-color: #68635c;
      color: var(--text);
    }}
    
    /* Layout */
    .layout-container {{
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 290px 1fr;
      gap: 36px;
      padding: 32px 24px;
    }}
    
    /* Sidebar TOC */
    .sidebar {{
      position: sticky;
      top: 76px;
      height: calc(100vh - 100px);
      overflow-y: auto;
      padding-right: 12px;
    }}
    .sidebar-title {{
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 12px;
    }}
    .toc-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .toc-list li a {{
      display: block;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13.5px;
      line-height: 1.45;
      padding: 6px 10px;
      border-radius: 6px;
      transition: all .15s;
    }}
    .toc-list li a:hover {{
      color: var(--text);
      background: var(--bg-subtle);
    }}
    .toc-list li.toc-level-1 {{ font-weight: 600; margin-top: 8px; }}
    .toc-list li.toc-level-2 {{ font-weight: 500; padding-left: 8px; }}
    .toc-list li.toc-level-3 {{ font-size: 12.5px; padding-left: 18px; }}
    
    /* Content */
    .content-article {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 44px;
      min-width: 0;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }}
    
    .heading-1 {{
      font-family: 'Newsreader', Georgia, serif;
      font-size: 30px;
      font-weight: 600;
      line-height: 1.3;
      margin-bottom: 24px;
      color: var(--text);
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
    }}
    .heading-2 {{
      font-family: 'Newsreader', Georgia, serif;
      font-size: 22px;
      font-weight: 600;
      margin-top: 36px;
      margin-bottom: 14px;
      color: var(--text);
      display: flex;
      align-items: baseline;
      gap: 8px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 8px;
    }}
    .heading-3 {{
      font-size: 16px;
      font-weight: 600;
      margin-top: 24px;
      margin-bottom: 10px;
      color: var(--primary);
    }}
    .anchor-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 17px;
      opacity: .4;
    }}
    .anchor-link:hover {{ opacity: 1; color: var(--primary); }}
    
    p {{
      margin-bottom: 15px;
      color: var(--text);
    }}
    strong {{
      color: var(--text);
      font-weight: 600;
    }}
    code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      background: var(--bg-subtle);
      color: var(--primary);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid var(--border-subtle);
    }}
    
    .doc-list, .doc-ordered-list {{
      margin: 0 0 18px 22px;
    }}
    .doc-list li, .doc-ordered-list li {{
      margin-bottom: 7px;
    }}
    .doc-quote {{
      border-left: 3px solid var(--primary);
      background: var(--bg-subtle);
      padding: 12px 18px;
      border-radius: 0 8px 8px 0;
      margin: 18px 0;
      font-style: italic;
      color: var(--text);
    }}
    .divider {{
      border: 0;
      height: 1px;
      background: var(--border);
      margin: 32px 0;
    }}
    
    /* Code blocks */
    .code-wrapper {{
      margin: 18px 0;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid var(--border);
      background: var(--code-bg);
    }}
    .code-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 14px;
      background: rgba(0, 0, 0, 0.03);
      border-bottom: 1px solid var(--border);
    }}
    .code-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      color: var(--text-muted);
      font-weight: 500;
    }}
    .copy-btn {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 4px 9px;
      border-radius: 6px;
      font-size: 11.5px;
      cursor: pointer;
      transition: all .15s;
    }}
    .copy-btn:hover {{
      border-color: #68635c;
    }}
    pre {{
      padding: 14px 16px;
      overflow-x: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      line-height: 1.6;
      color: var(--text);
    }}
    
    @media (max-width: 900px) {{
      .layout-container {{ grid-template-columns: 1fr; }}
      .sidebar {{ display: none; }}
      .content-article {{ padding: 22px 18px; }}
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <a href="index.html" class="nav-brand">
      <span class="brand-badge">Znews</span>
      <span class="brand-title">Cẩm nang quy chuẩn CMS</span>
    </a>
    <div class="nav-actions">
      <a href="index.html" class="btn">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Về danh sách công cụ
      </a>
      <button class="btn" onclick="toggleTheme()">Giao diện</button>
    </div>
  </header>

  <div class="layout-container">
    <aside class="sidebar">
      <div class="sidebar-title">Mục lục tài liệu</div>
      <ul class="toc-list">
        {toc_rendered}
      </ul>
    </aside>

    <main class="content-article">
      {rendered_body}
    </main>
  </div>

  <script>
    function copySnippet(btn) {{
      const code = btn.closest('.code-wrapper').querySelector('code').innerText;
      navigator.clipboard.writeText(code).then(() => {{
        const oldText = btn.innerHTML;
        btn.innerHTML = 'Đã chép!';
        setTimeout(() => {{ btn.innerHTML = oldText; }}, 2000);
      }});
    }}
    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('znews_theme', next);
    }}
    const savedTheme = localStorage.getItem('znews_theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
  </script>
</body>
</html>
'''

with open('guide.html', 'w', encoding='utf-8') as f:
    f.write(guide_html)

print("Generated guide.html with Claude-style light theme successfully!")
