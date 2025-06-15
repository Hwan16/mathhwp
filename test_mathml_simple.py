#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
3번, 4번 문제 수식의 MathML 변환 검증 (간단 버전)
"""

import json
from latex_converter import convert_latex_to_mathml
from text_parser import split_text_and_latex

def test_mathml_conversion():
    """MathML 변환 테스트"""
    print("MathML 변환 테스트")
    print("=" * 50)
    
    # test.json 로드
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 3번 문제 테스트
    print("\n3번 문제:")
    problem3 = data['problems'][2]['latex_string']
    parts3 = split_text_and_latex(problem3)
    
    for i, (part_type, content) in enumerate(parts3):
        if part_type == 'math':
            print(f"수식 {i}: {repr(content)}")
            try:
                mathml = convert_latex_to_mathml(content)
                print(f"  -> 변환 성공 (길이: {len(mathml)})")
            except Exception as e:
                print(f"  -> 변환 실패: {e}")
    
    # 4번 문제 테스트
    print("\n4번 문제:")
    problem4 = data['problems'][3]['latex_string']
    parts4 = split_text_and_latex(problem4)
    
    for i, (part_type, content) in enumerate(parts4):
        if part_type == 'math':
            print(f"수식 {i}: {repr(content)}")
            try:
                mathml = convert_latex_to_mathml(content)
                print(f"  -> 변환 성공 (길이: {len(mathml)})")
            except Exception as e:
                print(f"  -> 변환 실패: {e}")
    
    # 특정 수식 개별 테스트
    print("\n개별 수식 테스트:")
    
    # 3번의 블록 수식
    block_math = r"\frac{a_{4}}{a_{2}}+\frac{a_{2}}{a_{1}}=30"
    print(f"블록 수식: {repr(block_math)}")
    try:
        mathml = convert_latex_to_mathml(block_math)
        print(f"  -> 변환 성공 (길이: {len(mathml)})")
    except Exception as e:
        print(f"  -> 변환 실패: {e}")
    
    # 4번의 array 환경
    array_math = r"f(x)=\left\{\begin{array}{ll}5 x+a & (x<-2) \\x^{2}-a & (x \geq-2)\end{array}\right."
    print(f"Array 환경: {repr(array_math)}")
    try:
        mathml = convert_latex_to_mathml(array_math)
        print(f"  -> 변환 성공 (길이: {len(mathml)})")
    except Exception as e:
        print(f"  -> 변환 실패: {e}")

if __name__ == "__main__":
    test_mathml_conversion() 