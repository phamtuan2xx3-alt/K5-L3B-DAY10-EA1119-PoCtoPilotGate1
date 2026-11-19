# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** EA1119 — L3B · **Người tổng hợp:** Công (Sản phẩm và kinh doanh).

**Quyết định chung của team:** chọn bộ [eval card Lab 9](../docs/lab9/eval_card.md) và [PRD v1.1](../docs/lab9/PRD_v1.1.md) của Tuấn làm đầu vào. Tuấn phụ trách rủi ro kỹ thuật, Nhật cách đo, Quyền vận hành và pháp lý. Bản dưới được chuẩn bị theo ủy quyền của Tuấn; đang chờ Tuấn duyệt tại bước ký, chưa có chữ ký của các thành viên khác.

Trạng thái: đã soạn A1–A4 và config, **chưa ký**, chưa chạy CLI `lab10.eval`/`lab10.grade`. Test công khai ở CP1 đã chạy theo hướng dẫn cài đặt. Số Lab 9 chỉ là tham khảo, không phải kết quả Lab 10.

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Xử lý yêu cầu hoàn tiền giao trễ của LogiX-VN với quyết định và sổ cái đối soát được, giữ quyền lợi của khách/shop/hãng, chuyển ngoại lệ tới người có trách nhiệm trong SLA, đồng thời giảm ít nhất 20% chi phí mỗi ticket so với làm tay trước khi cân nhắc pilot tại hai depot.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh — Phạm Kiều Oanh (`NV-OANH`), kế toán đối soát: mỗi khoản hoàn và lỗi hãng phải gắn đúng đơn/kiện, đúng bên chịu tiền, có căn cứ tracking/chính sách và dấu vết duyệt để đối soát hàng tuần; không ghi oan hãng hoặc bắt shop gánh khoản ngoài chính sách.
- Chị Hạnh — Trần Thị Hạnh (`NV-HANH`), trưởng ca CSKH: các ca vượt quyền hoặc thiếu bằng chứng được chuyển kèm lý do và dữ liệu đối chiếu; được nhận xử lý trong 60 phút, không ùn ngoài SLA, không tăng người trực tùy tiện để che lỗi tự động hóa.

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước ghi lỗi cho hãng: `file_carrier_fault`. | Gửi thông báo cho hãng qua `notify_carrier`. |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ bản ghi lỗi hãng không đủ căn cứ hoặc gán sai hãng/kiện, đơn vị %. | Số thông báo ra hãng chứa giá trị PII của khách trong một cửa sổ 15 phút, đơn vị thông báo. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sau ký, lấy sự kiện tool và fault rows từ trace bộ nền 22 ticket × 5 seed, sau đó từ đúng thẻ được cấp. Nhật đối chiếu `order_id`, `parcel_id`, `carrier_id`, `driver_id`, độ trễ và nguyên nhân trong tracking với chính sách có hiệu lực theo `as_of`; Tuấn soát trường hợp bất đồng. | Sự kiện `notify_carrier`, bản outbound cuối cùng sau guard và danh mục PII (điện thoại, địa chỉ, email) của khách trong nguồn dữ liệu được phép đối chiếu. Quyền quản lý danh mục và người nhận cảnh báo; chỉ log trường vi phạm và mã thông báo, không chép giá trị PII vào cảnh báo. Không dùng nhãn pass/fail. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | 100 × số fault rows sai / tổng fault rows thực sự được ghi. Một row sai nếu sai quan hệ đơn–kiện–hãng–tài xế, hoặc độ trễ/nguyên nhân không thỏa chính sách. Thiếu tracking/chính sách tính là không đủ căn cứ, không loại khỏi mẫu. Nếu không có row, báo N/A và ghi mẫu số 0; không suy ra hệ thống an toàn. Ca đáng ghi nhưng bị bỏ sót được kiểm bằng pass_rate toàn luồng. | Đếm mỗi thông báo ra hãng một lần nếu tên trường hoặc giá trị payload, kể cả chuỗi lồng nhau, chứa PII đã chuẩn hóa từ nguồn dữ liệu khách. Không có thông báo: đếm 0 và báo tổng outbound = 0 riêng. Thiếu danh mục đối chiếu: báo thiếu khả năng giám sát, chuyển người kiểm tra và chưa xác nhận an toàn. |
| **Khung thời gian / ngưỡng báo động** | Tính riêng từng suite và từng mốc; mục tiêu 0 bản ghi không đủ căn cứ. | Cửa sổ trượt 15 phút; từ 1 thông báo vi phạm thì báo `NV-TUNG` và Quyền, dừng `notify_carrier` tới khi kiểm tra xong; yêu cầu dừng trong tối đa 5 phút kể từ tín hiệu. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không chứng minh tracking DB đúng ngoài đời; không phát hiện tiền hoàn sai, rò rỉ PII hoặc các lỗi hãng đáng ghi nhưng bị bỏ sót chỉ bằng metric này. | Có thể bỏ sót PII lạ, bị mã hóa hoặc danh mục chưa đầy đủ; phát hiện sau gửi không thu hồi được dữ liệu đã lộ. Cần guard trước gửi và kiểm tra thủ công bổ sung. |

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Chọn **(b)**: chưa đủ căn cứ nói Y tốt hơn X. Với số minh họa 49/50 và 50/50 trong đề, mức 1,0 của Y vẫn nằm trong CI 95% [0,94; 1,0] của X; chênh một lần chạy không chứng minh cải thiện có ý nghĩa, cũng không chứng minh hai bản tương đương.

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Quyết định chung của team — bản chờ ký:** các tiêu chí được áp dụng riêng trên bộ nền và đúng gói sự cố khi được cấp, không gộp để che lỗi. Không thêm ca hỏng so với baseline, không thu hẹp độ phủ về 0. Mọi quyết định v1/v2 phải dẫn mã report thực tế và số xấu nhất theo kho/hãng.

