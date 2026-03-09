# 🇨🇦 AI-ML RTR Real-Time Payment Rail Monitoring Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.14.0-green)](https://dash.plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Payments Canada](https://img.shields.io/badge/RTR-v1.4-red)](https://www.payments.ca/)

A comprehensive real-time payment monitoring dashboard simulating Canada's Real-Time Rail (RTR) payment system with AI/ML-powered risk detection, based on Payments Canada ISO 20022 specifications v1.4.

## ✨ Features

### 🏦 Real-Time Payment Simulation
- **ISO 20022-compliant** message generation
- **10+ Canadian banks** with actual headquarters locations
- **Realistic payment flows** with liquidity management
- **Configurable transaction patterns** (normal, high-value, structuring)

### 🤖 AI/ML Risk Detection
- **Isolation Forest** anomaly detection
- **Multi-factor risk scoring** (amount, bank, patterns)
- **Real-time ML model training** on streaming data
- **Risk visualization** with color-coded transactions

### 🗺️ Interactive Visualizations
- **Geographic map** of Canada with bank locations
- **Live transaction timeline** with risk indicators
- **Bank liquidity monitoring** with color gradients
- **Network graph** showing payment flows

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/naimish-kakkad/AI-ML-RTR-Fraud-Monitoring-Platform.git
cd rtr-payment-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py


Usage
Open your browser to http://localhost:8050
Click "Start" to begin the payment stream
Watch real-time transactions flow across Canada
Use filters to analyze specific transactions
Download data as CSV for further analysis

📊 Dashboard Controls
Control	Function
▶️ Start	Begins generating simulated payments
⏸️ Stop	Pauses payment generation
🔄 Reset	Clears all data and resets liquidity
📥 Download	Exports transactions to CSV
🔍 Filtering Options
Filter	Options

Bank	All banks or specific institution
Status	Settled, Finality, Accepted, Rejected
Risk Level	ML HIGH, CRITICAL, HIGH, MEDIUM, LOW
Amount Range	Min/Max values in CAD

🤖 AI/ML Risk Scoring
Risk Factors
Factor	Score	Description
Extreme High Amount	70	> $10,000 (10x normal)
Very High Amount	50	> $5,000 (5x normal)
Just Below Threshold	30	$9,500 - $9,999
Round Amount	25	Suspicious structuring
High Amount	20	> $1,000
Cross-border	15	International payment
NeoBank Risk	10	Newer institution

Risk Levels
CRITICAL RISK: Score > 70
HIGH RISK: Score > 50
MEDIUM RISK: Score > 20
LOW RISK: Score ≤ 20
ML HIGH RISK: Isolation Forest anomaly

🙏 Acknowledgements
Payments Canada for RTR ISO 20022 specifications v1.4
Plotly/Dash for the interactive dashboard framework
scikit-learn for Isolation Forest ML implementation
Faker for realistic payment data generation
Canadian Banks for headquarters location data

