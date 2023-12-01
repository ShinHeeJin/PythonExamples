import base64

# 사용자 이름 & 비밀번호
username = "stanleyjobson"
password = "swordfish"

# "username:password"
credentials = f"{username}:{password}"

# 바이트로 변환한 후 Base64 인코딩
encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode()

print("Encoded Credentials:", encoded_credentials)  # Encoded Credentials: c3RhbmxleWpvYnNvbjpzd29yZGZpc2g=

"""
HTTP Basic Authentication
클라이언트가 서버로 요청을 보낼 때, 이 Authorization 헤더를 함께 보내면
서버는 이를 확인하고 해당 사용자의 권한을 부여.
"""
