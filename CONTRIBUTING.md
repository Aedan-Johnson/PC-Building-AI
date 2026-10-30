# Workflow

## The golden rule
Never push directly to `main`. Every change goes through a branch and a pull request.

## Workflow
```bash
git checkout main
git pull
git checkout -b aedan/add-cpus        # name/what-you-are-doing
# ...make changes...
git add .
git commit -m "Add first 10 CPUs"
git push -u origin aedan/add-cpus
```
Then open a pull request on GitHub, check the diff and the template checklist, and merge it.

## Habits
1. **Check in**, 15 to 30 minutes: what's done, what's stuck.
2. **Stuck for over an hour?** Write down what's wrong in the process journal, then ask the teacher or check the resources in the plan.
3. **Save everything** (loss charts, example chats, test results) in `results/`. That's the presentation material.
