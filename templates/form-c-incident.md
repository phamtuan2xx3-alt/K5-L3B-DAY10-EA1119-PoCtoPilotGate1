# Phiếu C · Sự cố S5 — CP4

**Bàn:** EA1119 — L3B · **Thẻ đã bốc:** S5

Tuấn: cổng; Nhật: đo/monitor; Công: kinh doanh; Đồng Văn Quyến: vận hành/pháp lý. Hồ sơ chung của team. C12 dành cho CP5, chưa chốt tại CP4.

## C0 · Nhật ký lần chạy vòng 2

| Mã lần chạy | Mốc / thay đổi | pass_rate · CI95 · pass_k | Hoàn sai · oan · PII | Kết luận |
|---|---|---|---|---|
| R-S5-grade-20261119-163631-a12887 | Nhận thẻ, chưa sửa; prepared R-S5-prepared-20261119-163633-a12887 | 1.0 · [1;1] · 1.0 | 0 · 0 · 0 | Cổng vòng1 giữ an toàn nhưng HCM-B2B10.382đ/ticket, chưa monitor mới. |
| R-S5-after-20261119-164946-0ebfdb | Chỉ đổi scope: HN,HCM,DN,CT; B2B chuyển thủ công | 1.0 · [1;1] · 1.0 | 0 · 0 · 0 | 90 lượt; độ phủ0.6; chi phí3.980đ, ROI1.51. |
| R-S5-after-20261119-165009-65d527 | Chỉ thêm monitor chi phí | 1.0 · [1;1] · 1.0 | 0 · 0 · 0 | Monitor đọc trial không nhãn, không đổi quyết định xử lý. |
| R-base-after-20261119-165010-65d527 | Kiểm regression | 1.0 · [1;1] · 1.0 | 0 · 0 · 0 | 110/110, không ca mới hỏng. |
| R-S5-grade-20261119-165012-65d527 | Kiểm tổng hợp | 1.0 · [1;1] · 1.0 | 0 · 0 · 0 | Integrity đỏ do Windows checkout đổi LF thành CRLF; khôi phục byte gốc đúng hash, không đổi nội dung thẻ. |
| R-S5-grade-20261119-165030-65d527 | Kiểm lại sau khôi phục byte thẻ | 1.0 · [1;1] · 1.0 | 0 · 0 · 0 | PASS-VISIBLE; integrity, criteria, visible, regression, monitor đều đạt. Test ẩn chưa có. |

## C1 · Câu 3.0 · Prepared và pre-mortem

Grade trước sửa `R-S5-grade-20261119-163631-a12887`; base `R-S5-before-20261119-163633-a12887`; prepared `R-S5-prepared-20261119-163633-a12887`. Cổng vòng1 giảm hoàn sai toàn bộ trial từ890.000đ xuống0, lỗi hãng oan20 xuống0, LLM cao nhất2.412đ xuống765đ. ROI từ-0.33 lên0.53. Prepared còn kho HCM-B2B10.382đ/ticket>10.000đ, escalation50% và chi phí bình quân6.541đ.

Đã dự báo trong B6: chi lặp, ngân sách và chuyển người làm mất ROI. Bỏ sót định tuyến sớm nhóm có tính kinh tế âm: budget chỉ chặn tiền máy lớn, không tránh tiền máy cộng công người cho ticket B2B nhỏ/ngắn. Lăng kính kinh doanh kết hợp kỹ thuật và vận hành.

| Lý do bổ sung (giả định ở thì quá khứ) | Lăng kính | Bằng chứng |
|---|---|---|
| Nhóm B2B đã luôn phải xin duyệt nhưng vẫn trả tiền đọc máy trước khi chuyển. | Kinh doanh/vận hành | S5-51@11 proposal230.000đ rồi escalated; kho HCM-B2B report10.382đ. |

## C2 · Câu 3.1 · Soát lỗi

Tác hại cho Finance, khách và hãng: lỗ ròng base60.486đ/ngày, hoàn sai890.000đ trên150 trial,20 fault oan; nhóm B2B tốn hơn làm tay.

