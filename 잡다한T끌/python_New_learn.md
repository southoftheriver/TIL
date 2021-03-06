- ## 2진수, 8진수, 16진수 변환 및 출력
    - int('변환값 문자열', 진법) / int('B',16) 
    - f'2진법:{10:b}, 8진법{20:o}, 16진법{30:X}'

- ## EOFError
    - 입력 도중 파일이 끝나면 에러가 발생한다



- ## 비트 연산자
    - a = 60, b =13 일때
        - a = 0011 1100
        - b = 0000 1101
    
    - a & b = 12, 0000 1100
    - a | b = 61, 0011 1101
    - a ^ b = 49, 0011 0001
    - ~a = -61, 1100 0011
    - a << 2 = 240 , 1111 0000 (변수 값을 왼쪽으로 지정된 비트수(2) 만큼 이동)
    - a >> 2 = 15 , 0000 1111 (오른쪽으로 이동)

    - 1 or 2 -> 1을 반환
    - 1 and 2 -> 2를 반환
    


- ## python Garbage Collection
    - reference counting과 garbage collection을 이용해서 메모리를 할당,해제하는 장치이다
    
    - reference cycles 
        - 참조 순환의 발생으로 참조횟수가 절대 0이 되지 않는 오류

    - 전통적 GC
        - 스택에 저장된 상수, 전역 정보, 내장 데이터들로 부터 검색해서 찾아진 '살아있는'데이터 빼고는 전부 메모리를 해제했었다
        - 하지만 파이썬은 내장된 데이터들의 영역을 정확하게 구분하지 못하기 때문에 이러한 방법을 쓸 수 없다
    
    - 파이썬의 GC
        - 참조횟수를 통해 데이터중에 사용되지 않는 데이터를 찾아서 해제한다
        - 메모리 해제 절차
            - 컨테이너 자료형들만 참조순환을 일으킬 수 있고 다른 자료형은 무시한다
            - 이중 연결 리스트를 활용, 모든 컨테이터 자료형을 삽입해서 관리한다
            - 각 객체에 참조 횟수값을 갖는 gc_refs라는 이름의 필드를 각각 추가한다
            - 각 객체가 참조하는 객체를 찾고 나서 해당객체의 gc_refs필드를 줄인다
            - 그 후 1보다 큰 gc_refs필드가 있는 객체들(컨테이너가 아닌 다른 자료형이 참조하는 객체)을 이중연결리스트에서 빼서 다른 셋으로 옮긴다
            - 옮겨진 객체가 참조하는 객체도 해제될 수 없기 때문에 연결된 모든 객체를 옮긴다
            - 원래 리스트에 남은 객체들의 메모리를 해제한다

        - finalizers 문제
            - ```__del__```메서드가 하는 역할
            - 메모리를 해제 하기 전에 호출된다
            - 참조순환이 발생했을 때 양쪽의 객체가 finalizer를 호출하면 한쪽에서 삭제하려해도 다른 쪽에서 계속 접근하기 때문에 삭제 할 수 없다
            - 따라서 삭제되지않는 값은 따로 전역 리스트에 추가된다
            - 결국 코드를 다시 작성하거나 전역 목록과 자유 주기에 액세스 하는 방법이 있다
    - 약한참조
        - reference count를 올리지 않고 객체를 참조한다
        - 메모리 누수가 발생할 가능성이 높은지점에서 사용한다
        - a = weakret.ref(b(참조값))로 a가 b를 약한참조하게 한다

