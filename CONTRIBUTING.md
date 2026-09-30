# How We Work Together

## The golden rule
Never push directly to `main`. Every change goes through a branch and a pull request.

## Workflow
```bash
git checkout main
git pull
git checkout -b yunior/add-cpus        # name/what-you-are-doing
# ...make changes...
git add .
git commit -m "Add first 10 CPUs"
git push -u origin yunior/add-cpus
```
Then open a pull request on GitHub and request a review from the other person. Merge only after they approve.

## Habits
1. **Check in every Monday**, 15 to 30 minutes: what's done, what's stuck.
2. **Stuck for over an hour?** Hop on VS Code Live Share and solve it together.
3. **Run `pytest` before opening a pull request.**
4. **Save everything** (loss charts, example chats, test results) in `results/`. That's our presentation material.
