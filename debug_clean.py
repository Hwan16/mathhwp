#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
문제 분석을 위한 깔끔한 디버깅 스크립트
"""

import json
from text_parser import split_text_and_latex

def analyze_problem_1():
    """1번 문제 순서 문제 분석"""
    print("1번 문제 분석")
    print("=" * 50)
    
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    problem1 = data['problems'][0]['latex_string']
    print("원본 텍스트:")
    print(repr(problem1))
    print()
    
    parts = split_text_and_latex(problem1)
    print("파싱 결과:")
    for i, (part_type, content) in enumerate(parts):
        print(f"{i+1}. [{part_type}] {repr(content)}")
    print()

def analyze_problem_3():
    """3번 문제 블록 수식 분석"""
    print("3번 문제 분석")
    print("=" * 50)
    
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    problem3 = data['problems'][2]['latex_string']
    print("원본 텍스트:")
    print(repr(problem3))
    print()
    
    parts = split_text_and_latex(problem3)
    print("파싱 결과:")
    for i, (part_type, content) in enumerate(parts):
        print(f"{i+1}. [{part_type}] {repr(content)}")
    print()

def analyze_problem_4():
    """4번 문제 array 환경 분석"""
    print("4번 문제 분석")
    print("=" * 50)
    
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    problem4 = data['problems'][3]['latex_string']
    print("원본 텍스트:")
    print(repr(problem4))
    print()
    
    parts = split_text_and_latex(problem4)
    print("파싱 결과:")
    for i, (part_type, content) in enumerate(parts):
        print(f"{i+1}. [{part_type}] {repr(content)}")
    print()

if __name__ == "__main__":
    analyze_problem_1()
    analyze_problem_3()
    analyze_problem_4() 