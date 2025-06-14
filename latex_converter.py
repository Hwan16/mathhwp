import os
import tempfile
from latex2mathml.converter import convert

def convert_latex_to_mathml(latex_string: str) -> str:
    """
    LaTeX 수식을 MathML 형식으로 변환하는 함수
    
    Args:
        latex_string (str): LaTeX 수식 문자열 (예: "\\frac{a}{b}")
        
    Returns:
        str: MathML XML 문자열
    """
    try:
        # latex2mathml을 사용하여 변환
        mathml_string = convert(latex_string)
        return mathml_string
    except Exception as e:
        print(f"LaTeX 변환 오류: {e}")
        print(f"입력된 LaTeX: {latex_string}")
        # 오류 발생 시 기본 MathML 반환
        return f'<math><mtext>변환 오류: {latex_string}</mtext></math>'

def create_temp_mathml_file(mathml_content: str) -> str:
    """
    MathML 내용을 임시 파일로 저장하고 파일 경로를 반환
    
    Args:
        mathml_content (str): MathML XML 문자열
        
    Returns:
        str: 임시 MathML 파일의 경로
    """
    # 임시 파일 생성
    temp_fd, temp_path = tempfile.mkstemp(suffix='.mml', text=True)
    
    try:
        with os.fdopen(temp_fd, 'w', encoding='utf-8') as temp_file:
            temp_file.write(mathml_content)
        return temp_path
    except Exception as e:
        # 파일 디스크립터 정리
        os.close(temp_fd)
        raise e

def cleanup_temp_file(file_path: str):
    """
    임시 파일을 삭제하는 함수
    
    Args:
        file_path (str): 삭제할 파일 경로
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"임시 파일 삭제 오류: {e}")

def test_latex_converter():
    """LaTeX 변환기 테스트 함수"""
    # 테스트 케이스들
    test_cases = [
        r"\frac{4}{2^{\sqrt{2}}}",
        r"\lim_{x \rightarrow \infty} \frac{\sqrt{x^{2}-2}+3x}{x+5}",
        r"\frac{1}{4}",
        r"\{a_n\}",
        r"a_2 + a_4 = 30, \quad a_4 + a_6 = \frac{15}{2}",
        r"a_1"
    ]
    
    print("LaTeX → MathML 변환 테스트:")
    print("=" * 80)
    
    for i, latex in enumerate(test_cases, 1):
        print(f"\n{'='*20} 테스트 {i} {'='*20}")
        print(f"LaTeX 입력: {latex}")
        print("-" * 60)
        
        # LaTeX → MathML 변환
        mathml = convert_latex_to_mathml(latex)
        print(f"MathML 출력:")
        print(mathml)
        print("-" * 60)
        
        # MathML 길이 및 유효성 확인
        if mathml and len(mathml) > 0:
            print(f"✅ 변환 성공 (길이: {len(mathml)} 문자)")
            
            # MathML 기본 구조 확인
            if '<math' in mathml and '</math>' in mathml:
                print("✅ MathML 구조 유효")
            else:
                print("❌ MathML 구조 문제 발견")
        else:
            print("❌ 변환 실패 또는 빈 결과")
        
        # 임시 파일 생성 테스트
        try:
            temp_file = create_temp_mathml_file(mathml)
            print(f"✅ 임시 파일 생성: {temp_file}")
            
            # 파일 내용 확인
            with open(temp_file, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            if file_content == mathml:
                print("✅ 파일 내용 일치")
            else:
                print("❌ 파일 내용 불일치")
                print(f"파일 길이: {len(file_content)}, 원본 길이: {len(mathml)}")
            
            # 임시 파일 정리
            cleanup_temp_file(temp_file)
            print("✅ 임시 파일 정리 완료")
            
        except Exception as e:
            print(f"❌ 임시 파일 처리 오류: {e}")
        
        print("=" * 80)

if __name__ == "__main__":
    test_latex_converter() 