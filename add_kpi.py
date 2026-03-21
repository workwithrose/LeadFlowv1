import re

with open("index.html", "r") as f:
    content = f.read()

# Add the Edit KPIs button
content = content.replace(
    """<button onclick="generateReport()">Generate Daily Report</button>""",
    """<div style="display: flex; gap: 12px;">
        <button class="btn-outline" onclick="openKpiModal()">Edit KPIs</button>
        <button onclick="generateReport()">Generate Daily Report</button>
      </div>"""
)

# Add the KPI Modal HTML
kpi_modal_html = """
<!-- Modal: Edit KPIs -->
<div class="modal-overlay" id="kpiModal">
  <div class="modal-content">
    <h2>Edit KPIs</h2>
    <form id="kpiForm">
      <div id="kpiInputsContainer"></div>
      <div style="margin-top:16px; margin-bottom: 16px;">
        <button type="button" class="btn-outline" style="font-size:12px; padding: 4px 8px;" onclick="addKpiField()">+ Add KPI</button>
      </div>
      <div class="modal-actions">
        <button type="button" class="btn-outline" onclick="closeKpiModal()">Cancel</button>
        <button type="submit">Save KPIs</button>
      </div>
    </form>
  </div>
</div>
"""

content = content.replace("<!-- Modal: Generate Report -->", kpi_modal_html + "\n<!-- Modal: Generate Report -->")

# Update renderDashboard to render appData.kpis
kpi_render_code = """
  let topStatsHtml = '';

  // Render user KPIs
  for (const [key, val] of Object.entries(appData.kpis)) {
    let iconHtml = '<div class="icon icon-purple"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>';
    let subtitle = '&nbsp;';

    // Maintain some specific styling for the default KPIs if they still exist
    if (key === 'Leads Today' || key === 'leadsToday') {
      iconHtml = '<div class="icon icon-purple"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>';
      subtitle = 'from running campaigns';
    }
    if (key === 'Broken Automations' || key === 'brokenAutomations') {
      iconHtml = '<div class="icon icon-orange"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></div>';
    }

    topStatsHtml += `
      <div class="card stat-card">
        <div class="title">${key}</div>
        <div class="value">${val}</div>
        <div class="subtitle">${subtitle}</div>
        ${iconHtml}
      </div>
    `;
  }

  // Render calculated stats
  topStatsHtml += `
    <div class="card stat-card">
      <div class="title">Active Campaigns</div>
      <div class="value">${activeCampaigns}</div>
      <div class="subtitle">${totalCampaigns} total</div>
      <div class="icon icon-blue"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg></div>
    </div>
    <div class="card stat-card red">
      <div class="title">Tasks Overdue</div>
      <div class="value">${overdueTasks}</div>
      <div class="subtitle">&nbsp;</div>
      <div class="icon icon-red"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
    </div>
  `;

  document.getElementById('dashTopStats').innerHTML = topStatsHtml;
"""

# Replace the existing hardcoded dashTopStats update
content = re.sub(r"document\.getElementById\('dashTopStats'\)\.innerHTML = `.*?`;", kpi_render_code, content, flags=re.DOTALL)

# Default KPIs modification to match new key format
content = content.replace(
    "leadsToday: 8,",
    "'Leads Today': 8,"
)
content = content.replace(
    "brokenAutomations: 0",
    "'Broken Automations': 0"
)

# Inject KPI Logic
kpi_logic = """
// --- KPI Logic ---
function openKpiModal() {
  const container = document.getElementById('kpiInputsContainer');
  container.innerHTML = '';
  for (const [key, val] of Object.entries(appData.kpis)) {
    addKpiField(key, val);
  }
  document.getElementById('kpiModal').classList.add('active');
}

function closeKpiModal() {
  document.getElementById('kpiModal').classList.remove('active');
}

function addKpiField(key = '', val = '') {
  const container = document.getElementById('kpiInputsContainer');
  const div = document.createElement('div');
  div.style.display = 'flex';
  div.style.gap = '8px';
  div.style.marginBottom = '8px';
  div.innerHTML = `
    <input type="text" placeholder="KPI Name" value="${key}" class="kpi-key" style="flex:1;" required>
    <input type="text" placeholder="Value" value="${val}" class="kpi-val" style="flex:1;" required>
    <button type="button" class="btn-outline" style="padding:0 12px;" onclick="this.parentElement.remove()">X</button>
  `;
  container.appendChild(div);
}

document.getElementById('kpiForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const keys = document.querySelectorAll('.kpi-key');
  const vals = document.querySelectorAll('.kpi-val');

  appData.kpis = {};
  for(let i=0; i<keys.length; i++) {
    const k = keys[i].value.trim();
    const v = vals[i].value.trim();
    if(k) appData.kpis[k] = v;
  }

  saveData();
  closeKpiModal();
  renderAll();
});

// --- Reports ---
"""

content = content.replace("// --- Reports ---", kpi_logic)

# Change grid-4 to a flexible grid like grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
content = content.replace(
    """grid-template-columns: repeat(4, 1fr);""",
    """grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));"""
)

with open("index.html", "w") as f:
    f.write(content)
