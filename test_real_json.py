from json_processor import process_json_to_hwp

# 실제 업로드된 test.json 파일 처리
print("실제 JSON 파일 처리 테스트...")
print("=" * 50)

success = process_json_to_hwp('test.json', 'real_test_converted.hwpx')

if success:
    print("🎉 실제 JSON → HWPX 변환 성공!")
else:
    print("❌ 변환 실패")

print("=" * 50) 