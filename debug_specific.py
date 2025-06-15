import json
from text_parser import split_text_and_latex
from latex_converter import convert_latex_to_mathml

def debug_specific_problems():
    """특정 문제들을 상세 분석"""
    
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("=== 특정 문제 상세 분석 ===")
    
    # 1번 문제 분석
    problem1 = data['problems'][0]['latex_string']
    print("🔍 1번 문제 분석:")
    print(f"원본: {repr(problem1)}")
    print()
    
    parts1 = split_text_and_latex(problem1)
    print("파싱 결과:")
    for i, (part_type, content) in enumerate(parts1):
        print(f"  {i+1}. [{part_type}] {repr(content)}")
    print()
    
    # 3번 문제 분석 (줄바꿈 포함)
    problem3 = data['problems'][2]['latex_string']
    print("🔍 3번 문제 분석:")
    print(f"원본: {repr(problem3)}")
    print()
    
    parts3 = split_text_and_latex(problem3)
    print("파싱 결과:")
    for i, (part_type, content) in enumerate(parts3):
        print(f"  {i+1}. [{part_type}] {repr(content)}")
        if part_type == 'math':
            print(f"      → 수식 변환 테스트:")
            try:
                mathml = convert_latex_to_mathml(content)
                print(f"      ✅ 성공 (길이: {len(mathml)})")
            except Exception as e:
                print(f"      ❌ 실패: {e}")
    print()
    
    # 4번 문제 분석
    problem4 = data['problems'][3]['latex_string']
    print("🔍 4번 문제 분석:")
    print(f"원본: {repr(problem4)}")
    print()
    
    parts4 = split_text_and_latex(problem4)
    print("파싱 결과:")
    for i, (part_type, content) in enumerate(parts4):
        print(f"  {i+1}. [{part_type}] {repr(content)}")
        if part_type == 'math':
            print(f"      → 수식 변환 테스트:")
            try:
                mathml = convert_latex_to_mathml(content)
                print(f"      ✅ 성공 (길이: {len(mathml)})")
            except Exception as e:
                print(f"      ❌ 실패: {e}")

def test_newline_handling():
    """줄바꿈이 포함된 LaTeX 처리 테스트"""
    print("\n=== 줄바꿈 처리 테스트 ===")
    
    # 줄바꿈이 포함된 블록 수식
    test_latex = r"\[\n\frac{a_{4}}{a_{2}}+\frac{a_{2}}{a_{1}}=30\n\]"
    print(f"테스트 LaTeX: {repr(test_latex)}")
    
    # 줄바꿈 제거 버전
    cleaned_latex = test_latex.replace('\n', ' ').strip()
    print(f"정리된 LaTeX: {repr(cleaned_latex)}")
    
    # 변환 테스트
    print("변환 테스트:")
    try:
        mathml1 = convert_latex_to_mathml(test_latex)
        print(f"원본: ✅ 성공 (길이: {len(mathml1)})")
    except Exception as e:
        print(f"원본: ❌ 실패: {e}")
    
    try:
        mathml2 = convert_latex_to_mathml(cleaned_latex)
        print(f"정리된 버전: ✅ 성공 (길이: {len(mathml2)})")
    except Exception as e:
        print(f"정리된 버전: ❌ 실패: {e}")

if __name__ == "__main__":
    debug_specific_problems()
    test_newline_handling() 