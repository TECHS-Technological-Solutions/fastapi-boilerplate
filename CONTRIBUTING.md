# Contributing Guide

### Pre-Commit

Commits must be executed in the project's base directory - This is so that `pre-commit` works properly.
No solution to run `pipenv` that is inside the `src` directory along with `pre-commit` has been found yet, so we will do a compromise for now.

#### Commits

Commit messages must follow this specific format:
`<descriptor>: <message>`

Descriptors are: `feature`, `fix`, `chore`, etc.

Examples:
- `feature: added a good feature`
- `fix: updated some feature`

#### Branches

Branch names must follow this format:
`<descriptor>/<ticket_id>/<ticket_description>`

Descriptors are the same as in commits

Examples:
- `feature/TICKET-1/implement-this-feature`
- `fix/TICKET-2/remove-this-bug`

#### Merging

*IMPORTANT: DO NOT merge directly into the main/develop branches unless explicitly directed to do so by the project lead*

All branches should follow this merging flow:

1. Push branch to host (Github/Gitlab)
2. Create a Pull/Merge request (`your branch [source branch]` -> `develop/master [target branch]`)
3. Request for a review on your newly created PR/MR
4. Once your PR/MR is accepted and if you have permission to merge your branch, simply merge.
4.1 If you do not have permissions, you will most likely have to wait for your lead to merge your branch

#### Python Specific Notes

- When adding a new package with Pipenv, please update the `Pipenv` file with the specific version of the package you installed. Please don't leave it to be `*` in the `Pipenv` file.
