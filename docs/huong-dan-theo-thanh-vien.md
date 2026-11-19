# Hướng dẫn tự kiểm chứng theo vai — team EA1119

Team đã kiểm tra code và bộ bài: 13 public tests OK, S5 PASS-VISIBLE, collect ĐỦ THÀNH PHẦN. Đây là kết quả chung có report; từng thành viên dùng hướng dẫn này để tự chạy, hiểu và giải thích phần phụ trách. Test ẩn, demo và LMS không nằm trong xác nhận trên.

## Chuẩn bị chung

Chạy PowerShell tại thư mục repo (có README.md). Nếu chưa có thay đổi riêng, `git pull --ff-only`; nếu có thì lưu/commit phần mình trước, không discard công việc người khác.

```powershell
git config --local user.name 2A202603824
git config --local user.email 2A202603824@example.com
py -3 -X utf8 -m lab10.criteria verify
py -3 -X utf8 -m lab10.checkpoint verify
```

Kỳ vọng hai lệnh verify có `ok: true`. Không chạy sign hoặc checkpoint take lần nữa; không sửa acceptance_criteria.json, guards_round1.py, operating_gates.round1.json, round1.lock hay incidents/S5.

Nếu integrity báo các file chỉ khác do CRLF trên Windows, dừng chỉnh nội dung, đối chiếu MANIFEST và nhờ Tuấn khôi phục đúng byte LF gốc. Không sửa hash để làm xanh.

## Tuấn — cổng kiểm soát

Đọc `lab10/guards.py`, `helpers.py`, Phiếu B B2/B7 và Phiếu C C7/C9.

```powershell
py -3 -X utf8 -m unittest discover -s tests
py -3 -X utf8 docs/cp3-evidence/behavior_checks.py
py -3 -X utf8 -m lab10.trace --suite base --stage after --ticket T-002 --seed 55
py -3 -X utf8 -m lab10.trace --suite S5 --stage after --ticket S5-02 --seed 11
```

Kỳ vọng13 tests OK;6 kiểm tra hành vi true; T-002 không có khoản hoàn hoặc lỗi hãng; S5-02 không chi thêm sau S5-01. Trace replay các ticket cùng scenario trước ca được chọn, nên không chỉ nhìn ticket cuối riêng lẻ.

Cần giải thích: vì sao tracking thay lời khách; policy theo ngày thay index; ledger trừ quyền lợi còn lại; approval phải đúng scope; payload hãng chỉ giữ trường cho phép. Giới hạn: kiểm tuần tự chưa thay thế transaction chống race production.

## Nhật — kiểm thử và monitor

Đọc `lab10/monitors.py`, Phiếu C C0/C2/C8 và `submission/runs/grade-report.md`.

```powershell
py -3 -X utf8 -m lab10.grade --incident S5
```

Kỳ vọng PASS-VISIBLE, integrity/criteria/visible/regression/monitor đều xanh; hidden chưa chạy. Lệnh tạo mã run mới: ghi lại mã, không chép mã cũ làm bằng chứng cho lần chạy mới.

```powershell
py -3 -X utf8 -m lab10.eval --suite base --stage after --note "Nhat self-review: base regression"
py -3 -X utf8 -m lab10.eval --suite S5 --stage after --note "Nhat self-review: S5 cost monitors"
```

Kỳ vọng nền110/110, S5 90/90, pass_rate/pass_k1.0. Monitor kho lấy bình quân từng kho rồi max; machine khác review; không tính toàn bộ tiền hoàn hợp lệ là tiền mất. Nhóm kho? trên nền vẫn đắt; phải đọc giới hạn này. Sau chạy mới, Quyến gom lại bài để chứa journal/report mới.

## Công — tiêu chí, tiền và quyết định

Đọc Phiếu A A4, Phiếu C C3/C8/C12, `config/operating_gates.json` và `submission/submission.json`.

```powershell
py -3 -X utf8 -m lab10.gate --run submission/runs/R-S5-after-20261119-165032-65d527/report.json
py -3 -X utf8 -c "import json; r=json.load(open('submission/runs/grade-report.json',encoding='utf-8')); print('checks:',r['checks']); print('run_ids:',r['run_ids'])"
```

Kỳ vọng ngưỡng bắt buộc và business_ops đạt trên phần giữ. Cần giải thích:

- Chi phí3.980đ và ROI1.51 chỉ cho18 ticket/ngày trong scope;12 ca B2B/ngày đi manual. Độ phủ60%, không phải100%.
- Giả định manual10.000đ: tổng xấp xỉ191.640đ/30 ca, tiết kiệm108.360đ so300.000đ, chưa tính khác biệt giá/tải thật. Không gán ROI1.51 cho cả30 ca.
- V1/v2 Dừng theo trigger hai nhóm an toàn đã ký; grade cho phép cân nhắc Tiếp tục không tự miễn điều kiện dạng văn bản.
- ROI25% khi chi8.000 thay10.000 tương ứng tiết kiệm20%; không phải cùng mẫu số.

Không sửa tiêu chí để hợp kết quả. Nếu đề xuất thay đổi scope/config, giao Nhật đo lại nền/thẻ rồi mới cập nhật hồ sơ.

## Quyến — vận hành, pháp lý và gom bài

Đọc Phiếu B B7.5/B7.6, Phiếu C C10/C11, `SUBMISSION.md`, `docs/demo-cp5.md`.

```powershell
py -3 -X utf8 -m lab10.check_submission
```

Kỳ vọng ĐỦ THÀNH PHẦN; đây là kiểm đủ file, không phải chứng nhận test ẩn hoặc mọi người đã tự thao tác.

Sau khi nhóm chạy grade mới hoặc sửa tài liệu:

```powershell
py -3 -X utf8 -m lab10.check_submission --collect
py -3 -X utf8 -m lab10.check_submission
```

Kỳ vọng ĐỦ THÀNH PHẦN, code_hash đúng, manifest khớp. Nếu sửa code/config thì Nhật phải grade trước collect. Không chỉnh tay file đã gom trong submission; sửa nguồn rồi collect lại.

Cần giải thích:1 người/6 ca mỗi giờ; vàng30 phút, đỏ>60 phút hoặc ùn>0; Tùng giữ công tắc, dừng thao tác lỗi trong5 phút, Hạnh tiếp nhận manual, Oanh đối soát. Kênh cảnh báo và nhân viên là mô phỏng/runbook, không tuyên bố đã diễn tập production.

## Mỗi người xác nhận sau khi tự chạy

Điền phần cá nhân TEAM.md: việc thực tế mình đã làm, lệnh/mã run hoặc commit, một điều học được và một điều còn chưa chắc. Không dùng kết quả chung để ghi mình đã tự chạy khi chưa chạy. Nếu dùng AI cho phần nào thì ghi ngắn đúng phần đó theo RULES.md.

Demo dùng `docs/demo-cp5.md`. Mỗi người tự nộp link repo trên LMS; trưởng nhóm push bài không thay thế việc nộp cá nhân.
