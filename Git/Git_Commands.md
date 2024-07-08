## Commands:
- `git fetch origin`: get most up-to-date origin branch of repository
  - `git fetch -p`: prune all unused branches and automatically set upstream ones for locally created branches
- `git status`: track staged/unstaged changes from local vs remote repository
- `git checkout -f <branch name>`: foreces a change to the specified brnach
  - `git checkout --"<file name>"`: pull master version of named file from repository
- `git pull`: pulls current branch from remote repository
- `git add`: stage files for commit
  - `.`: all files
  - `*.cpp`: all files with extension "cpp"
- `git commit -m "message"`: commit changes with specified message
- `git push`: push changes to remote repository
  - `git push --set-upstream origin dev/Luke`: set local branch to track remote repository branch
- `git stash`: save changes on local working branch so a pull does delete them
  - `git stash pop`: re-apply changes that were stashed
- `git branch <branch_name>`, `git checkout`, and `git push`: create new branch from current one, change to that branch, and push to repository
  - `git branch -d <branch name>`: delete named branch
- `git update-index --assume-unchanged <file>`: assume file has not changed (useful for logs) and stop tracking with `git status`
- Workflow for pulling in branch updates:
  - `git stash`
  - `git pull origin <branch name>`
  - `git stash apply`
- `git commit --amend --no-edit`: ammend the last commit without changing the message (when you forgot to add a file for example)
- `git reset --hard origin/branch-name`: overwrite local branch to match remote branch

## Conventional Commits:
- https://conventionalcommits.org/en/v1.0.0/#summary

## Reset Last Commit:
- `reset --soft HEAD~1`
- `git push -f`
