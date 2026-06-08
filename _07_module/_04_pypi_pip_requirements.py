# PyPI (Python Package Index)
# - Python 패키지를 올리고 내려 받는 공식 저장소

# pip : PyPI에서 패키지를 검색, 설치, 삭제하는 도구

# requirements.txt : 프로젝트에 필요한 패키지 목록을 적어두는 파일
# -> 해당 패키지 목록을 이용해서 일괄 설치 가능
# == 의존성 명세 파일

# requirements.txt 예시 내용
sample_requirements = """
# 웹 요청 라이브러리
requests==2.32.3

# 환경변수 파일(.env) 로딩
python-dotenv>=1.0.1

# 테스트 도구
pytest~=8.3.0
"""


pip_commands = [
    "python -m venv .venv",
    ".venv\\Scripts\\activate", # windows
    "source .venv/bin/activate", # mac, lnux
    "python -m pip --version",
    "python -m pip install requests", # requests 패키지 설치
    "python -m pip show requests", # 설치된 request 패키지 정보 출력
    "python -m pip freeze > requirements.txt", # 현재 가상 환경에 설치된 패키지 목록을 requirements.txt 파일로 저장
    "python -m pip install -r requirements.txt", # requirements.txt에 적힌 패키지를 한 번에 설치
    "python -m pip uninstall requests",
]


# 필수 패키지 목록
REQUIRED_PACKAGES = {
    "requests": "requests",
    "colorama": "colorama",
    "python-dotenv": "python-dotenv"
}