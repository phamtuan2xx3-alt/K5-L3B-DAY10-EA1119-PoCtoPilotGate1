# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): EA1119
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-EA1119-PoCtoPilotGate1`
- Link repo: [https://github.com/phamtuan2xx3-alt/K5-L3B-DAY10-EA1119-PoCtoPilotGate1](https://github.com/phamtuan2xx3-alt/K5-L3B-DAY10-EA1119-PoCtoPilotGate1)
- Thẻ sự cố đã bốc (S1–S8): S5

## Thành viên


| STT | Họ và tên | MSSV | GitHub | Vai | Trưởng nhóm |
| ---: | --- | --- | --- | --- | :---: |
| 1 | Phạm Quang Tuấn | 2A202603824 | phamtuan2xx3-alt | Kỹ sư cổng — viết cổng kiểm soát | Có |
| 2 | Chu Văn Nhật | 2A202603848 | moyymochi11 | Kỹ sư cổng — kiểm thử và đo lường | |
| 3 | Nguyễn Thành Công | 2A202603789 | congnt180263 | Sản phẩm và kinh doanh | |
| 4 | Đồng Văn Quyến | 2A202603769 | dvq2609 | Vận hành và pháp lý | |

Thông tin thành viên đã được đối chiếu theo danh sách nhóm cung cấp ngày 19/11/2026. Mỗi người tự hoàn thiện đóng góp, bằng chứng và exit ticket. Ghi `members` trong `submission/submission.json` khớp bảng trên.

## Cá nhân

Mỗi thành viên tự điền đóng góp thực tế, bằng chứng và exit ticket. Nếu dùng AI, ghi rõ phần việc đã dùng.

## PhamQuangTuan-2A202603824

### Phần việc phụ trách

- Đọc luồng agent, helper và tool; viết 2–3 cổng phòng ngừa trong `lab10/guards.py` (`pre_guard`, `write_gate`).
- Vòng 1: Phiếu B B7.1–B7.2.
- Vòng 2: sửa cổng theo nguyên nhân sự cố; Phiếu C C7; đóng góp C5–C6 và C9.
- Phối hợp Nhật kiểm thử, Công xác định ngưỡng kinh doanh, Quyến xác định yêu cầu vận hành và pháp lý.

### Đóng góp cụ thể

Phụ trách đầu ra kỹ thuật: xây dựng ba nhóm cổng trong `lab10/guards.py`: xác minh chủ đơn/kiện và chính sách hiệu lực; tính lại quyền lợi còn lại từ tracking và ledger, kiểm tra approval và hạn mức; xác minh lỗi hãng và tối thiểu hóa dữ liệu gửi ra ngoài. Chuẩn bị hai ca thử hiểm và bộ kiểm tra hành vi; chốt snapshot vòng 1. Phân tích nguyên nhân và giới hạn cổng trong B7.1–B7.2, C5–C7 và C9. Rà soát, duyệt tiêu chí và ký đại diện nhóm. Có dùng AI hỗ trợ code, kiểm thử và tài liệu.

### Bằng chứng

Commit ký `45ef97b`; commit cổng vòng 1 `d3a6a0f`; snapshot `fdb61587`; `docs/cp3-evidence/behavior_checks.py`; Phiếu B B7.1–B7.3; Phiếu C C7/C9. Bộ nền sau sửa đạt 110/110, 13 public tests OK.

### Exit ticket

Một điều học được: Pass rate cao vẫn có thể che lỗi chi tiền và ghi oan hãng; cổng kiểm soát phải đối chiếu tracking, chính sách và ledger trước khi ghi.

Một điều còn chưa chắc: Cổng chống hoàn lặp hiện chạy đúng trong mô phỏng tuần tự; khi nhiều worker cùng xử lý một đơn, cần thêm transaction hoặc idempotency ở DB để tránh chi trùng.

## ChuVanNhat-2A202603848

### Phần việc phụ trách

- Chạy baseline sau khi ký tiêu chí; đọc trace `T-002@55`; thiết kế behavioral test và hai ticket thử; kiểm tra hồi quy.
- Thêm ít nhất một monitor mới trong `lab10/monitors.py`; quản lý report ba mốc `base`, `prepared`, `after`.
- Phiếu B B0–B2, B7.3; Phiếu C C0–C2, C8.

### Đóng góp cụ thể

Phụ trách đầu ra kiểm thử và đo lường: tổng hợp baseline và trace T-002@55, đối chiếu kết quả trước/sau cổng và theo dõi regression. Với S5, hồ sơ kiểm thử bao gồm đo prepared trước khi sửa, trace các nhánh chi phí B2B, ticket dài và hoàn lặp; đánh giá lại S5 và bộ nền. Phần monitor bổ sung đo chi phí máy/công duyệt theo kho và tiền LLM cao nhất, không đọc nhãn đúng/sai. Quản lý bảng mã lần chạy, report ba mốc và nhật ký tại B0–B2, B7.3, C0–C2 và C8.

### Bằng chứng

Đầu ra tại commit `8a4d28f`; `lab10/monitors.py`; grade `R-S5-grade-20261119-165030-65d527`; `docs/cp4-evidence/journal.jsonl`; S5 90/90 trong scope, nền 110/110, regression và monitor đạt. Đây là bằng chứng đầu ra theo vai; nhật ký thao tác cá nhân do thành viên xác nhận thêm.

### Exit ticket

Chờ thành viên tự ghi một điều học được và một điều còn chưa chắc.

## NguyenThanhCong-2A202603789

### Phần việc phụ trách

- Chủ trì Phiếu A và `config/acceptance_criteria.json`; cả nhóm thống nhất tiêu chí trước khi ký và đo.
- Điền mục `business` trong `config/operating_gates.json`: trần hoàn tiền, ngân sách, ROI và phạm vi pilot.
- Phiếu B B3, B7.4, B8; Phiếu C C12. Tổng hợp quyết định v1/v2 do cả nhóm thống nhất.

### Đóng góp cụ thể

Phụ trách đầu ra sản phẩm và kinh doanh: tổng hợp mục tiêu, thước đo và tiêu chí trong Phiếu A từ eval card/PRD Lab 9 và dữ liệu vận hành Lab 10; giải thích ngưỡng chất lượng, an toàn, chi phí và ROI. Hoàn thiện bản đồ dữ liệu B3 và cấu hình business: cap hoàn 1.800.000đ/ngày, budget LLM 1.200đ, ROI tối thiểu 0,25. Phân tích chi phí theo kho để đưa B2B về manual, giữ 60% phạm vi S5. Tổng hợp v1/v2 Dừng theo điều kiện đã ký; tách chi phí phần giữ và chi phí manual, không gán ROI phần giữ cho toàn bộ luồng.

### Bằng chứng

Phiếu A A1–A4; Phiếu B B3/B7.4/B8; Phiếu C C3/C8/C12; `config/operating_gates.json` mục business; commit bộ bài `fad298c`. Report S5: 3.980đ/ticket, ROI 1,51 cho 18 ca/ngày trong scope; 12 ca/ngày ngoài scope. Tiêu chí được Tuấn ký tại `45ef97b`.

### Exit ticket

Chờ thành viên tự ghi một điều học được và một điều còn chưa chắc.

## DongVanQuyen-2A202603769

### Phần việc phụ trách

- HAZOP, checklist có PIC, hàng chờ và người trực, bảo vệ dữ liệu, runbook và risk register.
- Điền mục `operations`, `legal` trong `config/operating_gates.json`; gom bài với `submission/submission.json`.
- Phiếu B B4–B5, B7.5–B7.6; Phiếu C C4, C10–C11.

### Đóng góp cụ thể

Phụ trách đầu ra vận hành và pháp lý: lập HAZOP, checklist 9 nhóm và risk register; xác định PIC NV-TUNG, người duyệt NV-HANH, đầu mối đối soát NV-OANH. Hoàn thiện cấu hình operations/legal và runbook: 1 người duyệt, 6 ca/giờ, SLA 60 phút, kiểm mẫu 10%, điều kiện dừng và bàn giao manual. Phân tích ảnh hưởng của B2B ngoài scope, PII và các bên thứ ba; cập nhật fault tree/runbook sau S5. Hoàn thiện thông tin thành viên, thẻ, quyết định và ba dòng bắt buộc trong submission.json; bộ bài đã được gom và kiểm đủ thành phần.

### Bằng chứng

Phiếu B B4–B5/B7.5–B7.6; Phiếu C C4/C10–C11; `config/operating_gates.json` mục operations/legal; `submission/submission.json` và `submission/manifest.json`; commit `fad298c`. Lệnh `lab10.check_submission` xác nhận ĐỦ THÀNH PHẦN; chưa ghi nhận nộp LMS hay diễn tập production.

### Exit ticket

Chờ thành viên tự ghi một điều học được và một điều còn chưa chắc.

## Quyết định chung của team

- Cả nhóm làm pre-mortem B6, C3 theo thẻ, phân tích C5–C6 và C9; thống nhất quyết định v1/v2.
- Ký, commit và push tiêu chí trước mọi lần đánh giá; giữ nguyên tiêu chí sau khi ký và bản chốt vòng 1.
- Mỗi thành viên tự hoàn thiện mục cá nhân và nộp link repo trên LMS.

### Phân công đã thống nhất


| Người | Việc riêng                                                                  | File chính                                              |
| ----- | --------------------------------------------------------------------------- | ------------------------------------------------------- |
| Tuấn  | Viết và sửa cổng kiểm soát; B7.1–B7.2, C7                                   | `lab10/guards.py`                                       |
| Nhật  | Kiểm thử, trace, monitor và report ba mốc; B0–B2, B7.3, C0–C2, C8           | `lab10/monitors.py`, report lần chạy                    |
| Công  | Tiêu chí, kinh doanh và tổng hợp quyết định; Phiếu A, B3, B7.4, B8, C12     | `config/acceptance_criteria.json`, mục `business`       |
| Quyến | HAZOP, checklist, runbook, rủi ro và gom bài; B4–B5, B7.5–B7.6, C4, C10–C11 | Mục `operations`, `legal`, `submission/submission.json` |


### Cách phối hợp đã thống nhất

- Công tổng hợp tiêu chí; cả team chịu trách nhiệm về ngưỡng và quy tắc quyết định. Ký, commit, push trước lần eval đầu tiên; sau khi ký giữ nguyên file tiêu chí.
- Nhật đo baseline và gửi mã run, trace lỗi, dữ liệu đối chiếu cho Tuấn trước khi Tuấn sửa cổng vòng 1.
- Tuấn viết 2–3 cổng dựa trên bằng chứng và pre-mortem/HAZOP; Công cung cấp ngưỡng kinh doanh, Quyến cung cấp yêu cầu vận hành/pháp lý.
- Nhật kiểm thử sau mỗi lần sửa; khi chốt vòng 1, tạo checkpoint và report prepared, giữ nguyên bản chụp vòng 1.
- Khi nhận thẻ, Nhật đo trước khi sửa; cả team phân tích, Tuấn sửa cổng, Nhật thêm monitor và kiểm tra lại bộ nền lẫn bộ thẻ.
- Cả team cùng làm B6, C3 theo thẻ, C5–C6 và C9. Công ghi quyết định v1/v2 dưới tên “Quyết định chung của team”, gắn với tiêu chí đã ký và mã report thực tế.
- Quyến gom bài và kiểm tra tới khi lệnh `python -m lab10.check_submission --collect` in `ĐỦ THÀNH PHẦN`; mỗi thành viên tự điền đóng góp và nộp LMS.

### Mốc nghiệm thu chung


| Mốc | Điều kiện cần xác nhận                                                                                  |
| --- | ------------------------------------------------------------------------------------------------------- |
| CP1 | Repo nhóm đúng, bảng thành viên đầy đủ, 13 tests OK                                                     |
| CP2 | Tiêu chí đã ký, commit và push trước mọi lần eval                                                       |
| CP3 | Có baseline, trace, cổng vòng 1, kiểm thử và report prepared; quyết định v1 đã ghi và push              |
| CP4 | Đã đo thẻ trước khi sửa; report có integrity, visible, regression, monitor đạt; phạm vi pilot lớn hơn 0 |
| CP5 | Quyết định v2 khớp bằng chứng; bài đủ thành phần; đã push; từng người nộp LMS                           |


Team đã hoàn thiện các đầu ra kỹ thuật và hồ sơ CP1–CP5, kiểm thử công khai và gom bài có bằng chứng. Demo, xác nhận đóng góp/exit ticket và LMS do từng thành viên hoàn tất riêng; test ẩn chưa chạy.

## Tài liệu và bàn giao

- [Đầu vào Lab 9 dùng chung](docs/lab9/README.md): eval card và PRD v1.1 của Tuấn.
- [Việc tiếp theo theo CP](docs/team-handoff.md): trạng thái chuẩn bị và thứ tự bàn giao.

## Danh tính Git của repo nhóm

Trưởng nhóm: Phạm Quang Tuấn, MSSV `2A202603824`. Mỗi máy làm repo nhóm đặt cấu hình local theo README (không dùng email cá nhân):

```powershell
git config --local user.name 2A202603824
git config --local user.email 2A202603824@example.com
```

Cấu hình chỉ áp dụng cho repo này; mỗi thành viên vẫn tự ghi đóng góp trong mục cá nhân và tự nộp LMS.

## Bàn giao sau CP3

Đã hoàn thành hồ sơ vòng1: Phiếu B B0–B8, guards/config, test và report prepared; snapshot `fdb61587`. Kết quả bộ nền110/110, không lỗi an toàn, không regression; v1 Dừng theo trigger baseline trong tiêu chí đã ký. CP4 chờ Coach cấp đúng thẻ trước khi đo/sửa. Xem [bằng chứng CP3](docs/cp3-evidence/README.md) và [bàn giao CP4](docs/team-handoff.md). Mục cá nhân của từng thành viên và thông tin còn thiếu do chính thành viên bổ sung.
## Kết quả kiểm tra chung và bàn giao theo vai

Team đã kiểm tra:13 public tests OK; S5 PASS-VISIBLE; required/business_ops và regression đạt; bộ bài ĐỦ THÀNH PHẦN. V1/v2 Dừng theo tiêu chí ký; không đồng nghĩa triển khai production. Các đầu ra được bàn giao theo vai dưới đây, không thay thế xác nhận thao tác cá nhân.

| Thành viên | Đầu ra đã hoàn thiện trong bộ bài chung | Bằng chứng |
| --- | --- | --- |
| Phạm Quang Tuấn | Ba nhóm guard, behavioral checks, snapshot vòng1 | d3a6a0f; docs/cp3-evidence; guards_round1 fdb61587 |
| Chu Văn Nhật | Report ba mốc, regression, monitor chi phí | 8a4d28f; grade R-S5-grade-20261119-165030-65d527; C8 |
| Nguyễn Thành Công | Phiếu A, business scope, phân tích chi phí và v1/v2 | 45ef97b; Phiếu B B8, Phiếu C C12; fad298c |
| Đồng Văn Quyến | HAZOP, risk register, runbook, bộ submission đã gom | C4/C10/C11; submission/manifest.json; fad298c |

[Hướng dẫn mỗi thành viên chạy/test và giải thích phần phụ trách](docs/huong-dan-theo-thanh-vien.md). Từng người bổ sung đóng góp thực tế và exit ticket sau khi tự kiểm chứng.
