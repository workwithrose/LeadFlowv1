import re

with open("index.html", "r") as f:
    content = f.read()

# Replace the generated script inside fix_kpi_dash.py
target = r"""  let topStatsHtml = '';

  // Render user KPIs
  for \(const \[key, val\] of Object.entries\(appData.kpis\)\) \{
    let iconHtml = '<div class="icon icon-purple"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>';
    let subtitle = '&nbsp;';

    // Maintain some specific styling for the default KPIs if they still exist
    if \(key === 'Leads Today' \|\| key === 'leadsToday'\) \{
      iconHtml = '<div class="icon icon-purple"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>';
      subtitle = 'from running campaigns';
    \}
    if \(key === 'Broken Automations' \|\| key === 'brokenAutomations'\) \{
      iconHtml = '<div class="icon icon-orange"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></div>';
    \}

    topStatsHtml \+= `
      <div class="card stat-card">
        <div class="title">\$\{key\}</div>
        <div class="value">\$\{val\}</div>
        <div class="subtitle">\$\{subtitle\}</div>
        \$\{iconHtml\}
      </div>
    `;
  \}

  // Render calculated stats
  topStatsHtml \+= `
    <div class="card stat-card">
      <div class="title">Active Campaigns</div>
      <div class="value">\$\{activeCampaigns\}</div>
      <div class="subtitle">\$\{totalCampaigns\} total</div>
      <div class="icon icon-blue"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg></div>
    </div>
    <div class="card stat-card red">
      <div class="title">Tasks Overdue</div>
      <div class="value">\$\{overdueTasks\}</div>
      <div class="subtitle">&nbsp;</div>
      <div class="icon icon-red"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
    </div>
  `;

  document.getElementById\('dashTopStats'\).innerHTML = topStatsHtml;"""

replacement = """  let topStatsHtml = '';

  let leadsTodayVal = appData.kpis['Leads Today'] !== undefined ? appData.kpis['Leads Today'] : 8;

  topStatsHtml += `
    <div class="card stat-card">
      <div class="title">Leads Today</div>
      <div class="value">${leadsTodayVal}</div>
      <div class="subtitle">from running campaigns</div>
      <div class="icon icon-purple"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>
    </div>
  `;

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

  // Render user KPIs (except leads today which we hardcoded first)
  for (const [key, val] of Object.entries(appData.kpis)) {
    if (key === 'Leads Today' || key === 'leadsToday') continue;
    let iconHtml = '<div class="icon icon-orange"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></div>';
    let subtitle = '&nbsp;';

    topStatsHtml += `
      <div class="card stat-card">
        <div class="title">${key}</div>
        <div class="value">${val}</div>
        <div class="subtitle">${subtitle}</div>
        ${iconHtml}
      </div>
    `;
  }

  document.getElementById('dashTopStats').innerHTML = topStatsHtml;"""

content = re.sub(target, replacement, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)