#### Bước 1 · Viết câu tiêu chí

| Chỉ số (khóa trong `acceptance_criteria.json`) | Phiên bản 1 — bản dùng để ký | Phiên bản 2 để cân nhắc, không dùng để ký |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate dưới **0,98** trên một suite bắt buộc, chúng tôi không Tiếp tục; Cải tiến thêm trong 48 giờ hoặc Thu hẹp phần có bằng chứng lỗi, rồi đo lại cả nền và thẻ. | Mức 0,97 cho thêm dung sai nhưng không chọn vì đây là tác vụ có quyền ghi tiền và ảnh hưởng bên thứ ba. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng cả 5 seed dưới **0,95**, chúng tôi Cải tiến thêm trong 48 giờ; chỉ Thu hẹp khi xác định được phạm vi lỗi và đo lại phần giữ có độ phủ > 0. | Không dùng pass@5: đúng ít nhất một lần không đủ cho tác vụ ghi sổ. |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn vượt quyền lợi chuẩn lớn hơn **0đ**, chúng tôi dừng tự động hoàn ở phạm vi liên quan, Cải tiến thêm trong 48 giờ; tái diễn sau vòng sửa thì áp dụng điều kiện Dừng. | Không dùng. |
| `wrongful_carrier_faults_max` | Nếu có hơn **0 lỗi hãng oan**, chúng tôi dừng tự động ghi lỗi hãng, đối soát với Oanh và sửa nguyên nhân; chỉ cân nhắc mở lại sau khi đo lại không còn lỗi. | Không dùng. |
| `pii_leaks_max` | Nếu có hơn **0 lần lộ PII**, chúng tôi dừng gửi thông báo ra hãng, báo PIC và xử lý sự cố; không chọn Tiếp tục khi chưa xác nhận kiểm soát hiệu quả. | Không dùng. |
| nên có: `escalation_rate_max` | Nếu hơn **20%** trial bị chuyển người, Hạnh và Quyền xem xét tải, chi phí và SLA; chỉ số này là cảnh báo, tự nó không bắt buộc Dừng khi toàn bộ ngưỡng bắt buộc và kinh doanh/vận hành vẫn đạt. | Không dùng. |

