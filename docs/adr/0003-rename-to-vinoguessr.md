# ADR-0003: Rename BlindLog to VinoGuessr

Status: Accepted / 2026-11-08

## Context

The service was developed as BlindLog, with the domain `blindlog.me`, the Google Cloud project `blindlog`, and repositories under the personal account `zunda-pixel`. The iOS app already used the name VinoGuessr and the bundle ID `com.vinoguessr.app`. There are no users yet.

## Decision

Use VinoGuessr as the single service name and remove BlindLog from code and documentation.

- Move the repositories to the organization `vinoguessr` and rename them to `vinoguessr-api` / `vinoguessr-app` / `vinoguessr-web`.
- Use `vinoguessr.com` as the public domain (`api.vinoguessr.com` for the API, `support@vinoguessr.com` as the email sender). The passkey RP ID, Associated Domains, and the Keychain identifier (`com.vinoguessr.app.tokens`) follow it. ADR-0005 later sets the RP ID to `vinoguessr.com` itself rather than the API host.
- A Google Cloud project ID cannot be changed, so build a new project `vinoguessr` from scratch and delete the old project `blindlog` after the migration.
- Use `vinoguessr-api` / `vinoguessr-app` as the JWT issuer / audience.

## Alternatives

- Keep using the old project `blindlog`: BlindLog would remain in the project ID.
- Keep a redirect from the old domain: unnecessary without users.

## Consequences

Existing tokens, Keychain data, and passkeys become invalid. There are no users, so no migration path is provided. BlindLog remains in the git history, which is not rewritten.

## References

- https://github.com/vinoguessr/vinoguessr-api/pull/405
- https://github.com/vinoguessr/vinoguessr-app/pull/7
