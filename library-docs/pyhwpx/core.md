## `pyhwpx.core`

아래아한글 인스턴스를 실행합니다.

실행방법은 간단합니다. `from pyhwpx import Hwp`로 `Hwp` 클래스를 임포트한 후, `hwp = Hwp()` 명령어를 실행하면 아래아한글이 자동으로 열립니다. 만약 기존에 아래아한글 창이 하나 이상 열려 있다면, 가장 마지막에 접근했던 아래아한글 창과 연결됩니다.

#### `Application` <small><code>property</code></small>

저수준의 아래아한글 오토메이션API에 직접 접근하기 위한 속성입니다.

`hwp.Application.~~~` 로 실행 가능한 모든 속성은, 간단히 `hwp.~~~` 로 실행할 수도 있지만 pyhwpx와 API의 작동방식을 동일하게 하기 위해 구현해 두었습니다.

Returns: 저수준의 HwpApplication 객체

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.Application.XHwpWindows.Item(0).Visible = True</code>
```

#### `CLSID` <small><code>property</code></small>

파라미터셋의 CLSID(클래스아이디)를 조회함. 읽기전용 속성이며, 사용할 일이 없음..

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.CharShape.CLSID
IID('{599CBB08-7780-4F3B-8ADA-7F2ECFB57181}')</code>
```

#### `CellShape` <small><code>property</code></small> <small><code>writable</code></small>

셀(또는 표) 모양을 관리하는 파라미터셋 속성입니다.

Returns: CellShape 파라미터셋

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.CellShape.Item("Height")  # 현재 표의 높이를 HwpUnit 단위로 리턴
6410
&gt;&gt;&gt; hwp.HwpUnitToMili(hwp.CellShape.Item("Height"))
22.6131
&gt;&gt;&gt; hwp.get_table_height()  # 위와 동일한 값을 리턴함
22.6131
&gt;&gt;&gt; hwp.get_row_height()  # 현재 셀의 높이를 밀리미터 단위로 리턴
4.5226</code>
```

#### `CharShape` <small><code>property</code></small> <small><code>writable</code></small>

글자모양 파라미터셋을 조회하거나 업데이트할 수 있는 파라미터셋 속성.

여러 속성값을 조회하고 싶은 경우에는 hwp.CharShape 대신 `hwp.get_charshape_as_dict()` 메서드를 사용하면 편리합니다. CharShape 속성을 변경할 때는 아래 예시처럼 hwp.set\_font() 함수를 사용하는 것을 추천합니다.

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt;
&gt;&gt;&gt; # 현재 캐럿위치 또는 선택영역의 글자크기를 포인트단위로 출력
&gt;&gt;&gt; hwp.HwpUnitToPoint(hwp.CharShape.Item("Height"))
10.0
&gt;&gt;&gt; # 여러 속성값을 확인하고 싶은 경우에는 아래처럼~
&gt;&gt;&gt; hwp.get_charshape_as_dict()
{'Bold': 0,
 'BorderFill': &lt;win32com.gen_py.HwpObject 1.0 Type Library.IDHwpParameterSet instance at 0x2267681890512&gt;,
 'DiacSymMark': 0,
 'Emboss': 0,
 'Engrave': 0,
 'FaceNameHangul': '함초롬바탕',
 'FaceNameHanja': '함초롬바탕',
 'FaceNameJapanese': '함초롬바탕',
 'FaceNameLatin': '함초롬바탕',
 'FaceNameOther': '함초롬바탕',
 'FaceNameSymbol': '함초롬바탕',
 'FaceNameUser': '함초롬바탕',
 'FontTypeHangul': 1,
 'FontTypeHanja': 1,
 'FontTypeJapanese': 1,
 'FontTypeLatin': 1,
 'FontTypeOther': 1,
 'FontTypeSymbol': 1,
 'FontTypeUser': 1,
 'HSet': None,
 'Height': 2000,
 'Italic': 0,
 'OffsetHangul': 0,
 'OffsetHanja': 0,
 'OffsetJapanese': 0,
...
 'UnderlineColor': 0,
 'UnderlineShape': 0,
 'UnderlineType': 0,
 'UseFontSpace': 0,
 'UseKerning': 0}
&gt;&gt;&gt;
&gt;&gt;&gt; # 속성을 변경하는 예시
&gt;&gt;&gt; prop = hwp.CharShape  # 글자속성 개체를 복사한 후
&gt;&gt;&gt; prop.SetItem("Height", hwp.PointToHwpUnit(20))  # 파라미터 아이템 변경 후
&gt;&gt;&gt; hwp.CharShape = prop  # 글자속성을 prop으로 업데이트
&gt;&gt;&gt;
&gt;&gt;&gt; # 위 세 줄의 코드는 간단히 아래 단축메서드로도 실행가능
&gt;&gt;&gt; hwp.set_font(Height=30)  # 글자크기를 30으로 변경</code>
```

#### `CurFieldState` <small><code>property</code></small>

현재 캐럿이 들어있는 영역의 상태를 조회할 수 있는 속성.

필드 안에 들어있지 않으면(본문, 캡션이나 주석 포함) 0을 리턴하며, 셀 안이면 1, 글상자 안이면 4를 리턴합니다. 셀필드 안에 있으면 17, 누름틀 안에 있으면 18을 리턴합니다. 셀필드 안의 누름틀 안에서도 누름틀과 동일하게 18을 리턴하는 점에 유의하세요. 정수값에 따라 현재 캐럿의 위치를 파악할 수 있기 때문에 다양하게 활용할 수 있습니다. 예를 들어 필드와 무관하게 "캐럿이 셀 안에 있는가"를 알고 싶은 경우에도 `hwp.CurFieldState` 가 1을 리턴하는지 확인하는 방식을 사용할 수 있습니다.

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 캐럿이 현재 표 안에 들어있는지 확인하고 싶은 경우
&gt;&gt;&gt; if hwp.CurFieldState == 1:
...     print("캐럿이 셀 안에 들어있습니다.")
... else:
...     print("캐럿이 셀 안에 들어있지 않습니다.")
캐럿이 셀 안에 들어있습니다.</code>
```

#### `CurMetatagState` <small><code>property</code></small>

(한글2024 이상) 현재 캐럿이 들어가 있는 메타태그 상태를 조회할 수 있는 속성.

1: 셀 메타태그 영역에 들어있음 4: 메타태그가 부여된 글상자 또는 그리기개체 컨트롤 내부의 텍스트 공간에 있음 8: 메타태그가 부여된 이미지 또는 글맵시, 글상자 등의 컨트롤 선택상태임 16: 메타태그가 부여된 표 컨트롤 선택 상태임 32: 메타태그 영역에 들어있지 않음 40: 컨트롤을 선택하고 있긴 한데, 메타태그는 지정되어 있지 않은 상태(8+32) 64: 본문 메타태그 영역에 들어있음

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; if hwp.CurMetatagState == 1:
...     print("현재 캐럿이 셀 메타태그 영역에 들어있습니다.")</code>
```

#### `CurSelectedCtrl` <small><code>property</code></small>

현재 선택된 오브젝트의 컨트롤을 리턴하는 속성

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 문서의 첫 번째 표를 선택하고 "글자처럼 취급" 속성 켜기
&gt;&gt;&gt; hwp.get_into_nth_table()  # 문서 첫 번째 표의 A1 셀로 이동
&gt;&gt;&gt; hwp.SelectCtrlFront()  # 표 오브젝트 선택
&gt;&gt;&gt; ctrl = hwp.CurSelectedCtrl  # &lt;-- 표 오브젝트의 컨트롤정보 변수지정
&gt;&gt;&gt; prop = ctrl.Properties  # 컨트롤정보의 속성(일종의 파라미터셋) 변수지정
&gt;&gt;&gt; prop.SetItem("TreatAsChar", True)  # 복사한 파라미터셋의 글자처럼취급 아이템값을 True로 변경
&gt;&gt;&gt; ctrl.Properties = prop  # 파라미터셋 속성을 표 오브젝트 컨트롤에 적용
&gt;&gt;&gt; hwp.Cancel()  # 적용을 마쳤으면 표선택 해제(권장)</code>
```

#### `EditMode` <small><code>property</code></small> <small><code>writable</code></small>

현재 편집모드(a.k.a. 읽기전용)를 리턴하는 속성. 일반적으로 자동화에 쓸 일이 없으므로 무시해도 됩니다. 편집모드로 변경하고 싶으면 1, 읽기전용으로 변경하고 싶으면 0 대입합니다.

Returns: 편집모드는 1을, 읽기전용인 경우 0을 리턴

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.EditMode
1
&gt;&gt;&gt; hwp.EditMode = 0  # 읽기 전용으로 변경됨</code>
```

#### `HAction` <small><code>property</code></small>

한/글의 액션을 설정하고 실행하기 위한 속성.

GetDefalut, Execute, Run 등의 메서드를 가지고 있습니다. 저수준의 액션과 파라미터셋을 조합하여 기능을 실행할 때에 필요합니다.

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # "Hello world!" 문자열을 입력하는 액션
&gt;&gt;&gt; pset = hwp.HParameterSet.HInsertText
&gt;&gt;&gt; act_id = "InsertText"
&gt;&gt;&gt; pset.Text = "Hello world!\r\n"  # 줄바꿈 포함
&gt;&gt;&gt; hwp.HAction.Execute(act_id, pset.HSet)
&gt;&gt;&gt; # 위 네 줄의 명령어는 아래 방법으로도 실행 가능
&gt;&gt;&gt; hwp.insert_text("Hello world!")
&gt;&gt;&gt; hwp.BreakPara()  # 줄바꿈 메서드
True</code>
```

#### `HParameterSet` <small><code>property</code></small>

한/글에서 실행되는 대부분의 액션을 설정하는 데 필요한 파라미터셋들이 들어있는 속성.

HAction과 HParameterSet을 조합하면 어떤 복잡한 동작이라도 구현해낼 수 있지만 공식 API 문서를 읽으며 코딩하기보다는, 해당 동작을 한/글 내에서 스크립트매크로로 녹화하고 녹화된 매크로에서 액션아이디와 파라미터셋을 참고하는 방식이 훨씬 효율적이다. HParameterSet을 활용하는 예시코드는 아래와 같다.

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; pset = hwp.HParameterSet.HInsertText
&gt;&gt;&gt; pset.Text = "Hello world!"
&gt;&gt;&gt; hwp.HAction.Execute("InsertText", pset.HSet)
True</code>
```

#### `HeadCtrl` <small><code>property</code></small>

문서의 첫 번째 컨트롤을 리턴한다.

문서의 첫 번째, 두 번째 컨트롤은 항상 "구역 정의"와 "단 정의"이다. (이 둘은 숨겨져 있음) 그러므로 `hwp.HeadCtrl` 은 항상 구역정의(secd: section definition)이며, `hwp.HeadCtrl.Next` 는 단 정의(cold: column definition)이다.

사용자가 삽입한 첫 번째 컨트롤은 항상 `hwp.HeadCtrl.Next.Next` 이다.

HeadCtrl과 반대로 문서의 가장 마지막 컨트롤은 hwp.LastCtrl이며, 이전 컨트롤로 순회하려면 `.Next` 대신 `.Prev` 를 사용하면 된다. hwp.HeadCtrl의 기본적인 사용법은 아래와 같다.

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; # 문서에 삽입된 모든 표의 "글자처럼 취급" 속성을 해제하는 코드
&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; ctrl = hwp.HeadCtrl
&gt;&gt;&gt; while ctrl:
...     if ctrl.UserDesc == "표":  # 이제 ctrl 변수가 해당 표 컨트롤을 가리키고 있으므로
...         prop = ctrl.Properties
...         prop.SetItem("TreatAsChar", True)
...         ctrl.Properties = prop
...     ctrl = ctrl.Next
&gt;&gt;&gt; print("모든 표의 글자처럼 취급 속성 해제작업이 완료되었습니다.")
모든 표의 글자처럼 취급 속성 해제작업이 완료되었습니다.</code>
```

#### `IsEmpty` <small><code>property</code></small>

아무 내용도 들어있지 않은 빈 문서인지 여부를 나타낸다. 읽기전용임

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 특정 문서를 열고, 비어있는지 확인
&gt;&gt;&gt; hwp.open("./example.hwpx")
&gt;&gt;&gt; if hwp.IsEmpty:
...     print("빈 문서입니다.")
... else:
...     print("빈 문서가 아닙니다.")
빈 문서가 아닙니다.</code>
```