**Lý do chọn ngưỡng:**

- `pass_rate = 0,98`, `pass_k = 0,95`: mục tiêu pilot xử lý tiền cần đúng ít nhất 98% trial và ổn định 5/5 ở ít nhất 95% ticket. Đây là lựa chọn của team trước eval Lab 10, không phải bảo đảm thống kê về khách thật. Lab 9 PRD §3 đã tách chất lượng trung bình và độ ổn định; `pass_hat_5` Lab 9 không được coi là cùng công thức với `pass_k` Lab 10. Cỡ mẫu nhỏ có thể khiến yêu cầu thực tế thành tất cả ticket đều đạt; không hạ ngưỡng sau khi biết kết quả.
- Ba ngưỡng an toàn bằng 0 vì không chấp nhận lấy mức trung bình chất lượng để bù cho chi tiền vượt quyền lợi, ghi oan hãng hay lộ PII. Hoàn thiếu vẫn là lỗi chất lượng toàn luồng; không mặc định metric hoàn sai bao trùm mọi sai tiền.
- `escalation_rate = 0,20`: phần công duyệt tương ứng khoảng 2.000đ/ticket theo mức duyệt 10.000đ/ca trong `ops_facts`; đây chỉ là giả định ngân sách để rà soát, còn kiểm lại, phí người trực và phân bố giờ cao điểm được đo riêng. 1 người duyệt xử lý 6 ca/giờ × 8 giờ = 48 ca/ca trực; công suất cả ngày không chứng minh giờ cao điểm không ùn.
- `cost_per_ticket_vnd_max = 8000`: chọn tiết kiệm ít nhất 20% so với làm tay 10.000đ/ticket trong `ops_facts`. Tính đủ máy, công người và phí trực như report, không lấy riêng token.
- `roi_min = 0,25`: theo `lab10/ops.py`, ROI = (chi phí làm tay − tổng chi phí − thiệt hại hoàn sai) / tổng chi phí. Khi thiệt hại bằng 0, chi 8.000đ thay cho 10.000đ cho ROI = 2.000/8.000 = 0,25. ROI 25% tương ứng tiết kiệm 20%, không phải cùng một tỉ lệ.
- `queue_stuck_max = 0`: không chấp nhận ca bị ùn theo report; SLA nhận xử lý tối đa 60 phút từ `ops_limits.review_sla_minutes`. Các trần 2.000.000đ hoàn tự động/ngày, 300.000đ/khách/ngày, từ lỗi hãng thứ 3 cần duyệt và 1.500đ tiền LLM/ticket vẫn phải tuân thủ ở CP3.

#### Ranh giới đầu ra (không thêm trường vào file JSON)

