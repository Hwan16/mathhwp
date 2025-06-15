#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test.json 파일을 사용한 LaTeX to HWP 변환 테스트
"""

import os
import sys
from json_processor import process_json_to_hwp

def main():
    """test.json 파일로 변환 테스트 실행"""
    
    # 입력 파일과 출력 파일 경로 설정
    input_file = "test.json"
    output_file = "test_json_converted.hwpx"
    
    print("=" * 60)
    print("LaTeX to HWP 변환 테스트 (test.json)")
    print("=" * 60)
    
    # 입력 파일 존재 확인
    if not os.path.exists(input_file):
        print(f"❌ 오류: {input_file} 파일을 찾을 수 없습니다.")
        return False
    
    print(f"📁 입력 파일: {input_file}")
    print(f"📄 출력 파일: {output_file}")
    print()
    
    try:
        # 변환 실행
        print("🔄 변환 시작...")
        success = process_json_to_hwp(input_file, output_file)
        
        if success:
            print("✅ 변환 완료!")
            print(f"📄 생성된 파일: {output_file}")
            
            # 파일 크기 확인
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                print(f"📊 파일 크기: {file_size:,} bytes")
            
            return True
        else:
            print("❌ 변환 실패")
            return False
            
    except Exception as e:
        print(f"❌ 오류 발생: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 테스트 성공!")
    else:
        print("\n💥 테스트 실패!")
        sys.exit(1) 