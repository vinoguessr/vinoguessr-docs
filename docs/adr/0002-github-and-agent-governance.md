# ADR-0002: Cross-repository GitHub management and Codex review

Status: Accepted / 2026-11-08

## Context

VinoGuessr was developed in three repositories (api, app, web) under a personal account. With the rename, we move to the same repository structure and development process as sauna-studio. There is a single owner, and AI agents do the implementation and review. Codex can review PRs on GitHub automatically, but its usage limit (tokens) sometimes runs out.

## Decision

The GitHub organization `vinoguessr` holds six public repositories: `vinoguessr-api`, `vinoguessr-app`, `vinoguessr-web`, `vinoguessr-infrastructure`, `vinoguessr-docs`, and `.github`. An organization Project tracks cross-repository planning and progress with Status, Priority, Phase, and Area fields.

`.github` is the source of truth for the shared rules. AGENTS.md, CLAUDE.md, CODEOWNERS, and CI are not inherited from the organization, so each repository carries an explicit copy that is updated through follow-up PRs when the shared rules change. Shared workflows are called by a commit SHA retained in the default branch history.

Changes go through `codex/*` branches and PRs, and `main` is protected by a ruleset: PR required, required CI passing, threads resolved, no force pushes or deletion, squash merge only. With a single owner, the required approval count is 0, and review results are recorded in the PR.

PRs are reviewed by GitHub Codex and merged once there are no findings and the required CI has passed. Only when Codex cannot review because of its usage limit, a Claude Code independent review substitutes (the `reviewer` agent in a context separate from the implementer, plus `security-reviewer` when needed), and the PR records the evidence of the limit, the reviewed commit, and the findings and fixes. Other failures (no response, missing integration, failed run) do not qualify.

Code and documentation are written in English; Issue and PR bodies are written in Japanese.

## Alternatives

- Codex only, as in sauna-studio: every PR would stall whenever the usage limit runs out.
- Substituting Claude Code for any Codex failure: it would make it easy to miss a broken integration.
- Admin app, admin web, and automation repositories: there are no plans for admin features or integration bots yet.

## Consequences

Each PR merges only after an independent Review Agent during implementation, real builds and tests, and a Codex review (or the Claude Code substitute). Claude Code loads AGENTS.md through CLAUDE.md and follows the same rules.

## References

- https://github.com/vinoguessr/.github
- https://github.com/sauna-studio/.github/blob/main/docs/adr/0003-github-and-agent-governance.md
- https://github.com/sauna-studio/.github/blob/main/docs/adr/0005-review-and-workflow-references.md
