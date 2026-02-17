# GitHub Actions Workflows

This directory contains the GitHub Actions workflows for the eic-spack repository.

## Workflows

### trigger-container-build.yml

This workflow automatically triggers a container build in the [eic/containers](https://github.com/eic/containers) repository when a pull request is opened or updated in this repository. This enables automatic testing of changes to eic-spack packages.

**How it works:**
- Triggers on pull request events (opened, synchronize, reopened)
- Gets the HEAD commit SHA from the pull request
- Calls the `build-push` workflow in the eic/containers repository via workflow_dispatch
- Passes the commit SHA as the `EICSPACK_VERSION` input parameter

**Requirements:**
- Requires a repository secret named `CONTAINERS_TRIGGER_TOKEN`
- The token must be a GitHub Personal Access Token (PAT) or GitHub App token with:
  - `repo` scope (to access the eic/containers repository)
  - `workflow` scope (to trigger workflow_dispatch)

**Setting up the secret:**
1. Create a Personal Access Token with `repo` and `workflow` scopes
2. Add it as a repository secret in Settings > Secrets and variables > Actions
3. Name it `CONTAINERS_TRIGGER_TOKEN`

**Note:** The workflow will silently skip if the secret is not configured, making it safe for forks.

### build_packages.yml

This workflow validates changes to package definitions by attempting to concretize modified packages using Spack.

### check-new-versions.yaml

This workflow checks for new versions of packages and creates pull requests when updates are available.

### pr-backport.yml

This workflow automatically creates backport pull requests when changes are merged to the main branch.