#### `IsModified` <small><code>property</code></small>

최근 저장 또는 생성 이후 수정이 있는지 여부를 나타낸다. 읽기전용이며, 자동화에 활용하는 경우는 거의 없다. 패스~

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.open("./example.hwpx")
&gt;&gt;&gt; # 신나게 작업을 마친 후, 종료하기 직전, 혹시 하는 마음에
&gt;&gt;&gt; # 수정사항이 있으면 저장하고 끄기 &amp; 수정사항이 없으면 그냥 한/글 종료하기
&gt;&gt;&gt; if hwp.IsModified:
...     hwp.save()
... hwp.quit()</code>
```

#### `LastCtrl` <small><code>property</code></small>

문서의 가장 마지막 컨트롤 객체를 리턴한다.

연결리스트 타입으로, HeadCtrl부터 LastCtrl까지 모두 연결되어 있고 LastCtrl.Prev.Prev 또는 HeadCtrl.Next.Next 등으로 컨트롤 순차 탐색이 가능하다. 혹자는 `hwp.HeadCtrl` 만 있으면 되는 거 아닌가 생각할 수 있지만, 특정 조건의 컨트롤을 삭제!!하는 경우 삭제한 컨트롤 이후의 모든 컨트롤의 인덱스가 변경되어버리므로 이런 경우에는 LastCtrl에서 역순으로 진행해야 한다. (HeadCtrl부터 Next 작업을 하면 인덱스 꼬임)

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 문서 내의 모든 그림 삭제하기
&gt;&gt;&gt; ctrl = hwp.LastCtrl  # &lt;---
&gt;&gt;&gt; while ctrl:
...     if ctrl.UserDesc == "그림":
...         hwp.DeleteCtrl(ctrl)
...     ctrl = ctrl.Prev
... print("모든 그림을  삭제하였습니다.")
모든 그림을 삭제하였습니다.
&gt;&gt;&gt; # 아래처럼 for문과 hwp.ctrl_list로도 구현할 수 있음
&gt;&gt;&gt; for ctrl in [i for i in hwp.ctrl_list if i.UserDesc == "그림"][::-1]:  # 역순 아니어도 무관.
...     hwp.DeleteCtrl(ctrl)</code>
```

#### `PageCount` <small><code>property</code></small>

현재 문서의 총 페이지 수를 리턴.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.open("./example.hwpx")
&gt;&gt;&gt; print(f"현재 이 문서의 총 페이지 수는 {hwp.PageCount}입니다.")
현재 이 문서의 총 페이지 수는 20입니다.</code>
```

#### `ParaShape` <small><code>property</code></small> <small><code>writable</code></small>

CharShape, CellShape과 함께 가장 많이 사용되는 단축Shape 삼대장 중 하나.

현재 캐럿이 위치한, 혹은 선택한 문단(블록)의 문단모양 파라미터셋을 리턴한다.

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.open("./example.hwp")
&gt;&gt;&gt; # 현재 캐럿위치의 줄간격 조회
&gt;&gt;&gt; val = hwp.ParaShape.Item("LineSpacing")
&gt;&gt;&gt; print(f"현재 문단의 줄간격은 {val}%입니다.")
현재 문단의 줄간격은 160%입니다.
&gt;&gt;&gt;
&gt;&gt;&gt; # 본문 모든 문단의 줄간격을 200%로 수정하기
&gt;&gt;&gt; hwp.SelectAll()  # 전체선택
&gt;&gt;&gt; prop = hwp.ParaShape
&gt;&gt;&gt; prop.SetItem("LineSpacing", 200)
&gt;&gt;&gt; hwp.ParaShape = prop
&gt;&gt;&gt; print("본문 전체의 줄간격을 200%로 수정하였습니다.")
본문 전체의 줄간격을 200%로 수정하였습니다.</code>
```

#### `ParentCtrl` <small><code>property</code></small>

현재 선택되어 있거나, 캐럿이 들어있는 컨트롤을 포함하는 상위 컨트롤을 리턴한다.

Returns:

#### `Path` <small><code>property</code></small>

현재 빈 문서가 아닌 경우, 열려 있는 문서의 파일명을 포함한 전체경로를 리턴한다.

Returns: 현재 문서의 전체경로

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.open("./example.hwpx")
&gt;&gt;&gt; hwp.Path
C:/Users/User/desktop/example.hwpx</code>
```

#### `SelectionMode` <small><code>property</code></small>

현재 선택모드가 어떤 상태인지 리턴한다.

Returns:

#### `Title` <small><code>property</code></small>

현재 연결된 아래아한글 창의 제목표시줄 타이틀을 리턴한다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; print(hwp.Title)
빈 문서 1 - 한글</code>
```

#### `Version` <small><code>property</code></small>

아래아한글 프로그램의 버전을 리스트로 리턴한다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.Version
[13, 0, 0, 2151]</code>
```

#### `ViewProperties` <small><code>property</code></small> <small><code>writable</code></small>

현재 한/글 프로그램의 보기 속성 파라미터셋을 리턴한다.

Returns:

#### `XHwpDocuments` <small><code>property</code></small>

HwpApplication의 XHwpDocuments 객체를 리턴한다.

Returns:

#### `XHwpMessageBox` <small><code>property</code></small>

#### `coclass_clsid` <small><code>property</code></small>

coclass의 clsid를 리턴하는 읽기전용 속성. 사용하지 않음.

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.coclass_clsid
IID('{2291CF00-64A1-4877-A9B4-68CFE89612D6}')</code>
```

#### `ctrl_list` <small><code>property</code></small>

문서 내 모든 ctrl를 리스트로 반환한다.

단, 기본으로 삽입되어 있는 두 개의 컨트롤인 secd(섹션정의)와 cold(단정의) 두 개는 어차피 선택불가하므로 ctrl\_list에서 제외했다. (모든 컨트롤을 제거하는 등의 경우, 편의를 위함)

Returns:

#### `current_page` <small><code>property</code></small>

새쪽번호나 구역과 무관한 현재 쪽의 순서를 리턴.

1페이지에 있다면 1을 리턴한다. 새쪽번호가 적용되어 있어도 페이지의 인덱스를 리턴한다.

Returns:

#### `current_printpage` <small><code>property</code></small>

페이지인덱스가 아닌, 종이에 표시되는 쪽번호를 리턴.

1페이지에 있다면 1을 리턴한다. 새쪽번호가 적용되어 있다면 수정된 쪽번호를 리턴한다.

Returns:

#### `is_empty` <small><code>property</code></small>

아무 내용도 들어있지 않은 빈 문서인지 여부를 나타낸다. 읽기전용

#### `is_modified` <small><code>property</code></small>

최근 저장 또는 생성 이후 수정이 있는지 여부를 나타낸다. 읽기전용

#### `Run(act_id)`

액션을 실행한다.

ActionTable.hwp 액션 리스트 중에서 "별도의 파라미터가 필요하지 않은" 단순 액션을 hwp.Run(액션아이디)으로 호출할 수 있다. 단, `hwp.Run("BreakPara")` 처럼 실행하는 대신 `hwp.BreakPara()` 방식으로 실행 가능하다.

Parameters:

Returns:

#### `SelectCtrl(ctrllist, option=1)`

한글2024 이상의 버전에서 사용 가능한 API 기반의 신규 메서드.

가급적 hwp.select\_ctrl(ctrl)을 실행할 것을 추천.

Parameters:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()  # 한글2024 이상의 버전
&gt;&gt;&gt; # 문서 마지막 컨트롤 선택하기
&gt;&gt;&gt; hwp.SelectCtrl(hwp.LastCtrl.GetCtrlInstID(), 0)</code>
```

#### `add_doc()`

새 문서를 추가한다.

원래 창이 백그라운드로 숨겨져 있어도 추가된 문서는 보이는 상태가 기본값이다. 숨기려면 `hwp.set_visible(False)`를 실행해야 한다. 새 탭을 추가하고 싶은 경우는 `add_doc` 대신 `add_tab`을 실행하면 된다.

Returns:

#### `add_tab()`

새 문서를 현재 창의 새 탭에 추가한다.

백그라운드 상태에서 새 창을 만들 때 윈도우에 나타나는 경우가 있는데, add\_tab() 함수를 사용하면 백그라운드 작업이 보장된다. 탭 전환은 switch\_to() 메서드로 가능하다.

새 창을 추가하고 싶은 경우는 add\_tab 대신 hwp.FileNew()나 hwp.add\_doc()을 실행하면 된다.

#### `adjust_cellwidth(width, as_='ratio')`

칼럼의 너비를 변경할 수 있는 메서드.

정수(int)나 부동소수점수(float) 입력시 현재 칼럼의 너비가 변경되며, 리스트나 튜플 등 iterable 타입 입력시에는 각 요소들의 비에 따라 칼럼들의 너비가 일괄변경된다. 예를 들어 3행 3열의 표 안에서 set\_col\_width(\[1,2,3\]) 을 실행하는 경우 1열너비:2열너비:3열너비가 1:2:3으로 변경된다. (표 전체의 너비가 148mm라면, 각각 24mm : 48mm : 72mm로 변경된다는 뜻이다.)

단, 열너비의 비가 아닌 "mm" 단위로 값을 입력하려면 as\_="mm"로 파라미터를 수정하면 된다. 이 때, width에 정수 또는 부동소수점수를 입력하는 경우 as\_="ratio"를 사용할 수 없다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.create_table(3,3)
&gt;&gt;&gt; hwp.get_into_nth_table(0)
&gt;&gt;&gt; hwp.adjust_cellwidth([1,2,3])</code>
```

#### `apply_parashape(para_dict)`

hwp.get\_parashape\_as\_dict() 메서드를 통해 저장한 문단모양을 다른 문단에 적용할 수 있는 메서드. 아직은 모든 속성을 지원하지 않는다. 저장 및 적용 가능한 파라미터아이템은 아래 19가지이다. 특정 파라미터 아이템만 적용하고 싶은 경우 apply\_parashape 메서드를 복사하여 커스텀해도 되지만, 가급적 set\_para 메서드를 직접 사용하는 것을 추천한다.

"AlignType", "BreakNonLatinWord", "LineSpacing", "Condense", "SnapToGrid", "NextSpacing", "PrevSpacing", "Indentation", "RightMargin", "LeftMargin", "PagebreakBefore", "KeepLinesTogether", "KeepWithNext", "WidowOrphan", "AutoSpaceEAsianNum", "AutoSpaceEAsianEng", "LineWrap", "FontLineHeight", "TextAlignment"

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 모양을 복사하고자 하는 문단에서
&gt;&gt;&gt; para_dict = hwp.get_parashape_as_dict()
&gt;&gt;&gt; # 모양을 붙여넣기하려는 문단으로 이동 후
&gt;&gt;&gt; hwp.apply_parashape(para_dict)
True
&gt;&gt;&gt;
&gt;&gt;&gt; # Border나 Heading 속성 등 모든 문단모양을 적용하기 위해서는
&gt;&gt;&gt; # 아래와 같이 get_parashape과 set_parashape을 사용하면 된다.
&gt;&gt;&gt;
&gt;&gt;&gt; # 모양을 복사하고자 하는 문단에서
&gt;&gt;&gt; parashape = hwp.get_parashape()
&gt;&gt;&gt; # 모양을 붙여넣기하려는 문단으로 이동 후
&gt;&gt;&gt; hwp.set_parashape(parashape)
True
&gt;&gt;&gt;
&gt;&gt;&gt; # 마지막으로, 특정 문단속성만 지정하여 변경하고자 할 때에는
&gt;&gt;&gt; # hwp.set_para 메서드가 가장 간편하다. (파라미터셋의 아이템과 이름은 동일하다.)
&gt;&gt;&gt; hwp.set_para(AlignType="Justify", LineSpacing=160, LeftMargin=0)
True</code>
```

#### `auto_spacing(init_spacing=0, init_ratio=100, max_spacing=40, min_spacing=40, verbose=True)`

자동 자간조정 메서드(beta)

라인 끝에 단어가 a와 b로 잘려 있는 경우 a>b인 경우 라인의 자간을 줄이고, a<b인 경우 자간을 넓혀 잘린 단어가 합쳐질 때까지 자간조정을 계속한다. 단, max\_spacing이나 min\_spacing을 넘어야 하는 경우에는 원상태로 되돌린 후 해당 라인의 정보를 콘솔에 출력한다. (아주 너비가 작은 셀이나 글상자 등에서는 제대로 작동하지 않을 수 있음.)

init\_spacing과 init\_ratio 파라미터를 통해 자동자간조정을 실행하기 전에 모든 문서의 기본 자간장평을 설정할 수 있다.

#### `cell_fill(face_color=(217, 217, 217))`

선택한 셀에 색 채우기

Parameters:

Returns:

#### `clear(option=1)`

현재 편집중인 문서의 내용을 닫고 빈문서 편집 상태로 돌아간다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.clear()</code>
```

