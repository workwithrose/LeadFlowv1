import re

html_content = ""
with open("index.html", "r") as f:
    html_content = f.read()

replacement = """function renderMyWork() {
  const prioContainer = document.getElementById('myWorkPriority');
  const otherContainer = document.getElementById('myWorkOther');
  prioContainer.innerHTML = '';
  otherContainer.innerHTML = '';

  const myItems = appData.items.filter(i => i.owner === 'Rose');
  let hasPrio = false;
  let hasOther = false;

  myItems.forEach(item => {
    const isPrio = item.status === 'Delayed' || isStale(item) || item.status === 'At Risk';
    const html = `
      <div class="list-card" onclick="openModal(${item.id})">
        <div>
          <div class="list-card-title">[${item.type.toUpperCase()}] ${item.title}</div>
          <div class="list-card-sub">Next: ${item.nextAction}</div>
        </div>
        <div class="list-card-right">
          ${getStatusBadge(item.status)}
          ${item.type === 'pipeline' ? `<div style="font-size:12px; margin-top:4px; color:var(--text-muted)">Stage: ${item.stage}</div>` : ''}
          ${isStale(item) ? '<div class="stale-warning" style="justify-content:flex-end;">⚠ Stale</div>' : ''}
        </div>
      </div>
    `;
    if (isPrio) { prioContainer.innerHTML += html; hasPrio = true; }
    else { otherContainer.innerHTML += html; hasOther = true; }
  });

  if (!hasPrio) prioContainer.innerHTML = '<p style="color:var(--text-muted); font-size:14px;">No priority items. Good job!</p>';
  if (!hasOther) otherContainer.innerHTML = '<p style="color:var(--text-muted); font-size:14px;">No other work assigned to you.</p>';
}"""

# Nothing actually needs patching there, it was correct. Let's make sure React conversion was actually asked for!
