import os

reserved_branches = ['master', 'develop']
current_branch_symbol = '*'
branches_to_delete = []

branches = os.popen('git branch').read().split('\n')
for b in branches:
  branch = b.strip()
  if not len(branch):
    continue
  if current_branch_symbol in branch:
    continue
  if branch in reserved_branches:
    continue
  branches_to_delete.append(branch)
  
print('Branches to delete:', branches_to_delete)

for branch in branches_to_delete:
  os.system('git branch -D {0}'.format(branch))

print('New branches state:', os.popen('git branch').read(), sep='\n')
