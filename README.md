# Prism 베타 다운로드

논문 읽기·AI 번역·질문·로컬 노트를 위한 데스크톱 앱입니다.

## 최신 버전: 0.2.0-beta.7

[Windows x64 설치 EXE 다운로드](https://github.com/help-me-prism/prism-releases/releases/download/v0.2.0-beta.7/Prism-0.2.0-beta.7-Windows-x64.exe)

SHA-256: `309f3b63b4e2a576d955eaf1458c87de9ba9ffe6c68a035337be99226c409edb`

[macOS Apple Silicon DMG 다운로드](https://github.com/help-me-prism/prism-releases/releases/download/v0.2.0-beta.7/Prism-0.2.0-beta.7-macOS-arm64.dmg)

SHA-256: `5bf4b0ecdbbb75d406ca9cce58872f833818a5c7a2349aa550745f07f3c19298`

이번 beta.7은 Windows x64와 macOS Apple Silicon(arm64) 설치 파일을 제공합니다. Intel Mac용 파일은 포함하지 않습니다. 이전 버전과 전체 배포 파일은 [Releases](https://github.com/help-me-prism/prism-releases/releases)에서 확인할 수 있습니다.

## 변경 내용

- 기본 꺼짐인 선택형 사용 통계를 추가했습니다. 첫 안내 또는 설정 → **사용 통계**에서 참여 여부를 정하고 언제든 끌 수 있습니다.
- 참여한 설치의 최초 실행, 한국 날짜별 실행 수, 읽기 창에서 열린 논문 횟수와 설치 안에서 중복을 뺀 논문 수를 개발팀만 확인합니다. 논문 제목·본문·경로·대화는 보내지 않습니다.
- 오프라인에서는 집계를 보관하고 다시 연결되면 재전송하며, 같은 집계를 중복으로 더하지 않습니다.
- 문장·수식·표·캡처 태그만 넣어도 채팅을 전송할 수 있습니다.
- 메인 화면에 PDF를 드래그하면 기존 논문 추가 과정으로 가져옵니다.
- 업데이트 확인과 문제 신고 버튼을 앱 테마에 맞췄습니다.
- 설정의 버전 표시를 빠르게 세 번 누르면 작은 제작자 인사가 나타납니다.
- Windows 설치 위치와 바탕화면 바로가기를 설치 과정에서 선택할 수 있습니다.
- Gemini 연결을 제거하고 기존 Gemini 대화는 읽을 수 있도록 보존했습니다.

## 설치

Windows: EXE를 실행합니다. 기본 설치 위치는 `%LOCALAPPDATA%\Programs\Prism`이며 바탕화면 바로가기를 선택할 수 있습니다. 설치가 끝난 뒤 다운로드한 EXE는 삭제해도 됩니다. 이번 베타는 코드 서명이 없어 Windows 경고가 나타날 수 있습니다. SmartScreen 화면이 나타나면 [Windows 설치 안내](docs/windows-install.md)를 참고하세요.

macOS Apple Silicon: DMG를 열고 Prism을 Applications로 복사합니다. 이번 베타는 임시 서명이며 Apple 공증을 받지 않았습니다. 설치 또는 첫 실행이 차단되면 출처를 확인한 뒤 시스템 설정 → 개인정보 보호 및 보안 → 그래도 열기에서 해당 앱을 허용하세요. [Apple 공식 안내](https://support.apple.com/102445)

설정·대화는 사용자 프로필, 논문·노트는 선택한 보관함에 저장됩니다. 앱을 업데이트하거나 제거해도 사용자 데이터와 기존 보관함은 자동으로 삭제되지 않습니다.

## 사용 통계

beta.7부터 기본 꺼짐인 선택형 사용 통계를 제공합니다. 참여하면 실행 날짜와 열린 논문 수를 개발팀만 확인하며, 논문 제목·본문·대화는 보내지 않습니다. [수집 항목·보관·참여 해제 안내](docs/usage-privacy.md)를 확인하세요. 참여하지 않은 설치와 이전 버전의 사용량은 집계하지 않습니다.

## 문제 신고

앱 상단의 **문제 신고**를 사용하세요. GitHub 로그인 없이 접수하며 전송 내용을 확인하고 동의한 정보만 보냅니다. 연구 내용·연락처·스크린샷을 이 공개 저장소에 올리지 마세요. 문의: ysjsprism@gmail.com.

신고 본문·이메일·선택 첨부는 비공개 GitHub 저장소에서 담당자가 확인하며 담당자가 삭제할 때까지 보관합니다. Cloudflare 접수 서버의 사본은 신고·연락처 180일, 이미지 30일 후 삭제합니다. 삭제 요청: ysjsprism@gmail.com. 개인 보관함 전체·대화·노트·인증정보는 자동 첨부하지 않습니다. 자동 업데이트 설치 없이 새 버전 알림과 수동 교체 설치를 제공합니다.
