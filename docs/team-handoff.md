# Bàn giao CP1 → CP2 → CP3 — EA1119

## Đã chuẩn bị

- Repo chung: `K5-L3B-DAY10-EA1119-PoCtoPilotGate1`; origin trỏ về repo nhóm.
- Ngày 19/11/2026: chạy `py -3 -m unittest discover -s tests`, kết quả `Ran 13 tests`, `OK`.
- Windows máy Tuấn dùng `py -3`; lệnh `python` chưa có trong PATH. Các máy khác dùng Python 3 tương ứng.
- Quyết định chung của team: dùng [eval card](lab9/eval_card.md) và [PRD v1.1](lab9/PRD_v1.1.md) của Tuấn cho CP2; nguồn và hash tại [đây](lab9/README.md).
- Đã điền tên nhóm trong `config/acceptance_criteria.json`; chưa đặt ngưỡng, chưa ký tiêu chí, chưa chạy CLI eval/grade, chưa sửa guard và chưa tạo checkpoint vòng 1.
- Đã lấy họ tên Phạm Quang Tuấn và MSSV 2A202603824 từ tên folder/repo Lab 9. Còn thiếu họ tên đầy đủ/MSSV của Nhật, Công, Quyền và xác nhận trưởng nhóm; vì vậy chưa chốt toàn bộ CP1.

## Công làm tiếp — CP2

1. Đọc hai tài liệu Lab 9 và `data/world.json` mục `ops_limits`, `ops_facts`.
2. Hoàn thiện Phiếu A A1–A4; xác định cách đo, các ngưỡng, hành động khi trượt và ngày xem lại.
3. Điền `signed_by`, `required`, `nice_to_have`, `business_ops`, `stop_condition`, bốn dòng `decision_rule` trong `config/acceptance_criteria.json`.
4. Tuấn góp ý rủi ro kỹ thuật; Nhật kiểm tra cách tính metric; Quyền kiểm tra dữ liệu cá nhân, hàng chờ và điều kiện dừng. Ghi kết luận là “Quyết định chung của team”.
5. Khi đầy đủ và chốt xong, ký rồi commit/push ngay; ghi giờ ký và commit vào A5. Sau ký không sửa file tiêu chí.

```powershell
py -3 -m lab10.criteria sign
# Chỉ tiếp tục khi lệnh ký thành công. Trên PowerShell, chạy từng dòng Git máy in ra.
git add config/acceptance_criteria.json config/acceptance_criteria.lock
git commit -m "Sign acceptance criteria"
git push origin main
```

## Nhật làm tiếp — đầu CP3, sau khi CP2 hoàn tất

```powershell
py -3 -m lab10.eval --suite base --stage base --note "baseline"
# Thay RUN_ID bằng mã lệnh trên in ra trước khi chạy:
py -3 -m lab10.gate --run runs/RUN_ID/report.json
py -3 -m lab10.trace --suite base --ticket T-002 --seed 55
```

Bàn giao Tuấn: mã run, chỉ số trượt, ticket@seed, sự kiện/tool và tham số sai, dữ liệu đúng để đối chiếu; chuẩn bị hai tình huống thử hiểm cùng kết quả mong đợi. Điền B0–B2 và B7.3 theo bằng chứng thực tế.

## Tuấn và Quyền làm tiếp — CP3

- Trong lúc Nhật đo: Công làm B3; Quyền làm B4–B5. Cả team làm pre-mortem B6.
- Sau baseline và phân tích rủi ro: Tuấn mới sửa `guards.py`, viết 2–3 cổng và B7.1–B7.2.
- Công điền `business`; Quyền điền `operations`, `legal`, checklist và runbook. Tuấn nhận các ngưỡng và quy định này để viết cổng.
- Nhật kiểm thử cổng, hai ca thử hiểm và regression; khi ổn mới chạy checkpoint, eval prepared và gate, rồi cả team chốt v1/B8 và push.

Không tạo lock/checkpoint trước khi hoàn thiện đầu vào. Không ghi mã run, kết quả đạt hoặc quyết định v1/v2 khi chưa có bằng chứng.

## CP2 đã ký — cập nhật sau cùng

Tuấn đã đọc và duyệt tiêu chí; ký lúc 2026-11-19T15:12:44 (GMT+7). Commit ký: `45ef97b`, đã push lên origin/main và verify trả về ok. Các chỉ dẫn chờ ký ở trên là lịch sử chuẩn bị; không chạy sign lại. Nhật có thể bắt đầu CP3 sau khi pull bản mới; chưa có lần eval CLI nào được thực hiện.
