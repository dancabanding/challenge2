Instructions to test:
- Create an AWS EC2 Linux Instance.
- SSH to the instance and execute the commands: 
- sudo yum install python3 git
- git clone https://github.com/dancabanding/challenge2.git
- sudo pip3 install pipenv
- cd challenge2
- pipenv install
- python3 get_metadata.py