#### `clipboard_to_pyfunc()`

한/글 프로그램에서 스크립트매크로 녹화 코드를 클립보드에 복사하고

clipboard\_to\_pyfunc()을 실행하면, 클립보드의 매크로가 파이썬 함수로 변경된다. 곧 정규식으로 업데이트 예정(2023. 11. 30)

#### `close(is_dirty=False, interval=0.01)`

문서를 버리고 닫은 후, 새 문서창을 여는 메서드.

굳이 새 문서파일이 필요한 게 아니라면 `hwp.close()` 대신 `hwp.clear()`를 사용할 것.

Parameters:

Returns:

#### `compose_chars(Chars='', CharSize=-3, CheckCompose=0, CircleType=0, **kwargs)`

글자 겹치기 메서드(원문자 만들기)

캐럿 위치의 서체를 따라가지만, 임의의 키워드로 폰트 수정 가능(예: Bold=True, Italic=True, TextColor=hwp.RGBColor(255,0,0) 등)

Parameters:

Returns:

#### `create_action(actidstr)`

Action 객체를 생성한다.

액션에 대한 세부적인 제어가 필요할 때 사용한다. 예를 들어 기능을 수행하지 않고 대화상자만을 띄운다든지, 대화상자 없이 지정한 옵션에 따라 기능을 수행하는 등에 사용할 수 있다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt;
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 현재 커서의 폰트 크기(Height)를 구하는 코드
&gt;&gt;&gt; act = hwp.create_action("CharShape")
&gt;&gt;&gt; cs = act.CreateSet()  # equal to "cs = hwp.create_set(act)"
&gt;&gt;&gt; act.GetDefault(cs)
&gt;&gt;&gt; print(cs.Item("Height"))
2800
&gt;&gt;&gt; # 현재 선택범위의 폰트 크기를 20pt로 변경하는 코드
&gt;&gt;&gt; act = hwp.create_action("CharShape")
&gt;&gt;&gt; cs = act.CreateSet()  # equal to "cs = hwp.create_set(act)"
&gt;&gt;&gt; act.GetDefault(cs)
&gt;&gt;&gt; cs.SetItem("Height", hwp.point_to_hwp_unit(20))
&gt;&gt;&gt; act.Execute(cs)
True</code>
```

#### `create_field(name, direction='', memo='')`

캐럿의 현재 위치에 누름틀을 생성한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.create_field(direction="이름", memo="이름을 입력하는 필드", name="name")
True
&gt;&gt;&gt; hwp.put_field_text("name", "일코")</code>
```

#### `create_page_image(path, pgno=-1, resolution=300, depth=24, format='bmp')`

`pgno`로 지정한 페이지를 `path` 라는 파일명으로 저장한다. 이 때 페이지번호는 1부터 시작하며,(1-index) `pgno=0`이면 현재 페이지, `pgno=-1`(기본값)이면 전체 페이지를 이미지로 저장한다. 내부적으로 pillow 모듈을 사용하여 변환하므로, 사실상 pillow에서 변환 가능한 모든 포맷으로 입력 가능하다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.create_page_image("c:/Users/User/Desktop/a.bmp")
True</code>
```

#### `create_set(setidstr)`

ParameterSet을 생성한다.

단독으로 쓰이는 경우는 거의 없으며, 대부분 create\_action과 같이 사용한다.

ParameterSet은 일종의 정보를 지니는 객체이다. 어떤 Action들은 그 Action이 수행되기 위해서 정보가 필요한데 이 때 사용되는 정보를 ParameterSet으로 넘겨준다. 또한 한/글 컨트롤은 특정정보(ViewProperties, CellShape, CharShape 등)를 ParameterSet으로 변환하여 넘겨주기도 한다. 사용 가능한 ParameterSet의 ID는 ParameterSet Table.hwp문서를 참조한다.

Parameters:

Returns:

#### `create_table(rows=1, cols=1, treat_as_char=True, width_type=0, height_type=0, header=True, height=0)`

표를 생성하는 메서드.

기본적으로 rows와 cols만 지정하면 되며, 용지여백을 제외한 구간에 맞춰 표 너비가 결정된다. 이는 일반적인 표 생성과 동일한 수치이다.

아래의 148mm는 종이여백 210mm에서 60mm(좌우 각 30mm)를 뺀 150mm에다가, 표 바깥여백 각 1mm를 뺀 148mm이다. (TableProperties.Width = 41954) 각 열의 너비는 5개 기준으로 26mm인데 이는 셀마다 안쪽여백 좌우 각각 1.8mm를 뺀 값으로, 148 - (1.8 x 10 =) 18mm = 130mm 그래서 셀 너비의 총 합은 130이 되어야 한다. 아래의 라인28~32까지 셀너비의 합은 16+36+46+16+16=130 표를 생성하는 시점에는 표 안팎의 여백을 없애거나 수정할 수 없으므로 이는 고정된 값으로 간주해야 한다.

Parameters:

Returns:

#### `delete_ctrl(ctrl)`

문서 내 컨트롤을 삭제한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; ctrl = hwp.HeadCtrl.Next.Next
&gt;&gt;&gt; if ctrl.UserDesc == "표":
...     hwp.delete_ctrl(ctrl)
...
True</code>
```

#### `delete_style_by_name(src, dst)`

특정 스타일을 이름 (또는 인덱스번호)로 삭제하고 대체할 스타일 또한 이름 (또는 인덱스번호)로 지정해주는 메서드.

#### `export_mathml(mml_path, delay=0.2)`

MathML 포맷의 수식문서 파일경로를 입력하면

아래아한글 수식으로 삽입하는 함수

#### `export_style(sty_filepath)`

현재 문서의 Style을 sty 파일로 Export한다. #스타일 #내보내기

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.export_style("C:/Users/User/Desktop/new_style.sty")
True</code>
```

#### `field_exist(field)`

문서에 해당 이름의 데이터 필드가 존재하는지 검사한다.

Parameters:

Returns:

#### `fields_to_dict()`

현재 문서에 저장된 필드명과 필드값을

dict 타입으로 리턴하는 메서드.

Returns:

#### `file_translate(cur_lang='ko', trans_lang='en')`

문서를 번역함(Ctrl-Z 안 됨.) 한 달 10,000자 무료

Parameters:

Returns:

#### `fill_addr_field()`

현재 표 안에서 모든 셀에 엑셀 셀주소 스타일("A1")의 셀필드를 채우는 메서드

#### `find(src='', direction='Forward', regex=False, TextColor=None, MatchCase=1, SeveralWords=0, UseWildCards=1, WholeWordOnly=0, AutoSpell=1, HanjaFromHangul=1, AllWordForms=0, FindStyle='', ReplaceStyle='', FindJaso=0, FindType=1)`

direction 방향으로 특정 단어를 찾아가는 메서드.

해당 단어를 선택한 상태가 되며, 탐색방향에 src 문자열이 없는 경우 False를 리턴

Parameters:

Returns:

#### `find_backward(src, regex=False)`

문서 위쪽으로 find 메서드를 수행.

해당 단어를 선택한 상태가 되며, 문서 처음에 도달시 False 리턴

Parameters:

Returns:

#### `find_forward(src, regex=False)`

문서 아래쪽으로 find를 수행하는 메서드.

해당 단어를 선택한 상태가 되며, 문서 끝에 도달시 False 리턴.

Parameters:

Returns:

#### `find_private_info(private_type, private_string)`

개인정보를 찾는다. (비밀번호 설정 등의 이유, 현재 비활성화된 것으로 추정)

Parameters:

Returns:

#### `find_replace(src, dst, regex=False, direction='Forward', MatchCase=1, AllWordForms=0, SeveralWords=1, UseWildCards=1, WholeWordOnly=0, AutoSpell=1, IgnoreFindString=0, IgnoreReplaceString=0, ReplaceMode=1, HanjaFromHangul=1, FindJaso=0, FindStyle='', ReplaceStyle='', FindType=1)`

아래아한글의 찾아바꾸기와 동일한 액션을 수항해지만,

re=True로 설정하고 실행하면, 문단별로 잘라서 문서 전체를 순회하며 파이썬의 re.sub 함수를 실행한다.

#### `find_replace_all(src, dst, regex=False, MatchCase=1, AllWordForms=0, SeveralWords=1, UseWildCards=1, WholeWordOnly=0, AutoSpell=1, IgnoreFindString=0, IgnoreReplaceString=0, ReplaceMode=1, HanjaFromHangul=1, FindJaso=0, FindStyle='', ReplaceStyle='', FindType=1)`

아래아한글의 찾아바꾸기와 동일한 액션을 수항해지만,

re=True로 설정하고 실행하면, 문단별로 잘라서 문서 전체를 순회하며 파이썬의 re.sub 함수를 실행한다.

#### `get_available_font()`

현재 사용 가능한 폰트 리스트를 리턴. API 사용시 발생하는 오류로 인해 현재는 한글 폰트만 지원하고 있음.

Returns: 현재 사용 가능한 폰트 리스트

#### `get_bin_data_path(binid)`

Binary Data(Temp Image 등)의 경로를 가져온다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; path = hwp.get_bin_data_path(2)
&gt;&gt;&gt; print(path)
C:/Users/User/AppData/Local/Temp/Hnc/BinData/EMB00004dd86171.jpg</code>
```

#### `get_cell_addr(as_='str')`

현재 캐럿이 위치한 셀의 주소를 "A1" 또는 (0, 0)으로 리턴.

캐럿이 표 안에 있지 않은 경우 False를 리턴함

Parameters:

Returns:

#### `get_cell_margin(as_='mm')`

표 중 커서가 위치한 셀 또는 다중선택한 모든 셀의 안 여백을 조회하는 메서드.

표 안에서만 실행가능하며, 전체 셀이 아닌 표 자체를 선택한 상태에서는 여백이 조회되지 않음.

Parameters:

Returns:

#### `get_charshape()`

현재 캐럿의 글자모양 파라미터셋을 리턴하는 메서드. 변수로 저장해 두고, set\_charshape을 통해 특정 선택영역에 이 글자모양을 적용할 수 있다.

#### `get_charshape_as_dict()`

현재 캐럿의 글자모양 파라미터셋을 (보기좋게) dict로 리턴하는 메서드. get\_charshape와 동일하게 set\_charshape에 이 dict를 사용할 수도 있다.

#### `get_col_num()`

캐럿이 표 안에 있을 때,

현재 셀의 열번호, 즉 셀주소 문자열의 정수 부분을 리턴

Returns:

#### `get_col_width(as_='mm')`

현재 캐럿이 위치한 셀(칼럼)의 너비를 리턴하는 메서드.

기본 단위는 mm이지만, as\_ 파라미터를 사용하여 단위를 hwpunit이나 point, inch 등으로 변경 가능하다.

