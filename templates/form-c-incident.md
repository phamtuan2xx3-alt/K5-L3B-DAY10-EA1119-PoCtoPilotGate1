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

## C12 · Quyết định Gate 1 · v2

**Quyết định chung của team: DỪNG pilot, giữ so với v1.** Đây là quyết định không triển khai thật, không phủ nhận các cải thiện của bản sửa trong môi trường mock. Giữ nguyên v1 và tiêu chí đã ký.

| Mục | v2 |
|---|---|
| Commit ký tiêu chí | `45ef97b`, hash `081e817c9c3251ae569f8491cba9d35444a91c62cfec5804a928d96c857d9a6d` |
| Hash chốt vòng1 | `fdb61587fed47f033c198ba3b30881bdef7f7cfe7801ad555c61df92700c9a9e` |
| Run S5 | base `R-S5-before-20261119-165031-65d527`; prepared `R-S5-prepared-20261119-165032-65d527`; after `R-S5-after-20261119-165032-65d527` |
| Grade | `R-S5-grade-20261119-165030-65d527` — PASS-VISIBLE; hidden chưa chạy |
| Vượt trần after | Không; required/business_ops đạt trên nền và phần S5 giữ lại. Nền escalation22,73% vẫn vượt nice-to-have20%, đã giải trình; không che bằng số16,67% của S5. |
| Kho/hãng xấu nhất | S5 phần giữ HN4.277đ/ticket, pass1.0, mọi hãng lỗi an toàn0. B2B prepared10.382đ>10.000đ đã chuyển manual, không nằm trong chi phí after. Nền nhóm?10.359đ vẫn cần đối soát. Chỉ nhìn phân khúc không làm team đổi từ Dừng sang Tiếp tục. |
| Quyết định | **Dừng** |
| Bằng chứng1 | S5 base hoàn sai890.000đ/150 trial và20 fault oan; baseline nền từng hoàn sai20.000đ và1 fault oan. Hai nhóm an toàn đã chạm stop_condition. |
| Bằng chứng2 | S5 after90/90 lượt, pass_rate/pass_k1.0; hoàn sai/under-refund/fault oan/PII0; nền110/110, không regression. Prepared S5 đã an toàn trước khi biết thẻ nhưng vẫn còn chi phí kho âm. |
| Bằng chứng3 | Phần giữ S5: độ phủ0.6,18 ticket/ngày,12 ngoài scope, chi phí3.980đ, ROI1.51, ùn0, maxwait0 phút, LLM max765đ. Không gán ROI1.51 cho cả30 ticket. |
| Khớp decision_rule | Dừng ưu tiên khi chạm stop_condition hai nhóm an toàn. Bản ký không cho miễn trừ lịch sử sau khi sửa; không nới tiêu chí. |
| Nếu Thu hẹp | Không chọn nhãn quyết định này; kỹ thuật đã thu scope còn60%,1 người trực, B2B12 ca/ngày đi manual. Đây là cấu hình ứng viên offline, chưa được phép chạy thật. |
| Nếu Cải tiến thêm | Không áp dụng nhãn; các rủi ro dữ liệu/tải/concurrency/giá thật phải xử lý trước một đề xuất pilot mới. |
| Nếu Dừng: bài học | Chất lượng trung bình cao vẫn có thể che chi sai, fault oan và kho lỗ. Cổng an toàn và báo cáo kinh tế theo phân khúc đều cần; viết rõ điều kiện reset ở phiên bản tương lai, không sửa bản hiện tại. |
| Ngày quyết định lại | Không áp dụng với Dừng. Mốc21/11/2026 là rà soát bài học nội bộ, không gia hạn LMS hoặc tự cấp phép mở lại. |
| PIC ký | Phạm Quang Tuấn (2A202603824), đại diện team EA1119; không tạo chữ ký của người khác. |

### Chỉ ở v2

- Giữ Dừng so với v1: S5 xác nhận base cũng có hai nhóm lỗi an toàn; bản sửa cải thiện chất lượng và economics nhưng không hủy trigger ký trước.
- Grade không còn ô đỏ công khai; hidden chưa có. PASS-VISIBLE không phải điểm chấm cuối và không phải phép triển khai production.
- Prepared đã chặn toàn bộ890.000đ hoàn sai,20 lỗi hãng oan và giảm max LLM2.412→765đ trên S5; bỏ sót B2B chi phí kép10.382đ/ticket. Vòng2 thêm scope routing và monitor để xử lý đúng nhánh kinh doanh.
- Máy ghi “Được phép cân nhắc Tiếp tục”; đây là kết luận các ngưỡng số hiện tại, không thay thế stop_condition/decision_rule dạng văn bản. Team chọn Dừng thận trọng và khớp điều kiện đã ký.
- Chưa đo hidden, model thật, công suất manual B2B và race ledger; do đó không khẳng định sẵn sàng pilot dù after xanh.

### Ba dòng bắt buộc

1. Thiết kế giả định 12 ticket B2B/ngày ngoài scope được người xử lý với giá 10.000đ/ticket và đủ công suất; giá hoặc tải thật tăng sẽ làm ước tính tiết kiệm toàn luồng sai.
2. Scope ngăn gọi trợ lý cho kho bị loại trong simulator, budget và ledger gate ngăn các nhánh chi vượt đã quan sát khi chạy tuần tự; monitor chỉ phát hiện, chưa bảo đảm khi kho/giá nguồn sai hoặc nhiều worker ghi đồng thời.
3. Trước Gate 2 của một đợt pilot được phê duyệt riêng, cần đo giá API và độ trễ thật, chi phí manual B2B, tải giờ cao điểm, đối soát tiền và PII, kiểm giao dịch đồng thời, đồng thời diễn tập cảnh báo và công tắc dừng.
