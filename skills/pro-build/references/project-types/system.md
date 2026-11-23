# Project type: System (backends, APIs, services, data and automation)

Use it for REST or GraphQL APIs, microservices, background workers, data pipelines, integrations, bots and automations, CLIs, and the backend behind a web or mobile product. Combine it with any track; headless systems shrink stage 3 (design) to the API and CLI ergonomics.

## Pick the shape first

| Shape | Signs | Default stack | Alternatives, and when to use them |
|:--|:--|:--|:--|
| **API service** | Clients call endpoints; CRUD and business rules | **TypeScript** (Hono, Fastify or NestJS: `ecc:nestjs-patterns`) or **Python FastAPI** (`ecc:fastapi-patterns`) + **PostgreSQL** (`ecc:postgres-patterns`); OpenAPI contract first (`ecc:contract-first`, `ecc:api-design`) | Go (`ecc:golang-patterns`) for high-throughput or low-memory services; Django (`ecc:django-patterns`) when an admin panel is needed fast |
| **Workers and queues** | Long or retryable jobs, schedules, webhooks | The API's language + a queue (Postgres-based such as pg-boss, or Redis-based: `ecc:redis-patterns`) or managed (Cloudflare Queues, AWS SQS); jobs designed to be safely re-run (see retry safety) | Temporal or Inngest for multi-step workflows that need durability |
| **Data pipeline** | Ingest, transform, report | Python + SQL (dbt for transforms), Postgres or a warehouse, a scheduler (Airflow, Dagster or cron) | A stream processor (Kafka or Redpanda) only when there's true real-time need |
| **Integration, bot or automation** | Glue between SaaS tools, chat bots | A serverless function (Cloudflare Workers, Vercel Functions or AWS Lambda) + a small database; strict retry and backoff | n8n or Zapier when no custom logic is needed |
| **CLI or library** | Used by developers | The ecosystem's language; semantic versioning; docs with examples | — |

**Decision rules:**
- **Architecture:** a modular monolith first (`ecc:hexagonal-architecture` for clean boundaries); split into services only for a proven scaling or team reason.
- **Data:** Postgres by default.
- **Contract:** write the API contract before the implementation.
- **Deploys:** containers (`ecc:docker-patterns`) when the platform doesn't run the code directly.

## Tools by stage

| Stage | Use |
|:--|:--|
| 2 Architecture | `ecc:api-design`, `ecc:contract-first`, `ecc:backend-patterns`, `ecc:hexagonal-architecture`, `ecc:database-migrations`; data model and ADRs; SLOs and the infrastructure approach (`references/devops.md`) |
| 3 Design (compact) | API style guide (naming, errors, pagination, versioning); CLI help text; developer docs outline |
| 4 Platform | `ecc:docker-patterns`, infrastructure as code where chosen, secrets management, OpenTelemetry traces, structured logs, health endpoints |
| 5 Engineering | `ecc:orch-add-feature` with contract tests; `ecc:postgres-patterns`; a timeout on every external call; retries only where they're safe, and reconciliation for ambiguous writes (see the quality bar) |
| 6 QA | Contract tests against the OpenAPI spec, load tests at 2× the expected peak (`ecc:benchmark`), `ecc:security-review` (authn and authz, injection, SSRF, secrets), failure-injection tests for dependencies |

## Quality bar (stage 6 checks against it)

- **Contract:** every endpoint is in the OpenAPI or schema spec; breaking changes only in a new version.
- **Reliability:** a timeout on every external call; graceful shutdown; health and readiness checks.
- **Retry safety** (see the AWS Builders' Library article on making retries safe with idempotent APIs):
  - Retry automatically **only** reads, operations that are idempotent by design, and writes the downstream service **deduplicates** (it honours an idempotency key, or rejects duplicates by a unique business ID). Sending an idempotency key the other side ignores doesn't make a retry safe.
  - Retries are **bounded** (for example, 3 attempts), only on retryable errors (timeouts, connection errors, 429, 5xx, never 4xx validation errors), with **exponential backoff and jitter**.
  - **Ambiguous outcomes on non-idempotent writes** (a timeout after the request was sent): don't retry blindly. Record the attempt, then **reconcile**: look up the result with the downstream system (by your own reference or order number), and only create it again if it really doesn't exist. Alert when it can't be confirmed.
  - Inbound webhooks and queue jobs are processed **idempotently**: store processed event IDs and skip duplicates.
- **Performance:** p95 latency targets per endpoint (for example under 300ms), tested at 2× the expected peak.
- **Security:** least-privilege credentials; authorization checked on every request; input validated at the edge; rate limiting; audit logs for sensitive actions.
- **Data:** backward-compatible migrations (expand, then contract); backups and restore tests (stage 4); data retention rules.
- **Observability:** structured logs, metrics, traces, and an SLO per critical endpoint.

## Kickoff questions for systems (on top of the universal ones)

1. Who or what calls it: your own frontend, mobile apps, partners, the public, or other internal services?
2. The main operations: list the endpoints, jobs or commands, even roughly.
3. Expected load: requests per second or jobs per day, now and in a year? Spiky or steady?
4. Data: what's stored, how much, how sensitive (personal, financial, health), and for how long?
5. Consistency: is it acceptable for data to be briefly stale, or must every read be exact (money, inventory)?
6. Latency needs: real time (under 100ms), interactive (under 1s), or batch?
7. Which external systems does it depend on? What happens when they're down?
8. Authentication: API keys, OAuth, user sessions, mTLS? Multi-tenant?
9. Where must it run: a specific cloud, a region (data residency), on-premises, or anywhere?
10. Existing systems to integrate with or replace? Migration of existing data?
11. Compliance: GDPR, HIPAA, PCI, SOC 2, or audit requirements?
12. Who operates it after launch, and what uptime does the business need?
13. For each external system it writes to: does it support idempotency keys or reject duplicates? What should happen when a write times out and we don't know whether it succeeded?