### Phần 1 · Ghi lỗi

| Lỗi / bằng chứng trace base | Ai chịu / mức độ | Loại |
|---|---|---|
| S5-51@11: extract → tracking8 ngày → proposal230.000đ → escalated thiếu approval; cost565đ vẫn cộng công người10.000đ. | Finance/Hạnh; cao ở quy mô nhóm | Lỗi ngữ cảnh: đúng xử lý ticket nhưng trái kỳ vọng tiết kiệm. |
| S5-50@11: nội dung dài vẫn extract, result cost1.856đ>trần1.500đ, sau đó chuyển người; toàn gói max2.412đ. | Finance; cao | Giới hạn hệ thống: không kiểm ngân sách trước đọc ở base. |
| S5-02@11: replay S5-01 cùng O-2501, ledger lại ghi25.000đ và fault GHSH dù nhãn không còn quyền lợi. | LogiX/hãng/kế toán; cao | Lỗi chìm. |

### Phần 2 · Tìm nguồn

| Nguồn | B2B | Ticket dài | Hoàn lặp |
|---|---|---|---|
| Đầu vào | Không cần hiểu hết text để biết economics theo kho | Độ dài làm tăng giá extract | Hai kênh gửi lại cùng đơn không phải quyền lợi mới |
| Độ liên quan | warehouse_id và policy/approval đã có | Giá theo4 ký tự có trong ops_facts | Ledger có thật, cờ refund_status batch không đủ tươi |
| Thứ bậc | Business chưa định tuyến trước máy | Chưa gắn trần Finance vào đường đọc base | Ledger phải là nguồn đã chi, không dùng flag thay thế |
| Trạng thái hỏng | Không có429 trong trace51; không đổ cho hạ tầng | Không cần429 vẫn vượt chi phí | Không có429 ở ca02; gửi lại đa kênh là đủ |

### Phần 3 · Hướng xử lý

| | B2B | Ticket dài | Hoàn lặp |
|---|---|---|---|
| Vì sao lỗi | Thêm tiền máy không giảm công người | Vượt trần Finance | Chi quá quyền lợi còn lại |
| Giải pháp | Config scope → manual trước LLM | Giữ budget1.200đ vòng1 | Giữ gate ledger/remaining vòng1 |
| Đường đi | Hạnh tiếp nhận thủ công; Oanh báo chi phí riêng | Vượt budget chuyển người, không cắt nội dung mù | Không remaining thì deny; đối soát khoản cũ |
| Tín hiệu | warehouse_cost_max_vnd, review component | llm_cost_max_vnd | wrongful_refund_vnd offline + ledger audit; không bịa nhãn production |

## C3 · Câu 3.1 · Phần riêng S5

### C3.5 · Mở lại bản đồ dữ liệu

| Trường | Vòng1 | Sau thẻ | Ảnh hưởng |
|---|---|---|---|
| warehouse_id | Phân khúc để đọc report | Khóa định tuyến trước LLM; HCM-B2B có economics âm | Tách manual trước khi phát sinh tiền máy |
| ticket.text / ops_facts.llm_cost | Dữ liệu không tin cậy/giá mô phỏng | Độ dài là driver tiền máy dù không có câu lệnh độc | Cần budget trước extract, không chỉ lọc prompt |
| ledger_seed / refund_status | Ledger nguồn thật, flag batch | S5 có lịch sử đã chi và gửi lại nhiều kênh | Trừ ledger thực, không coi ticket mới là quyền lợi mới |

C3.1–C3.4 không áp dụng S5; không điền bài thẻ khác.

## C4 · Câu 3.1 · HAZOP thẻ

Tool: issue_refund; đọc cả tiền máy trước khi tới tool, không chỉ tham số đầu ra.

