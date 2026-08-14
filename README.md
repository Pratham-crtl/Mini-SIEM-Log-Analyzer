# Mini-SIEM-Log-Analyzer

## 📌 Overview
This project simulates a **basic SIEM log analyzer** for SOC workflows.  
It detects anomalies in authentication logs and generates visual reports.

## 🚀 Features
- Parse Linux auth logs / Apache access logs.
- Detect brute force attempts.
- Generate CSV + chart reports.

## 🛠️ Setup
```bash

git clone https://github.com/pratham-crtl/Mini-SIEM-Log-Analyzer.git

cd Mini-SIEM-Log-Analyzer

pip install -r requirements.txt
```

## 📑 Usage
```bash
python analyzer.py --input logs/sample.log --output reports/report.csv
(csv reports)
or
python analyzer.py --input logs/sample.log --output reports/report.json
(JSON report)
