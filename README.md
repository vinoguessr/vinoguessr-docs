# vinoguessr-docs
VinoGuessr architecture, ADRs, and development documentation

<!-- vinoguessr-foundation -->
## Scope

Architecture, ADRs, and the GitHub wiki index.

## Architecture

`.github` is the source of truth for the shared rules, and each product repository is the source of truth for its code. Record design changes as ADRs with context, decision, alternatives, and consequences.

## Verification

Verify Markdown links, including that they still work after export to the wiki, with `python3 -m unittest discover -s scripts`. Check the actual content on GitHub before syncing to the wiki.

Follow [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md): satisfy the Issue's dependencies, then implement with an independent Review Agent running in parallel. Shared rules source: [vinoguessr/.github@38adaa6afdfb](https://github.com/vinoguessr/.github/tree/38adaa6afdfb7df020feb2a7ff93a6ddf1d79af8).

Design documents: [Architecture ADR](docs/adr/0001-architecture.md) / [Wiki source](docs/wiki/Home.md).
