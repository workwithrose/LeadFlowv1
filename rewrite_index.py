import re

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LeadFlow OS</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
  --bg-color: #fafafa;
  --sidebar-bg: #ffffff;
  --sidebar-border: #eaebea;
  --sidebar-text: #4b5563;
  --sidebar-hover: #f3f4f6;
  --sidebar-active-bg: #f3f4f6;
  --sidebar-active-text: #111827;

  --card-bg: #ffffff;
  --text-main: #111827;
  --text-muted: #6b7280;
  --border-color: #e5e7eb;

  --color-green: #10b981;
  --color-green-bg: #d1fae5;
  --color-yellow: #f59e0b;
  --color-yellow-bg: #fef3c7;
  --color-red: #ef4444;
  --color-red-bg: #fee2e2;
  --color-blue: #3b82f6;
  --color-purple: #8b5cf6;
  --color-orange: #f97316;

  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
  --radius: 12px;
  --radius-sm: 6px;
}

body {
  margin: 0;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  display: flex;
  background: var(--bg-color);
  color: var(--text-main);
  height: 100vh;
  overflow: hidden;
}

* {
  box-sizing: border-box;
}

/* Sidebar */
.sidebar {
  width: 260px;
  background: var(--sidebar-bg);
  color: var(--sidebar-text);
  height: 100vh;
  padding: 24px 16px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  border-right: 1px solid var(--sidebar-border);
}

.sidebar h2 {
  font-size: 20px;
  margin: 0 0 24px 12px;
  font-weight: 700;
  color: var(--text-main);
}

.nav-item {
  padding: 10px 12px;
  cursor: pointer;
  border-radius: var(--radius-sm);
  transition: all 0.2s ease;
  font-size: 14px;
  font-weight: 500;
  color: var(--sidebar-text);
  display: flex;
  align-items: center;
  gap: 12px;
}

.nav-item:hover {
  background: var(--sidebar-hover);
  color: var(--sidebar-active-text);
}

.nav-item.active {
  background: var(--sidebar-active-bg);
  color: var(--sidebar-active-text);
  font-weight: 600;
}

/* Main Area */
.main {
  flex: 1;
  padding: 40px 48px;
  overflow-y: auto;
}

.header-actions {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
}

.page-title {
  font-size: 28px;
  margin: 0 0 8px 0;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.page-subtitle {
  font-size: 14px;
  color: var(--text-muted);
  margin: 0;
}

/* Buttons */
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
}

button:hover {
  opacity: 0.9;
}

.btn-outline {
  background: transparent;
  color: var(--text-main);
  border: 1px solid var(--border-color);
}
.btn-outline:hover {
  background: var(--bg-color);
}

/* Cards & Grid */
.card {
  background: var(--card-bg);
  padding: 24px;
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border-color);
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 24px;
}

.grid-2-layout {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 20px;
  margin-bottom: 24px;
}

/* Dashboard Top Cards */
.stat-card {
  position: relative;
  display: flex;
  flex-direction: column;
}
.stat-card .title {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-muted);
  margin-bottom: 16px;
}
.stat-card .value {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--text-main);
}
.stat-card.red .value {
  color: var(--color-red);
}
.stat-card .subtitle {
  font-size: 12px;
  color: var(--text-muted);
}
.stat-card .icon {
  position: absolute;
  top: 24px;
  right: 24px;
  width: 32px;
  height: 32px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
}
.icon-purple { background: var(--color-purple); }
.icon-blue { background: var(--color-blue); }
.icon-red { background: var(--color-red); }
.icon-orange { background: var(--color-orange); }

/* Issues Detected */
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.card-title {
  font-size: 16px;
  font-weight: 600;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}
.badge {
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}
.badge-red-light {
  background: var(--color-red-bg);
  color: var(--color-red);
}

