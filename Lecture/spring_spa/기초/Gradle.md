## 의존성 추가
- python에는 pip, java는 mavenCentral, jcenter
- 의존성 추가 하기(intellij)
	1. Maven Repository에서 원하는 라이브러리 찾기
	2. build.gradle에 원하는 프로젝트 파일 넣기
	3. dependencies 옆에 Run 클릭
	4. 우측 Gradle탭의 새로고침
	5. 프로젝트 추가 확인

	

## 배포 파일 build 하기
- intellij에서 jar 파일 생성
	- Gradle 탭 -> Tasks > build > build 더블클릭
	- lib에 jar 생성

- jar 실행
```
java -jar JAR파일명.jar
```