| Dòng dữ liệu | Guideword | Lệch / bằng chứng | Hậu quả | Cổng |
|---|---|---|---|---|
| ledger amount | INCOMPLETE | S5-02 bỏ khoản S5-01 | Hoàn lặp | G2 remaining ledger vòng1 |
| text length | PERTURBED | S5-50 đính kèm danh sách dài, không nhất thiết ác ý | LLM>1.500đ | Budget1.200đ vòng1 trước read |
| routing/amount | WRONG | S5-51 đọc rồi mới biết vượt quyền | Chi phí kép | Scope warehouse trước agent |
| refund_status batch | INVALID | Giả thuyết chưa quan sát trực tiếp: flag cập nhật trễ theo chiều REFUNDED sai | Từ chối khoản còn quyền lợi | Audit ledger/flag; cần dữ liệu thật, chưa khẳng định đã ngăn nhánh từ chối sớm |

## C5 · Specification và giả định môi trường

Specification: trên phần giữ, không có kho xác định nào cost_per_ticket>10.000đ, LLM max≤1.500đ và tổng ledger không vượt quyền lợi theo policy. Kiểm qua ops.violations, llm_cost_max_vnd, G2 và report wrongful_refund_vnd; không dùng pass_rate trung bình bù chi phí kho.

Giả định ngoài phần mềm: B2B chuyển thủ công được phục vụ với giá10.000đ/ca và Hạnh có người/công suất thực tế. Có thể sai khi hợp đồng sỉ phức tạp hoặc dồn việc; phải đo riêng chi phí/lưu lượng ngoài scope, không tuyên bố tiết kiệm toàn công ty từ report phần giữ.

## C6 · Fault tree TRƯỚC sửa

Mã grade trước sửa163631-a12887; các lá là bằng chứng từ base/prepared, không lẫn hai mốc.

```text
ĐỈNH: Chi phí và thiệt hại vượt lợi ích trợ lý
 HOẶC
 [1] Kinh doanh: B2B cần người VÀ agent vẫn đọc trước
     lá: S5-51@11; prepared HCM-B2B10.382đ/ticket
 [2] Kỹ thuật/giá: text dài VÀ không có budget trước đọc (base)
     lá: S5-50@11 cost1.856đ; base max2.412đ
 [3] Dữ liệu/ghi: gửi lại cùng đơn VÀ không kiểm ledger (base)
     lá: S5-01→02, row25.000đ lần nữa; base hoàn sai890.000đ
```

Prepared đã ngăn[2]/[3] trên mẫu, còn[1]; không mô tả hai nhánh đã sửa là lỗi mới của prepared.

## C7 · Câu 3.5 · Bảng sửa

| Nhánh | Thay đổi | Tầng | Giảm hay ngăn | Run |
|---|---|---|---|---|
| [1] | business.pilot_scope all→warehouse HN,HCM,DN,CT; B2B manual | Kinh doanh/định tuyến trước máy | Ngăn tiền LLM nhóm bị loại trong simulator; không ngăn chi phí/lỗi manual | R-S5-after-20261119-164946-0ebfdb |
| [2] | Giữ cost_budget_per_ticket1.200 và G1/G2 vòng1 | Giới hạn thiệt hại | Giảm chi phí máy, không bảo đảm mọi API production tính đúng giá mock | prepared so base, không sửa snapshot |
| [3] | Giữ ledger gate; thêm monitor chi phí để phát hiện economics | Chặn + phát hiện | Gate ngăn vượt remaining trong thực thi tuần tự; monitor chỉ phát hiện, không chặn, chưa giải quyết race đa worker | R-S5-after-20261119-165009-65d527 |

Không sửa guards.py vòng2 vì cơ chế tài chính đã đủ trên S5; không tạo thay đổi code giả để lấp phiếu.

## C8 · Câu 3.6 · Monitor chi phí theo kho

