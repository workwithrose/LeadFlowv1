import re

html_content = ""
with open("index.html", "r") as f:
    html_content = f.read()

# Make the button white text, black background, softer border-radius
html_content = html_content.replace(
"""/* Buttons */
button {
  background: var(--text-main);
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: opacity 0.2s;
}""",
"""/* Buttons */
button {
  background: var(--text-main);
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  transition: opacity 0.2s;
}"""
)

# And dashboard top stats styling, wait let's use the provided design completely.
# Let's fix up some of the svg icons.

html_content = html_content.replace(
"""<div class="icon icon-purple">📈</div>""",
"""<div class="icon icon-purple"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>"""
)

html_content = html_content.replace(
"""<div class="icon icon-blue">📢</div>""",
"""<div class="icon icon-blue"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg></div>"""
)

html_content = html_content.replace(
"""<div class="icon icon-red">⏰</div>""",
"""<div class="icon icon-red"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>"""
)

html_content = html_content.replace(
"""<div class="icon icon-orange">✖</div>""",
"""<div class="icon icon-orange"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></div>"""
)

html_content = html_content.replace(
"""<div class="issue-icon red">⏰</div>""",
"""<div class="issue-icon red"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>"""
)

html_content = html_content.replace(
"""<div class="issue-icon yellow">⚠</div>""",
"""<div class="issue-icon yellow"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg></div>"""
)

html_content = html_content.replace(
"""<div class="issue-icon orange">📢</div>""",
"""<div class="issue-icon orange"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path></svg></div>"""
)

with open("index.html", "w") as f:
    f.write(html_content)
