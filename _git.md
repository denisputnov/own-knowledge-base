### Git Knowledge Base
>Here you can see useful commands for Windows console, that I use in my work.

### git status
Show info about files in your repository. 
```
git status
```
### git pull
I suggest use this command every morning, if you are working on a project not alone. To be honest, the more often the better 

This command update files on your computer and download new and modified files from repository.
```
git pull
```
### git add
This command let you make changes to the index, that later will send to commit.


```
git add . - add to the index all files
```
```
git add FILENAME - add to the index direct file.

For example:
git add _markdown.md 
```

### git rm <i>or</i> git reset
This commands let you remove added files from the index.

``` 
git rm FILENAME1 FILENAME2 - optional - deletes specified files
``` 
```
git rm Documentation/\*.txt - deletes all .txt files from Documentation folder
```
```
git reset - clear all index
```
### git commit
Makes commit, if index isn't empty.
```
git commit -a - commit all new, modified and deleted files, automatically added them to the index
```
```
git commit -m "MESSAGE_TEXT" - commit files from index with message MESSAGE_TEXT

For example:
git commit -m "Update _git.md"
```
```
git commit FILENAME - commit file FILENAME and automatically added it to the index
```
### git push
These command let you send last commit to GitHub Cloud in your online repository.
```
git push
```
---
### git branch
Show you all branches, that you have.
```
git branch
```
### git checkout -b "BRANCH_NAME"
Create new branch with name BRANCH_NAME.
```
git checkout -b "BRANCH_NAME"
```
### git checkout BRANCH_NAME
```
git checkout BRANCH_NAME
```
## FAQ:

### How can I delete file from all github repository story?

```
> git filter-branch --force --index-filter "git rm --cached --ignore-unmatch FILENAME" --prune-empty --tag-name-filter cat -- --all

> git push origin --force --all
> git push origin --force --tags
```

That's all for now.

---

### Find me here:
* [Telegram](https://t.me/grnbows) </br>
* [Вконтакте](https://vk.com/grnbows) </br>
* [Instagram](https://www.instagram.com/grnbows) </br>
* [Twitter](https://twitter.com/grnbows) </br>

<i>With respect and love,</i></br> by grnbows