| Mục | Nội dung |
|---|---|
| Tên MONITORS | warehouse_cost_max_vnd; warehouse_review_cost_max_vnd; llm_cost_max_vnd |
| Hành vi | Tiền máy và công người theo kho, rồi lấy kho có bình quân cao nhất; max LLM theo ticket riêng |
| Dữ liệu | warehouse,cost_vnd,review_kind của trial không nhãn; giá public ops_facts. Không đọc label, pass hoặc wrongful_refund_vnd. |
| Công thức | Mỗi kho: machine=sum(cost_vnd)/N; review=sum(units×10.000)/N, units=1 escalated hoặc0.4 recheck; total=machine+review. Hàm warehouse_cost_components trả bảng thành phần, MONITORS trả max dạng số. N=0 không tạo nhóm; tập rỗng trả0. Thiếu warehouse nhóm?, không loại; thiếu cost bắt lỗi thay vì im lặng bỏ mẫu. |
| Tiền mất | Không thể xác định khoản sai từ trial không nhãn bằng tổng hoàn tiền. Báo riêng wrongful_refund_vnd offline: base890.000đ/150 lượt→prepared/after0; production phải đối soát Oanh. Không tính khoản hoàn hợp lệ là mất tiền. |
| Phạm vi chi phí | Monitor không phân bổ standby; report.ops.cost gồm phí trực30.000đ/ca. Không cộng hai số rồi đếm đôi. Giá mock cố định, cần sửa cơ chế nguồn giá khi áp dụng production. |
| Báo động | Theo ca và cửa sổ1 giờ: kho>10.000đ hoặc LLM>1.500đ đỏ; kho>8.000đ vàng để rà tổng budget; N nhỏ phải ghi cỡ mẫu. Tùng/Công quyết định khoanh phạm vi, Hạnh bàn giao manual. |
| Giá trị | Base nền max kho10.359đ (nhóm?); base S5 max11.325,666667đ; after nền10.359đ, after S5 4.276,75đ. Review max after nền10.000đ vs S5 3.750đ; LLM765đ S5 vs770đ nền. Monitor sáng đèn theo grade; nền? vẫn cần theo dõi, không giấu cảnh báo nền. |
| Điểm mù | Không chứng minh sai tiền nếu không có đối soát; không bao gồm chi phí manual ngoài scope, latency/giá API thật hoặc standby từng kho. |

## C9 · Fault tree SAU sửa

Mã grade `R-S5-grade-20261119-165030-65d527`, after `R-S5-after-20261119-165032-65d527`.

```text
ĐỈNH: Chi phí/thiệt hại vượt lợi ích
 HOẶC
 [1] B2B cần người VÀ scope routing hỏng → còn chi phí manual phải đo riêng
 [2] Text dài VÀ budget gate hỏng/giá ngoài đời khác mock
 [3] Gửi lại VÀ ledger gate hỏng hoặc hai worker ghi đồng thời
 [4] Giá manual/tải khác giả định → còn hở, monitor+đối soát phát hiện
```

Scope ngăn gọi agent cho B2B theo warehouse gốc; budget giới hạn chi phí máy; G2 ngăn chi vượt remaining trong mock tuần tự. Monitor phát hiện chi phí chứ không tự thực hiện kill switch. Còn hở dữ liệu kho sai, giá thật, race ghi và tải người duyệt.

## C10 · Risk register

| Rủi ro | Khả năng / tác động | PIC | Metric/ngưỡng | Xử lý / quyết định | Nhóm |
|---|---|---|---|---|---|
| B2B manual quá tải hoặc giá không còn10.000đ | Vừa / cao | Đồng Văn Quyến | queue_stuck>0 hoặc maxwait>60; báo cost manual riêng | Chưa mở rộng scope, bổ sung nhân lực có đo chi phí; không ép vào agent | MAP/MANAGE |
| Kho còn lại tăng chi phí | Vừa / cao | Nguyễn Thành Công | warehouse_cost_max_vnd>10.000 hoặc ROI<0.25 | Dừng mở rộng, đối soát rồi đo scope mới | MEASURE/MANAGE |
| Ghi tiền đồng thời vượt remaining | Chưa đo / cao | Phạm Quang Tuấn | wrongful_refund_vnd>0 qua audit | Dừng chi, thêm transaction/idempotency production trước mở thật | GOVERN/MANAGE |