.issue-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.issue-item {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 14px;
  color: var(--sidebar-text);
}
.issue-icon {
  width: 24px;
  height: 24px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 12px;
}
.issue-icon.red { background: var(--color-red); }
.issue-icon.yellow { background: var(--color-yellow); }
.issue-icon.orange { background: var(--color-orange); }

/* Pipeline Stats */
.pipeline-stats {
  display: flex;
  justify-content: space-between;
  padding: 0 16px;
  margin-top: 24px;
}
.pipeline-stat {
  text-align: center;
}
.pipeline-stat .value {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 8px;
}
.pipeline-stat .label {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 12px;
}
.pipeline-bar {
  height: 6px;
  border-radius: 3px;
  width: 100%;
}
.bar-gray { background: #e5e7eb; }
.bar-blue { background: var(--color-blue); }
.bar-yellow { background: var(--color-yellow); }
.bar-purple { background: var(--color-purple); }
.bar-green { background: var(--color-green); }

.view-all {
  font-size: 13px;
  color: var(--color-purple);
  text-decoration: none;
  font-weight: 500;
  cursor: pointer;
}
.view-all:hover {
  text-decoration: underline;
}

/* Task Activity */
.task-list {
  display: flex;
  flex-direction: column;
}
.task-row {
  display: flex;
  align-items: center;
  padding: 16px 0;
  border-bottom: 1px solid var(--border-color);
  font-size: 14px;
}
.task-row:last-child {
  border-bottom: none;
  padding-bottom: 0;
}
.task-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-right: 16px;
}
.task-dot.green { background: var(--color-green); }
.task-dot.blue { background: var(--color-blue); }
.task-dot.yellow { background: var(--color-yellow); }
.task-dot.red { background: var(--color-red); }

.task-title {
  flex: 1;
  color: var(--text-main);
  font-weight: 500;
}
.task-owner {
  color: var(--text-muted);
  margin-right: 16px;
  width: 60px;
  text-align: right;
}
.task-tag {
  font-size: 12px;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: 4px;
}
.task-tag.stale {
  background: #fffbeb;
  color: #b45309;
}
.task-tag.overdue {
  background: var(--color-red-bg);
  color: var(--color-red);
}

/* Modals */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
  backdrop-filter: blur(2px);
}

.modal-overlay.active {
  opacity: 1;
  pointer-events: auto;
}

.modal-content {
  background: var(--card-bg);
  padding: 32px;
  border-radius: var(--radius);
  width: 100%;
  max-width: 500px;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-color);
}

.modal-content h2 {
  margin-top: 0;
  margin-bottom: 24px;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  font-size: 14px;
  font-weight: 500;
  margin-bottom: 8px;
  color: var(--text-main);
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  font-size: 14px;
  font-family: inherit;
}
.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--color-purple);
  box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2);
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 24px;
}

/* Kanban / Pipeline */
.pipeline-board {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  padding-bottom: 16px;
  min-height: 400px;
}

.pipeline-col {
  background: #f9fafb;
  padding: 16px;
  min-width: 280px;
  flex: 1;
  border-radius: var(--radius);
  display: flex;
  flex-direction: column;
  gap: 12px;
  border: 1px solid var(--border-color);
}

.pipeline-col h4 {
  margin: 0 0 8px 0;
  font-size: 14px;
  color: var(--text-muted);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.kanban-item {
  background: var(--card-bg);
  padding: 16px;
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border-color);
  font-size: 14px;
  cursor: grab;
  transition: box-shadow 0.2s;
}
.kanban-item:hover {
  box-shadow: var(--shadow-md);
}
.kanban-item:active {
  cursor: grabbing;
}
.kanban-title {
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-main);
}
.kanban-meta {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 8px;
}
.kanban-badge {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}
.bg-green { background: var(--color-green-bg); color: var(--color-green); }
.bg-yellow { background: var(--color-yellow-bg); color: var(--color-yellow); }
.bg-red { background: var(--color-red-bg); color: var(--color-red); }

.stale-warning {
  color: var(--color-red);
  font-size: 12px;
  font-weight: 500;
  margin-top: 8px;
  display: flex;
  align-items: center;
  gap: 4px;
}

