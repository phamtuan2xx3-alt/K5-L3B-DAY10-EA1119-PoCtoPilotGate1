# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): EA1119
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-EA1119-PoCtoPilotGate1`
- Link repo: https://github.com/phamtuan2xx3-alt/K5-L3B-DAY10-EA1119-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): Chưa cập nhật

## Thành viên

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
| 1 | Phạm Quang Tuấn | 2A202603824 | Kỹ sư cổng — viết cổng kiểm soát | Chờ xác nhận |
| 2 | Nhật (cần bổ sung họ tên đầy đủ) | Chờ bổ sung | Kỹ sư cổng — kiểm thử và đo lường | |
| 3 | Công (cần bổ sung họ tên đầy đủ) | Chờ bổ sung | Sản phẩm và kinh doanh | |
| 4 | Quyền (cần bổ sung họ tên đầy đủ) | Chờ bổ sung | Vận hành và pháp lý | |

Trước khi nộp, bổ sung họ tên đầy đủ, MSSV và trưởng nhóm; đổi tiêu đề cá nhân thành `HoVaTen-MSSV`. Ghi `members` trong `submission/submission.json` khớp bảng trên.

## Cá nhân

Mỗi thành viên tự điền đóng góp thực tế, bằng chứng và exit ticket. Nếu dùng AI, ghi rõ phần việc đã dùng.

## PhamQuangTuan-2A202603824

### Phần việc phụ trách

- Đọc luồng agent, helper và tool; viết 2–3 cổng phòng ngừa trong `lab10/guards.py` (`pre_guard`, `write_gate`).
- Vòng 1: Phiếu B B7.1–B7.2.
- Vòng 2: sửa cổng theo nguyên nhân sự cố; Phiếu C C7; đóng góp C5–C6 và C9.
- Phối hợp Nhật kiểm thử, Công xác định ngưỡng kinh doanh, Quyền xác định yêu cầu vận hành và pháp lý.

### Đóng góp cụ thể

Chuẩn bị đầu vào Lab 9, rà soát và duyệt tiêu chí CP2. Có dùng AI hỗ trợ soạn tài liệu và kiểm tra cấu hình.

### Bằng chứng

Chờ bổ sung mã commit, mã lần chạy và mục phiếu.

### Exit ticket

Chờ thành viên tự ghi một điều học được và một điều còn chưa chắc.

## Nhat — chờ họ tên đầy đủ và MSSV

### Phần việc phụ trách

- Chạy baseline sau khi ký tiêu chí; đọc trace `T-002@55`; thiết kế behavioral test và hai ticket thử; kiểm tra hồi quy.
- Thêm ít nhất một monitor mới trong `lab10/monitors.py`; quản lý report ba mốc `base`, `prepared`, `after`.
- Phiếu B B0–B2, B7.3; Phiếu C C0–C2, C8.

### Đóng góp cụ thể

Chờ thành viên tự ghi, kèm phần việc có sử dụng AI.

### Bằng chứng

Chờ bổ sung mã commit, mã lần chạy và mục phiếu.

### Exit ticket

Chờ thành viên tự ghi một điều học được và một điều còn chưa chắc.

## Cong — chờ họ tên đầy đủ và MSSV

### Phần việc phụ trách

- Chủ trì Phiếu A và `config/acceptance_criteria.json`; cả nhóm thống nhất tiêu chí trước khi ký và đo.
- Điền mục `business` trong `config/operating_gates.json`: trần hoàn tiền, ngân sách, ROI và phạm vi pilot.
- Phiếu B B3, B7.4, B8; Phiếu C C12. Tổng hợp quyết định v1/v2 do cả nhóm thống nhất.

### Đóng góp cụ thể

Chờ thành viên tự ghi, kèm phần việc có sử dụng AI.

### Bằng chứng

Chờ bổ sung mã commit, mã lần chạy và mục phiếu.

### Exit ticket

Chờ thành viên tự ghi một điều học được và một điều còn chưa chắc.

## Quyen — chờ họ tên đầy đủ và MSSV

### Phần việc phụ trách

- HAZOP, checklist có PIC, hàng chờ và người trực, bảo vệ dữ liệu, runbook và risk register.
- Điền mục `operations`, `legal` trong `config/operating_gates.json`; gom bài với `submission/submission.json`.
- Phiếu B B4–B5, B7.5–B7.6; Phiếu C C4, C10–C11.

### Đóng góp cụ thể

Chờ thành viên tự ghi, kèm phần việc có sử dụng AI.

### Bằng chứng

Chờ bổ sung mã commit, mã lần chạy và mục phiếu.

### Exit ticket

Chờ thành viên tự ghi một điều học được và một điều còn chưa chắc.

## Quyết định chung của team

- Cả nhóm làm pre-mortem B6, C3 theo thẻ, phân tích C5–C6 và C9; thống nhất quyết định v1/v2.
- Ký, commit và push tiêu chí trước mọi lần đánh giá; giữ nguyên tiêu chí sau khi ký và bản chốt vòng 1.
- Mỗi thành viên tự hoàn thiện mục cá nhân và nộp link repo trên LMS.
### Phân công đã thống nhất

| Người | Việc riêng | File chính |
| --- | --- | --- |
| Tuấn | Viết và sửa cổng kiểm soát; B7.1–B7.2, C7 | `lab10/guards.py` |
| Nhật | Kiểm thử, trace, monitor và report ba mốc; B0–B2, B7.3, C0–C2, C8 | `lab10/monitors.py`, report lần chạy |
| Công | Tiêu chí, kinh doanh và tổng hợp quyết định; Phiếu A, B3, B7.4, B8, C12 | `config/acceptance_criteria.json`, mục `business` |
| Quyền | HAZOP, checklist, runbook, rủi ro và gom bài; B4–B5, B7.5–B7.6, C4, C10–C11 | Mục `operations`, `legal`, `submission/submission.json` |

### Cách phối hợp đã thống nhất

- Công tổng hợp tiêu chí; cả team chịu trách nhiệm về ngưỡng và quy tắc quyết định. Ký, commit, push trước lần eval đầu tiên; sau khi ký giữ nguyên file tiêu chí.
- Nhật đo baseline và gửi mã run, trace lỗi, dữ liệu đối chiếu cho Tuấn trước khi Tuấn sửa cổng vòng 1.
- Tuấn viết 2–3 cổng dựa trên bằng chứng và pre-mortem/HAZOP; Công cung cấp ngưỡng kinh doanh, Quyền cung cấp yêu cầu vận hành/pháp lý.
- Nhật kiểm thử sau mỗi lần sửa; khi chốt vòng 1, tạo checkpoint và report prepared, giữ nguyên bản chụp vòng 1.
- Khi nhận thẻ, Nhật đo trước khi sửa; cả team phân tích, Tuấn sửa cổng, Nhật thêm monitor và kiểm tra lại bộ nền lẫn bộ thẻ.
- Cả team cùng làm B6, C3 theo thẻ, C5–C6 và C9. Công ghi quyết định v1/v2 dưới tên “Quyết định chung của team”, gắn với tiêu chí đã ký và mã report thực tế.
- Quyền gom bài và kiểm tra tới khi lệnh `python -m lab10.check_submission --collect` in `ĐỦ THÀNH PHẦN`; mỗi thành viên tự điền đóng góp và nộp LMS.

### Mốc nghiệm thu chung

| Mốc | Điều kiện cần xác nhận |
| --- | --- |
| CP1 | Repo nhóm đúng, bảng thành viên đầy đủ, 13 tests OK |
| CP2 | Tiêu chí đã ký, commit và push trước mọi lần eval |
| CP3 | Có baseline, trace, cổng vòng 1, kiểm thử và report prepared; quyết định v1 đã ghi và push |
| CP4 | Đã đo thẻ trước khi sửa; report có integrity, visible, regression, monitor đạt; phạm vi pilot lớn hơn 0 |
| CP5 | Quyết định v2 khớp bằng chứng; bài đủ thành phần; đã push; từng người nộp LMS |

Các ngưỡng cụ thể, quyết định v1/v2 và trạng thái đạt checkpoint chỉ được ghi là đã chốt/đã đạt khi có dữ liệu và bằng chứng tương ứng. Hiện chưa xác nhận các mốc này đã hoàn thành.

## Tài liệu và bàn giao

- [Đầu vào Lab 9 dùng chung](docs/lab9/README.md): eval card và PRD v1.1 của Tuấn.
- [Việc tiếp theo theo CP](docs/team-handoff.md): trạng thái chuẩn bị và thứ tự bàn giao.
