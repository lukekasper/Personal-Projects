touch test.html: in terminal window creates new file


Git commands:
- git clone <url>: from command window, clones repository to current directory
- git add "filename": add files to be committed
- git status: track file changes staged for commit or check current state of repository
- git commit -m "message": commit added files to repository
- git push: push changes to remote repository
- git commit -am "message": shorthand to add and commit all changes
- git pull: pulls most recent changes form github to current repository
- git log: gives a description of recent commits
- git reset -- hard <commit> OR origin/master: reverts repository back to previous state
- git branch: shows structure of repository
- git checkout -f "name of branch"
    - use "-b" to create a new branch
- git merge <name of branch to merge into current branch>: merge branches
- fork: can make a copy of repository into own personal github account
- pull request: make a request to have your code pulled into a remote repository



Merge Conflicts:
<<<< HEAD (current branch)
...
=====
...
>>>>> <conflicting commit>

- to resolve conflicts, remove extra characters and select desired combination of two versions


GitHub Pages:
- create website to test out html/css/java code for other people to see
- to set up, create new repository: username.github.io
    - can scroll down on github website to Github Pages and click on link "your site is ready to be published at: "
