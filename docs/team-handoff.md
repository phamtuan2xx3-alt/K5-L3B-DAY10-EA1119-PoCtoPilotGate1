# Bàn giao CP3 → CP4 — EA1119

## Trạng thái hiện tại

- CP2 đã ký tại commit `45ef97b`; hash tiêu chí `081e817c9c3251ae569f8491cba9d35444a91c62cfec5804a928d96c857d9a6d`. Không sửa file tiêu chí.
- CP3 đã có baseline, phân tích B1–B6, 3 nhóm cổng, config và runbook B7, behavioral tests, bản chốt prepared và quyết định v1/B8.
- Bản chốt vòng1: `fdb61587`, tạo19/11/2026 15:46:24 GMT+7. Giữ nguyên `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`.
- Prepared:110/110 trial, pass_rate/pass_k1.0, hoàn sai/lỗi hãng oan/PII0, không regression;4.449đ/ticket, ROI1.25, ùn0, maxwait0 phút, độ phủ1.0.
- Escalation22,73% vượt chỉ số nên có20%; tổng ca vào hàng duyệt gồm kiểm mẫu27,27%. Không ép giảm chuyển người để đạt hình thức.
- **v1: Dừng pilot** theo stop_condition đã ký vì baseline chạm2 nhóm lỗi an toàn. Bản sửa nền đã đạt không tự xóa trigger. Chưa có pilot thật đang chạy; CP4 vẫn đánh giá offline.
- Họ tên đầy đủ/MSSV của Nhật, Công, Quyến và exit ticket từng người vẫn cần bổ sung; không coi các mục cá nhân là đã hoàn thành.

## Team đọc

1. `TEAM.md`: vai và danh tính Git. Trưởng nhóm Tuấn, MSSV2A202603824; mỗi máy đặt local user.name=`2A202603824`, user.email=`2A202603824@example.com` theo README.
2. `templates/form-b-evaluation-gates.md`: toàn bộ kết quả và v1; không ghi đè v1 khi nhận thẻ.
3. `docs/cp3-evidence/README.md`: report và trace có thể đọc ngay trên GitHub.

## Chờ Coach phát thẻ — đầu CP4

- Chỉ nhận đúng số S1–S8 Coach cấp; chưa có số thì không lấy ngẫu nhiên và không xem thẻ bàn khác.
- Một người nhận thẻ bằng ba lệnh README, ghi số vào đầu Phiếu C và TEAM.md, rồi commit/push để team pull.
- **Nhật:** chạy `py -3 -X utf8 -m lab10.grade --incident Sx` trước khi ai sửa code/config. Ghi mã prepared và kết quả vào C0–C1; trace ít nhất hai ticket hỏng khác kiểu. Giữ mọi report/journal.
- **Cả team:** làm C2–C6 theo bằng chứng; Công đọc tiền/ROI/phạm vi, Quyến đọc người duyệt/dữ liệu/bên thứ ba. C3 chỉ phần của thẻ.
- **Tuấn:** sau khi đã đo và phân tích, sửa tiếp `lab10/guards.py`, ghi C7; không sửa snapshot.
- **Nhật:** thêm ít nhất1 monitor mới trong `lab10/monitors.py`; escalation_rate có sẵn không tính. Đo thẻ và bộ nền sau sửa, kiểm regression; C8.
- **Quyến:** cập nhật risk register C10, checklist/runbook C11; cả nhóm cập nhật fault tree C9. Công tổng hợp v2/C12 theo cùng tiêu chí đã ký.

Bài chưa phải submission cuối: chưa thẻ, monitor mới, Phiếu C, v2 hay collect. Chỉ chạy collect ở CP5 sau khi đủ đầu vào; mỗi người tự nộp link LMS.

## CP4 S5 đã hoàn thành — cập nhật mới nhất

Đã nhận S5, đo trước sửa, phân tích và hoàn thiện Phiếu C C0–C11. Scope đánh giá giữ HN/HCM/DN/CT, B2B manual. Grade `R-S5-grade-20261119-165030-65d527` đạt PASS-VISIBLE; integrity/criteria/visible/regression/monitor đều xanh, hidden chưa chạy. S5 giữ60% độ phủ,90/90 đúng,3.980đ/ticket,ROI1.51; nền110/110,13 tests OK. Tiêu chí và snapshot giữ nguyên. CP5 còn C12/v2, ba dòng bắt buộc, collect và phần cá nhân mỗi người; chưa báo bài nộp cuối hoàn thành.

## CP5 — bộ bài đã gom, phần người còn lại

C12/v2 và ba dòng trong submission.json đã hoàn thiện, quyết định Dừng khớp tiêu chí ký. check_submission --collect báo ĐỦ THÀNH PHẦN. Xem docs/demo-cp5.md để chuẩn bị demo. Chưa ghi nhận demo/feedback, exit ticket cá nhân hay LMS; từng người tự hoàn thiện phần này rồi push trước hạn. Không sửa code/config mà quên grade và collect lại.
