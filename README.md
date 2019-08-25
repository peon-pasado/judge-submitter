# judge-submitter
a submitter to online judges (only codeforces)

### install:

	- docker-compose up -d
	- docker-compose run submitter bash
	- cd code

### use:

	configure .env (see .sample-env)
		
```cpp
python3 main.py -codeforces [problem-file (example: 33C.cpp)]
```