/* List views (Campaigns, Tasks, My Work) */
.list-view {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.list-card {
  background: var(--card-bg);
  padding: 20px;
  border-radius: var(--radius);
  border: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: box-shadow 0.2s;
}
.list-card:hover {
  box-shadow: var(--shadow-sm);
}
.list-card-title {
  font-weight: 600;
  font-size: 16px;
  margin-bottom: 4px;
}
.list-card-sub {
  font-size: 13px;
  color: var(--text-muted);
}
.list-card-right {
  text-align: right;
}

</style>
</head>

<body>

<div class="sidebar">
  <h2>LeadFlow OS</h2>
  <div class="nav-item active" onclick="showTab('dashboard', this)">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
    Dashboard
  </div>
  <div class="nav-item" onclick="showTab('campaigns', this)">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon></svg>
    Campaigns
  </div>
  <div class="nav-item" onclick="showTab('pipeline', this)">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>
    Production Pipeline
  </div>
  <div class="nav-item" onclick="showTab('tasks', this)">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
    Tasks
  </div>
  <div class="nav-item" onclick="showTab('mywork', this)">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
    My Work
  </div>
</div>

<div class="main">

  <!-- DASHBOARD TAB -->
  <div id="dashboard" class="tab">
    <div class="header-actions">
      <div>
        <h1 class="page-title">Command Center</h1>
        <p class="page-subtitle" id="currentDate">Saturday, March 21, 2026</p>
      </div>
      <button onclick="generateReport()">Generate Daily Report</button>
    </div>

    <!-- Top Stats -->
    <div class="grid-4" id="dashTopStats">
      <!-- Rendered dynamically -->
    </div>

    <!-- Middle section -->
    <div class="grid-2-layout">
      <!-- Issues Detected -->
      <div class="card">
        <div class="card-header">
          <h3 class="card-title">⚠️ Issues Detected</h3>
          <span class="badge badge-red-light" id="issuesCount">3</span>
        </div>
        <div class="issue-list" id="dashIssues">
          <!-- Rendered dynamically -->
        </div>
      </div>

      <!-- Production Pipeline -->
      <div class="card">
        <div class="card-header">
          <h3 class="card-title">🎬 Production Pipeline</h3>
          <a class="view-all" onclick="showTab('pipeline', document.querySelectorAll('.nav-item')[2])">View all →</a>
        </div>
        <div class="pipeline-stats" id="dashPipeline">
          <!-- Rendered dynamically -->
        </div>
      </div>
    </div>

    <!-- Bottom section -->
    <div class="card">
      <div class="card-header">
        <h3 class="card-title">✓ Recent Task Activity</h3>
        <a class="view-all" onclick="showTab('tasks', document.querySelectorAll('.nav-item')[3])">View all →</a>
      </div>
      <div class="task-list" id="dashTasks">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </div>


  <!-- CAMPAIGNS TAB -->
  <div id="campaigns" class="tab" style="display:none;">
    <div class="header-actions">
      <div>
        <h1 class="page-title">Campaigns</h1>
        <p class="page-subtitle">Manage and track active campaigns</p>
      </div>
      <button onclick="openModal(null, 'campaign')">+ Add Campaign</button>
    </div>
    <div class="list-view" id="campaignsList"></div>
  </div>


  <!-- PIPELINE TAB -->
  <div id="pipeline" class="tab" style="display:none;">
    <div class="header-actions">
      <div>
        <h1 class="page-title">Production Pipeline</h1>
        <p class="page-subtitle">Track video production stages</p>
      </div>
      <button onclick="openModal(null, 'pipeline')">+ Add Item</button>
    </div>
    <div class="pipeline-board" id="pipelineBoard"></div>
  </div>


  <!-- TASKS TAB -->
  <div id="tasks" class="tab" style="display:none;">
    <div class="header-actions">
      <div>
        <h1 class="page-title">Tasks</h1>
        <p class="page-subtitle">All tasks across projects</p>
      </div>
      <button onclick="openModal(null, 'task')">+ Add Task</button>
    </div>
    <div class="list-view" id="tasksList"></div>
  </div>


  <!-- MY WORK TAB -->
  <div id="mywork" class="tab" style="display:none;">
    <div class="header-actions">
      <div>
        <h1 class="page-title">My Work</h1>
        <p class="page-subtitle">Filtered for Rose</p>
      </div>
      <button onclick="openModal()">+ Add Item</button>
    </div>

    <h3 style="margin-top:0; font-size:16px; margin-bottom:12px;">Priority / Needs Attention</h3>
    <div class="list-view" id="myWorkPriority" style="margin-bottom: 32px;"></div>

    <h3 style="margin-top:0; font-size:16px; margin-bottom:12px;">All Other Work</h3>
    <div class="list-view" id="myWorkOther"></div>
  </div>

</div>

<!-- Modal: Add/Edit Item -->
<div class="modal-overlay" id="itemModal">
  <div class="modal-content">
    <h2 id="modalTitle">Add Item</h2>
    <form id="itemForm">
      <input type="hidden" id="itemId">
      <div class="form-group">
        <label>Type</label>
        <select id="itemType" required onchange="toggleStageField()">
          <option value="task">Task</option>
          <option value="campaign">Campaign</option>
          <option value="pipeline">Pipeline Item</option>
        </select>
      </div>
      <div class="form-group">
        <label>Title</label>
        <input type="text" id="itemTitle" required>
      </div>
      <div class="form-group">
        <label>Owner</label>
        <input type="text" id="itemOwner" required>
      </div>
      <div class="form-group">
        <label>Status</label>
        <select id="itemStatus" required>
          <option value="On Track">On Track</option>
          <option value="At Risk">At Risk</option>
          <option value="Delayed">Delayed</option>
        </select>
      </div>
      <div class="form-group" id="stageGroup" style="display:none;">
        <label>Stage (Pipeline only)</label>
        <select id="itemStage">
          <option value="Script">Script</option>
          <option value="Filming">Filming</option>
          <option value="Editing">Editing</option>
          <option value="Review">Review</option>
          <option value="Approved">Approved</option>
          <option value="Uploaded">Uploaded</option>
        </select>
      </div>
      <div class="form-group">
        <label>Due Date</label>
        <input type="date" id="itemDueDate">
      </div>
      <div class="form-group">
        <label>Next Action (Required)</label>
        <input type="text" id="itemNextAction" required>
      </div>
      <div class="form-group">
        <label>Notes</label>
        <textarea id="itemNotes" rows="3"></textarea>
      </div>
      <div class="modal-actions">
        <button type="button" class="btn-outline" onclick="closeModal()">Cancel</button>
        <button type="submit">Save Item</button>
      </div>
    </form>
  </div>
</div>

<!-- Modal: Generate Report -->
<div class="modal-overlay" id="reportModal">
  <div class="modal-content">
    <h2>Daily Report</h2>
    <div id="reportContent" style="background:#f9fafb; padding:16px; border-radius:8px; border:1px solid var(--border-color); white-space: pre-wrap; font-family: monospace; font-size: 14px; max-height: 400px; overflow-y:auto; line-height: 1.5;"></div>
    <div class="modal-actions">
      <button type="button" class="btn-outline" onclick="closeReportModal()">Close</button>
    </div>
  </div>
</div>

<script>
// --- UI Helpers ---
function setDate() {
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  document.getElementById('currentDate').innerText = new Date().toLocaleDateString('en-US', options);
}
setDate();

function showTab(tabId, element) {
  document.querySelectorAll('.tab').forEach(t => t.style.display = 'none');
  document.getElementById(tabId).style.display = 'block';

  if (element) {
    document.querySelectorAll('.sidebar .nav-item').forEach(i => i.classList.remove('active'));
    element.classList.add('active');
  }
}

// --- Data & LocalStorage ---
const defaultData = {
  kpis: {
    leadsToday: 8,
    brokenAutomations: 0
  },
  items: [
    { id: 1, type: 'campaign', title: 'FitLife Summer Video', owner: 'Alex', status: 'At Risk', dueDate: '2023-12-01', nextAction: 'Write script', notes: '', lastUpdated: Date.now() - (48 * 3600 * 1000) },
    { id: 2, type: 'campaign', title: 'Bright Solar ad account', owner: 'Taylor', status: 'Delayed', dueDate: '2023-11-20', nextAction: 'Fix issue', notes: '', lastUpdated: Date.now() - (48 * 3600 * 1000) },
    { id: 3, type: 'task', title: 'Review Q1 performance report', owner: 'Jordan', status: 'On Track', dueDate: '2023-11-25', nextAction: 'Approve', notes: '', lastUpdated: Date.now() },
    { id: 4, type: 'task', title: 'Update Apex Roofing ad creative', owner: 'Jordan', status: 'On Track', dueDate: '2023-11-15', nextAction: 'Upload', notes: '', lastUpdated: Date.now() },
    { id: 5, type: 'pipeline', title: 'Ad #1', stage: 'Script', owner: 'Rose', status: 'On Track', dueDate: '2023-11-28', nextAction: 'Draft', notes: '', lastUpdated: Date.now() },
    { id: 6, type: 'pipeline', title: 'Ad #2', stage: 'Filming', owner: 'Rose', status: 'On Track', dueDate: '2023-11-28', nextAction: 'Shoot', notes: '', lastUpdated: Date.now() },
    { id: 7, type: 'pipeline', title: 'Ad #3', stage: 'Editing', owner: 'Rose', status: 'On Track', dueDate: '2023-11-28', nextAction: 'Cut', notes: '', lastUpdated: Date.now() },
    { id: 8, type: 'pipeline', title: 'Ad #4', stage: 'Approved', owner: 'Rose', status: 'On Track', dueDate: '2023-11-28', nextAction: 'Upload', notes: '', lastUpdated: Date.now() },
    { id: 9, type: 'pipeline', title: 'Ad #5', stage: 'Uploaded', owner: 'Rose', status: 'On Track', dueDate: '2023-11-28', nextAction: 'Monitor', notes: '', lastUpdated: Date.now() },
    { id: 10, type: 'task', title: 'Fix broken tracking', owner: 'Rose', status: 'Delayed', dueDate: '2023-11-10', nextAction: 'Check tags', notes: '', lastUpdated: Date.now() - (48 * 3600 * 1000) }
  ]
};

let appData = JSON.parse(localStorage.getItem('leadFlowData'));
if (!appData) {
  appData = defaultData;
  saveData();
}

function saveData() {
  localStorage.setItem('leadFlowData', JSON.stringify(appData));
}

function generateId() {
  return appData.items.length > 0 ? Math.max(...appData.items.map(i => i.id)) + 1 : 1;
}

// --- Render Functions ---
function renderAll() {
  renderDashboard();
  renderPipeline();
  renderCampaigns();
  renderTasks();
  renderMyWork();
}

function isStale(item) {
  return Date.now() - item.lastUpdated > 24 * 60 * 60 * 1000;
}

function getStatusBadge(status) {
  if (status === 'On Track') return '<span class="kanban-badge bg-green">On Track</span>';
  if (status === 'At Risk') return '<span class="kanban-badge bg-yellow">At Risk</span>';
  if (status === 'Delayed') return '<span class="kanban-badge bg-red">Delayed</span>';
  return '';
}

function renderDashboard() {
  const activeCampaigns = appData.items.filter(i => i.type === 'campaign' && i.status !== 'Delayed').length;
  const totalCampaigns = appData.items.filter(i => i.type === 'campaign').length;
  const overdueTasks = appData.items.filter(i => i.type === 'task' && i.status === 'Delayed').length;

  document.getElementById('dashTopStats').innerHTML = `
    <div class="card stat-card">
      <div class="title">Leads Today</div>
      <div class="value">${appData.kpis.leadsToday || 8}</div>
      <div class="subtitle">from running campaigns</div>
      <div class="icon icon-purple">📈</div>
    </div>
    <div class="card stat-card">
      <div class="title">Active Campaigns</div>
      <div class="value">${activeCampaigns}</div>
      <div class="subtitle">${totalCampaigns} total</div>
      <div class="icon icon-blue">📢</div>
    </div>
    <div class="card stat-card red">
      <div class="title">Tasks Overdue</div>
      <div class="value">${overdueTasks}</div>
      <div class="subtitle">&nbsp;</div>
      <div class="icon icon-red">⏰</div>
    </div>
    <div class="card stat-card">
      <div class="title">Broken Automations</div>
      <div class="value">${appData.kpis.brokenAutomations || 0}</div>
      <div class="subtitle">&nbsp;</div>
      <div class="icon icon-orange">✖</div>
    </div>
  `;

  // Issues Detected
  const staleItems = appData.items.filter(isStale);
  const delayedItems = appData.items.filter(i => i.status === 'Delayed');

  let issuesHtml = '';
  let issuesCount = 0;

  const staleTasks = staleItems.filter(i => i.type === 'task').length;
  if (overdueTasks > 0) {
    issuesHtml += `<div class="issue-item"><div class="issue-icon red">⏰</div>${overdueTasks} task${overdueTasks>1?'s':''} overdue</div>`;
    issuesCount++;
  }
  if (staleTasks > 0) {
    issuesHtml += `<div class="issue-item"><div class="issue-icon yellow">⚠</div>${staleTasks} task${staleTasks>1?'s':''} with no update in 24h</div>`;
    issuesCount++;
  }
  const brokenCampaigns = appData.items.filter(i => i.type === 'campaign' && (i.status === 'Delayed' || isStale(i))).length;
  if (brokenCampaigns > 0) {
    issuesHtml += `<div class="issue-item"><div class="issue-icon orange">📢</div>${brokenCampaigns} campaign${brokenCampaigns>1?'s':''} need fixing</div>`;
    issuesCount++;
  }

  if (issuesCount === 0) issuesHtml = '<div style="color:var(--text-muted); font-size:14px;">No issues detected! 🎉</div>';

  document.getElementById('dashIssues').innerHTML = issuesHtml;
  document.getElementById('issuesCount').innerText = issuesCount;

  // Pipeline Stats
  const stages = ['Script', 'Filming', 'Editing', 'Approved', 'Uploaded'];
  const stageColors = ['gray', 'blue', 'yellow', 'purple', 'green'];
  let pipelineHtml = '';

  stages.forEach((stg, idx) => {
    const count = appData.items.filter(i => i.type === 'pipeline' && i.stage === stg).length;
    pipelineHtml += `
      <div class="pipeline-stat">
        <div class="value">${count}</div>
        <div class="label">${stg}</div>
        <div class="pipeline-bar bar-${stageColors[idx]}"></div>
      </div>
    `;
  });
  document.getElementById('dashPipeline').innerHTML = pipelineHtml;

  // Recent Tasks
  let taskRows = '';
  const recentTasks = appData.items.filter(i => i.type !== 'pipeline').slice(-4); // just mock recent
  recentTasks.forEach(task => {
    let dotColor = 'green';
    if (task.status === 'At Risk') dotColor = 'yellow';
    if (task.status === 'Delayed') dotColor = 'red';
    if (task.title.includes('Apex')) dotColor = 'blue';

    let tag = '';
    if (isStale(task)) tag = '<span class="task-tag stale">Stale</span>';
    if (task.status === 'Delayed') tag = '<span class="task-tag overdue">Overdue</span>';

    taskRows += `
      <div class="task-row" onclick="openModal(${task.id})" style="cursor:pointer;">
        <div class="task-dot ${dotColor}"></div>
        <div class="task-title">${task.title}</div>
        <div class="task-owner">${task.owner}</div>
        ${tag}
      </div>
    `;
  });
  document.getElementById('dashTasks').innerHTML = taskRows;
}

function renderCampaigns() {
  const container = document.getElementById('campaignsList');
  container.innerHTML = '';
  const items = appData.items.filter(i => i.type === 'campaign');
  if (items.length === 0) container.innerHTML = '<p>No campaigns yet.</p>';
  items.forEach(item => {
    container.innerHTML += `
      <div class="list-card" onclick="openModal(${item.id})">
        <div>
          <div class="list-card-title">${item.title}</div>
          <div class="list-card-sub">Next: ${item.nextAction} | Owner: ${item.owner}</div>
        </div>
        <div class="list-card-right">
          ${getStatusBadge(item.status)}
          ${isStale(item) ? '<div class="stale-warning" style="justify-content:flex-end;">⚠ Stale</div>' : ''}
        </div>
      </div>
    `;
  });
}

function renderTasks() {
  const container = document.getElementById('tasksList');
  container.innerHTML = '';
  const items = appData.items.filter(i => i.type === 'task');
  if (items.length === 0) container.innerHTML = '<p>No tasks yet.</p>';
  items.forEach(item => {
    container.innerHTML += `
      <div class="list-card" onclick="openModal(${item.id})">
        <div>
          <div class="list-card-title">${item.title}</div>
          <div class="list-card-sub">Next: ${item.nextAction} | Owner: ${item.owner}</div>
        </div>
        <div class="list-card-right">
          ${getStatusBadge(item.status)}
          ${isStale(item) ? '<div class="stale-warning" style="justify-content:flex-end;">⚠ Stale</div>' : ''}
        </div>
      </div>
    `;
  });
}

function renderMyWork() {
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
}

// --- Drag & Drop ---
let draggedItemId = null;

function handleDragStart(e, id) {
  draggedItemId = id;
  e.dataTransfer.effectAllowed = 'move';
  e.target.style.opacity = '0.5';
}
function handleDragEnd(e) {
  e.target.style.opacity = '1';
  draggedItemId = null;
}
function handleDragOver(e) {
  e.preventDefault();
  e.dataTransfer.dropEffect = 'move';
}
function handleDrop(e, stage) {
  e.preventDefault();
  if (draggedItemId) {
    const item = appData.items.find(i => i.id === draggedItemId);
    if (item && item.stage !== stage) {
      item.stage = stage;
      item.lastUpdated = Date.now();
      saveData();
      renderAll();
    }
  }
}

function renderPipeline() {
  const container = document.getElementById('pipelineBoard');
  const stages = ['Script', 'Filming', 'Editing', 'Review', 'Approved', 'Uploaded'];
  container.innerHTML = '';

  stages.forEach(stage => {
    const col = document.createElement('div');
    col.className = 'pipeline-col';
    col.ondragover = handleDragOver;
    col.ondrop = (e) => handleDrop(e, stage);

    const count = appData.items.filter(i => i.type === 'pipeline' && i.stage === stage).length;
    col.innerHTML = `<h4>${stage} &nbsp;<span style="color:#9ca3af">${count}</span></h4>`;

    const stageItems = appData.items.filter(i => i.type === 'pipeline' && i.stage === stage);
    stageItems.forEach(item => {
      const el = document.createElement('div');
      el.className = 'kanban-item';
      el.draggable = true;
      el.ondragstart = (e) => handleDragStart(e, item.id);
      el.ondragend = handleDragEnd;
      el.onclick = () => openModal(item.id);

      el.innerHTML = `
        <div class="kanban-title">${item.title}</div>
        <div class="kanban-meta">Owner: ${item.owner}</div>
        ${getStatusBadge(item.status)}
        ${isStale(item) ? '<div class="stale-warning">⚠ Stale (>24h)</div>' : ''}
      `;
      col.appendChild(el);
    });
    container.appendChild(col);
  });
}

// --- Modals ---
function openModal(id = null, type = 'task') {
  const modal = document.getElementById('itemModal');
  const form = document.getElementById('itemForm');
  form.reset();

  if (id) {
    document.getElementById('modalTitle').innerText = 'Edit Item';
    const item = appData.items.find(i => i.id === id);
    if (item) {
      document.getElementById('itemId').value = item.id;
      document.getElementById('itemType').value = item.type;
      document.getElementById('itemTitle').value = item.title;
      document.getElementById('itemOwner').value = item.owner;
      document.getElementById('itemStatus').value = item.status;
      if (item.stage) document.getElementById('itemStage').value = item.stage;
      document.getElementById('itemDueDate').value = item.dueDate || '';
      document.getElementById('itemNextAction').value = item.nextAction;
      document.getElementById('itemNotes').value = item.notes || '';
    }
  } else {
    document.getElementById('modalTitle').innerText = 'Add Item';
    document.getElementById('itemId').value = '';
    document.getElementById('itemType').value = type;
    document.getElementById('itemOwner').value = 'Rose';
  }

  toggleStageField();
  modal.classList.add('active');
}

function closeModal() {
  document.getElementById('itemModal').classList.remove('active');
}

function toggleStageField() {
  const type = document.getElementById('itemType').value;
  document.getElementById('stageGroup').style.display = type === 'pipeline' ? 'block' : 'none';
}

document.getElementById('itemForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const idStr = document.getElementById('itemId').value;
  const itemData = {
    type: document.getElementById('itemType').value,
    title: document.getElementById('itemTitle').value,
    owner: document.getElementById('itemOwner').value,
    status: document.getElementById('itemStatus').value,
    dueDate: document.getElementById('itemDueDate').value,
    nextAction: document.getElementById('itemNextAction').value,
    notes: document.getElementById('itemNotes').value,
    lastUpdated: Date.now()
  };

  if (itemData.type === 'pipeline') {
    itemData.stage = document.getElementById('itemStage').value || 'Script';
  }

  if (idStr) {
    const id = parseInt(idStr, 10);
    const index = appData.items.findIndex(i => i.id === id);
    if (index !== -1) appData.items[index] = { ...appData.items[index], ...itemData };
  } else {
    itemData.id = generateId();
    appData.items.push(itemData);
  }

  saveData();
  closeModal();
  renderAll();
});