- ## 쓰레드(Thread)
    - 파이썬 프로그램은 기본적으로 하나의 쓰레드에서 순차적으로 실행된다
        - 전역 인터프리터 락킹(Global interpreter Lock)때문에 특정 시점에 하나의 코드만 실행하기 때문에 파이썬은 코드를 병렬로 실행 할 수 없고 인터리빙(interleaving)방식으로 분할 하여 실행한다
        
        > Global Interpreter Lock
        - 특정시점에 하나의 쓰레드만 실행되도록 설계한것
        - 파이썬이 느린 이유중 하나
        - 이유
            - 파이썬은 참조횟수(reference count)를 통해 GC를 운영하는데 멀티쓰레딩 환경에서 여러쓰레드가 한 객체를 사용한다면 락을 걸어야만 참조횟수가 가능하다, 이는 굉장히 비효율적이다
    - 병렬 처리를 위해 쓰레드를 생성할 수 있는데 threading모듈, thread모듈을 사용할 수 있다.
        - 일반적으로 쓰레도 처리를 위해서는 thread 모듈위에서 구현된 threading 모듈을 사용하고 있다
    - ### 멀티 쓰레딩
        - 하나의 프로세스에서 여러개의 쓰레드를 생성해 하나의 호스트에서 병렬 처리하는 기능
            - 공유되는 자원(전역변수, I/O 작업)에 대해 여러 개의 쓰레드가 동시에 접근해야 한다면 세마포어, 뮤텍스 등의 동기화 방법을 사용해야 한다

- ## 파일 핸들
    - 핸들이란 : 프로그램과 파일을 이어주는 파이프, 연결 통로 같은 역할을 해준다(파일 객체)

- ## ```__slots__```
    - 사용목적
        - 파이썬에서 클래스,인스턴스의 속성은 dict형 자료로 저장된다
        - 인스턴스가 생성 될 때 정해진 메모리양만 쓰지 않고 과도하게 쓰게 되는데
        - 인스턴스가 생성될 때마다 속성을 ```__dict__```가 아닌 고정된 set 인slot에 저장해서 메모리 사용량을 줄인다
        - 더 빠르게 속성에 접근한다.
        
    - 클래스속성에 인스턴스속성값을 리스트로 갖는 ```__slots__```를 선언한다
        ```py
        class foo()
            __slots__ = 'a'
            def __init__(self, a):
                self.a = a
        ```
    - 인스턴스 속성값을 동적으로 할당하려면 ```__slots__```에 ```__dict__```를 추가한다
        ```py
        class Foo(object):
        __slots__ = 'bar', 'baz', '__dict__'
        ```
        - 메모리사용량이 많아지지만 여전히 이점이 있다
        - 동적으로 속성을 할당할 수 있게된다
        - ```__weakref__```를 할당할 수도 있다
    - 주의점
        - 클래스 상속 트리에서 특정 slots은 한번만 선언해야한다. 

- ## Object class
    - 파이썬의 최상위 클래스로 상속하지 않아도 기본적으로 상속된다
    - 특별한 기능이 없고 속성이 없는 객체를 생성하는 역할을 한다


- ## 메모리 할당

    > 정적 메모리 할당
    - 프로그램 컴파일시 메모리가 할당 됨
    - 고정 크기로만 정적 배열을 선언함
    - 메모리는 컴파일 할 때 할당됨
    
    > 동적 메모리 할당
    - 런타임에 메모리가 할당
    - "힙"은 동적 할당을 구현하는 데 사용됨
    - 필요하지 않은 메모리를 비우고 재사용할 수 있음


- ## 메타 클래스(Meta Class)
    - 클래스가 인스턴스를 생성하듯이 클래스를 생성하느 또다른 클래스다
    ```py
    type(int)
    # -> class 'type'을 반환한다
    # type()함수가 다른 클래스를 만드는 클래스이다

    type('', (), {})
    # '클래스명', (클래스상속), {속성명:값, 메서드명:함수}
    # 위와 같이 선언해서 동적으로 클래스를 생성할 수 있다
    ```
    - 커스텀 메타 클래스 만들기
    ```py
    class MetaClass(type):
        # type클래스를 상속받아야 한다
        def __new__(cls, clsname, bases, dct):
            # __new__를 오버라이딩 한다
            # 클래스명, 상속, 속성/메서드를 입력
            return type.__new__(cls, clsname, bases, dct)

    class temp(metaclass=MetaClass)
        x = 1
    a = temp()
    ```


