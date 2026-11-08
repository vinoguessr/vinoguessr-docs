# ADR-0004: Move Terraform to the infrastructure repository

Status: Accepted / 2026-11-08

## Context

Terraform and the OpenTelemetry Collector configuration lived in `vinoguessr-api` under `Terraform/` and `Deploy/`. sauna-studio keeps its infrastructure code in `sauna-infrastructure`. Before bootstrapping the new Google Cloud project `vinoguessr`, we need to decide where to bootstrap it from.

## Decision

Move Terraform and its runbook to `vinoguessr-infrastructure`, and bootstrap the new project from that repository. DNS for the Cloudflare zone `vinoguessr.com` is managed there as well.

Building container images and rolling them out to Cloud Run stays in `vinoguessr-api`'s GitHub Actions. Workload Identity Federation trusts only runs from the `main` branch of `vinoguessr/vinoguessr-api`. Terraform ignores drift in the running image.

`terraform apply`, creating billed resources, and broad IAM grants run locally only after the owner's explicit approval. GitHub Actions never runs apply; PRs run only `terraform fmt -check`, `init -backend=false`, and `validate`.

## Alternatives

- Keep Terraform in the api repository: application and infrastructure changes would share PRs and CI, blurring the review focus.
- Move deploys to the infrastructure repository too: images are built from api commits, so keeping deploys in api makes it easier to trace a commit to its image.

## Consequences

Once this repository holds the Terraform, a follow-up PR removes `Terraform/`, `Deploy/cloud-run/`, the Terraform CI job, and the Terraform Dependabot entry from the api repository, tracked by an Issue. The api ruleset that requires the `terraform` check is updated first, so removing the job does not block merges. Infrastructure changes go through PRs in the infrastructure repository, and adding environment variables or secrets that the API uses is tracked with an Issue spanning both repositories.

## References

- https://github.com/vinoguessr/vinoguessr-infrastructure
- https://github.com/sauna-studio/sauna-infrastructure