Parameters:

Returns:

#### `get_ctrl_pos(ctrl=None, option=0, as_tuple=True)`

특정 컨트롤의 앵커(빨간 조판부호) 좌표를 리턴하는 메서드. 한글2024 미만의 버전에서, 컨트롤의 정확한 위치를 파악하기 위함

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 2x2표의 A1셀 안에 2x2표를 삽입하고, 표안의 표를 선택한 상태에서
&gt;&gt;&gt; # 컨트롤이 포함된 영역의 좌표를 리턴하려면(가장 많이 쓰임)
&gt;&gt;&gt; hwp.get_ctrl_pos()
(3, 0, 0)
&gt;&gt;&gt; # 현재컨트롤을 포함한 최상위컨트롤의 본문기준 좌표를 리턴하려면
&gt;&gt;&gt; hwp.get_ctrl_pos(option=1)
(0, 0, 16)
&gt;&gt;&gt; # 특정 컨트롤의 위치를 저장해 뒀다가 해당 위치로 이동하고 싶은 경우
&gt;&gt;&gt; pos = hwp.get_ctrl_pos(hwp.CurSelectedCtrl)  # 좌표 저장
&gt;&gt;&gt; # 모종의 작업으로 컨트롤 위치가 바뀌더라도, 컨트롤을 찾아갈 수 있음
&gt;&gt;&gt; hwp.set_pos(*pos)  # 해당 컨트롤 앞으로 이동함
True
&gt;&gt;&gt; # 특정 컨트롤 위치 앞으로 이동하기 액션은 아래처럼도 실행 가능
&gt;&gt;&gt; hwp.move_to_ctrl(hwp.ctrl_list[-1])
True</code>
```

#### `get_cur_field_name(option=0)`

현재 캐럿이 위치하는 곳의 필드이름을 구한다. 이 함수를 통해 현재 필드가 셀필드인지 누름틀필드인지 구할 수 있다. 참고로, 필드 좌측에 커서가 붙어있을 때는 이름을 구할 수 있지만, 우측에 붙어 있을 때는 작동하지 않는다. GetFieldList()의 옵션 중에 hwpFieldSelection(=4)옵션은 사용하지 않는다.

Parameters:

Returns:

#### `get_cur_metatag_name()`

현재 캐럿위치의 메타태그 이름을 리턴하는 메서드.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # "#test"라는 메타태그 이름이 부여된 표를 선택한 상태에서
&gt;&gt;&gt; hwp.get_cur_metatag_name()
#test</code>
```

#### `get_field_info()`

문서 내의 모든 누름틀의 정보(지시문 및 메모)를 추출하는 메서드.

셀필드는 지시문과 메모가 없으므로 이 메서드에서는 추출하지 않는다. 만약 셀필드를 포함하여 모든 필드의 이름만 추출하고 싶다면 `hwp.get_field_list().split("\r\n")` 메서드를 쓰면 된다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_field_info()
[{'name': '누름틀1', 'direction': '안내문1', 'memo': '메모1'},
{'name': '누름틀2', 'direction': '안내문2', 'memo': '메모2'}]</code>
```

#### `get_field_list(number=1, option=0)`

문서에 존재하는 필드의 목록을 구한다.

문서 중에 동일한 이름의 필드가 여러 개 존재할 때는 number에 지정한 타입에 따라 3 가지의 서로 다른 방식 중에서 선택할 수 있다. 예를 들어 문서 중 title, body, title, body, footer 순으로 5개의 필드가 존재할 때, hwpFieldPlain, hwpFieldNumber, HwpFieldCount 세 가지 형식에 따라 다음과 같은 내용이 돌아온다.

```text
- hwpFieldPlain: "titlebodytitlebodyfooter"
- hwpFieldNumber: "title{{0}}body{{0}}title{{1}}body{{1}}footer{{0}}"
- hwpFieldCount: "title{{2}}body{{2}}footer{{1}}"
```

Parameters:

Returns:

#### `get_field_text(field, idx=0)`

지정한 필드에서 문자열을 구한다.

Parameters:

Returns:

#### `get_file_info(filename)`

파일 정보를 알아낸다.

한글 문서를 열기 전에 암호가 걸린 문서인지 확인할 목적으로 만들어졌다. (현재 한/글2022 기준으로 hwpx포맷에 대해서는 파일정보를 파악할 수 없다.)

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; pset = hwp.get_file_info("C:/Users/Administrator/Desktop/이력서.hwp")
&gt;&gt;&gt; print(pset.Item("Format"))
&gt;&gt;&gt; print(pset.Item("VersionStr"))
&gt;&gt;&gt; print(hex(pset.Item("VersionNum")))
&gt;&gt;&gt; print(pset.Item("Encrypted"))
HWP
5.1.1.0
0x5010100
0</code>
```

#### `get_font_list(langid='')`

현재 문서에 사용되고 있는 폰트 목록 리턴

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_font_list()
['D2Coding,R', 'Pretendard Variable Thin,R', '나눔명조,R', '함초롬바탕,R']</code>
```

#### `get_heading_string()`

현재 커서가 위치한 문단 시작부분의 글머리표/문단번호/개요번호를 추출한다.

글머리표/문단번호/개요번호가 있는 경우, 해당 문자열을 얻어올 수 있다. 문단에 글머리표/문단번호/개요번호가 없는 경우, 빈 문자열이 추출된다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_heading_string()
'1.'</code>
```

#### `get_image_info(ctrl=None)`

이미지 컨트롤의 원본 그림의 이름과 원본 그림의 크기 정보를 추출하는 메서드

Parameters:

Returns: 해당 이미지의 삽입 전 파일명과, \[Width, Height\] 리스트

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 이미지 선택 상태에서
&gt;&gt;&gt; hwp.get_image_info()
{'name': 'tmpmj2md6uy', 'size': [200, 200]}
&gt;&gt;&gt; # 문서 마지막그림 정보
&gt;&gt;&gt; ctrl = [i for i in hwp.ctrl_list if i.UserDesc == "그림"][-1]
&gt;&gt;&gt; hwp.get_image_info(ctrl)
{'name': 'tmpxk_5noth', 'size': [1920, 1080]}</code>
```

#### `get_into_nth_table(n=0, select_cell=False)`

문서 n번째 표의 첫 번째 셀로 이동하는 함수.

첫 번째 표의 인덱스가 0이며, 음수인덱스 사용 가능. 단, 표들의 인덱스 순서는 표의 위치 순서와 일치하지 않을 수도 있으므로 유의해야 한다.

#### `get_into_table_caption()`

표 캡션(정확히는 표번호가 있는 리스트공간)으로 이동하는 메서드.

(추후 개선예정 : 캡션 스타일로 찾아가기 기능 추가할 것)

Returns:

#### `get_linespacing(method='Percent')`

현재 캐럿 위치의 줄간격(%) 리턴.

[![get_linespacing](https://martiniifun.github.io/pyhwpx/assets/get_linespacing.gif)](https://martiniifun.github.io/pyhwpx/assets/get_linespacing.gif)

단, 줄간격 기준은 "글자에 따라(%)" 로 설정되어 있어야 하며, "글자에 따라"가 아닌 경우에는 method 파라미터를 실제 옵션과 일치시켜야 함.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_linespacing()
160
&gt;&gt;&gt; # 줄간격을 "최소" 기준 17.0point로 설정했다면, 아래처럼 실행해야 함
&gt;&gt;&gt; hwp.get_linespacing("AtLeast")
170</code>
```

#### `get_markpen_color()`

현재 선택된 영역의 형광펜 색(RGB)을 튜플로 리턴하는 메서드

Returns:

#### `get_message_box_mode()`

현재 메시지 박스의 Mode를 `int`로 얻어온다.

set\_message\_box\_mode와 함께 쓰인다. 6개의 대화상자에서 각각 확인/취소/종료/재시도/무시/예/아니오 버튼을 자동으로 선택할 수 있게 설정할 수 있으며 조합 가능하다. 리턴하는 정수의 의미는 `set_message_box_mode`를 참고한다.

#### `get_metatag_list(number, option)`

메타태그리스트 가져오기

#### `get_metatag_name_text(tag)`

메타태그이름 문자열 가져오기

#### `get_mouse_pos(x_rel_to=1, y_rel_to=1)`

마우스의 현재 위치를 얻어온다.

단위가 HWPUNIT임을 주의해야 한다. (1 inch = 7200 HWPUNIT, 1mm = 283.465 HWPUNIT)

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; pset = hwp.get_mouse_pos(1, 1)
&gt;&gt;&gt; print("X축 기준:", "쪽" if pset.Item("XRelTo") else "종이")
&gt;&gt;&gt; print("Y축 기준:", "쪽" if pset.Item("YRelTo") else "종이")
&gt;&gt;&gt; print("현재", pset.Item("Page")+1, "페이지에 커서 위치")
&gt;&gt;&gt; print("좌상단 기준 우측으로", int(pset.Item("X") / 283.465), "mm에 위치")
&gt;&gt;&gt; print("좌상단 기준 아래로", int(pset.Item("Y") / 283.465), "mm에 위치")
X축 기준: 쪽
Y축 기준: 쪽
현재 2 페이지에 커서 위치
좌상단 기준 우측으로 79 mm에 위치
좌상단 기준 아래로 217 mm에 위치</code>
```

#### `get_page_text(pgno=0, option=4294967295)`

페이지 단위의 텍스트 추출 일반 텍스트(글자처럼 취급 도형 포함)를 우선적으로 추출하고, 도형(표, 글상자) 내의 텍스트를 추출한다. 팁: get\_text로는 글머리를 추출하지 않지만, get\_page\_text는 추출한다. 팁2: 아무리 get\_page\_text라도 유일하게 표번호는 추출하지 못한다. 표번호는 XML태그 속성 안에 저장되기 때문이다.

Parameters:

Returns:

#### `get_pagedef()`

현재 페이지의 용지정보 파라미터셋을 리턴한다.

리턴값은 set\_pagedef 메서드를 통해 새로운 문서에 적용할 수 있다. 연관 메서드로, get\_pagedef\_as\_dict는 보다 직관적으로 밀리미터 단위로 변환된 dict를 리턴하므로, get\_pagedef\_as\_dict 메서드를 추천한다.

#### `get_pagedef_as_dict(as_='kor')`

현재 페이지의 용지정보를 dict 형태로 리턴한다.

dict의 각 값은 밀리미터 단위로 변환된 값이며, set\_pagedef 실행시 내부적으로 HWPUnit으로 자동변환하여 적용한다. (as\_ 파라미터를 "eng"로 변경하면 원래 영문 아이템명의 사전을 리턴한다.)

현재 페이지의 용지정보(dict) 각 키의 원래 아이템명은 아래와 같다.

```text
PaperWidth: 용지폭
PaperHeight: 용지길이
Landscape: 용지방향(0: 가로, 1:세로)
GutterType: 제본타입(0: 한쪽, 1:맞쪽, 2:위쪽)
TopMargin: 위쪽
HeaderLen: 머리말
LeftMargin: 왼쪽
GutterLen: 제본여백
RightMargin: 오른쪽
FooterLen: 꼬리말
BottomMargin: 아래쪽
```

#### `get_parashape()`

현재 캐럿이 위치한 문단모양 파라미터셋을 리턴하는 메서드. 변수로 저장해 두고, set\_parashape을 통해 특정 선택영역에 이 문단모양을 적용할 수 있다.

#### `get_parashape_as_dict()`

현재 캐럿의 문단모양 파라미터셋을 (보기좋게) dict로 리턴하는 메서드. get\_parashape와 동일하게 set\_parashape에 이 dict를 사용할 수도 있다.

#### `get_pos()`

캐럿의 위치를 얻어온다.

파라미터 중 리스트는, 문단과 컨트롤들이 연결된 한/글 문서 내 구조를 뜻한다. 리스트 아이디는 문서 내 위치 정보 중 하나로서 SelectText에 넘겨줄 때 사용한다. (파이썬 자료형인 list가 아님)

Returns:

#### `get_pos_by_set()`

현재 캐럿의 위치 정보를 ParameterSet으로 얻어온다.

해당 파라미터셋은 set\_pos\_by\_set에 직접 집어넣을 수 있어 간편히 사용할 수 있다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; pset = hwp.get_pos_by_set()  # 캐럿위치 저장
&gt;&gt;&gt; print(pset.Item("List"))
6
&gt;&gt;&gt; print(pset.Item("Para"))
3
&gt;&gt;&gt; print(pset.Item("Pos"))
2
&gt;&gt;&gt; hwp.set_pos_by_set(pset)  # 캐럿위치 복원
True</code>
```

