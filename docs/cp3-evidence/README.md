# Bằng chứng CP3 — EA1119

- Bản quyết định và giải thích: [Phiếu B](../../templates/form-b-evaluation-gates.md).
- Các report nguyên bản: [runs](runs/); có cả lần thử bị regression để giữ lịch sử trung thực.
- [Journal đầy đủ CP3](journal.jsonl), [trace baseline T-002@55](baseline-T-002-seed55.json), [trace prepared T-002@55](prepared-T-002-seed55.json).
- Hai ca tự viết: [adhoc-1](adhoc-1.txt), [adhoc-2](adhoc-2.txt).
- Sáu kiểm tra hành vi: [kết quả](behavior-checks.json), [script chạy lại](behavior_checks.py). Chạy từ repo: `py -3 -X utf8 docs/cp3-evidence/behavior_checks.py`.

Bản prepared `R-base-prepared-20261119-154624-a12887`:110/110, không lỗi an toàn hoặc regression,4.449đ/ticket, ROI1.25;13 public tests OK. Nice-to-have escalation22,73% cần giải trình; nhóm kho? vẫn tốn hơn làm tay. Không xóa hoặc giấu các giới hạn này.

Hash snapshot vòng1 `fdb61587`; hash tiêu chí `081e817c`. Quyết định v1 **Dừng pilot** do trigger2 nhóm lỗi an toàn của baseline theo tiêu chí đã ký. Bản sửa đạt mẫu không đồng nghĩa production được phép triển khai.

Đây là lưu bằng chứng trung gian CP3, không thay thế `submission/` do collect gom ở CP5. Các lần chạy đầy đủ cùng110 trace mỗi lần vẫn ở `runs/` local; collector sẽ gom vào bài cuối. Chưa xem thẻ sự cố hoặc test ẩn.