// --- Reports ---
function generateReport() {
  const dateStr = new Date().toLocaleDateString();
  const delayedItems = appData.items.filter(i => i.status === 'Delayed');
  const onTrackItems = appData.items.filter(i => i.status === 'On Track');
  const atRiskItems = appData.items.filter(i => i.status === 'At Risk');

  let reportText = `DAILY REPORT - ${dateStr}\n`;
  reportText += `==============================\n\n`;

  reportText += `🚨 OVERDUE / DELAYED (${delayedItems.length}):\n`;
  delayedItems.forEach(i => reportText += `- [${i.type.toUpperCase()}] ${i.title} (Owner: ${i.owner})\n  Next: ${i.nextAction}\n`);

  reportText += `\n⚠️ AT RISK (${atRiskItems.length}):\n`;
  atRiskItems.forEach(i => reportText += `- [${i.type.toUpperCase()}] ${i.title} (Owner: ${i.owner})\n  Next: ${i.nextAction}\n`);

  reportText += `\n✅ ON TRACK (${onTrackItems.length}):\n`;
  onTrackItems.forEach(i => reportText += `- [${i.type.toUpperCase()}] ${i.title} (Owner: ${i.owner})\n  Next: ${i.nextAction}\n`);

  document.getElementById('reportContent').innerText = reportText;
  document.getElementById('reportModal').classList.add('active');
}

function closeReportModal() {
  document.getElementById('reportModal').classList.remove('active');
}

// Init
document.addEventListener('DOMContentLoaded', renderAll);

</script>

</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
