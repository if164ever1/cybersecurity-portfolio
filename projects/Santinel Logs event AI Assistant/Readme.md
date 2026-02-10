<!-- Improved README: clean, readable, and GitHub-friendly -->
# Sentinel Log ML

Lightweight Windows Event Log collection and anomaly-detection toolkit using Python and ML.

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About

Sentinel Log ML collects Windows Event Logs, processes them for feature engineering, and applies anomaly-detection models (unsupervised and semi-supervised) to surface suspicious activity. The project is intended as a research/prototyping workstation for security analysts and data scientists.

## Features

- Automated Windows Event Log collection (System & Security)
- Preprocessing & feature engineering for log events
- Unsupervised anomaly detection (Isolation Forest) and classifier experiments
- Optional MySQL storage for long-term retention
- Alerting hooks (Telegram, email — pluggable)
- Lightweight dashboard (Streamlit — planned)

## Tech Stack

- Python 3.10+
- pandas, numpy
- scikit-learn
- PyWin32 (Windows Event Log access)
- MySQL (optional persistence)
- Streamlit (visualization — optional)

## Quick Start

Prerequisites:

- Windows (for Event Log access)
- Python 3.10+
- Optional: MySQL server

Clone and install:

```bash
git clone https://github.com/your-username/sentinel-log-ml.git
cd "Sentinel Logs event AI Assistant"
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Run the collector (Administrator privileges required):

```bash
python src/collector.py
```

Train / run model (example):

```bash
python src/model.py --train
python src/model.py --infer --input "data/latest_events.csv"
```

## Configuration

- Edit `src/config.yaml` (or `src/config.example.yaml`) to set database, alerting, and model options.
- Use environment variables for secrets (DB password, Telegram token).

## Development

- Run tests (if available): `pytest`
- Follow code style: `black .` and `ruff` where configured
- Add small, focused commits and open PRs for review

## Contributing

Contributions welcome — please open issues or pull requests. Follow the established code style and include tests for critical features.

## License

Distributed under the MIT License. See `LICENSE` for details.

## Contact

Author: Ihor Zadorozhniak

Project: [Sentinel Log ML](https://github.com/your-username/sentinel-log-ml)

---

_This README was updated to improve clarity, structure, and usability for GitHub viewers._