## C11 · Checklist và Runbook4–5

### Checklist cập nhật

| Nhóm | Trạng thái mới / bằng chứng | PIC |
|---|---|---|
| 1 chất lượng | Xong visible S5:90/90, nền110/110, regression đạt; chưa hidden | Chu Văn Nhật |
| 2 dữ liệu | Đã mở lại warehouse/ledger/text tại C3; chưa nguồn thật | Nguyễn Thành Công |
| 3 bảo mật | Giữ G3 và legal; PII0 trên S5; chưa nghiệm thu thật | Phạm Quang Tuấn |
| 4 quyền hạn | Giữ G2, trigger stop đã ký, không cấp waiver | Phạm Quang Tuấn |
| 5 hiệu năng | Budget kiểm được trên mock; chưa tải/API thật | Chu Văn Nhật |
| 6 chi phí | Xong phần giữ:3.980đ,ROI1.51; manual ngoài scope cần đo | Nguyễn Thành Công |
| 7 vận hành | Cập nhật bàn giao B2B; kênh/kill switch chưa diễn tập thật | Đồng Văn Quyến |
| 8 con người/pháp lý | Hạnh/Oanh nhận xử lý và đối soát theo runbook; chưa xác nhận bên ngoài | Đồng Văn Quyến |
| 9 quyết định | CP4 đạt kỹ thuật; C12/v2 chờ CP5, v1 giữ nguyên | Nguyễn Thành Công |

### Runbook4 · Sau sự cố

- Tín hiệu đã có: chi phí theo kho/LLM trong report, chưa có monitor tự đăng ký trước CP4. Nay thêm3 monitor; không đổi ngưỡng tiêu chí đã ký.
- Scope all→HN,HCM,DN,CT; HCM-B2B và kho mới chưa được phê duyệt đi manual. Không loại theo ID ticket, không đổi nhãn.
- Người trực giữ1, công suất6/giờ, maxwait60; Hạnh đứng tên duyệt, Tùng điều phối, Oanh đối soát tiền. Không tăng người giả để làm xanh report.
- Công báo Finance tách phần giữ3.980đ/ticket và12 ca/ngày manual. Chi phí end-to-end ước tính 18×3.980+12×10.000≈191.640đ so300.000đ làm tay; đây là ước tính dựa giá mock, không phải ROI1.51 của toàn30 ca.
- Oanh đối soát khoản trùng/hãng oan ở baseline, Quyến phối hợp thông báo hãng/shop trong1 ngày làm việc theo quy trình đề xuất; không tuyên bố đã gửi thông báo thật. S5 không thấy PII lộ, không suy ra mọi hệ thống an toàn.
- Báo đỏ thì Tùng dừng thao tác liên quan trong5 phút, giữ audit, Hạnh nhận manual. Kênh vẫn là quy ước lab, cần diễn tập thực tế.

### Runbook5 · Ba kịch bản tuần đầu nếu một đợt pilot tương lai được cấp phép

1. Nếu lưu lượng tăng3 lần trong1 giờ, Hạnh kiểm backlog từ3 ca/chờ30 phút, báo Tùng; vượt60 phút hoặc ùn>0 thì dừng nhận tự động phạm vi quá tải, gọi dự phòng có tên và dự toán, đo lại trước mở rộng.
2. Nếu LLM lỗi quá5 phút, Tùng ngừng tự động chi, Hạnh xử lý manual; đối soát ledger trước retry, không suy đoán lỗi confirm nghĩa là chưa chi.
3. Nếu người duyệt không tin quyết định, khóa ca đó khỏi ghi, Tuấn/Nhật kiểm trace và nguồn thật, Oanh đối soát. Chỉ mở lại sau người có quyền xác nhận; không ghi approval thay người.

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1 |
| Hash chốt cổng vòng 1 | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: ________ · prepared: ________ · after: ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: …
- Report tự kiểm tra: mã lần chạy `__________` · ô nào còn đỏ (nguyên nhân × tầng): …
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: …
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: …

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
