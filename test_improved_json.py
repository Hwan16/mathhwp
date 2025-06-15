from json_processor import process_json_to_hwp

# 개선된 로직으로 실제 업로드된 test.json 파일 처리
print("🔧 개선된 로직으로 JSON 파일 처리 테스트...")
print("=" * 60)

success = process_json_to_hwp('test.json', 'test_final_improved.hwpx')

if success:
    print("🎉 개선된 JSON → HWPX 변환 성공!")
    print("📁 생성된 파일: test_final_improved.hwpx")
    print()
    print("🔍 변경사항:")
    print("  - 수식 삽입 순서 보장")
    print("  - 수식 처리 대기 시간 증가")
    print("  - 문서 저장 전 안정화 대기")
    print("  - 상세한 처리 로그 추가")
else:
    print("❌ 변환 실패")

print("=" * 60) 