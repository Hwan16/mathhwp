from pyhwpx import Hwp
from text_parser import split_text_and_latex
from latex_converter import convert_latex_to_mathml, create_temp_mathml_file, cleanup_temp_file
import time
from typing import List, Tuple

def create_hwp_document(latex_content: str, output_path: str = None) -> Hwp:
    """
    LaTeX 내용을 파싱하여 HWPX 문서를 생성하는 함수
    
    Args:
        latex_content (str): LaTeX 수식이 포함된 텍스트
        output_path (str, optional): 저장할 파일 경로
        
    Returns:
        Hwp: 생성된 HWP 문서 객체
    """
    # HWP 인스턴스 생성
    hwp = Hwp()
    
    # 텍스트와 수식 분리
    parts = split_text_and_latex(latex_content)
    
    # 각 부분을 순차적으로 처리
    for part_type, content in parts:
        if part_type == 'text':
            # 일반 텍스트 삽입
            hwp.insert_text(content)
        elif part_type == 'math':
            # LaTeX 수식을 MathML로 변환 후 삽입
            try:
                # LaTeX → MathML 변환
                mathml_content = convert_latex_to_mathml(content)
                
                # 임시 MathML 파일 생성
                temp_mml_path = create_temp_mathml_file(mathml_content)
                
                # HWP에 수식 삽입
                hwp.import_mathml(temp_mml_path)
                
                # 임시 파일 정리
                cleanup_temp_file(temp_mml_path)
                
            except Exception as e:
                print(f"수식 변환 오류: {e}")
                print(f"문제가 된 LaTeX: {content}")
                # 오류 발생 시 원본 LaTeX를 텍스트로 삽입
                hwp.insert_text(f"[수식 오류: {content}]")
    
    # 파일 저장
    if output_path:
        try:
            hwp.save_as(output_path)
            print(f"문서가 저장되었습니다: {output_path}")
        except Exception as e:
            print(f"파일 저장 오류: {e}")
    
    return hwp

def process_math_problems(problems_list: List[str], output_path: str = None) -> Hwp:
    """
    여러 수학 문제를 처리하여 하나의 HWPX 문서로 생성하는 함수
    
    Args:
        problems_list (List[str]): LaTeX 형식의 수학 문제 리스트
        output_path (str, optional): 저장할 파일 경로
        
    Returns:
        Hwp: 생성된 HWP 문서 객체
    """
    # HWP 인스턴스 생성
    hwp = Hwp()
    
    for i, problem_text in enumerate(problems_list, 1):
        print(f"문제 {i} 처리 중...")
        
        # 문제를 줄 단위로 분리
        lines = problem_text.strip().split('\n')
        
        for line in lines:
            if line.strip():  # 빈 줄이 아닌 경우만 처리
                # 텍스트와 수식 분리
                parts = split_text_and_latex(line)
                
                for part_type, content in parts:
                    if part_type == 'text':
                        hwp.insert_text(content)
                    elif part_type == 'math':
                        try:
                            # LaTeX → MathML 변환 후 삽입
                            mathml_content = convert_latex_to_mathml(content)
                            temp_mml_path = create_temp_mathml_file(mathml_content)
                            hwp.import_mathml(temp_mml_path)
                            cleanup_temp_file(temp_mml_path)
                        except Exception as e:
                            print(f"수식 변환 오류: {e}")
                            hwp.insert_text(f"[수식 오류: {content}]")
                
                # 줄바꿈
                hwp.insert_text("\r\n")
        
        # 문제 간 간격 추가
        if i < len(problems_list):
            hwp.insert_text("\r\n")
    
    # 파일 저장
    if output_path:
        try:
            hwp.save_as(output_path)
            print(f"문서가 저장되었습니다: {output_path}")
        except Exception as e:
            print(f"파일 저장 오류: {e}")
    
    return hwp

def test_hwp_document():
    """HWP 문서 생성 기능 테스트"""
    print("HWP 문서 생성 테스트 시작...")
    print("=" * 60)
    
    # 테스트 케이스 1: 간단한 수식이 포함된 텍스트
    test1 = r"1. \( \frac{4}{2^{\sqrt{2}}} \) 의 값은? [2점]"
    print(f"테스트 1: {test1}")
    
    try:
        hwp1 = create_hwp_document(test1, "test1.hwpx")
        print("✅ 테스트 1 성공")
        time.sleep(1)  # HWP 처리 대기
    except Exception as e:
        print(f"❌ 테스트 1 실패: {e}")
    
    print("-" * 60)
    
    # 테스트 케이스 2: 여러 수식이 포함된 복잡한 텍스트
    test2 = r"""2. \( \lim_{x \rightarrow \infty} \frac{\sqrt{x^{2}-2}+3x}{x+5} \) 의 값은? [2점]
(1) \( \frac{1}{4} \) (2) \( \frac{1}{2} \) (3) 1 (4) 2 (5) 4"""
    
    print(f"테스트 2: 복잡한 수식 문제")
    
    try:
        hwp2 = create_hwp_document(test2, "test2.hwpx")
        print("✅ 테스트 2 성공")
        time.sleep(1)  # HWP 처리 대기
    except Exception as e:
        print(f"❌ 테스트 2 실패: {e}")
    
    print("-" * 60)
    
    # 테스트 케이스 3: 여러 문제를 하나의 문서로
    problems = [
        r"1. \( \frac{4}{2^{\sqrt{2}}} \) 의 값은? [2점]",
        r"2. \( \lim_{x \rightarrow \infty} \frac{\sqrt{x^{2}-2}+3x}{x+5} \) 의 값은? [2점]",
        r"3. \( \{a_n\} \) 에서 \( a_1 = 48 \) 일 때의 값은? [3점]"
    ]
    
    print("테스트 3: 여러 문제 통합 문서")
    
    try:
        hwp3 = process_math_problems(problems, "test_multiple.hwpx")
        print("✅ 테스트 3 성공")
    except Exception as e:
        print(f"❌ 테스트 3 실패: {e}")
    
    print("=" * 60)
    print("HWP 문서 생성 테스트 완료!")

if __name__ == "__main__":
    test_hwp_document() 