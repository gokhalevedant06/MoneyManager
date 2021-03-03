# MoneyManager
A Money management software for today's youth

---
## Steps for installation of the project in you device

### Prerequisites
- Any IDE supporting python 
- [Git CLI](https://www.atlassian.com/git/tutorials/install-git)
- [Python 3](https://www.python.org/downloads/)
- [How to create Virtual Environment](https://docs.python.org/3/library/venv.html)

---
## Installation
- Navigate yourelf to the master Branch
![Master Branch](https://github.com/Mitrajeet-Golsangi/MoneyManager/blob/master/Git%20README/Picture1.png?raw=true)
- Copy the url of the repository
- ![Repository URL](https://github.com/Mitrajeet-Golsangi/MoneyManager/blob/master/Git%20README/Picture2.png?raw=true)
- Go to your preffered folder location
- Create a folder for the project
- Start your command prompt and navigate yourself to the folder we just created above in the command prompt
- Type the following command in your command prompt to initialize the git repository and copy the code from this remote repository
```git
  git clone https://github.com/Mitrajeet-Golsangi/MoneyManager.git
```
- Your code will be copied to you desired folder
- Now run the following commands in your command prompt
```
  virtualenv env
  env\Scripts\activate.bat
  cd MoneyManager
  pip install django
  pip install psycopg2
```
- Now you installation is completed and the code should run smoothly
---
## Setting up the git repository
- Run the following commands in you command prompt
```
  git init
  git add .
  git commit -m "Message for commit must be descriptive"
  git remote add origin https://github.com/Mitrajeet-Golsangi/MoneyManager.git
```
- These commands will set up your git repository and the
```
  git add .
  git commit -m "message"
```
must be repeated for every time you want to commit something in you git repository
- Now the Remote has branches in name of every participant. _**Thus commit only to the branch which has you name**_ using 
```
  git push -u origin your_name
```
- replace your_name with:
  - vedant
  - ashutosh
  - kaushal
  - aayush
---
