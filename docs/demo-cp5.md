# Demo Gate 1 — EA1119 — S5 (5 phút)

1. **30 giây — Bài toán:** trợ lý hoàn tiền giao trễ; S5 hỏi tiền máy, công người và chi lặp. Tiêu chí ký trước eval, commit45ef97b; snapshot vòng1 fdb61587.
2. **1 phút — Base:** S5 pass83,33%, hoàn sai890.000đ trên150 trial,20 lỗi hãng oan, LLM max2.412đ, ROI-0.33. Chỉ nhìn độ chính xác là chưa đủ.
3. **1 phút — Prepared:** cổng tính lại từ tracking/policy/ledger, kiểm approval, payload tối thiểu; pass100%, tiền sai/fault oan0, LLM max765đ. Vẫn HCM-B2B10.382đ/ticket, cao hơn làm tay.
4. **1 phút — After:** cấu hình định tuyến B2B về manual, giữ60% phạm vi;90/90 đúng,3.980đ/ticket,ROI1.51, không ùn. Monitor tách machine/review theo kho, không lấy khoản hoàn hợp lệ làm thiệt hại.12 ca B2B/ngày và chi phí manual báo riêng.
5. **1 phút — Quyết định:** v1/v2 Dừng do điều kiện hai nhóm lỗi an toàn đã ký; không sửa luật sau khi xem số. Máy PASS-VISIBLE không thay thế quyết định của người. Hidden và dữ liệu thật chưa đo.
6. **30 giây — Bằng chứng:** mở submission/runs/grade-report.md; Phiếu C C12; chạy check_submission để kiểm đủ thành phần. Nếu sửa code/config lúc demo phải grade và collect lại.

## Phân công thuyết trình đề xuất

- Tuấn giải thích ba nhóm cổng và giới hạn ledger tuần tự.
- Nhật trình bày ba mốc, monitor và regression.
- Công giải thích ROI/phạm vi và quyết định v2.
- Quyến giải thích manual, SLA60 phút, PIC và điều kiện dừng5 phút.

## Trước khi nộp

Mỗi thành viên tự hoàn thiện đóng góp thực tế, bằng chứng và exit ticket trong TEAM.md; không nhận thay phần chưa thực hiện. Từng người tự nộp cùng link repo trên LMS. Lab sáng hạn23h59 cùng ngày, lab chiều/tối11h59 ngày hôm sau GMT+7, trừ khi Coach thông báo khác. Không khẳng định đã demo hoặc nộp LMS khi chưa thực hiện.
