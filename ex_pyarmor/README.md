## 0. 설치
```bash
$ poetry add pyarmor
```


## 1. 단일 파일 암호화

### a. 암호화
- 디폴터 옵션으로 /dist 디렉토리 하위에 난독화된 파일이 저장된다.
```cmd
(python-ex-py3.11) D:\envs\public_repositories\python-ex\ex_pyarmor>pyarmor gen single_file.py
INFO     Python 3.11.7
INFO     Pyarmor 8.5.2 (trial), 000000, non-profits
INFO     Platform windows.x86_64
INFO     search inputs ...
INFO     find script single_file.py
INFO     find 1 top resources
INFO     start to generate runtime files
INFO     target platforms {'windows.amd64'}
INFO     write dist\pyarmor_runtime_000000\pyarmor_runtime.pyd
INFO     generate runtime files OK
INFO     start to obfuscate scripts
INFO     process resource "single_file"
INFO     obfuscating file single_file.py
INFO     write dist\single_file.py
INFO     obfuscate scripts OK
```

### b. 실행
- 정상적으로 실행됨을 볼수 있다.
```cmd
(python-ex-py3.11) D:\envs\public_repositories\python-ex\ex_pyarmor>python ./dist/single_file.py
main logic executed
```

### c. 배포
- dist 디렉토리와 함께 배포해야 한다.
- 동일한 OS과 Python 버전 환경에서 난독화 해야한다.
- 배포 대상 PC에는 Pyarmor를 설치하지 않아도 된다. ( 하지 말아야 한다. )

<br>

## 2. 단일 패키지 암호화

### a. 암호화
- O 옵션으로 암호화 결과 디렉토리를 변경할 수 있다.
```cmd
(python-ex-py3.11) D:\envs\public_repositories\python-ex\ex_pyarmor>pyarmor gen -O dist2 single_package
INFO     Python 3.11.7
INFO     Pyarmor 8.5.2 (trial), 000000, non-profits
INFO     Platform windows.x86_64
INFO     search inputs ...
INFO     find package at single_package
INFO     find 1 top resources
INFO     start to generate runtime files
INFO     target platforms {'windows.amd64'}
INFO     write dist2\pyarmor_runtime_000000\pyarmor_runtime.pyd
INFO     generate runtime files OK
INFO     start to obfuscate scripts
INFO     process resource "single_package"
INFO     obfuscating file __init__.py
INFO     write dist2\single_package\__init__.py
INFO     obfuscate scripts OK
```
- 하위 서브 패키지가 있다면 `-r` 옵션을 주면 재귀적으로 암호화 한다.
```cmd
$ pyarmor gen -O dist2 -r src/mypkg
```

- `-e` 옵션을 사용하면 스크립트 만료 날짜를 설정할 수 있다.
```cmd
$ pyarmor gen -O dist4 -e 30 foo.py
```

- `-b` 옵션을 사용하면 특정 이더넷 주소를 가진 PC에서만 실행되게 할 수 있다.
```cmd
$ pyarmor gen -O dist5 -b 00:16:3e:35:19:3d foo.py
```


### b. 실행

```cmd
(python-ex-py3.11) D:\envs\public_repositories\python-ex\ex_pyarmor>cd dist2

(python-ex-py3.11) D:\envs\public_repositories\python-ex\ex_pyarmor\dist2>python -c "from single_package import SinglePackage; SinglePackage().test()"
<class 'single_package.SinglePackage'>.test executed
```