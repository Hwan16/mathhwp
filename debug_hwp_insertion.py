#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HWP MathML 삽입 과정 디버깅
"""

import json
from pyhwpx import Hwp
from text_parser import split_text_and_latex
from latex_converter import convert_latex_to_mathml, create_temp_mathml_file, cleanup_temp_file
import time

def debug_hwp_insertion():
    """HWP MathML 삽입 과정 디버깅"""
    print("HWP MathML 삽입 디버깅")
    print("=" * 50)
    
    # test.json에서 3번 문제만 테스트
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    problem3 = data['problems'][2]['latex_string']
    print(f"3번 문제: {repr(problem3[:100])}...")
    
    # HWP 인스턴스 생성
    hwp = Hwp()
    
    # 텍스트 파싱
    parts = split_text_and_latex(problem3)
    print(f"\n파싱된 부분 수: {len(parts)}")
    
    for i, (part_type, content) in enumerate(parts):
        print(f"\n--- 부분 {i+1}: {part_type} ---")
        print(f"내용: {repr(content[:50])}...")
        
        if part_type == 'text':
            try:
                hwp.insert_text(content)
                print("텍스트 삽입 성공")
            except Exception as e:
                print(f"텍스트 삽입 실패: {e}")
                
        elif part_type == 'math':
            try:
                print("1. LaTeX -> MathML 변환 시작...")
                mathml_content = convert_latex_to_mathml(content)
                print(f"   MathML 변환 성공 (길이: {len(mathml_content)})")
                
                print("2. 임시 MathML 파일 생성...")
                temp_mml_path = create_temp_mathml_file(mathml_content)
                print(f"   임시 파일: {temp_mml_path}")
                
                print("3. HWP에 MathML 삽입 시도...")
                hwp.import_mathml(temp_mml_path, delay=0.3)
                print("   HWP MathML 삽입 성공!")
                
                print("4. 임시 파일 정리...")
                cleanup_temp_file(temp_mml_path)
                print("   정리 완료")
                
                # 삽입 후 대기
                time.sleep(0.2)
                
            except Exception as e:
                print(f"수식 처리 실패: {e}")
                print(f"실패한 LaTeX: {content}")
                # 실패 시 원본 텍스트 삽입 (이게 문제의 원인!)
                try:
                    hwp.insert_text(f"[수식 오류: {content}]")
                    print("오류 텍스트 삽입됨")
                except Exception as e2:
                    print(f"오류 텍스트 삽입도 실패: {e2}")
    
    # 파일 저장
    output_file = "debug_hwp_test.hwpx"
    try:
        print(f"\n파일 저장 중: {output_file}")
        time.sleep(1.0)
        hwp.save_as(output_file)
        print("파일 저장 성공!")
    except Exception as e:
        print(f"파일 저장 실패: {e}")

if __name__ == "__main__":
    debug_hwp_insertion() 