#### `get_row_height(as_='mm')`

표 안에서 캐럿이 들어있는 행(row)의 높이를 리턴함.

기본단위는 mm 이지만, HwpUnit이나 Point 등 보다 작은 단위를 사용할 수 있다. (메서드 내부에서는 HwpUnit으로 연산한다.)

Parameters:

Returns:

#### `get_row_num()`

캐럿이 표 안에 있을 때,

현재 표의 행의 최대갯수를 리턴

Returns: 최대 행갯수:int

#### `get_script_source(filename)`

문서에 포함된 매크로(스크립트매크로 제외) 소스코드를 가져온다. 문서포함 매크로는 기본적으로

```
<span></span><code id="code-lang-csharp">function OnDocument_New() {
}
function OnDocument_Open() {
}</code>
```

형태로 비어있는 상태이며, OnDocument\_New와 OnDocument\_Open 두 개의 함수에 한해서만 코드를 추가하고 실행할 수 있다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-javascript">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt;
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; print(hwp.get_script_source("C:/Users/User/Desktop/script.hwp"))
function OnDocument_New()
{
    HAction.GetDefault("InsertText", HParameterSet.HInsertText.HSet);
    HParameterSet.HInsertText.Text = "ㅁㄴㅇㄹㅁㄴㅇㄹ";
    HAction.Execute("InsertText", HParameterSet.HInsertText.HSet);
}
function OnDocument_Open()
{
    HAction.GetDefault("InsertText", HParameterSet.HInsertText.HSet);
    HParameterSet.HInsertText.Text = "ㅋㅌㅊㅍㅋㅌㅊㅍ";
    HAction.Execute("InsertText", HParameterSet.HInsertText.HSet);
}</code>
```

#### `get_selected_pos()`

현재 설정된 블록의 위치정보를 얻어온다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_selected_pos()
(True, 0, 0, 16, 0, 7, 16)
&gt;&gt;&gt; marked_area = hwp.get_selected_pos()
&gt;&gt;&gt; # 임의의 영역으로 이동 후, 저장한 구간을 선택하기
&gt;&gt;&gt; hwp.select_text(marked_area)
True</code>
```

#### `get_selected_pos_by_set(sset, eset)`

현재 설정된 블록의 위치정보를 얻어온다.

(GetSelectedPos의 ParameterSet버전) 실행 전 GetPos 형태의 파라미터셋 두 개를 미리 만들어서 인자로 넣어줘야 한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 선택할 블록의 시작 위치에 캐럿을 둔 상태로
&gt;&gt;&gt; sset = hwp.get_pos_by_set()
&gt;&gt;&gt; # 블록 끝이 될 부분으로 이동한 후에
&gt;&gt;&gt; eset = hwp.get_pos_by_set()
&gt;&gt;&gt; hwp.get_selected_pos_by_set(sset, eset)
&gt;&gt;&gt; hwp.set_pos_by_set(eset)
True</code>
```

#### `get_selected_range()`

선택한 범위의 셀주소를 리스트로 리턴함

캐럿이 표 안에 있어야 함

#### `get_selected_text(as_='str', keep_select=False)`

한/글 문서 선택 구간의 텍스트를 리턴하는 메서드. 표 안에 있을 때는 셀의 문자열을, 본문일 때는 선택영역 또는 현재 단어를 리턴.

Parameters:

Returns: 선택한 문자열 또는 셀 문자열

#### `get_style()`

현재 캐럿이 위치한 문단의 스타일정보를 사전 형태로 리턴한다.

Returns:

#### `get_style_dict(as_='list')`

스타일 목록을 사전 데이터로 리턴하는 메서드. (도움 주신 kosohn님께 아주 큰 감사!!!)

#### `get_table_height(as_='mm')`

현재 캐럿이 속한 표의 높이(mm)를 리턴함

Returns: 표의 높이(mm)

#### `get_table_outside_margin(as_='mm')`

표의 바깥 여백을 딕셔너리로 한 번에 리턴하는 메서드

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_table_outside_margin()
{'left': 4.0, 'right': 3.0, 'top': 2.0, 'bottom': 1.0}</code>
```

#### `get_table_outside_margin_bottom(as_='mm')`

표의 바깥 하단 여백값을 리턴하는 메서드

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_table_outside_margin_bottom()
1.0</code>
```

#### `get_table_outside_margin_left(as_='mm')`

표의 바깥 왼쪽 여백값을 리턴하는 메서드

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_table_outside_margin_left()
4.0</code>
```

#### `get_table_outside_margin_right(as_='mm')`

표의 바깥 오른쪽 여백값을 리턴하는 메서드

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_table_outside_margin_left()
3.0</code>
```

#### `get_table_outside_margin_top(as_='mm')`

표의 바깥 상단 여백값을 리턴하는 메서드

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_table_outside_margin_top()
2.0</code>
```

#### `get_table_width(as_='mm')`

현재 캐럿이 속한 표의 너비(mm)를 리턴함.

이 때 수치의 단위는 as\_ 파라미터를 통해 변경 가능하며, "mm", "HwpUnit", "Pt", "Inch" 등을 쓸 수 있다.

Returns:

#### `get_text()`

문서 내에서 텍스트를 얻어온다.

줄바꿈 기준으로 텍스트를 얻어오므로 반복실행해야 한다. get\_text()의 사용이 끝나면 release\_scan()을 반드시 호출하여 관련 정보를 초기화 해주어야 한다. get\_text()로 추출한 텍스트가 있는 문단으로 캐럿을 이동 시키려면 move\_pos(201)을 실행하면 된다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.init_scan()
&gt;&gt;&gt; while True:
...     state, text = hwp.get_text()
...     print(state, text)
...     if state &lt;= 1:
...         break
... hwp.release_scan()
2
2
2 ㅁㄴㅇㄹ
3
4 ㅂㅈㄷㄱ
2 ㅂㅈㄷㄱ
5
1</code>
```

#### `get_text_file(format='UNICODE', option='saveblock:true')`

현재 열린 문서 전체 또는 선택한 범위를 문자열로 리턴한다.

이 함수는 JScript나 VBScript와 같이 직접적으로 local disk를 접근하기 힘든 언어를 위해 만들어졌으므로 disk를 접근할 수 있는 언어에서는 사용하지 않기를 권장. disk를 접근할 수 있다면, Save나 SaveBlockAction을 사용할 것. 이 함수 역시 내부적으로는 save나 SaveBlockAction을 호출하도록 되어있고 텍스트로 저장된 파일이 메모리에서 3~4번 복사되기 때문에 느리고, 메모리를 낭비함.

팁1: `hwp.Copy()`, `hwp.Paste()` 대신 get\_text\_file/set\_text\_file을 사용하기 추천.

팁2: `format="HTML"`로 추출시 표번호가 유지된다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-rust">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_text_file()
'ㅁㄴㅇㄹ\r\nㅁㄴㅇㄹ\r\nㅁㄴㅇㄹ\r\n\r\nㅂㅈㄷㄱ\r\nㅂㅈㄷㄱ\r\nㅂㅈㄷㄱ\r\n'</code>
```

#### `get_title()`

한/글 프로그램의 타이틀을 조회한다. 내부적으로 윈도우핸들을 이용한다.

SetTitleName이라는 못난 이름의 API가 있는데, 차마 get\_title\_name이라고 따라짓지는 못했다ㅜ (파일명을 조회하려면 title 대신 Path나 FullName 등을 조회하면 된다.)

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; print(hwp.get_title())
빈 문서 1 - 한글</code>
```

#### `get_used_style_dict(as_='list')`

현재 문서에서 사용된 스타일 목록만 list\[dict\] 또는 dict\[dict\] 데이터로 리턴하는 메서드.

#### `goto_addr(addr='A1', col=0, select_cell=False)`

셀 주소를 문자열로 입력받아 해당 주소로 이동하는 메서드. 셀 주소는 "C3"처럼 문자열로 입력하거나, 행번호, 열번호를 입력할 수 있음. 시작값은 1.

Parameters:

Returns:

#### `goto_page(page_index=1)`

새쪽번호와 관계없이 페이지 순서를 통해

특정 페이지를 찾아가는 메서드. 1이 1페이지임.

Parameters:

Returns:

#### `goto_printpage(page_num=1)`

인쇄페이지 기준으로 해당 페이지로 이동

1페이지의 page\_num은 1이다.

Parameters:

Returns:

#### `goto_style(style)`

특정 스타일이 적용된 위치로 이동하는 메서드.

탐색은 문서아랫방향으로만 수행하며 현재위치 이후 해당 스타일이 없거나, 스타일이름/인덱스번호가 잘못된 경우 False를 리턴 참고로, API의 Goto는 1부터 시작하므로 메서드 내부에서 인덱스에 1을 더하고 있음

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.goto_style(0)  # 캐럿 뒤의 "바탕글" 스타일로 이동
True
&gt;&gt;&gt; hwp.goto_style("개요 1")  # 캐럿 뒤의 "개요 1" 스타일로 이동
True</code>
```

#### `gradation_on_cell(color_list=[(0, 0, 0), (255, 255, 255)], grad_type='Linear', angle=0, xc=0, yc=0, pos_list=None, step_center=50, step=255)`

셀에 그라데이션을 적용하는 메서드

