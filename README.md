# judge-submitter
a submitter to online judges (only codeforces)

### install:

	- docker-compose up -d
	- docker-compose run submitter bash
	- cd code

### use:

	configure .env (see .sample-env)
		
```cpp	
python3 code_submit.py [problem-id] [problem-file]
```
