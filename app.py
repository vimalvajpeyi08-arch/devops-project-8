from flask import Flask, jsonify, request, render_template_string
import datetime

app = Flask(__name__)

# Mock database for incidents
incidents = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Incident Management Portal</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 40px; }
        .container { max-width: 900px; margin: 0 auto; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #334155; padding-bottom: 20px; margin-bottom: 30px; }
        .status-badge { background-color: #22c55e; color: #000; font-weight: bold; padding: 6px 16px; border-radius: 20px; }
        .card { background-color: #1e293b; padding: 25px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #334155; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        .metric { font-size: 32px; font-weight: bold; color: #38bdf8; margin-top: 5px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { text-align: left; padding: 12px; border-bottom: 1px solid #334155; }
        th { color: #94a3b8; font-size: 14px; text-transform: uppercase; }
        .badge-open { background-color: #ef4444; color: white; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; }
        button { background-color: #ef4444; color: white; border: none; padding: 12px 20px; font-size: 14px; font-weight: bold; border-radius: 8px; cursor: pointer; transition: 0.2s; }
        button:hover { background-color: #dc2626; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1 style="margin: 0; font-size: 24px;">🚨 Incident Management Engine</h1>
                <p style="margin: 5px 0 0 0; color: #94a3b8;">Real-time System Status & Alert Logging</p>
            </div>
            <span class="status-badge">System Operational</span>
        </div>

        <div class="grid">
            <div class="card">
                <div style="color: #94a3b8; font-size: 14px;">Total Incidents Logged</div>
                <div class="metric">{{ total }}</div>
            </div>
            <div class="card">
                <div style="color: #94a3b8; font-size: 14px;">Active Open Incidents</div>
                <div class="metric" style="color: #ef4444;">{{ active }}</div>
            </div>
        </div>

        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <h3 style="margin: 0;">Recent Incidents</h3>
                <form action="/trigger-demo" method="post" style="margin: 0;">
                    <button type="submit">+ Trigger Test Incident</button>
                </form>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Title</th>
                        <th>Severity</th>
                        <th>Timestamp</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {% if incidents %}
                        {% for incident in incidents %}
                        <tr>
                            <td><b>{{ incident.id }}</b></td>
                            <td>{{ incident.title }}</td>
                            <td><span style="color: #f59e0b; font-weight: bold;">{{ incident.severity }}</span></td>
                            <td style="color: #94a3b8;">{{ incident.timestamp }}</td>
                            <td><span class="badge-open">{{ incident.status }}</span></td>
                        </tr>
                        {% endfor %}
                    {% else %}
                        <tr>
                            <td colspan="5" style="text-align: center; color: #64748b; padding: 30px;">No active incidents reported. All systems normal.</td>
                        </tr>
                    {% endif %}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    active_incidents = [i for i in incidents if i['status'] == 'OPEN']
    return render_template_string(
        HTML_TEMPLATE,
        incidents=incidents,
        total=len(incidents),
        active=len(active_incidents)
    )

@app.route('/trigger-demo', methods=['POST'])
def trigger_demo():
    incident = {
        "id": f"INC-{len(incidents) + 101}",
        "title": "High CPU Utilization Alert (>90%)",
        "severity": "CRITICAL",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "OPEN"
    }
    incidents.append(incident)
    return home()

@app.route('/alert', methods=['POST'])
def trigger_alert():
    data = request.json or {}
    incident = {
        "id": f"INC-{len(incidents) + 101}",
        "title": data.get("title", "High CPU Utilization Detected"),
        "severity": data.get("severity", "CRITICAL"),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "OPEN"
    }
    incidents.append(incident)
    return jsonify({"message": "Alert Received & Incident Created", "incident": incident}), 201

@app.route('/api/incidents', methods=['GET'])
def list_incidents_api():
    return jsonify({"total": len(incidents), "incidents": incidents})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)