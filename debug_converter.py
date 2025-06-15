import json
from text_parser import split_text_and_latex
from latex_converter import convert_latex_to_mathml

def debug_json_processing():
    """test.json 파일의 각 단계별 처리 과정을 디버깅"""
    
    # JSON 파일 로드
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("=== JSON 파일 디버깅 분석 ===")
    print(f"문제 개수: {len(data['problems'])}")
    print()
    
    for i, problem in enumerate(data['problems'], 1):
        print(f"🔍 문제 {i} 분석:")
        print(f"ID: {problem['id']}")
        print(f"원본 LaTeX: {problem['latex_string'][:100]}...")
        print()
        
        # 1단계: 텍스트 파싱
        print("1️⃣ 텍스트 파싱 결과:")
        parts = split_text_and_latex(problem['latex_string'])
        for j, (part_type, content) in enumerate(parts):
            if part_type == 'math':
                print(f"   수식 {j+1}: {content}")
            else:
                print(f"   텍스트 {j+1}: {content[:50]}...")
        print()
        
        # 2단계: 수식 변환 테스트
        print("2️⃣ 수식 변환 테스트:")
        math_parts = [content for part_type, content in parts if part_type == 'math']
        
        for j, math_content in enumerate(math_parts):
            print(f"   수식 {j+1}: {math_content}")
            try:
                mathml = convert_latex_to_mathml(math_content)
                print(f"   ✅ 변환 성공 (길이: {len(mathml)})")
            except Exception as e:
                print(f"   ❌ 변환 실패: {e}")
        
        print("-" * 80)

if __name__ == "__main__":
    debug_json_processing() 