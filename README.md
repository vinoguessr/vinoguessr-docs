# vinoguessr-docs
VinoGuessr architecture, ADRs, and development documentation

<!-- vinoguessr-foundation -->
## Scope

Architecture, ADRs, and the GitHub wiki index.

## Architecture

`.github` is the source of truth for the shared rules, and each product repository is the source of truth for its code. Record design changes as ADRs with context, decision, alternatives, and consequences.

## Verification

Verify Markdown links, including that they still work after export to the wiki, with `python3 -m unittest discover -s scripts`. Check the actual content on GitHub before syncing to the wiki.

Follow [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md): satisfy the Issue's dependencies, then implement with an independent Review Agent running in parallel. Shared rules source: [vinoguessr/.github@01fd9c61bce2](https://github.com/vinoguessr/.github/tree/01fd9c61bce2139beb8ea173339d45c02d49b69f).

Design documents: [Architecture ADR](docs/adr/0001-architecture.md) / [Wiki source](docs/wiki/Home.md).
