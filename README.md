# 🇨🇦 RTR Real-Time Payment Rail Monitoring Dashboard

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
git clone https://github.com/yourusername/rtr-payment-dashboard.git
cd rtr-payment-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
