# django-table
## Introduction
다녀온 레스토랑을 등록하고 별점을 매기는 웹앱 프로그램입니다.

## Instruction
이 Instruction은 MacOS를 기준으로 작성되었습니다.

1. 원하는 디렉터리에서 아래 명령어를 통해 저장소의 데이터들을 해당 디렉터리로 가져옵니다.
```bash
git clone https://github.com/yjinjo/django-table.git
```

2. 가상환경을 통해서 이 프로젝트를 관리하기 때문에 우선 로컬 전체에 `virtualenv`를 설치합니다.
```bash
pip install virtualenv
```

3. 이제 해당 디렉터리로 이동하여 가상환경 디렉터리를 만듭니다. 
```bash
virtualenv -p python3 venv
```
이제 해당 디렉터리에 venv 디렉터리가 생겼을 것입니다.

4. 가상환경을 activate 시킵니다.
```bash
source venv/bin/activate
```

5. requirements.txt에 있는 모듈들을 아래 명령어를 통해 다운로드 받습니다.
```bash
pip install -r requirements.txt
```
이제 기본적인 setting은 끝났습니다.

## 참고사항
- 총 8개의 branch들로 이루어져있으며 ch01-initialization 부터 시작하여 ch08-add-functions 까지 있습니다.
- 각각의 branch들은 똑같은 번호의 issues들과 matching 되어있습니다.
  - 예를 들어 ch06-crud로 checkout 했다면, #6 번째 issue인 Django CRUD를 참고하시면 됩니다.
    - [Django CRUD #6 | Issue](https://github.com/yjinjo/django-table/issues/6)
  - Closed된 Issue들은 아래 링크에서 확인할 수 있습니다.
    - [Closed Issues](https://github.com/yjinjo/django-table/issues?q=is%3Aissue+is%3Aclosed)
