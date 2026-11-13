# Undo the last commit but keep the changes staged (soft reset).
git reset --soft HEAD~1

# Undo the last commit and unstage the changes (mixed reset, default).
git reset HEAD~1

# Undo the last commit and discard the changes entirely (hard reset).
# DANGER: this deletes the changes. Only use if you're sure.
git reset --hard HEAD~1
