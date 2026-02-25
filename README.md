# AI Stock Analyst

AI-powered stock analytics platform with a Flask backend, PostgreSQL datastore, React dashboard, and grounded AI assistant.

## Milestone Status

- [x] Milestone 0 - Repository scaffolding
- [ ] Milestone 1 - Database + ingestion
- [ ] Milestone 2 - REST API
- [ ] Milestone 3 - Frontend dashboard
- [ ] Milestone 4 - AI analytics assistant
- [ ] Milestone 5 - Polish

## Architecture (Target)

```text
+---------------------------+        +---------------------------+        +------------------------+
| Presentation Tier         | <----> | Application Tier          | <----> | Data Tier              |
| React + TypeScript (Vite) |        | Flask REST + Services     |        | PostgreSQL             |
| - Dashboard               |        | - Ingestion orchestration |        | - tickers              |
| - Comparison charts       |        | - Query/aggregation       |        | - price_history        |
| - AI chat panel           |        | - AI grounding + OpenAI   |        | - fundamentals         |
+---------------------------+        +---------------------------+        +------------------------+
```

## Repository Layout

```text
.
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── ingestion/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── tests/
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml
└── .env.example
```

## Local Setup

1. Copy env template and fill secrets when available:
   ```bash
   cp .env.example .env
   ```
2. Start PostgreSQL:
   ```bash
   docker-compose up -d db
   ```
3. Start backend:
   ```bash
   cd backend
   poetry install
   poetry run flask --app app run --debug
   ```
4. Start frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Initial API Availability

- `GET /api/health` -> basic backend status check.

## Notes / To Be Completed in Later Milestones

- Real stock data ingestion provider implementation and DB schema migrations.
- REST resources for tickers, summaries, price history, and comparison.
- Grounded AI assistant endpoint using OpenAI Responses API with citations.
- CI workflow for backend tests + frontend build.
