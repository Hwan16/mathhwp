## `pyhwpx.core.XHwpDocuments`

한글과컴퓨터 문서(HWP) COM 객체의 컬렉션을 표현하는 클래스입니다.

이 클래스는 COM 객체로 표현된 문서 컬렉션과 상호작용하기 위한 속성과 메서드를 제공합니다. 문서 컬렉션에 대한 반복, 인덱싱, 길이 조회 등의 컬렉션 유사 동작을 지원하며, 문서를 추가하고, 닫고, 특정 문서 오브젝트를 검색하는 메서드를 포함합니다.

Attributes:

|        Name         |     Type     |      Description       |
|---------------------|--------------|------------------------|
| `Active_XHwpDocument` | `XHwpDocument` |       컬렉션의 활성 문서       |
|     `Application`     |              | COM 객체와 연결된 애플리케이션을 반환 |
|        `CLSID`        |              |     COM 객체의 CLSID      |
|        `Count`        |     `int`      |      컬렉션 내 문서 개수       |

Methods:

|   Name   |                      Description                       |
|----------|--------------------------------------------------------|
|   `Add`    |    bool = False) -> XHwpDocument: 컬렉션에 새 문서를 추가합니다.    |
|  `Close`   |         bool = False) -> None: 활성 문서 창을 닫습니다.          |
| `FindItem` | int) -> XHwpDocument: 주어진 문서 ID에 해당하는 문서 객체를 찾아 반환합니다. |

### `Add(isTab=False)`

문서 추가

Parameters:

| Name  | Type |               Description               | Default |
|-------|------|-----------------------------------------|---------|
| `isTab` | `bool` | 탭으로 열 건지(True), 문서로 열 건지(False, 기본값) 결정 |  `False`  |

Returns:

|      Type      |       Description        |
|----------------|--------------------------|
| `'XHwpDocument'` | 문서 오브젝트(XHwpDocument) 리턴 |

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.XHwpDocuments.Add(True)</code>
```

### `Close(isDirty=False)`

문서창 닫기

### `FindItem(lDocID)`

해당 DocumentID의 문서 오브젝트가 있는지 탐색

Parameters:

|  Name  | Type |    Description    | Default  |
|--------|------|-------------------|----------|
| `lDocID` | `int`  | 찾고자 하는 문서오브젝트의 ID | _required_ |

Returns:

| Name |      Type      |       Description       |
|------|----------------|-------------------------|
| `int`  | `'XHwpDocument'` | 해당 아이디의 XHwpDocument 리턴 |
| `None` | `'XHwpDocument'` |      없는 경우 None 리턴      |