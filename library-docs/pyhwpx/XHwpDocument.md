## `pyhwpx.core.XHwpDocument`

한글과컴퓨터 문서(HWP)의 COM 객체를 래핑한 클래스입니다.

이 클래스는 HwpDocument COM 객체와 상호작용하기 위한 속성과 메서드를 제공합니다. 문서 속성, 데이터 조작 기능, 상태 제어 등 다양한 기능을 제공하며, 한글과컴퓨터의 문서 관리 시스템을 파이썬스럽게 다룰 수 있도록 설계되었습니다.

속성

Application: 문서와 연결된 어플리케이션 객체 CLSID: 문서의 클래스 ID DocumentID: 문서의 고유 식별자 EditMode: 현재 문서의 편집 모드 Format: 문서의 형식 FullName: 문서의 전체 경로를 문자열로 반환. 저장되지 않은 문서는 빈 문자열 반환 Modified: 문서의 수정 여부를 나타냄 Path: 문서가 저장된 폴더 경로 XHwpCharacterShape: 문서의 글자모양 설정에 접근 XHwpDocumentInfo: 문서의 상세 정보에 접근 XHwpFind: 텍스트 찾기 기능에 접근 XHwpFormCheckButtons: 체크박스 양식 요소에 접근 XHwpFormComboBoxs: 콤보박스 양식 요소에 접근 XHwpFormEdits: 편집 양식 요소에 접근 XHwpFormPushButtons: 버튼 양식 요소에 접근 XHwpFormRadioButtons: 라디오버튼 양식 요소에 접근 XHwpParagraphShape: 문단 모양 설정에 접근 XHwpPrint: 문서 인쇄 제어에 접근 XHwpRange: 문서 내 범위 설정에 접근 XHwpSelection: 현재 선택된 텍스트나 개체에 접근 XHwpSendMail: 메일 보내기 기능에 접근 XHwpSummaryInfo: 문서 요약 정보에 접근

### `FullName` <small><code>property</code></small>

문서의 전체경로 문자열. 저장하지 않은 빈 문서인 경우에는 빈 문자열 ''