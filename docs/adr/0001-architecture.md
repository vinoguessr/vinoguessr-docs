# ADR-0001: The API and PostgreSQL are the source of truth for business data

Status: Accepted / 2026-11-08

## Context

VinoGuessr is a service for blind wine tasting: people create events, set questions, answer them, get scored, and build a season rating. The iOS, iPadOS, and macOS app and the web work on the same data, and event tickets are delivered as Apple Wallet passes. There are no users yet, so breaking changes that align the system with its intended design are acceptable.

## Decision

The Swift 6 / Hummingbird API and PostgreSQL are the source of truth for business data. PostgreSQL runs on Neon and is accessed through PostgresNIO (postgres-kit / hummingbird-postgres). `Database/schema.sql` is the source of truth for the schema, managed with forward-only Atlas migrations. The data model is immutable as a rule: changes are recorded by inserting new rows rather than updating existing ones.

OpenAPI is the contract, and the server interface is generated with Swift OpenAPI Generator. Generated code is never edited by hand.

Sign-in uses passkeys (WebAuthn) and email one-time codes, and the API issues JWT access tokens and refresh tokens. Passkey challenges, one-time codes, rate limits, and short-lived caches live in Valkey. Valkey is never the source of truth and is limited to data whose loss does not corrupt business data.

Images use Cloudflare Images, and email uses Cloudflare Email Service. The API runs on Google Cloud Run and is published through Cloudflare proxied DNS and a Google external HTTPS Load Balancer. OpenTelemetry data goes to Google Cloud through a Collector sidecar on Cloud Run.

Clients are split into SwiftUI (iOS, iPadOS, and macOS 27.0 or later) and a Swift / Hummingbird web. Both treat the API as the source of truth and never finalize scores or participation from client-side values.

## Alternatives

- Cloud SQL: sauna-studio uses Cloud SQL, but VinoGuessr already runs on Neon, and moving before there are any users brings little benefit.
- Valkey as the source of truth: its durability and consistency guarantees are weaker than PostgreSQL's.
- SvelteKit for the web: sauna-studio uses SvelteKit, but the VinoGuessr web is still a template, and we keep it in Swift alongside the API and the app.

## Consequences

Nothing other than the API writes to the business database directly. Every schema change comes with a migration and integration tests. OpenTelemetry never records names, email addresses, tokens, or passkey challenges.

## References

- https://github.com/vinoguessr/vinoguessr-api
- https://github.com/hummingbird-project/hummingbird
- https://github.com/vapor/postgres-nio
- https://atlasgo.io/docs
