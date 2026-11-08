# ADR-0005: Use vinoguessr.com as the passkey relying party ID

Status: Accepted / 2026-11-08

## Context

ADR-0003 moved the passkey relying party ID (RP ID) to `api.vinoguessr.com`, the host that serves the API. A passkey is bound to its RP ID, and a page can use a passkey only when the RP ID is its own host or a parent domain of it. With `api.vinoguessr.com`, a web client served at `vinoguessr.com` could never use the passkeys created in the app. Changing the RP ID later invalidates every passkey, and VinoGuessr has no users yet, so this is the cheapest moment to choose the final value.

The API verifies passkeys with swift-webauthn, which accepts exactly one origin. An iOS app reports its origin as `https://<RP ID>`.

## Decision

- The RP ID is `vinoguessr.com`, and the only allowed origin is `https://vinoguessr.com`. Both the iOS, iPadOS, and macOS app (which reports `https://vinoguessr.com`) and vinoguessr-web (served at `https://vinoguessr.com`) use it.
- The app's associated domain is `webcredentials:vinoguessr.com`.
- `https://vinoguessr.com/.well-known/apple-app-site-association` is served by the API, which already generates it from `APPLE_APP_ID`. The load balancer routes only that path on `vinoguessr.com` to the API backend; other paths on `vinoguessr.com` are not served until vinoguessr-web is deployed, and then go to its backend.
- The API's passkey playground (`public/`) is a local development tool. It keeps working on `localhost` with `RELYING_PARTY_ID=localhost`; on `api.vinoguessr.com` its origin does not match and it is not supported.

## Alternatives

- Keep `api.vinoguessr.com`: the web on `vinoguessr.com` could not share passkeys with the app, and moving the web onto the API host would mix the API and the web on one origin.
- Allow several origins (`https://vinoguessr.com` and `https://api.vinoguessr.com`): it needs a change to swift-webauthn and only serves the playground in production. Revisit it if another client needs a different origin, such as an Android app (`android:apk-key-hash:...`).
- Serve the association file from a Cloudflare Worker or from vinoguessr-web: it would create a second source for `APPLE_APP_ID`. Routing one path to the API keeps a single source.

## Consequences

Passkeys created for `api.vinoguessr.com` stop working; there are no users, so no migration is provided. The infrastructure serves `vinoguessr.com` through the same load balancer (certificate, DNS, and a host rule), and production sets `RELYING_PARTY_ID=vinoguessr.com` and `RELYING_PARTY_ORIGIN=https://vinoguessr.com`. The app changes its RP ID and associated domain.

## References

- https://www.w3.org/TR/webauthn-3/#relying-party-identifier
- https://developer.apple.com/documentation/xcode/supporting-associated-domains
- ADR-0003: [Rename BlindLog to VinoGuessr](0003-rename-to-vinoguessr.md)
