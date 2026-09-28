# Python Data Pipeline

A portfolio-safe **data engineering and analytics project** built with Python, Pandas, NumPy, PostgreSQL and Metabase-compatible outputs.

The project simulates an e-commerce orders pipeline using fictional data. It validates records, transforms them, calculates business metrics and prepares a clean dataset for loading into PostgreSQL or a BI tool.

## Highlights

- ETL pipeline with Pandas
- Data validation and cleaning
- Derived metrics with NumPy
- PostgreSQL-ready schema
- CSV input/output
- Unit tests
- Docker Compose with PostgreSQL
- Example SQL for analytics and Metabase

## Pipeline

```text
Raw CSV
   |
   v
Validation
   |
   v
Cleaning + Transformation
   |
   v
Business Metrics
   |
   +---- cleaned_orders.csv
   |
   +---- PostgreSQL
             |
             v
          Metabase
```

## Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/pipeline.py
```

## Run tests

```bash
pytest
```

## PostgreSQL

```bash
docker compose up -d
```

Then use the SQL in `sql/analytics.sql` as a starting point for dashboards.

## Portfolio safety

All records in this repository are fictional. No company data, client information or production code is used.
