import re
from typing import List, Tuple

def split_text_and_latex(full_text: str) -> List[Tuple[str, str]]:
    """
    LaTeX 문자열에서 일반 텍스트와 수식을 분리하는 함수
    
    Args:
        full_text (str): LaTeX 수식이 포함된 전체 텍스트
        
    Returns:
        List[Tuple[str, str]]: (타입, 내용) 튜플의 리스트
                              타입은 'text' 또는 'math'
    """
    parts = []
    last_end = 0
    
    # 인라인 수식과 블록 수식을 각각 처리
    # 인라인 수식 패턴: \( ... \)
    inline_math_pattern = r'\\\((.*?)\\\)'
    # 블록 수식 패턴: \[ ... \]
    block_math_pattern = r'\\\[(.*?)\\\]'
    
    # 모든 수식 위치를 찾기
    math_matches = []
    
    # 인라인 수식 찾기
    for match in re.finditer(inline_math_pattern, full_text, re.DOTALL):
        math_matches.append((match.start(), match.end(), 'inline', match.group(1)))
    
    # 블록 수식 찾기
    for match in re.finditer(block_math_pattern, full_text, re.DOTALL):
        math_matches.append((match.start(), match.end(), 'block', match.group(1)))
    
    # 위치 순으로 정렬
    math_matches.sort(key=lambda x: x[0])
    
    # 텍스트와 수식을 순서대로 분리
    for start, end, math_type, math_content in math_matches:
        # 수식 앞의 일반 텍스트 부분
        if start > last_end:
            text_part = full_text[last_end:start]
            if text_part.strip():  # 공백만 있는 경우가 아니면 추가
                parts.append(('text', text_part))
        
        # 수식 부분 추가
        parts.append(('math', math_content.strip()))
        last_end = end
    
    # 마지막 텍스트 부분
    if last_end < len(full_text):
        remaining_text = full_text[last_end:]
        if remaining_text.strip():
            parts.append(('text', remaining_text))
    
    return parts

def test_text_parser():
    """텍스트 파서 테스트 함수"""
    # 테스트 케이스 1: 간단한 수식이 포함된 텍스트
    test1 = r"1. \( \frac{4}{2^{\sqrt{2}}} \) 의 값은? [2점]"
    print("테스트 1:")
    print(f"입력: {test1}")
    result1 = split_text_and_latex(test1)
    for i, (part_type, content) in enumerate(result1):
        print(f"  {i+1}. [{part_type}] {content}")
    print()
    
    # 테스트 케이스 2: 여러 수식이 포함된 텍스트
    test2 = r"2. \( \lim_{x \rightarrow \infty} \frac{\sqrt{x^{2}-2}+3x}{x+5} \) 의 값은? (1) \( \frac{1}{4} \) (2) \( \frac{1}{2} \)"
    print("테스트 2:")
    print(f"입력: {test2}")
    result2 = split_text_and_latex(test2)
    for i, (part_type, content) in enumerate(result2):
        print(f"  {i+1}. [{part_type}] {content}")
    print()
    
    # 테스트 케이스 3: 블록 수식이 포함된 텍스트
    test3 = r"""3. 공비가 양수인 등비수열 \( \{a_n\} \) 이
\[
a_2 + a_4 = 30, \quad a_4 + a_6 = \frac{15}{2}
\]
를 만족시킬 때, \( a_1 \) 의 값은?"""
    print("테스트 3:")
    print(f"입력: {test3}")
    result3 = split_text_and_latex(test3)
    for i, (part_type, content) in enumerate(result3):
        print(f"  {i+1}. [{part_type}] {content}")

if __name__ == "__main__":
    test_text_parser() 