- ## 디스크립터(Descriptor)
    -  ***읽거나, 쓰거나, 삭제하는 메서드중 하나라도 미리 정의된 객체를 디스크립터(Descriptor)*** 라고 한다
    - @classmethod, @staticmethod, @property 구현에 사용된다
    - 디스크립터를 사용하려면, 다른 클래스에 클래스 변수로 저장해야 한다
    - 장점
        - 디스크립터는 동적으로 값을 연산할 때 이점이 있다
        - 함수나 메소드를 써서 동적으로 계산할 수 도 있지만 디스크립터를 사용하면 클래스의 개인속성값들에 접근할 수 있기때문에 함수보다 안전하다
        - 메서드로도 할 수 있지만 속성에 접근하는 방식으로 호출할 수 있기 때문에 직관적이고 편리하다
            - 메서드는 ```___str___```과 같이 인스턴스의 전체 속성값을 다루는 느낌
            - 디스크립터는 속성값 하나를 잡고 다루는 
    - 디스크립터의 ```__get__()과 __set__()```메서드는 공용속성으로 접근할 때 호출 된다
    - 예제
    ```py
    class DirectorySize:

        def __get__(self, obj, objtype=None):
            self.sizeofdir = len(os.listdir(obj.dirname))
            return sizeofdir

        def __set__(self, obj, value)
            self.sizeofdir = value

    class Directory:
        size = DirectorySize()              
        # Descriptor instance

        def __init__(self, dirname):
            self.dirname = dirname          
            # Regular instance attribute
    
    dir = Directory('songs')
    print(dir.size)
    dir.size = 
    ```
    - ```__get___(self, obj, objtype=None)```
        - self : 상위 클래스의 속성이면서 하위 클래스의 인스턴스이다 (size)
        - obj : 상위 클래스의 인스턴스 (dir)
        - objtype : 상위 클래스 (Directory)
    - ```__set___(self, obj, value)```
        - self :  ~~
        - obj : ~~
        - value : 대입할 값
    
    - 사용자 정의 이름
        - 디스크립터를 호출할 때 하나의 식별자(속성명을대신하는)로만 호출 할 수 있다
    - 활용
    ```py
    class desc():
    def __init__(self) -> None:
        self.data = {}
    # 사전형 값에는 item을 붙혀야 한다
    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        return f"{self.data}"


    def sort_num(numbers: dict, ranks: desc):
        nums = list(numbers.values())

        for i, num in enumerate(nums, 1):
            ranks[num] = i
        # 디스크립터 호출 __setitem__실행

    num = {1: 3, 2: 2, 3: 1}
    rank = desc()
    sort_num(num, rank)
    print(rank)
    ```

- ## property
    - 프로퍼티(property)는 일부 객체 지향 프로그래밍 언어에서 필드(데이터 멤버)와 메소드 간 기능의 중간인 클래스 멤버의 특수한 유형이다. 프로퍼티의 읽기와 쓰기는 일반적으로 게터(getter)와 세터(setter) 메소드 호출로 변환된다
    ```py
    class a():
        def __init__(self) -> None:
            self._x = 1

        @ property
        def x(self):
            print('getter', self._x)

        @ x.setter
        def x(self, num):
            self._x = num
            print('setter')

    b = a()
    b.x = 10
    b.x
    ```
    - x메소드 위에 @property 데코레이터를 선언함으로써 @x.setter가 데코레이터가 사용가능해진다
    - 사실상 메소드를 호출하는 방식만 바꿔진거고 값에 접근하는 명령문은 직접 작성해야한다
    - 속성 값을 _(언더바)로 직접 접근하지 못하게 하고 메서드로 의도한 방향으로만 접근하게 하는 좋은 방법이다
    - 하나의 속성에 해당하는 결과만 구현할 수 있어서 재사용성이 매우 떨어지고 속성마다 작성하면 가독성이 매우 떨어진다

- ## mutablity, immutablity
    - 객체가 가리키는 값이 바뀐다는 것은 그 주소값을 참조하고 있는 모든 객체의 값이 바뀐다는 뜻이다
    - 가변형
    - 불변형
        - 해쉬데이터를 생성할 수 있다
        - str형이 불변형이기때문에 사전형의 키(해쉬값처럼)로 사용가능
    - 한 객체에서 가변,불변이 혼용되어진다면 메서드를 사용할 때 고려해야 함으로 훨씬 복잡해진다

- ## list for vs list comprehension
    - 변수의 범위
        - for 문의 경우 iter에서 받은 원소값에 for문이 끝나도 접근할 수 있다
        - comprehension
            - iteration이 끝나면 원소값을 참조하는 변수에 접근 할 수 없다
            - class내에서 중첩된 for문을 사용하면 안쪽의 Nameerror가 발생한다
- ## in, not in(포함연산자)
    - 시퀀스형 자료를 비교할 경우 가장 높은 차원를 자료에서 같은 값을 찾는다
    - iterable하지 않은 값은 in 뒤에 사용할 수 없다
    - Dict형의 경우 디폴트로 키값에서만 값을 찾는다 
        - Dict.values()로 value값들에서 찾을 수 있다

- ## Hash Table
    - ***Hash***
        - 인풋 데이터를 고정된 길이의 숫자열로 변환한 결과물
    - key, value를 기반으로 하는 데이터
    - key값이 해쉬함수를 거쳐 숫자(해쉬주소)로 변경, value값을 참조 할 수있다
    - 불변형 값만 해쉬값을 가진다
    - 파이썬 해쉬 함수의 경우 환경마다 아웃풋이 달라서 hashlib의 sha1, sha256을 쓰기도 한다
   
    - ***해쉬 충돌*** 
        -  Key값이 다른데도 같은 해쉬값을 가지는 경우
        - *해결방안*
            - 오픈 해싱 (체이닝 기법)
                - 중복된 해쉬의 value를 연결리스트로 연결해서 해쉬가 중복되면 중복된 값 모두 참조하도록 만든다
            - 클로즈 해싱
                - 중복된 해시가 발생하면 나중에 입력된 값은 순차적으로 빈공간을 찾아 값이 비어있는 해쉬에 값을 저장한다 
- ## in-place operation
    - += 와 같은 연산자
    - in-place연산자는 실행시 값을 다른 주소값에 생성하지 않고 원래 주소에 결과 값을 저장한다
    - ***예외 사항***
        - **Immutable(불변)변수** 일 때는 새로운 주소값에 결과값 생성
        - 객체타입이 --iadd-- 메서드를 호출하지 않으면 x = x + 1 으로 실행된다(int...) 
        - --iadd-- 메서드가 NotImplemented(지원하지 않는 연산) 를 반환하면 x = x + 1 으로 실행된다
    - *값을 계속해서 연산하는 경우 in-place연산을 지원하는 타입을 쓰면 계속 같은 메모리주소의 값을 저장하기 때문에 메모리를 아낄 수 있겠다*
- ## async_iterable
    - 비동기 이터레이터
    - aiter(), anext()메서드를 구현하는 객체

- ## iterable 호출시 실행되는 것
    - 객체를 ***iter객체로 변환***하기 위해 --iter-- 메소드가 호출된다
    - iter객체의 ***다음 노드를 얻기위해*** --next-- 메소드가 호출 된다
    - 더 이상 가져올 노드가 없을 때 ***StopIteration exception*** 이 실행되서 루프를 멈춘다

- ## Generator 
    - 다른 iter객체와 다르게 for문에서 메모리를 유지하지 않아서 메모리를 적게 사용한다
    - 매번 값을 가져와서 실행하기 위해 함수의 값들을 저장해야하기 때문에 느려질 수 있다.
    - Generator는 인자로 받는 iter객체를 한 개씩 연산한다.(--next-- 메소드가 자동실행되지 않음)
    - yield문은 인자인 iter객체가 마지막 시퀀스까지 연산이 끝날때 까지 객체의 값을 기억한다
    - Generator Expression은 yield문 없이 간단하게 Generator를 생성한다


- ## *args, **kwargs   

    -  args 는 *arguments 의 줄임말 사실상 * 다음 어떤문자열이와도 상관없다.
이 지시어는 여러개의 인자를 팩킹해서 함수에 인자로 받고 언팩킹 할때 쓰인다
함수호출시 인자갯수를 동적으로 쓸 수있고 **튜플형**으로 값을 받는다

    -  **kwargs 는 {키워드:인자값}형태로 **사전형** 값을 함수에 전달한다, 
함수내에서 key, value로 값에 접근할 수 있다.


