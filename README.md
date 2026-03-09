# 🇨🇦 AI-ML-RTR-Fraud-Monitoring-Platform

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.14.0-green)](https://dash.plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Payments Canada](https://img.shields.io/badge/RTR-v1.4-red)](https://www.payments.ca/)
[![AI/ML](https://img.shields.io/badge/AI-ML-powered-orange)](https://scikit-learn.org/)
[![Synthetic Data](https://img.shields.io/badge/Data-Synthetic%20%F0%9F%93%8A-purple)](https://github.com/)

> ⚠️ **IMPORTANT: This dashboard uses 100% SYNTHETIC/FAKE data for educational purposes only. Not for production use.**

A comprehensive real-time payment monitoring dashboard simulating Canada's Real-Time Rail (RTR) payment system with **AI/ML-powered risk detection**, based on Payments Canada ISO 20022 specifications v1.4. **All transactions, bank names, and payment data shown are completely fake and randomly generated.**
<img width="1912" height="886" alt="image" src="https://github.com/user-attachments/assets/9f26b2e6-f7ce-49b0-9cdc-3681bec39c8c" />
<img width="1888" height="630" alt="image" src="https://github.com/user-attachments/assets/3cef8a92-009b-4069-8bce-623d4ae0be58" />
<img width="1890" height="828" alt="image" src="https://github.com/user-attachments/assets/03f75d78-a6e2-481d-813a-515cb0828cfe" />


## ✨ Features

### 🏦 Real-Time Payment Simulation (with Synthetic Data)
- **ISO 20022-compliant** fake message generation (pacs.008, pacs.002)
- **10+ simulated Canadian banks** with actual headquarters locations (Toronto, Montreal, Halifax, Vancouver, Ottawa, Levis)
- **Fake payment flows** with simulated liquidity management between institutions
- **Configurable fake transaction patterns** including normal payments, high-value wires, and structuring attempts

### 🤖 AI/ML Risk Detection (on Fake Data)
- **Isolation Forest** unsupervised learning trained on synthetic data
- **Multi-factor risk scoring** on simulated transactions
- **Real-time ML model training** on fake streaming data
- **Adaptive learning** that improves on made-up patterns
- **Automated flagging** of suspicious fake transactions

### 🗺️ Interactive Visualizations
- **Geographic map** of Canada with real bank headquarters (but fake transactions)
- **Live fake transaction timeline** with color-coded risk indicators
- **Simulated bank liquidity monitoring** with dynamic color gradients
- **Network graph** showing fake payment flows between institutions
- **Risk heat maps** highlighting made-up high-activity corridors

### Usage
Open your browser to http://localhost:8050
Click "Start" to begin the payment stream
Watch real-time transactions flow across Canada
Use filters to analyze specific transactions
Download data as CSV for further analysis

### 📊 Dashboard Controls
Control	Function
▶️ Start	Begins generating simulated payments
⏸️ Stop	Pauses payment generation
🔄 Reset	Clears all data and resets liquidity
📥 Download	Exports transactions to CSV
🔍 Filtering Options

### Filter	Options
Bank	All banks or specific institution
Status	Settled, Finality, Accepted, Rejected
Risk Level	ML HIGH, CRITICAL, HIGH, MEDIUM, LOW
Amount Range	Min/Max values in CAD

### 🤖 AI/ML Risk Scoring
Risk Factors
Factor	Score	Description
Extreme High Amount	70	> $10,000 (10x normal)
Very High Amount	50	> $5,000 (5x normal)
Just Below Threshold	30	$9,500 - $9,999
Round Amount	25	Suspicious structuring
High Amount	20	> $1,000
Cross-border	15	International payment
NeoBank Risk	10	Newer institution

### Risk Levels
CRITICAL RISK: Score > 70
HIGH RISK: Score > 50
MEDIUM RISK: Score > 20
LOW RISK: Score ≤ 20
ML HIGH RISK: Isolation Forest anomaly

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/naimish-kakkad/AI-ML-RTR-Fraud-Monitoring-Platform.git
cd rtr-payment-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

