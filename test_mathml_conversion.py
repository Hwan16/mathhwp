#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
3번, 4번 문제 수식의 MathML 변환 실패 검증 테스트
"""

import json
from latex_converter import convert_latex_to_mathml
from text_parser import split_text_and_latex

def test_problem_3_mathml():
    """3번 문제 수식들의 MathML 변환 테스트"""
    print("=" * 60)
    print("3번 문제 MathML 변환 테스트")
    print("=" * 60)
    
    # test.json에서 3번 문제 추출
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    problem3 = data['problems'][2]['latex_string']
    parts = split_text_and_latex(problem3)
    
    print("3번 문제의 수식들:")
    for i, (part_type, content) in enumerate(parts):
        if part_type == 'math':
            print(f"\n수식 {i}: {repr(content)}")
            try:
                mathml = convert_latex_to_mathml(content)
                print(f"✅ 변환 성공! (길이: {len(mathml)})")
                print(f"MathML 미리보기: {mathml[:100]}...")
            except Exception as e:
                print(f"❌ 변환 실패: {e}")
                print(f"실패한 LaTeX: {content}")

def test_problem_4_mathml():
    """4번 문제 수식들의 MathML 변환 테스트"""
    print("\n" + "=" * 60)
    print("4번 문제 MathML 변환 테스트")
    print("=" * 60)
    
    # test.json에서 4번 문제 추출
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    problem4 = data['problems'][3]['latex_string']
    parts = split_text_and_latex(problem4)
    
    print("4번 문제의 수식들:")
    for i, (part_type, content) in enumerate(parts):
        if part_type == 'math':
            print(f"\n수식 {i}: {repr(content)}")
            try:
                mathml = convert_latex_to_mathml(content)
                print(f"✅ 변환 성공! (길이: {len(mathml)})")
                print(f"MathML 미리보기: {mathml[:100]}...")
            except Exception as e:
                print(f"❌ 변환 실패: {e}")
                print(f"실패한 LaTeX: {content}")

def test_specific_expressions():
    """특정 문제가 되는 수식들을 개별적으로 테스트"""
    print("\n" + "=" * 60)
    print("특정 수식 개별 테스트")
    print("=" * 60)
    
    # 3번 문제의 블록 수식
    block_math = r"\frac{a_{4}}{a_{2}}+\frac{a_{2}}{a_{1}}=30"
    print(f"\n블록 수식 테스트: {repr(block_math)}")
    try:
        mathml = convert_latex_to_mathml(block_math)
        print(f"✅ 변환 성공! (길이: {len(mathml)})")
    except Exception as e:
        print(f"❌ 변환 실패: {e}")
    
    # 4번 문제의 array 환경
    array_math = r"f(x)=\left\{\begin{array}{ll}5 x+a & (x<-2) \\x^{2}-a & (x \geq-2)\end{array}\right."
    print(f"\nArray 환경 테스트: {repr(array_math)}")
    try:
        mathml = convert_latex_to_mathml(array_math)
        print(f"✅ 변환 성공! (길이: {len(mathml)})")
    except Exception as e:
        print(f"❌ 변환 실패: {e}")
        
        # cases 환경으로 대체 테스트
        cases_math = r"f(x)=\begin{cases}5x+a & (x<-2) \\x^{2}-a & (x \geq-2)\end{cases}"
        print(f"\nCases 환경 대체 테스트: {repr(cases_math)}")
        try:
            mathml2 = convert_latex_to_mathml(cases_math)
            print(f"✅ Cases 변환 성공! (길이: {len(mathml2)})")
        except Exception as e2:
            print(f"❌ Cases도 실패: {e2}")

if __name__ == "__main__":
    test_problem_3_mathml()
    test_problem_4_mathml()
    test_specific_expressions() 