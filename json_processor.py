import json
import os
from typing import Dict, List, Any
from hwp_document import process_math_problems

def load_json_file(json_path: str) -> Dict[str, Any]:
    """
    JSON 파일을 로드하고 유효성을 검사하는 함수
    
    Args:
        json_path (str): JSON 파일 경로
        
    Returns:
        Dict[str, Any]: 파싱된 JSON 데이터
        
    Raises:
        FileNotFoundError: 파일이 존재하지 않는 경우
        json.JSONDecodeError: JSON 형식이 잘못된 경우
        ValueError: 필수 필드가 없는 경우
    """
    # 파일 존재 확인
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"JSON 파일을 찾을 수 없습니다: {json_path}")
    
    # JSON 파일 읽기
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"JSON 파싱 오류: {e}")
    
    # 필수 필드 검증
    if 'problems' not in data:
        raise ValueError("JSON 파일에 'problems' 필드가 없습니다.")
    
    if not isinstance(data['problems'], list):
        raise ValueError("'problems' 필드는 배열이어야 합니다.")
    
    # 각 문제 객체 검증
    for i, problem in enumerate(data['problems']):
        if not isinstance(problem, dict):
            raise ValueError(f"문제 {i+1}이 객체가 아닙니다.")
        
        if 'latex_string' not in problem:
            raise ValueError(f"문제 {i+1}에 'latex_string' 필드가 없습니다.")
    
    return data

def extract_latex_strings(json_data: Dict[str, Any]) -> List[str]:
    """
    JSON 데이터에서 latex_string들을 추출하는 함수
    
    Args:
        json_data (Dict[str, Any]): 파싱된 JSON 데이터
        
    Returns:
        List[str]: latex_string 리스트
    """
    latex_strings = []
    
    for problem in json_data['problems']:
        latex_string = problem['latex_string']
        latex_strings.append(latex_string)
    
    return latex_strings

def process_json_to_hwp(json_path: str, output_path: str = None) -> bool:
    """
    JSON 파일을 읽어서 HWPX 문서로 변환하는 메인 함수
    
    Args:
        json_path (str): 입력 JSON 파일 경로
        output_path (str, optional): 출력 HWPX 파일 경로
        
    Returns:
        bool: 성공 시 True, 실패 시 False
    """
    try:
        print(f"JSON 파일 로딩 중: {json_path}")
        
        # JSON 파일 로드 및 검증
        json_data = load_json_file(json_path)
        
        # 메타데이터 출력
        source_file = json_data.get('source_file', '알 수 없음')
        converted_at = json_data.get('converted_at', '알 수 없음')
        problem_count = len(json_data['problems'])
        
        print(f"✅ JSON 파일 로드 성공")
        print(f"   - 원본 파일: {source_file}")
        print(f"   - 변환 시간: {converted_at}")
        print(f"   - 문제 개수: {problem_count}개")
        
        # LaTeX 문자열 추출
        latex_strings = extract_latex_strings(json_data)
        
        # 출력 파일 경로 설정
        if output_path is None:
            base_name = os.path.splitext(os.path.basename(json_path))[0]
            output_path = f"{base_name}_converted.hwpx"
        
        print(f"HWPX 문서 생성 중: {output_path}")
        
        # HWPX 문서 생성
        hwp = process_math_problems(latex_strings, output_path)
        
        print(f"✅ 변환 완료: {output_path}")
        return True
        
    except FileNotFoundError as e:
        print(f"❌ 파일 오류: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        return False
    except ValueError as e:
        print(f"❌ 데이터 검증 오류: {e}")
        return False
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")
        return False

def create_sample_json(output_path: str = "sample_problems.json"):
    """
    테스트용 샘플 JSON 파일을 생성하는 함수
    
    Args:
        output_path (str): 생성할 JSON 파일 경로
    """
    sample_data = {
        "source_file": "수학영역_문제지_풀수형.pdf",
        "converted_at": "2025-06-15T14:24:32.524Z",
        "problems": [
            {
                "id": 1,
                "latex_string": r"1. \( \left(\frac{4}{2^{\sqrt{2}}}\right)^{2+\sqrt{2}} \) 의 값은? [2점]\n(1) \( \frac{1}{4} \)\n(2) \( \frac{1}{2} \)\n(3) 1\n(4) 2\n(5) 4",
                "comment": "1번 문제",
                "confidence": 100
            },
            {
                "id": 2,
                "latex_string": r"2. 함수 \( f(x)=x^{3}-8 x+7 \) 에 대하여 \( \lim_{h \rightarrow 0} \frac{f(2+h)-f(2)}{h} \) 의 값은? [2점]\n(1) 1\n(2) 2\n(3) 3\n(4) 4\n(5) 5",
                "comment": "2번 문제",
                "confidence": 100
            },
            {
                "id": 3,
                "latex_string": r"3. 첫째항과 공비가 모두 양수인 \( k \) 인 등비수열 \( \left\{a_{n}\right\} \) 이 \( a_{4}\left(a_{2}\right)+\frac{a_{2}}{a_{1}}=30 \) 을 만족시킬 때, \( k \) 의 값은? [3점]\n(1) 1\n(2) 2\n(3) 3\n(4) 4\n(5) 5",
                "comment": "3번 문제",
                "confidence": 100
            },
            {
                "id": 4,
                "latex_string": r"4. 함수 \( f(x)=\left\{\begin{array}{ll}5 x+a & (x<-2) \\ x^{2}-a & (x \geq-2)\end{array}\right. \) 에서 연속일 때, 상수 \( a \) 의 값은? [3점]\n(1) 6\n(2) 7\n(3) 8\n(4) 9\n(5) 10",
                "comment": "4번 문제",
                "confidence": 93
            }
        ]
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 샘플 JSON 파일 생성: {output_path}")

def test_json_processor():
    """JSON 처리 기능 테스트"""
    print("JSON 처리 기능 테스트 시작...")
    print("=" * 60)
    
    # 1. 샘플 JSON 파일 생성
    sample_file = "sample_problems.json"
    create_sample_json(sample_file)
    
    print("-" * 60)
    
    # 2. JSON → HWPX 변환 테스트
    success = process_json_to_hwp(sample_file, "sample_converted.hwpx")
    
    if success:
        print("✅ JSON → HWPX 변환 테스트 성공!")
    else:
        print("❌ JSON → HWPX 변환 테스트 실패!")
    
    print("=" * 60)
    print("JSON 처리 기능 테스트 완료!")

if __name__ == "__main__":
    test_json_processor() 