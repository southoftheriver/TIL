
### IntelliJ 단축키
- ⌘ + n 		: 새로 생성(경로, 파일, 패키지 등등)
- ⌃ + ⇧ + r 	: 실행환경(구성편집) 실행
- ⌃ + r		: 이전 실행환경 실행
- ⌘ + ⇧ + j 	: 문자열 합치기(라인단위)

- ⌘ + p		: 매개변수 타입 확인
- ⌥ + space 	: 오브젝트의 내부구현보기
- fn + f1		: 오브젝트의 javadoc보기

- ⌘ + [ or ] 	:  포커스위치 이전, 이후 위치로 이동(파일이동가능)
- ⌘ + ⇧ + [ or ]: 이전, 이후 파일로 이동
- fn + f2		: 에러가 있는 위치로 포커스 이동

- ⌘ + ⇧ + r 	: 모든 프로젝트의 텍스트 교체
- ⌘ + ⇧ + f	: 모든 프로젝트의 텍스트 검색
- ⌘ + ⇧ + o 	: 파일 검색(패키지포함가능)
- ⌘ + ⌥ + o 	: 메서드 검색
- ⌘ + ⇧ + a	: 액션 검색(전체 설정검색)
- ⌘ + e		: 최근 파일기록 
- ⌘ + ⇧ + e	: 최근 수정파일기록

### 자동완성
- ⌃ + space 	: 자동완성(가능한 모든 경우 출력)
- ⌃ + ⇧ + space: 스마트 자동완성(문맥에 더 적합한 경우 출력)
- ⌃ + space + space : 스태틱 메서드 자동완성
- ⌘ + n		: 생성자, 게터, 세터 등 메서드 선언부 자동 완성
- ⌃ + I		: 상속, 구현시 구현할 메서드 자동 완성


### 라이브 템플릿 (주로 한자리만 따서 사용)
- ⌘ + j		: 문맥에 맞는 라이브템플릿
- 라이브 템플릿 설정에서 사용자화 할 수 있다
- psvm 		: main 메소드 선언 
- sout			: println
- souf			: printf 
- ifn			: if( x == null) 

### 리팩토링
- ⌥ + ⌘ + v 	: 선택된 범위의 값 변수로 추출
- ⌥ + ⌘ + p 	: 선택된 범위의 값 인수로 추출 
- ⌥ + ⌘ + m	: 선택된 범위의 값 메서드로 추출
- fn + f6		: 내부클래스를 외부, 독립클래스로 추출
- ⇧ + fn + f6	: 선택된 텍스트 모두 바꾸기
- ⌘ +⇧ + fn + f6: 같은 식별자의 타입 바꾸기
- ⌃ + ⌥ + o		: import문 최적화
	- 액션 검색으로 optimize import on 을 검색해서 자동으로 설정가능
- ⌘ + ⌥ + l		: 코드 정렬

### 디버깅
- ⌃ + ⇧ + d		: 디버깅 시작
- ⌥ + ⌘ + r 		: 디버깅 재개
- ⌘ + fn + f8		: 중단점 설정
- step over 		: 한 줄만 실행
- step into		: 메서드의 내부구현으로 포커스 이동
- step out		: 내부구현 밖으로 포커스 이동
- Conditional break : 설정 if문이 참일 때만 멈추도록 중단점을 설정(중단점 우클릭)
- Evaluate expression : 중단된 상태에서 코드를 작성해서 값을 확인(한번만 확인)
- New watch 	: 중단될 때마다 작성된 값을 확인(지속적으로 확인)
 
### Git(⌘+9)
- Local Changes 	: 변경된 파일
- ⌘ + d		: 변경된 사항 확인(git Diff)
- ⌃ + v		: git 관련 작업표시 (commit, push, branch…..)
- 새 프로젝트 레포지토리 생성 : Share GitHub -> github로그인, 입력후 확인