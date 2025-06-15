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
        
        # 특정 패턴에 대한 대체 처리
        if "\\begin{array}" in latex_string:
            print("→ array 환경 감지: 단순화된 형태로 변환 시도")
            simplified = simplify_array_environment(latex_string)
            try:
                return convert(simplified)
            except:
                pass
        
        # 오류 발생 시 기본 MathML 반환 (더 안전한 형태)
        escaped_latex = latex_string.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;')
        return f'<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>[변환 실패: {escaped_latex[:50]}...]</mtext></math>'

def simplify_array_environment(latex_string: str) -> str:
    """
    array 환경을 단순한 형태로 변환하는 함수
    
    Args:
        latex_string (str): array 환경이 포함된 LaTeX 문자열
        
    Returns:
        str: 단순화된 LaTeX 문자열
    """
    # array 환경을 cases 환경으로 변경 시도
    if "\\begin{array}" in latex_string:
        # array를 cases로 변경
        simplified = latex_string.replace("\\begin{array}{ll}", "\\begin{cases}")
        simplified = simplified.replace("\\end{array}", "\\end{cases}")
        simplified = simplified.replace(" & ", " & ")  # 구분자 유지
        return simplified
    
    return latex_string

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
    # 테스트 케이스들 (문제가 되는 array 환경 포함)
    test_cases = [
        r"\frac{4}{2^{\sqrt{2}}}",
        r"\lim_{x \rightarrow \infty} \frac{\sqrt{x^{2}-2}+3x}{x+5}",
        r"\frac{1}{4}",
        r"\{a_n\}",
        r"a_2 + a_4 = 30, \quad a_4 + a_6 = \frac{15}{2}",
        r"a_1",
        # 문제가 되는 array 환경
        r"f(x)=\left\{\begin{array}{ll} 5x+a & (x<-2) \\ x^{2}-a & (x \geq-2) \end{array}\right."
    ]
    
    print("LaTeX → MathML 변환 테스트 (에러 핸들링 개선):")
    print("=" * 80)
    
    for i, latex in enumerate(test_cases, 1):
        print(f"\n{'='*20} 테스트 {i} {'='*20}")
        print(f"LaTeX 입력: {latex}")
        print("-" * 60)
        
        # LaTeX → MathML 변환
        mathml = convert_latex_to_mathml(latex)
        print(f"MathML 출력:")
        print(mathml[:200] + "..." if len(mathml) > 200 else mathml)
        print("-" * 60)
        
        # MathML 길이 및 유효성 확인
        if mathml and len(mathml) > 0:
            print(f"✅ 변환 완료 (길이: {len(mathml)} 문자)")
            
            # MathML 기본 구조 확인
            if '<math' in mathml and '</math>' in mathml:
                if '[변환 실패:' in mathml:
                    print("⚠️  대체 텍스트로 처리됨")
                else:
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