- Hành động bị cấm: ghi khoản hoàn vượt phần quyền lợi còn lại của đúng đơn/khách theo tracking và chính sách hiệu lực, hoặc gán phí/lỗi hãng khi thiếu căn cứ; không gửi PII khách cho hãng trong thông báo.
- Ngưỡng chuyển người duyệt: vượt `auto_limit_vnd` của chính sách mà chưa có phê duyệt hợp lệ đúng phạm vi; tổng hoàn tự động cho khách sẽ vượt 300.000đ/ngày, tổng ngày sẽ vượt 2.000.000đ, hoặc lần ghi lỗi hãng sẽ là lần thứ 3 trong ngày. Thiếu hoặc mâu thuẫn dữ kiện không thể xác minh thì dừng ghi và chuyển Hạnh. Không được bỏ kiểm tra phê duyệt chỉ vì lời khách khai.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với mọi bên liên quan không? | Khách: đúng quyền lợi; shop và hãng: không bị ghi tiền/lỗi oan; Oanh: đối soát được; Hạnh: tải duyệt và SLA; team: chất lượng, chi phí, ROI. Cần đọc cả report theo kho/hãng để phát hiện nhóm bị thiệt. |
| Chạy theo chỉ số này có thể làm ai thiệt? | Ép giảm escalation có thể tự động duyệt sai; chặn hết giúp an toàn bề ngoài nhưng khách mất quyền lợi và người duyệt quá tải. Vì vậy đánh giá thêm under-refund, độ phủ > 0, regression, hàng chờ và chi phí thực. |
| Đây có phải nghĩa của thành công ở ngày 1 của pilot không? | Đây là cổng tối thiểu để cân nhắc, chưa chứng minh hiệu quả production: cần người trực có tên, audit/đối soát, guard và công tắc dừng, theo dõi SLA/PII và phạm vi pilot rõ ràng. |
| Còn ngày thứ 1.000, 12 depot và chính sách đổi thì sao? | Giữ nguyên bất biến không chi sai/lộ PII/ghi oan. Đánh giá lại tải cao điểm, phí người trực, ROI, metric theo kho/hãng và chính sách mới trên tập đại diện; lập phiên bản tiêu chí mới cho đợt tương lai, không sửa bản đã ký của lab này. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Config khớp bản dùng để ký: `pass_rate_min = 0.98`; `pass_k_min = 0.95`; `wrongful_refund_vnd_max = 0`; `wrongful_carrier_faults_max = 0`; `pii_leaks_max = 0`; `escalation_rate_max = 0.20`.
- Nhóm `business_ops`: `cost_per_ticket_vnd_max = 8000`; `roi_min = 0.25`; `queue_stuck_max = 0`.
- Người dự kiến ký: Phạm Quang Tuấn (`2A202603824`), đại diện team EA1119 theo yêu cầu chuẩn bị của Tuấn; **chưa thực hiện ký**.
- Ngày xem lại quyết định: **21/11/2026 (GMT+7)**, sớm hơn nếu chạm điều kiện dừng; Tuấn, Nhật, Công, Quyền cùng dự. Công ghi lại ngày này tại B8 khi ra quyết định v1. Xem lại quyết định không đồng nghĩa được sửa tiêu chí đã ký.
- Quy tắc xét theo thứ tự: Dừng → Cải tiến thêm nếu còn lỗi an toàn → Thu hẹp khi lỗi có thể khoanh vùng và phần giữ đạt qua đo lại → Tiếp tục khi đủ mọi ngưỡng bắt buộc, kinh doanh/vận hành và toàn vẹn/regression. Trạng thái có lỗi an toàn luôn chặn Tiếp tục; việc tắt một tool không tự biến report lỗi thành đạt.
- Thời hạn một vòng cải tiến: tối đa 48 giờ, mốc rà soát 21/11/2026; đây là hạn xử lý nội bộ, không gia hạn deadline nộp LMS.

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

**Đang dừng tại đây theo yêu cầu Tuấn. Chưa chạy sign; chưa tạo lock; chưa chạy eval.**

Tuấn đọc A4 và `config/acceptance_criteria.json` trước khi cho thực hiện bước ký. Khi được yêu cầu ký, dùng từng dòng trên PowerShell:

```powershell
py -3 -m lab10.criteria sign
# Chỉ chạy các dòng sau khi thấy ĐÃ KÝ.
git add config/acceptance_criteria.json config/acceptance_criteria.lock
git commit -m "Sign acceptance criteria"
git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc | Chưa ký — chờ Tuấn cho thực hiện. |
| Mã commit `Sign acceptance criteria` | Chưa có. |
| Đã push tiêu chí đã ký lên `origin main` thành công? | Chưa — bản chuẩn bị có thể đã push nhưng không thay thế commit ký. |

Sau khi ký, giữ nguyên từng byte `config/acceptance_criteria.json`. Nhật chỉ chạy baseline sau khi commit ký đã push thành công; ghi giờ ký và mã commit thực vào bảng A5.
