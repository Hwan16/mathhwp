#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
특정 문제들 디버깅: 1번 순서 문제, 3번/4번 변환 문제
"""

import json
from text_parser import split_text_and_latex
from latex_converter import convert_latex_to_mathml

def debug_problem_order():
    """1번 문제 순서 문제 디버깅"""
    print("=" * 60)
    print("1번 문제 순서 문제 디버깅")
    print("=" * 60)
    
    # test.json에서 1번 문제 추출
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    problem1 = data['problems'][0]['latex_string']
    print(f"1번 문제 원본:")
    print(f"'{problem1}'")
    print()
    
    # 텍스트 파싱 결과 확인
    parts = split_text_and_latex(problem1)
    print("파싱 결과:")
    for i, (part_type, content) in enumerate(parts):
        print(f"  {i+1}. [{part_type}] '{content}'")
    print()

def debug_problem_3_and_4():
    """3번, 4번 문제 변환 문제 디버깅"""
    print("=" * 60)
    print("3번, 4번 문제 변환 문제 디버깅")
    print("=" * 60)
    
    # test.json에서 3번, 4번 문제 추출
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for problem_num in [2, 3]:  # 0-based index이므로 2, 3
        problem = data['problems'][problem_num]
        problem_id = problem['id']
        latex_string = problem['latex_string']
        
        print(f"\n{problem_id}번 문제 분석:")
        print(f"원본: {latex_string}")
        print()
        
        # 텍스트 파싱
        parts = split_text_and_latex(latex_string)
        print("파싱 결과:")
        for i, (part_type, content) in enumerate(parts):
            print(f"  {i+1}. [{part_type}] '{content}'")
            
            # 수식 부분에 대해 MathML 변환 테스트
            if part_type == 'math':
                try:
                    print(f"    → LaTeX: {content}")
                    mathml = convert_latex_to_mathml(content)
                    print(f"    → MathML 변환 성공 (길이: {len(mathml)})")
                    # MathML 내용의 일부만 출력 (너무 길면 생략)
                    if len(mathml) > 200:
                        print(f"    → MathML 미리보기: {mathml[:100]}...")
                    else:
                        print(f"    → MathML: {mathml}")
                except Exception as e:
                    print(f"    ❌ MathML 변환 실패: {e}")
        print("-" * 40)

def debug_array_environment():
    """array 환경 처리 문제 디버깅"""
    print("=" * 60)
    print("Array 환경 처리 디버깅")
    print("=" * 60)
    
    # 4번 문제의 array 환경 부분만 추출
    array_latex = r"""f(x)=\left\{\begin{array}{ll}
5 x+a & (x<-2) \\
x^{2}-a & (x \geq-2)
\end{array}\right."""
    
    print(f"Array LaTeX:")
    print(f"'{array_latex}'")
    print()
    
    try:
        mathml = convert_latex_to_mathml(array_latex)
        print("✅ MathML 변환 성공")
        print(f"MathML 길이: {len(mathml)}")
        print(f"MathML 미리보기: {mathml[:200]}...")
    except Exception as e:
        print(f"❌ MathML 변환 실패: {e}")
        
        # 간단한 버전으로 테스트
        simple_version = r"f(x) = \begin{cases} 5x+a & (x<-2) \\ x^{2}-a & (x \geq-2) \end{cases}"
        print(f"\n간단한 버전 테스트:")
        print(f"'{simple_version}'")
        try:
            mathml2 = convert_latex_to_mathml(simple_version)
            print("✅ 간단한 버전 변환 성공")
            print(f"MathML 길이: {len(mathml2)}")
        except Exception as e2:
            print(f"❌ 간단한 버전도 실패: {e2}")

def debug_block_math_parsing():
    """블록 수식 파싱 문제 디버깅"""
    print("=" * 60)
    print("블록 수식 파싱 디버깅")
    print("=" * 60)
    
    # 3번 문제의 블록 수식 부분
    block_text = r"""3. 첫째항과 공비가 모두 양수 \( k \) 인 등비수열 \( \left\{a_{n}\right\} \) 이
\[
\frac{a_{4}}{a_{2}}+\frac{a_{2}}{a_{1}}=30
\]

을 만족시킬 때, \( k \) 의 값은? [3점]"""
    
    print("3번 문제 블록 수식:")
    print(f"'{block_text}'")
    print()
    
    parts = split_text_and_latex(block_text)
    print("파싱 결과:")
    for i, (part_type, content) in enumerate(parts):
        print(f"  {i+1}. [{part_type}] '{content}'")
        
        if part_type == 'math':
            # 수식에 개행이나 공백이 포함되어 있는지 확인
            print(f"    → 수식 길이: {len(content)}")
            print(f"    → 개행 포함: {'\\n' in content}")
            print(f"    → 공백 포함: {' ' in content}")
            print(f"    → 수식 내용 (repr): {repr(content)}")

if __name__ == "__main__":
    debug_problem_order()
    debug_problem_3_and_4()
    debug_array_environment()
    debug_block_math_parsing() 