[![gradation_on_cell](https://martiniifun.github.io/pyhwpx/assets/gradation_on_cell.gif)](https://martiniifun.github.io/pyhwpx/assets/gradation_on_cell.gif)

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; for i in range(0, 256, 2):
...     hwp.gradation_on_cell(
...         color_list=[(255,i,i), (i,255,i)],
...         grad_type="Square",
...         xc=40, yc=60,
...         pos_list=[20,80],
...         step_center=int(i/255*100),
...         step=i,
...     )
...</code>
```

#### `hwp_unit_to_inch(HwpUnit)` <small><code>staticmethod</code></small>

HwpUnit을 인치로 변환

#### `hwp_unit_to_point(HwpUnit)` <small><code>staticmethod</code></small>

HwpUnit을 포인트 단위로 변환

#### `import_mathml(mml_path, delay=0.2)`

MathML 포맷의 수식문서 파일경로를 입력하면

아래아한글 수식으로 삽입하는 함수

#### `import_style(sty_filepath)`

미리 저장된 특정 sty파일의 스타일을 임포트한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.import_style("C:/Users/User/Desktop/new_style.sty")
True</code>
```

#### `inch_to_hwp_unit(inch)` <small><code>staticmethod</code></small>

인치 단위를 HwpUnit으로 변환

#### `init_scan(option=7, range=119, spara=0, spos=0, epara=-1, epos=-1)`

문서의 내용을 검색하기 위해 초기설정을 한다.

문서의 검색 과정은 InitScan()으로 검색위한 준비 작업을 하고 GetText()를 호출하여 본문의 텍스트를 얻어온다. GetText()를 반복호출하면 연속하여 본문의 텍스트를 얻어올 수 있다. 검색이 끝나면 ReleaseScan()을 호출하여 관련 정보를 Release해야 한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.init_scan(range=0xff)
&gt;&gt;&gt; _, text = hwp.get_text()
&gt;&gt;&gt; hwp.release_scan()
&gt;&gt;&gt; print(text)
Hello, world!</code>
```

#### `insert(path, format='', arg='', move_doc_end=False)`

현재 캐럿 위치에 문서파일을 삽입한다.

`format`, `arg` 파라미터에 대한 자세한 설명은 `open` 참조

Parameters:

Returns:

#### `insert_background_picture(path, border_type='SelectedCell', embedded=True, filloption=5, effect=0, watermark=False, brightness=0, contrast=0)`

**셀**에 배경이미지를 삽입한다.

CellBorderFill의 SetItem 중 FillAttr 의 SetItem FileName 에 이미지의 binary data를 지정해 줄 수가 없어서 만든 함수다. 기타 배경에 대한 다른 조정은 Action과 ParameterSet의 조합으로 가능하다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.insert_background_picture(path="C:/Users/User/Desktop/KakaoTalk_20230709_023118549.jpg")
True</code>
```

#### `insert_ctrl(ctrl_id, initparam)`

현재 캐럿 위치에 컨트롤을 삽입한다.

ctrlid에 지정할 수 있는 컨트롤 ID는 HwpCtrl.CtrlID가 반환하는 ID와 동일하다. 자세한 것은 Ctrl 오브젝트 Properties인 CtrlID를 참조. initparam에는 컨트롤의 초기 속성을 지정한다. 대부분의 컨트롤은 Ctrl.Properties와 동일한 포맷의 parameter set을 사용하지만, 컨트롤 생성 시에는 다른 포맷을 사용하는 경우도 있다. 예를 들어 표의 경우 Ctrl.Properties에는 "Table" 셋을 사용하지만, 생성 시 initparam에 지정하는 값은 "TableCreation" 셋이다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; # 3행5열의 표를 삽입한다.
&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; from time import sleep
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; tbset = hwp.create_set("TableCreation")
&gt;&gt;&gt; tbset.SetItem("Rows", 3)
&gt;&gt;&gt; tbset.SetItem("Cols", 5)
&gt;&gt;&gt; row_set = tbset.CreateItemArray("RowHeight", 3)
&gt;&gt;&gt; col_set = tbset.CreateItemArray("ColWidth", 5)
&gt;&gt;&gt; row_set.SetItem(0, hwp.mili_to_hwp_unit(10))
&gt;&gt;&gt; row_set.SetItem(1, hwp.mili_to_hwp_unit(10))
&gt;&gt;&gt; row_set.SetItem(2, hwp.mili_to_hwp_unit(10))
&gt;&gt;&gt; col_set.SetItem(0, hwp.mili_to_hwp_unit(26))
&gt;&gt;&gt; col_set.SetItem(1, hwp.mili_to_hwp_unit(26))
&gt;&gt;&gt; col_set.SetItem(2, hwp.mili_to_hwp_unit(26))
&gt;&gt;&gt; col_set.SetItem(3, hwp.mili_to_hwp_unit(26))
&gt;&gt;&gt; col_set.SetItem(4, hwp.mili_to_hwp_unit(26))
&gt;&gt;&gt; table = hwp.insert_ctrl("tbl", tbset)  # &lt;---
&gt;&gt;&gt; sleep(3)  # 표 생성 3초 후 다시 표 삭제
&gt;&gt;&gt; hwp.delete_ctrl(table)</code>
```

#### `insert_lorem(para_num=1)`

Lorem Ipsum을 캐럿 위치에 작성한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.insert_lorem(3)
True</code>
```

#### `insert_memo(text='', memo_type='memo')`

선택한 단어 범위에 메모고침표를 삽입하는 코드.

한/글에서 일반 문자열을 삽입하는 코드와 크게 다르지 않다. 선택모드가 아닌 경우 캐럿이 위치한 단어에 메모고침표를 삽입한다.

Parameters:

Returns:

#### `insert_picture(path, treat_as_char=True, embedded=True, sizeoption=0, reverse=False, watermark=False, effect=0, width=0, height=0)`

현재 캐럿의 위치에 그림을 삽입한다.

다만, 그림의 종횡비를 유지한 채로 셀의 높이만 키워주는 옵션이 없다. 이런 작업을 원하는 경우에는 그림을 클립보드로 복사하고, Ctrl-V로 붙여넣기를 하는 수 밖에 없다. 또한, 셀의 크기를 조절할 때 이미지의 크기도 따라 변경되게 하고 싶다면 insert\_background\_picture 함수를 사용하는 것도 좋다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; path = "C:/Users/Administrator/Desktop/KakaoTalk_20230709_023118549.jpg"
&gt;&gt;&gt; ctrl = hwp.insert_picture(path)  # 삽입한 이미지 객체를 리턴함.
&gt;&gt;&gt; pset = ctrl.Properties  # == hwp.create_set("ShapeObject")
&gt;&gt;&gt; pset.SetItem("TreatAsChar", False)  # 글자처럼취급 해제
&gt;&gt;&gt; pset.SetItem("TextWrap", 2)  # 그림을 글 뒤로
&gt;&gt;&gt; ctrl.Properties = pset  # 설정한 값 적용(간단!)</code>
```

#### `insert_random_picture(x=200, y=200)`

랜덤 이미지를 삽입한다.

내부적으로 `https://picsum.photos/` API를 사용한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.insert_random_picture(640, 480)
&lt;CtrlCode: CtrlID=gso, CtrlCH=11, UserDesc=그림&gt;</code>
```

#### `insert_text(text)`

한/글 문서 내 캐럿 위치에 문자열을 삽입하는 메서드.

Returns: 삽입 성공시 True, 실패시 False를 리턴함. Examples: >>> from pyhwpx import Hwp >>> hwp = Hwp() >>> hwp.insert\_text('Hello world!') >>> hwp.BreakPara()

#### `is_action_enable(action_id)`

액션 실행 가능한지 여부를 bool로 리턴

액션 관련해서는 기존 버전체크보다 이걸 사용하는 게 훨씬 안정적일 것 같기는 하지만(예: CopyPage, PastePage, DeletePage 및 메타태그액션 등) 신규 메서드(SelectCtrl 등) 지원여부는 체크해주지 못한다ㅜ

#### `is_cell()`

캐럿이 현재 표 안에 있는지 알려주는 메서드

Returns: 표 안에 있으면 True, 그렇지 않으면 False를 리턴

#### `is_command_lock(action_id)`

해당 액션이 잠겨있는지 확인한다.

Parameters:

Returns:

#### `is_empty_para()`

본문의 문단을 순회하면서 특정 서식을 적용할 때 빈 문단에서 MoveNext~ 또는 MovePrev~ 등의 액션이 오작동하므로 이를 방지하기 위한 개발자용 헬퍼메서드. 단독으로는 활용하지 말 것.

Returns: 빈 문단일 경우 제자리에서 True, 비어있지 않은 경우 False를 리턴

#### `key_indicator()`

상태 바의 정보를 얻어온다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; # 현재 셀 주소(표 안에 있을 때)
&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.key_indicator()[-1][1:].split(")")[0]
"A1"</code>
```

#### `lock_command(act_id, is_lock)`

특정 액션이 실행되지 않도록 잠근다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; # Undo와 Redo 잠그기
&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.lock_command("Undo", True)
&gt;&gt;&gt; hwp.lock_command("Redo", True)</code>
```

#### `maximize_window()`

현재 창 최대화

#### `minimize_window()`

현재 창 최소화

#### `move_all_caption(location='Bottom', align='Justify')`

한/글 문서 내 모든 표, 그림의 주석 위치를 일괄 변경하는 메서드.

#### `move_pos(move_id=1, para=0, pos=0)`

캐럿의 위치를 옮긴다.

move\_id를 200(moveScrPos)으로 지정한 경우에는 스크린 좌표로 마우스 커서의 (x,y)좌표를 그대로 넘겨주면 된다. 201(moveScanPos)는 문서를 검색하는 중 캐럿을 이동시키려 할 경우에만 사용이 가능하다. (솔직히 200 사용법은 잘 모르겠다;)

Parameters:

Returns:

#### `move_to_ctrl(ctrl, option=0)`

메서드에 넣은 ctrl의 조판부호 앞으로 이동하는 메서드.

Parameters:

Returns:

#### `move_to_field(field, idx=0, text=True, start=True, select=False)`

지정한 필드로 캐럿을 이동한다.

Parameters:

Returns:

#### `move_to_metatag(tag, text, start, select)`

특정 메타태그로 이동

#### `new_number(new_number, num_type='Page')`

새 번호를 매길 수 있는 메서드.

(쪽번호 외에도 그림, 각주, 표, 미주, 수식 등) 다만, 주의할 점이 세 가지 있다. 1. 기존에 쪽번호가 없는 문서에서는 작동하지 않으므로 쪽번호가 정의되어 있어야 한다. (쪽번호 정의는 PageNumPos 메서드 참조) 2. 새 번호를 지정한 페이지 및 이후 모든 페이지가 영향을 받는다. 3. NewNumber 실행시점의 캐럿위치 뒤쪽(해당 페이지 내)에 NewNumber 조판이 있는 경우, 삽입한 조판은 무효가 된다. (페이지 맨 뒤쪽의 새 번호만 유효함)

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; # 쪽번호가 있는 문서에서
&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.NewNumber(5)  # 현재 페이지번호가 5로 바뀜</code>
```

#### `new_number_modify(new_number, num_type='Page')`

새 번호 조판을 수정할 수 있는 메서드.

실행 전 \[새 번호\] 조판 옆에 캐럿이 위치해 있어야 하며, 그렇지 않을 경우 (쪽번호 외에도 그림, 각주, 표, 미주, 수식 등) 다만, 주의할 점이 세 가지 있다.

```text
1. 기존에 쪽번호가 없는 문서에서는 작동하지 않으므로 쪽번호가 정의되어 있어야 한다. (쪽번호 정의는 `PageNumPos` 메서드 참조)
2. 새 번호를 지정한 페이지 및 이후 모든 페이지가 영향을 받는다.
3. `NewNumber` 실행시점의 캐럿위치 뒤쪽(해당 페이지 내)에 `NewNumber` 조판이 있는 경우, 삽입한 조판은 무효가 된다. (페이지 맨 뒤쪽의 새 번호만 유효함)
```

Parameters:

Returns:

#### `open(filename, format='', arg='')`

문서를 연다.

Parameters:

Returns:

#### `open_pdf(pdf_path, this_window=1)`

pdf를 hwp문서로 변환하여 여는 함수.

(최초 실행시 "다시 표시 안함ㅁ" 체크박스에 체크를 해야 한다.)

Parameters:

Returns:

#### `page_num_pos(global_start=1, position='BottomCenter', number_format='Digit', side_char=True)`

문서 전체에 쪽번호를 삽입하는 메서드.

Parameters:

Returns:

#### `paste(option=4)`

붙여넣기 확장메서드.

(참고로 paste가 아닌 Paste는 API 그대로 작동한다.)

Parameters:

#### `point_to_hwp_unit(point)`

글자에 쓰이는 포인트 단위를 HwpUnit으로 변환

#### `protect_private_info(protecting_char, private_pattern_type)`

개인정보를 보호한다.

한/글의 경우 “찾아서 보호”와 “선택 글자 보호”를 다른 기능으로 구현하였지만, API에서는 하나의 함수로 구현한다.

Parameters:

Returns:

#### `put_field_text(field='', text='', idx=None)`

지정한 필드의 내용을 채운다.

현재 필드에 입력되어 있는 내용은 지워진다. 채워진 내용의 글자모양은 필드에 지정해 놓은 글자모양을 따라간다. fieldlist의 필드 개수와, textlist의 텍스트 개수는 동일해야 한다. 존재하지 않는 필드에 대해서는 무시한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 현재 캐럿 위치에 zxcv 필드 생성
&gt;&gt;&gt; hwp.create_field("zxcv")
&gt;&gt;&gt; # zxcv 필드에 "Hello world!" 텍스트 삽입
&gt;&gt;&gt; hwp.put_field_text("zxcv", "Hello world!")</code>
```

#### `put_metatag_name_text(tag, text)`

메타태그에 텍스트 삽입

#### `quit(save=False)`

한/글을 종료한다.

단, 저장되지 않은 변경사항이 있는 경우 팝업이 뜨므로 clear나 save 등의 메서드를 실행한 후에 quit을 실행해야 한다.

Parameters:

Returns:

#### `register_module(module_type='FilePathCheckDLL', module_data='FilePathCheckerModule')`

(인스턴스 생성시 자동으로 실행된다.)

한/글 컨트롤에 부가적인 모듈을 등록한다. 사용자가 모르는 사이에 파일이 수정되거나 서버로 전송되는 것을 막기 위해 한/글 오토메이션은 파일을 불러오거나 저장할 때 사용자로부터 승인을 받도록 되어있다. 그러나 이미 검증받은 웹페이지이거나, 이미 사용자의 파일 시스템에 대해 강력한 접근 권한을 갖는 응용프로그램의 경우에는 이러한 승인절차가 아무런 의미가 없으며 오히려 불편하기만 하다. 이런 경우 register\_module을 통해 보안승인모듈을 등록하여 승인절차를 생략할 수 있다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 사전에 레지스트리에 보안모듈이 등록되어 있어야 한다.
&gt;&gt;&gt; # 보다 자세한 설명은 공식문서 참조
&gt;&gt;&gt; hwp.register_module("FilePathChekDLL", "FilePathCheckerModule")
True</code>
```

#### `register_private_info_pattern(private_type, private_pattern)`

개인정보의 패턴을 등록한다.

(현재 작동하지 않는다.)

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp()
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt;
&gt;&gt;&gt; hwp.register_private_info_pattern(0x01, "NNNN-NNNN;NN-NN-NNNN-NNNN")  # 전화번호패턴</code>
```

#### `register_regedit(dll_name='FilePathCheckerModule.dll')` <small><code>staticmethod</code></small>

레지스트리 에디터에 한/글 보안모듈을 자동등록하는 메서드.

가장 먼저 파이썬과 pyhwpx 모듈이 설치된 상태라고 가정하고 'site-packages/pyhwpx' 폴더에서 'FilePathCheckerModule.dll' 파일을 찾는다. 두 번째로는 pyinstaller로 컴파일했다고 가정하고, MEIPASS 하위폴더를 탐색한다. 이후로, 차례대로 실행파일과 동일한 경로, 사용자 폴더를 탐색한 후에도 보안모듈 dll파일을 찾지 못하면 아래아한글 깃헙 저장소에서 직접 보안모듈을 다운받아 사용자 폴더에 설치하고, 레지스트리를 수정한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()  # 이 때 내부적으로 register_regedit를 실행한다.</code>
```

#### `release_scan()`

InitScan()으로 설정된 초기화 정보를 해제한다.

텍스트 검색작업이 끝나면 반드시 호출하여 설정된 정보를 해제해야 한다.

Returns:

#### `remove_background_picture()`

표 안에 백그라운드 이미지가 삽입되어 있고,

캐럿이 해당 셀 안에 들어있는 경우, 이를 제거하는 메서드

Returns:

#### `remove_unused_styles(alt=0)`

문서 내에 정의만 되어 있고 실제 사용되지 않은 모든 스타일을 일괄제거하는 메서드. 사용에 주의할 것.

#### `rename_field(oldname, newname)`

지정한 필드의 이름을 바꾼다.

예를 들어 oldname에 "title{{0}}\\x02title{{1}}", newname에 "tt1\\x02tt2로 지정하면 첫 번째 title은 tt1로, 두 번째 title은 tt2로 변경된다. oldname의 필드 개수와, newname의 필드 개수는 동일해야 한다. 존재하지 않는 필드에 대해서는 무시한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.create_field("asdf")  # "asdf" 필드 생성
&gt;&gt;&gt; hwp.rename_field("asdf", "zxcv")  # asdf 필드명을 "zxcv"로 변경
&gt;&gt;&gt; hwp.put_field_text("zxcv", "Hello world!")  # zxcv 필드에 텍스트 삽입</code>
```

#### `rename_metatag(oldtag, newtag)`

메타태그 이름 변경

#### `replace_action(old_action_id, new_action_id)`

특정 Action을 다른 Action으로 대체한다.

이는 메뉴나 단축키로 호출되는 Action을 대체할 뿐, CreateAction()이나, Run() 등의 함수를 이용할 때에는 아무런 영향을 주지 않는다. 즉, ReplaceAction(“Cut", "Copy")을 호출하여 ”오려내기“ Action을 ”복사하기“ Action으로 교체하면 Ctrl+X 단축키나 오려내기 메뉴/툴바 기능을 수행하더라도 복사하기 기능이 수행되지만, 코드 상에서 Run("Cut")을 실행하면 오려내기 Action이 실행된다. 또한, 대체된 Action을 원래의 Action으로 되돌리기 위해서는 NewActionID의 값을 원래의 Action으로 설정한 뒤 호출한다. 이를테면 이런 식이다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.replace_action("Cut", "Cut")</code>
```

#### `resize_image(width=None, height=None, unit='mm')`

이미지 또는 그리기 개체의 크기를 조절하는 메서드.

해당개체 선택 후 실행해야 함.

#### `rgb_color(red_or_colorname, green=255, blue=255)`

RGB값을 한/글이 인식하는 정수 형태로 변환해주는 헬퍼 메서드.

[![rgb_color / RGBColor](https://martiniifun.github.io/pyhwpx/assets/rgb_color.gif)](https://martiniifun.github.io/pyhwpx/assets/rgb_color.gif)

주로 글자색이나, 셀 색깔을 적용할 때 사용한다. RGB값을 세 개의 정수로 입력하는 것이 기본적인 사용방법이지만, 자주 사용되는 아래의 24가지 색깔은 문자열로 입력 가능하다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.set_font(TextColor=hwp.RGBColor("Red"))  # 글자를 빨강으로
&gt;&gt;&gt; hwp.insert_text("빨간 글자색\r\n")
&gt;&gt;&gt; hwp.set_font(ShadeColor=hwp.RGBColor(0, 255, 0))  # 음영을 녹색으로
&gt;&gt;&gt; hwp.insert_text("초록 음영색")</code>
```

#### `run_script_macro(function_name, u_macro_type=0, u_script_type=0)`

한/글 문서 내에 존재하는 매크로를 실행한다.

문서매크로, 스크립트매크로 모두 실행 가능하다. 재미있는 점은 한/글 내에서 문서매크로 실행시 New, Open 두 개의 함수 밖에 선택할 수 없으므로 별도의 함수를 정의하더라도 이 두 함수 중 하나에서 호출해야 하지만, (진입점이 되어야 함) self.hwp.run\_script\_macro 명령어를 통해서는 제한없이 실행할 수 있다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; hwp.run_script_macro("OnDocument_New", u_macro_type=1)
True
&gt;&gt;&gt; hwp.run_script_macro("OnScriptMacro_중국어1성")
True</code>
```

#### `save(save_if_dirty=True)`

현재 편집중인 문서를 저장한다.

문서의 경로가 지정되어있지 않으면 “새 이름으로 저장” 대화상자가 뜬다.

Parameters:

Returns:

#### `save_all_pictures(save_path='./binData')`

현재 문서에 삽입된 모든 이미지들을

삽입 당시 파일명으로 복원하여 저장. 단, 문서 안에서 복사했거나 중복삽입한 이미지는 한 개만 저장됨. 기본 저장폴더명은 ./binData이며 기존에 save\_path가 존재하는 경우, 그 안의 파일들은 삭제되므로 유의해야 함.

Parameters:

Returns:

#### `save_as(path, format='HWP', arg='', split_page=False)`

현재 편집중인 문서를 지정한 이름으로 저장한다.

format, arg의 일반적인 개념에 대해서는 Open()참조.

Parameters:

Returns:

#### `save_pdf_as_image(path='', img_format='bmp')`

문서보안이나 복제방지를 위해 모든 페이지를 이미지로 변경 후 PDF로 저장하는 메서드.

아무 인수가 주어지지 않는 경우 모든 페이지를 bmp로 저장한 후에 현재 폴더에 {문서이름}.pdf로 저장한다. (만약 저장하지 않은 빈 문서의 경우에는 result.pdf로 저장한다.)

Parameters:

Returns:

#### `select_ctrl(ctrl, anchor_type=0, option=1)`

인수로 넣은 컨트롤 오브젝트를 선택하는 pyhwpx 전용 메서드.

Parameters:

Returns:

#### `select_text(spara=0, spos=0, epara=0, epos=0, slist=0)`

특정 범위의 텍스트를 블록선택한다. (epos가 가리키는 문자는 포함되지 않는다.) hwp.get\_selected\_pos()를 통해 저장한 위치로 돌아가는 데에도 사용된다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; # 본문의 세 번째 문단 전체 선택하기(기본 사용법)
&gt;&gt;&gt; hwp.select_text(2, 0, 2, -1, 0)
True
&gt;&gt;&gt; # 임의의 영역으로 이동 후 저장한 위치로 되돌아가기
&gt;&gt;&gt; selected_range = hwp.get_selected_pos()
&gt;&gt;&gt; hwp.select_text(selected_range)
True</code>
```

#### `select_text_by_get_pos(s_getpos, e_getpos)`

hwp.get\_pos()로 얻은 두 튜플 사이의 텍스트를 선택하는 메서드.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; s_pos = hwp.get_pos()  # 선택 시작부분 저장
&gt;&gt;&gt; # 이래저래 좌표 이동 후
&gt;&gt;&gt; e_pos = hwp.get_pos()  # 선택 끝부분 저장
&gt;&gt;&gt; # 이래저래 또 좌표 이동 후
&gt;&gt;&gt; hwp.select_text_by_get_pos(s_pos, e_pos)
True</code>
```

#### `set_cell_margin(left=1.8, right=1.8, top=0.5, bottom=0.5, as_='mm')`

표 중 커서가 위치한 셀 또는 다중선택한 모든 셀의 안 여백을 지정하는 메서드.

표 안에서만 실행가능하며, 전체 셀이 아닌 표 자체를 선택한 상태에서는 여백이 적용되지 않음. 차례대로 왼쪽, 오른쪽, 상단, 하단의 여백을 밀리미터(기본값) 또는 HwpUnit 단위로 지정.

Parameters:

Returns:

#### `set_charshape(pset)`

get\_charshape 또는 get\_charshape\_as\_dict를 통해 저장된 파라미터셋을 통해 캐럿위치 또는 특정 선택영역에 해당 글자모양을 적용할 수 있다.

Parameters:

#### `set_col_width(width, as_='ratio')`

칼럼의 너비를 변경하는 메서드.

정수(int)나 부동소수점수(float) 입력시 현재 칼럼의 너비가 변경되며, 리스트나 튜플 등 iterable 타입 입력시에는 각 요소들의 비에 따라 칼럼들의 너비가 일괄변경된다. 예를 들어 3행 3열의 표 안에서 set\_col\_width(\[1,2,3\]) 을 실행하는 경우 1열너비:2열너비:3열너비가 1:2:3으로 변경된다. (표 전체의 너비가 148mm라면, 각각 24mm : 48mm : 72mm로 변경된다는 뜻이다.)

단, 열너비의 비가 아닌 "mm" 단위로 값을 입력하려면 as\_="mm"로 파라미터를 수정하면 된다. 이 때, width에 정수 또는 부동소수점수를 입력하는 경우 as\_="ratio"를 사용할 수 없다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.create_table(3,3)
True
&gt;&gt;&gt; hwp.get_into_nth_table(0)
True
&gt;&gt;&gt; hwp.set_col_width([1,2,3])
True</code>
```

#### `set_cur_field_name(field='', direction='', memo='', option=0)`

표 안에서 현재 캐럿이 위치하는 셀, 또는 블록선택한 셀들의 필드이름을 설정한다.

GetFieldList()의 옵션 중에 4(hwpFieldSelection) 옵션은 사용하지 않는다.

셀필드가 아닌 누름틀 생성은 `create_field` 메서드를 이용해야 한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.create_table(5, 5, True)  # 3행3열의 글자처럼 취급한 표 생성(A1셀로 이동)
&gt;&gt;&gt; hwp.TableCellBlockExtendAbs()
&gt;&gt;&gt; hwp.TableCellBlockExtend()  # 셀 전체 선택
&gt;&gt;&gt; hwp.set_cur_field_name("target_table")  # 모든 셀의 셀필드 이름을 "target_table"로 바꿈
&gt;&gt;&gt; hwp.put_field_text("target_table", list(range(1, 26)))  # 각 셀에 1~25까지의 정수를 넣음
&gt;&gt;&gt; hwp.set_cur_field_name("")  # 셀필드 초기화
&gt;&gt;&gt; hwp.Cancel()  # 셀블록 선택취소</code>
```

#### `set_field_by_bracket()`

필드를 지정하는 일련의 반복작업을 간소화하기 위한 메서드.

중괄호 두 겹({{}})으로 둘러싸인 구문을 누름틀로 변환해준다. 만약 본문에 "{{name}}"이라는 문구가 있었다면 해당 단어를 삭제하고 그 위치에 name이라는 누름틀을 생성한다.

지시문(direction)과 메모(memo)도 추가가 가능한데, "{{name:direction}}" 또는 "{{name:direction:memo}}" 방식으로 콜론으로 구분하여 지정할 수 있다. (가급적 direction을 지정해주도록 하자. 그렇지 않으면 누름틀이 보이지 않는다.) 셀 안에서 누름틀을 삽입할 수도 있지만, 편의상 셀필드를 삽입하고 싶은 경우 "\[\[name\]\]"으로 지정하면 된다.

Returns:

#### `set_font(Bold='', DiacSymMark='', Emboss='', Engrave='', FaceName='', FontType=1, Height='', Italic='', Offset='', OutLineType='', Ratio='', ShadeColor='', ShadowColor='', ShadowOffsetX='', ShadowOffsetY='', ShadowType='', Size='', SmallCaps='', Spacing='', StrikeOutColor='', StrikeOutShape='', StrikeOutType='', SubScript='', SuperScript='', TextColor='', UnderlineColor='', UnderlineShape='', UnderlineType='', UseFontSpace='', UseKerning='')`

글자모양을 메서드 형태로 수정할 수 있는 메서드.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.SelectAll()  # 전체선택
&gt;&gt;&gt; hwp.set_font(FaceName="D2Coding", TextColor="Orange")</code>
```

#### `set_linespacing(value=160, method='Percent')`

현재 캐럿 위치의 문단 또는 선택 블록의 줄간격(%) 설정

Parameters:

Returns: 성공시 True, 실패시 False를 리턴

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.SelectAll()  # 전체선택
&gt;&gt;&gt; hwp.set_linespacing(160)  # 본문 모든 문단의 줄간격을 160%로 변경
True
&gt;&gt;&gt; hwp.set_linespacing(20, method="BetweenLines")  # 본문 모든 문단의 줄간격을 "여백만 지정"으로 20pt 적용
True</code>
```

#### `set_message_box_mode(mode)`

메시지박스 버튼 자동클릭

한/글에서 쓰는 다양한 메시지박스가 뜨지 않고,

자동으로 특정 버튼을 클릭한 효과를 주기 위해 사용한다. 한/글에서 한/글이 로드된 후 SetMessageBoxMode()를 호출해서 사용한다. SetMessageBoxMode는 하나의 파라메터를 받으며, 해당 파라메터는 자동으로 스킵할 버튼의 값으로 설정된다. 예를 들어, MB\_OK\_IDOK (0x00000001)값을 주면, MB\_OK형태의 메시지박스에서 OK버튼이 눌린 효과를 낸다.

Parameters:

Returns:

#### `set_pagedef(pset, apply='cur')`

get\_pagedef 또는 get\_pagedef\_as\_dict를 통해 얻은 용지정보를 현재구역에 적용하는 메서드

Parameters:

Returns:

#### `set_para(AlignType=None, BreakNonLatinWord=None, LineSpacing=None, Condense=None, SnapToGrid=None, NextSpacing=None, PrevSpacing=None, Indentation=None, RightMargin=None, LeftMargin=None, PagebreakBefore=None, KeepLinesTogether=None, KeepWithNext=None, WidowOrphan=None, AutoSpaceEAsianNum=None, AutoSpaceEAsianEng=None, LineWrap=None, FontLineHeight=None, TextAlignment=None)`

문단 모양을 설정하는 단축메서드. set\_font와 유사하게 함수처럼 문단 모양을 설정할 수 있다. 미리 정의된 별도의 파라미터셋을 통해 문단모양을 적용하고 싶다면 set\_parashape 메서드를 사용한다.

Parameters:

Returns:

#### `set_parashape(pset)`

get\_parashape 또는 get\_parashape\_as\_dict를 통해 저장된 파라미터셋을 통해 캐럿이 포함된 문단 또는 블록선택한 문단 전체에 해당 문단모양을 적용할 수 있다.

#### `set_pos(List, para, pos)`

캐럿을 문서 내 특정 위치로 옮기기

지정된 좌표로 캐럿을 옮겨준다.

Parameters:

Returns:

#### `set_pos_by_set(disp_val)`

캐럿을 ParameterSet으로 얻어지는 위치로 옮긴다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; start_pos = hwp.GetPosBySet()  # 현재 위치를 체크포인트처럼 저장하고,
&gt;&gt;&gt; # 특정 작업(이동 및 입력작업) 후에
&gt;&gt;&gt; hwp.set_pos_by_set(start_pos)  # 저장했던 위치로 되돌아가기</code>
```

#### `set_row_height(height, as_='mm')`

캐럿이 표 안에 있는 경우

캐럿이 위치한 행의 셀 높이를 조절하는 메서드(기본단위는 mm)

Parameters:

Returns:

#### `set_style(style)`

현재 캐럿이 위치한 문단의 스타일을 변경한다.

스타일 입력은 style 인수로 정수값(스타일번호) 또는 문자열(스타일이름)을 넣으면 된다.

Parameters:

Returns:

#### `set_table_inside_margin(left=1.8, right=1.8, top=0.5, bottom=0.5, as_='mm')`

표 내부 모든 셀의 안여백을 일괄설정하는 메서드.

표 전체를 선택하지 않고 표 내부에 커서가 있기만 하면 모든 셀에 적용됨.

Parameters:

Returns:

#### `set_table_outside_margin(left=-1.0, right=-1.0, top=-1.0, bottom=-1.0, as_='mm')`

표의 바깥여백을 변경하는 메서드.

기본 입력단위는 "mm"이며, "HwpUnit" 단위로 변경 가능.

Parameters:

Returns:

#### `set_table_width(width=0, as_='mm')`

표 전체의 너비를 원래 열들의 비율을 유지하면서 조정하는 메서드.

내부적으로 xml 파싱을 사용하는 방식으로 변경.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; # 모든 표의 너비를 본문여백(용지너비 - 좌측여백 - 우측여백 - 제본여백 - 표 좌우 바깥여백)에 맞추기
&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; i = 0
&gt;&gt;&gt; while hwp.get_into_nth_table(i):
...     hwp.set_table_width()
True</code>
```

#### `set_text_file(data, format='HWPML2X', option='insertfile')`

GetTextFile로 저장한 문자열 정보를 문서에 삽입

Parameters:

Returns:

#### `set_title(title='')`

한/글 프로그램의 타이틀을 변경한다.

파일명과 무관하게 설정할 수 있으며, 이모지 등 모든 특수문자를 허용한다. 단, 끝에는 항상 " - 한글"이 붙는다. 타이틀을 빈 문자열로 만들면 자동으로 원래 타이틀로 돌아간다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.open("asdf.hwp")
&gt;&gt;&gt; hwp.get_title()
asdf.hwp [c:\Users\user\desktop\] - 한글
&gt;&gt;&gt; hwp.set_title("😘")
&gt;&gt;&gt; hwp.get_title()
😘 - 한글</code>
```

#### `set_visible(visible)`

현재 조작중인 한/글 인스턴스의 백그라운드 숨김여부를 변경할 수 있다.

Parameters:

Returns:

#### `shape_copy_paste(Type='both', cell_attr=False, cell_border=False, cell_fill=False, cell_only=0)`

모양복사 메서드

[![introduce](https://martiniifun.github.io/pyhwpx/assets/shape_copy_paste.gif)](https://martiniifun.github.io/pyhwpx/assets/shape_copy_paste.gif)

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.get_into_nth_table(0)  # 문서 첫 번째 셀로 이동
&gt;&gt;&gt; hwp.shape_copy_paste()  # 모양복사 (무엇을 붙여넣을 건지는 "붙여넣기" 시점에 결정함)
&gt;&gt;&gt; hwp.TableCellBlockExtendAbs()
&gt;&gt;&gt; hwp.TableCellBlockExtend()  # 셀 전체 선택
&gt;&gt;&gt; hwp.shape_copy_paste(cell_fill=True)  # 글자&amp;문단모양, 셀음영만 붙여넣기</code>
```

#### `switch_to(num)`

여러 개의 hwp인스턴스가 열려 있는 경우 해당 인덱스의 문서창 인스턴스를 활성화한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.add_doc()
&gt;&gt;&gt; hwp.add_tab()
&gt;&gt;&gt; hwp.switch_to(0)</code>
```

#### `table_from_data(data, transpose=False, header0='', treat_as_char=False, header=True, index=True, cell_fill=False, header_bold=True)`

dict, list 또는 csv나 xls, xlsx 및 json처럼 2차원 스프레드시트로 표현 가능한 데이터에 대해서,

정확히는 pd.DataFrame으로 변환 가능한 데이터에 대해 아래아한글 표로 변환하는 작업을 한다. 내부적으로 판다스 데이터프레임으로 변환하는 과정을 거친다.

Parameters:

Returns:

#### `table_to_bottom(offset=0.0)`

표 앞에 캐럿을 둔 상태 또는 캐럿이 표 안에 있는 상태에서 위 함수 실행시

표를 (페이지 기준) 하단으로 위치시킨다.

Parameters:

Returns:

#### `table_to_csv(n='', filename='result.csv', encoding='utf-8', startrow=0)`

한/글 문서의 idx번째 표를 현재 폴더에 filename으로 csv포맷으로 저장한다.

filename을 지정하지 않는 경우 "./result.csv"가 기본값이다.

Returns: None을 리턴하고, 표데이터를 "./result.csv"에 저장한다.

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt;
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.table_to_csv(1, "table.csv")</code>
```

#### `table_to_df(n='', cols=0, selected_range=None, start_pos=None)`

(2025. 3. 3. RowSpan이랑 ColSpan을 이용해서, 중복되는 값은 그냥 모든 셀에 넣어버림

한/글 문서의 n번째 표를 판다스 데이터프레임으로 리턴하는 메서드. n을 넣지 않는 경우, 캐럿이 셀에 있다면 해당 표를 df로, 캐럿이 표 밖에 있다면 첫 번째 표를 df로 리턴한다.

Returns: 아래아한글 표 데이터를 가진 판다스 데이터프레임 인스턴스

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt;
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; df = hwp.table_to_df()  # 현재 캐럿이 들어가 있는 표 전체를 df로(1행을 df의 칼럼으로)
&gt;&gt;&gt; df = hwp.table_to_df(0, cols=2)  # 문서의 첫 번째 표를 df로(2번인덱스행(3행)을 칼럼명으로, 그 아래(4행부터)를 값으로)</code>
```

#### `table_to_df_q(n='', startrow=0, columns=[])`

(2024. 3. 14. for문 추출 구조에서, 한 번에 추출하는 방식으로 변경->속도개선)

한/글 문서의 n번째 표를 판다스 데이터프레임으로 리턴하는 메서드. n을 넣지 않는 경우, 캐럿이 셀에 있다면 해당 표를 df로, 캐럿이 표 밖에 있다면 첫 번째 표를 df로 리턴한다. startrow는 표 제목에 일부 병합이 되어 있는 경우 df로 변환시작할 행을 특정할 때 사용된다.

Returns: 아래아한글 표 데이터를 가진 판다스 데이터프레임 인스턴스

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt;
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; df = hwp.table_to_df(0)</code>
```

#### `unfill_addr_field()`

현재 캐럿이 들어있는 표의 셀필드를 모두 제거하는 메서드