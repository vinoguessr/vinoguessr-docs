# Development

Issue dependencies and acceptance criteria → plan → Coding and Review Agents in parallel (plus a Security Review for authentication, personal data, participation authorization, scoring, and Apple Wallet pass signing) → real builds and tests → fix findings and add regression tests → re-review → GitHub Actions passing → Codex review (Claude Code substitutes only at the usage limit) → merge.

The rules live in AGENTS.md in [vinoguessr/.github](https://github.com/vinoguessr/.github). The organization Project tracks cross-repository planning and progress. Results of applying GitHub settings are recorded in `docs/setup-report.md` in `.github`. Never record a tool as used when it was unavailable.

Code and documentation are written in English; Issue and PR bodies are written in Japanese.
