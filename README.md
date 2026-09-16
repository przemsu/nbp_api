# NBP API Data Pipeline

A robust, automated ETL (Extract, Transform, Load) pipeline designed to fetch, store, and analyze financial data from the National Bank of Poland (NBP) API. The project follows the **Medallion Architecture** (Bronze, Silver, Gold) to ensure data integrity and scalability.

## 🚀 Features

- **Automated Extraction**: Daily snapshots of FX rates (Tables A, B, C) and Gold prices, with reactive backfill for missing dates.
- **Medallion Architecture**:
    - **Bronze Layer**: Raw JSON snapshots stored in a persistent `DuckDB` database with UPSERT logic to prevent duplicates.
    - **Silver Layer**: Cleaned and structured DuckDB views parsed from raw JSON — mid-rate currencies, buy/sell currencies, and gold prices.
    - **Gold Layer** *(in progress)*: Analytical view (`gold_wealth_index`) joining silver layers to compute purchasing-power metrics per currency.
    - **Data Lake**: Local storage of raw JSON files organized by date (`year/month/day`).
- **Production-Ready Logging**: Centralized logging system with timezone-aware timestamps (Europe/Warsaw) and module-specific loggers.
- **Robust CI/CD**: GitHub Actions workflow for daily automated runs with conflict resolution for log files.
- **Configuration-Driven**: All endpoints and paths are managed via `config.yaml` for easy maintenance.
- **Database**: Uses `DuckDB` for high-performance analytical queries and efficient JSON storage.

## 🛠 Tech Stack

- **Language**: Python 3.12+
- **Database**: DuckDB (Persistent storage)
- **Libraries**: Requests, Pathlib, PyYAML, Logging
- **Automation**: GitHub Actions
- **Configuration**: YAML

## 🏗 Project Structure

```text
├── etl/
│   ├── extract/       # API extraction logic (Raw data + backfill)
│   └── transform/     # Data loading into DuckDB (Bronze & Silver layers)
├── src/
│   └── utils/         # DB management, Logging setup, Config loader
├── data/
│   ├── raw/           # Raw JSON files (Data Lake)
│   ├── db/            # Persistent DuckDB files
│   └── sql_files/
│       ├── ddl/       # Silver & Gold layer view definitions (.sql)
│       └── dml/       # DML scripts
├── .github/workflows/ # Automation (CI/CD)
├── logs/              # Application execution logs
└── config.yaml        # Centralized configuration
```

## ⚙️ Setup & Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/nbp-api.git
   cd nbp-api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the pipeline**:
   ```bash
   python -m main
   ```

## 📈 Development Roadmap

- [x] **Sprint 1: Foundations** (Logging, Config, Basic Extraction)
- [x] **Sprint 2: Bronze Layer** (DuckDB Integration, Incremental Loading)
- [x] **Sprint 3: Silver Layer** (DuckDB Views: mid-rate currencies, buy/sell currencies, gold prices)
- [ ] **Sprint 4: Gold Layer** (Analytics Views, Purchasing Power Index) ← `gold_wealth_index` view started
- [ ] **Sprint 5: API Distribution** (FastAPI Integration)

## 🛡️ Best Practices Implemented

- **Idempotency**: The loader can be run multiple times without duplicating data in the database.
- **Resource Management**: Optimized database connections (open once, insert many).
- **Security**: Automated Git Hooks to prevent committing sensitive data (.env, absolute paths) and to enforce code formatting.
- **Traceability**: Detailed logs and error handling for every step of the ETL process.
