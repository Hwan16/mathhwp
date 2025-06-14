## `pyhwpx.core.Ctrl`

아래아한글의 모든 개체(표, 그림, 글상자 및 각주/미주 등)를 다루기 위한 클래스.

### `CtrlCh` <small><code>property</code></small>

선택한 개체(Ctrl)의 타입 확인할 수 있는 컨트롤 문자를 리턴

일반적으로 컨트롤 ID를 사용해 컨트롤의 종류를 판별하지만, 이보다 더 포괄적인 범주를 나타내는 컨트롤 문자로 판별할 수도 있다. 예를 들어 각주와 미주는 ID는 다르지만, 컨트롤 문자는 17로 동일하다. 컨트롤 문자는 1부터 31사이의 값을 사용한다. (그럼에도, CtrlCh는 개인적으로 잘 사용하지 않는다.)

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()  # 표 두 개가 들어있는 문서에서
&gt;&gt;&gt; for ctrl in hwp.ctrl_list:
...     print(ctrl.CtrlCh)
...
11
11</code>
```

### `CtrlID` <small><code>property</code></small>

컨트롤 아이디

컨트롤 ID는 컨트롤의 종류를 나타내기 위해 할당된 ID로서, 최대 4개의 문자로 구성된 문자열이다. 예를 들어 표는 "tbl", 각주는 "fn"이다. 이와 비슷하게 CtrlCh는 정수로, UserDesc는 한글 문자열로 리턴한다.

한/글에서 현재까지 지원되는 모든 컨트롤의 ID는 아래 Returns 참조.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()  # 2x2 표의 각 셀 안에 이미지가 총 4장 들어있는 문서
&gt;&gt;&gt; for ctrl in hwp.ctrl_list:
...     print(ctrl.CtrlID)
...
tbl
gso
gso
gso
gso</code>
```

### `Next` <small><code>property</code></small>

다음 컨트롤.

문서 중의 모든 컨트롤(표, 그림 등의 특수 문자들)은 linked list로 서로 연결되어 있는데, list 중 다음 컨트롤을 나타낸다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()  # 표 하나만 들어 있는 문서에서
&gt;&gt;&gt; print(hwp.HeadCtrl.Next.Next.UserDesc)
표</code>
```

### `Prev` <small><code>property</code></small>

앞 컨트롤.

문서 중의 모든 컨트롤(표, 그림 등의 특수 문자들)은 linked list로 서로 연결되어 있는데, list 중 앞 컨트롤을 나타낸다.

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()  # 빈 표, 그 아래에 그림 한 개 삽입된 문서에서
&gt;&gt;&gt; print(hwp.LastCtrl.Prev.UserDesc)
표</code>
```

### `Properties` <small><code>property</code></small> <small><code>writable</code></small>

컨트롤의 속성을 나타낸다.

모든 컨트롤은 대응하는 parameter set으로 속성을 읽고 쓸 수 있다.

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; # 문서의 모든 그림의 너비, 높이를 각각 절반으로 줄이는 코드
&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; for ctrl in hwp.ctrl_list:
...     if ctrl.UserDesc == "그림":
...         prop = ctrl.Properties
...         width = prop.Item("Width")
...         height = prop.Item("Height")
...         prop.SetItem("Width", width // 2)
...         prop.SetItem("Height", height // 2)
...         ctrl.Properties = prop</code>
```

### `UserDesc` <small><code>property</code></small>

컨트롤의 종류를 사용자에게 보여줄 수 있는 localize된 문자열로 나타낸다.

### `GetAnchorPos(type_=0)`

해당 컨트롤의 앵커(조판부호)의 위치를 반환한다.

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()  # 표만 두 개 있는 문서에 연결됨.
&gt;&gt;&gt; for ctrl in hwp.ctrl_list:
...     print(ctrl.GetAnchorPos().Item("List"), end=" ")
...     print(ctrl.GetAnchorPos().Item("Para"), end=" ")
...     print(ctrl.GetAnchorPos().Item("Pos"))
0 0 16
0 2 0</code>
```

### `GetCtrlInstID()`

**\[한글2024전용\]** 컨트롤의 고유 아이디를 정수형태 문자열로 리턴하는 메서드

한글2024부터 제공하는 기능으로 정확하게 컨트롤을 선택하기 위한 새로운 수단이다. 기존의 `FindCtrl()`, `hwp.SelectCtrlFront()`나 `hwp.SelectCtrlReverse()` 등 인접 컨트롤을 선택하는 방법에는 문제의 소지가 있었다. 대표적인 예로, 이미지가 들어있는 셀 안에서 표 컨트롤을 선택하려고 하면, 어떤 방법을 쓰든 이미지가 선택돼버리기 때문에 이미지를 선택하지 않는 여러 꼼수를 생각해내야 했다. 하지만 ctrl.GetCtrlInstID()와 hwp.SelectCtrl()을 같이 사용하면 그럴 걱정이 전혀 없게 된다.

다만 사용시 주의할 점이 하나 있는데,

`Get`/`SetTextFile`이나 `save_block_as` 등의 메서드 혹은 `Cut`/`Paste` 사용시에는, 문서상에서 컨트롤이 지워졌다 다시 씌어지는 시점에 `CtrlInstID`가 바뀌게 된다. (다만, 마우스로 드래그해 옮길 땐 아이디가 바뀌지 않는다.)

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp()
&gt;&gt;&gt; hwp.insert_random_picture()
&gt;&gt;&gt; hwp.insert_random_picture()
&gt;&gt;&gt; hwp.insert_random_picture()
&gt;&gt;&gt; for ctrl in hwp.ctrl_list:
...     print(ctrl.GetCtrlInstID())
...
1816447703
1816447705
1816447707
&gt;&gt;&gt; hwp.hwp.SelectCtrl("")</code>
```