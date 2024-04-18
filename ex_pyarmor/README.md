### 설치
```bash
$ poetry add pyarmor
```


## 1. 단일 파일 암호화

### a. 암호화
```bash
(python-ex-py3.11) D:\envs\public_repositories\python-ex\ex_pyarmor>pyarmor gen to_be_encrypted.py
INFO     Python 3.11.7
INFO     Pyarmor 8.5.2 (trial), 000000, non-profits
INFO     Platform windows.x86_64
INFO     search inputs ...
INFO     find script to_be_encrypted.py
INFO     find 1 top resources
INFO     start to generate runtime files
INFO     target platforms {'windows.amd64'}
INFO     write dist\pyarmor_runtime_000000\pyarmor_runtime.pyd
INFO     generate runtime files OK
INFO     start to obfuscate scripts
INFO     process resource "to_be_encrypted"
INFO     obfuscating file to_be_encrypted.py
INFO     write dist\to_be_encrypted.py
INFO     obfuscate scripts OK
```

### b. 실행
```bash
(python-ex-py3.11) D:\envs\public_repositories\python-ex\ex_pyarmor>python ./dist/to_be_encrypted.py
main logic executed
```

### c. 배포
- dist 디렉토리와 함께 배포해야 한다.
- 동일한 OS과 Python 버전 환경에서 난독화 해야한다.
- 배포 대상 PC에는 Pyarmor를 설치하지 않아도 된다. ( 하지 말아야 한다. )
