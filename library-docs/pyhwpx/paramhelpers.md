## `pyhwpx.param_helpers.ParamHelpers`

파라미터 헬퍼메서드 : 별도의 동작은 하지 않고, 파라미터 변환, 연산 등을 돕는다.

### `HeadType(heading_type)`

문단 종류를 결정할 때 사용하는 헬퍼함수

현재 문단의 머리에 '개요 번호'나 '문단 번호', '그럼리표' 등을 넣어 문단 종류를 바꿀 것인지, '없음'을 선택해 보통 모양의 문단으로 놓아둘 것인지를 선택.

Parameters:

Returns:

### `HwpLineType(line_type='Solid')`

한/글에서 표나 개체의 선 타입을 결정하는 헬퍼메서드. 단순히 문자열을 정수로 변환한다.

Parameters:

### `HwpLineWidth(line_width='0.1mm')`

선 너비를 정해주는 헬퍼 메서드.

목록은 아래와 같다.

Parameters:

Returns:

### `NumberFormat(num_format)`

개요번호 사용자 정의를 위해 미리 정의된 포맷 모음

Parameters:

Returns:

Examples:

```
<span></span><code id="code-lang-python">&gt;&gt;&gt; # 개요번호 사용자 정의
&gt;&gt;&gt; from pyhwpx import Hwp
&gt;&gt;&gt; hwp = Hwp(new=True)
&gt;&gt;&gt; pset = hwp.HParameterSet.HSecDef
&gt;&gt;&gt; hwp.HAction.GetDefault("OutlineNumber", pset.HSet)
&gt;&gt;&gt; pset.OutlineShape.StrFormatLevel0 = "^1."
&gt;&gt;&gt; pset.OutlineShape.NumFormatLevel0 = hwp.NumberFormat("RomanCapital")  # &lt;---
&gt;&gt;&gt; pset.OutlineShape.StartNumber0 = 1
&gt;&gt;&gt; pset.OutlineShape.NewList = 0
&gt;&gt;&gt; pset.HSet.SetItem("ApplyClass", 24)  # 앞 구역의 개요 번호에 이어서
&gt;&gt;&gt; pset.HSet.SetItem("ApplyTo", 3)  # 적용범위(2:현재구역, 3:문서 전체, 4:새 구역으로)
&gt;&gt;&gt; hwp.HAction.Execute("OutlineNumber", pset.HSet)
True</code>
```

### `hwp_unit_to_mili(hwp_unit)` <small><code>staticmethod</code></small>

HwpUnit 값을 밀리미터로 변환한 값을 리턴한다.

HwpUnit으로 리턴되었거나, 녹화된 코드의 HwpUnit값을 확인할 때 유용하게 사용할 수 있다.

Returns: