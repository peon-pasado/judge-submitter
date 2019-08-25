# judge-submitter
a submitter to online judges (only codeforces)

### install:

	- docker-compose up -d

### use:

	configure .env (see .sample-env)
		
```cpp
docker-compose run submitter python3 root/main.py -codeforces root/[filename:(example:33C.cpp)]
```
