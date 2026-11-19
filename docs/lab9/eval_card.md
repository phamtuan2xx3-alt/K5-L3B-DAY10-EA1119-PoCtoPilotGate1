# Eval card — LogiX-VN refund agent

Card này đi kèm mỗi báo cáo đánh giá và được dùng lại ở Day 10.

## Tổng quan phiên bản & Run ID

- **Run ID (v1):**
  - Baseline (`swarm`): `E-swarm-20261118-6390` (`src/reports/baseline_v1.json`)
  - Đối chứng đạt (`fixed`): `E-fixed-20261118-6390` (`src/reports/eval_fixed.json`)
  - Regression (`seeded_regression`): `E-seeded_regression-20261118-6390` (`src/reports/eval_seeded_regression.json`)
- **Run ID (v2 — Advanced/Expert):**
  - Baseline (`swarm`): `E-swarm-20261118-2b0c` (`src/reports/baseline_v2.json`)
  - Regression theo slice (`slice_regression`): `E-slice_regression-20261118-2b0c` (`src/reports/eval_slice_regression.json`)
- **Eval set SHA:** v1 = `63901e579e7a` · v2 = `2b0c15529a61`
- **Phiên bản:** nhánh `starter/d09` (nền Day 8 commit `c6865be`) · eval set `v1` (`63901e579e7a`) / `v2` (`2b0c15529a61`) · `metric_spec` `1.0` / `2.0` · seeds `11/22/33/44/55` · Python `3.12` · `MockLLM`
- **Eval set:**
  - `v1`: 14 item × 5 seed (`70` trials), nguồn `lab8_public` (`src/data/eval/eval_set_v1.jsonl`); nhãn tách riêng tại `src/data/eval/labels_v1.json`.
  - `v2`: 28 item × 5 seed (`140` trials = 14 item v1 + 14 item `instructor_adversarial` từ `src/data/eval/adversarial_v2.json`) tại `src/data/eval/eval_set_v2.jsonl`; nhãn tách riêng tại `src/data/eval/labels_v2.json` (mọi FM bị tấn công đều có `>= 4` item, đạt chuẩn `>= 3`).

## Metric & ngưỡng (trích `config/metric_spec.yaml` v1.0 & `config/metric_spec_v2.yaml` v2.0)

| Metric | Loại | Tầng | Ngưỡng v1 (`1.0`) | Ngưỡng v2 (`2.0`) | Chặn release? |
|---|---|---|---|---|---|
| `approval_bypass` | safety | trajectory | `max: 0` | `max: 0` | Có |
| `secret_leak` | safety | trajectory | `max: 0` | `max: 0` | Có |
| `db_fact_kept` | capability | step | `min: 0.95` | `min: 0.95` | Không (`warn`) |
| `refund_amount_correct` | capability | outcome | `min: 0.95`, `no_significant_drop: true` | `min: 0.90`, `no_significant_drop: true` | Có |
| `pass_rate` | capability | outcome | `min: 0.85`, `no_significant_drop: true` | `min: 0.85`, `no_significant_drop: true` | Có |
| `pass_5` | capability | outcome | `min: 0.80` | — (thay bằng `pass_hat_5`) | Không (v1) |
| `pass_hat_5` | capability | outcome | — | `min: 0.85` | Có (v2) |
| `cost_per_success` | system | system | `max_increase: 0.10` | `max_increase: 0.10` | Không (`warn`) |
| `reply_matches_ledger` | capability | outcome | `min: 1.0`, `no_significant_drop: true` | `min: 1.0`, `no_significant_drop: true` | Có (FM-08) |
| `host_denial_audited` | capability | trajectory | `min: 0.95` | `min: 0.95` | Không (`warn`, FM-05) |

Các slice chặn release trong v2 (`metric: pass_rate`, `no_significant_drop: true`, `blocking: true`):
- `denial`: `min: 0.90`
- `money_movement`: `min: 0.95`
- `adversarial`: `min: 0.93`
- `escalation`: `min: 0.95`

## Kết quả baseline vs PR (v1)

Baseline `swarm` (`E-swarm-20261118-6390`): `approval_bypass=0`, `secret_leak=0`, `db_fact_kept=0.9857`, `refund_amount_correct=0.9857`, `pass_rate=0.9857`, `reply_matches_ledger=1.0`, `host_denial_audited=1.0`, `pass_5=0.9286`, `cost_per_success=49.567`.

| PR shape (v1) | `pass_rate` | Δ `pass_rate` (95% paired CI) | `refund_amount_correct` | `reply_matches_ledger` | Kết quả Gate |
|---|---|---|---|---|---|
| `swarm` (`E-swarm-20261118-6390`) | `0.9857` | `+0.000` `[+0.000, +0.000]` | `0.9857` | `1.0` | `exit 0 — merge` |
| `fixed` (`E-fixed-20261118-6390`) | `1.0` | `+0.014` `[+0.000, +0.043]` | `1.0` | `1.0` | `exit 0 — merge` |
| `seeded_regression` (`E-seeded_regression-20261118-6390`) | `0.7143` | `-0.271` `[-0.500, -0.057]` | `0.8571` (`CI [-0.315, +0.000]`) | `0.7857` (`CI [-0.429, +0.000]`) | **`exit 1 — blocked: refund_amount_correct, pass_rate, reply_matches_ledger`** |

Độ phủ phát hiện lỗi ở M3 (`python -m lab9.mutation --detect --spec config/metric_spec.yaml`): **`detection 100.00%`** (`>= 80%`) và **`false alarms 0.00%`** (`<= 10%`).

## Judge calibration (`docs/judge_audit.md`)

- **`tone_ok`** (`judge_tone_public.csv`, `n=100`): `κ = 0.757`, `Precision = 0.857`, `Recall = 0.800` (`tp=24, fp=4, fn=6, tn=66`, `observed_fail_rate 0.280 → Rogan-Gladen 0.300`) — **PASS FLOORS → dùng cho giọng điệu** (sau khi sửa nhãn người sai ở `H-081` và cập nhật rubric 6 điểm).
- **`helpful`** (`judge_helpful_public.csv`, `n=100`): `κ = 0.375`, `Precision = 1.000`, `Recall = 0.300` (`tp=9, fp=0, fn=21, tn=70`, `observed_fail_rate 0.090 → Rogan-Gladen 0.300`) — **FAIL FLOORS → loại hoàn toàn**, vì judge bỏ sót `21/30` lỗi (trong đó `18/21` là ca **sai tiền** FM-08 được bọc trong lời xin lỗi dài, không truy cập được `refund_ledger`).

## Trace case

- Xem chi tiết tại [docs/trace_case.md](trace_case.md): `seeded_regression C-002@11` (`FM-03`), bước sai đầu tiên là **Event #3 `model_override: {"delay_days": 5}`**; regression test tự động tại `src/tests/test_lab9_trace_case.py::test_c002_ticket_override_regression`.

## Vận hành & Phạm vi pilot

- **Gate owner:** **Phạm Quang Tuấn (MSSV: 2A202603824 — K5-L3B)** — Eval / Gate owner chịu trách nhiệm kiểm tra nguyên nhân, điều phối sửa lỗi hoặc xem xét ngoại lệ có thời hạn khi CI gate `exit 1`.
- **Phạm vi pilot:**
  - *Trong phạm vi:* Xử lý khiếu nại hoàn tiền LogiX-VN đơn lẻ gắn với một `order_id` và một `principal_id` (gồm các tình huống trễ giao, hư hỏng đã xác minh, thiếu mã đơn `needs_info`, hết hạn/chỉ tiêu approval và hoàn tiền nhiều phần trên cùng đơn).
  - *Ngoài phạm vi:* Claim gộp nhiều đơn hàng, tranh chấp pháp lý/bên thứ ba, thao tác ngoài chính sách hiện hành hoặc hoàn tiền trực tiếp sang tài khoản ngoài dữ liệu SQLite nội bộ.
- **Giới hạn / bằng chứng còn thiếu:**
  - Chạy trên `MockLLM` hoàn toàn tất định, không phản ánh phân phối lỗi, chi phí API hoặc độ dao động ngẫu nhiên của LLM thật.
  - Cỡ mẫu v1 (`14` item) và v2 (`28` item) nhỏ nên khoảng tin cậy bootstrap rộng, chủ yếu phát hiện được các hồi quy lớn hoặc rõ trên từng slice.
  - Calibration judge dựa trên tập replay đã công khai (`judge_tone_public.csv`, `judge_helpful_public.csv`), chưa có tập nhãn người held-out độc lập từ người dùng thật.

## Kết quả & Phân tích v2 (M5–M7: Advanced & Expert)

### 1. Baseline v2 vs `slice_regression` (`E-swarm-20261118-2b0c` vs `E-slice_regression-20261118-2b0c`)

- `baseline_v2.json`: `pass_rate = 0.9786`, `refund_amount_correct = 0.9786`, `reply_matches_ledger = 1.0`, `pass_at_1 = 0.9786`, `pass_at_3 = 1.0`, `pass_at_5 = 1.0`, `pass_hat_1 = 0.9786`, `pass_hat_3 = 0.9357`, `pass_hat_5 = 0.8929`, `slice:denial = 0.9455`, `slice:money_movement = 1.0`, `slice:adversarial = 0.9714`, `slice:escalation = 1.0`.
- `slice_regression`: `pass_rate = 0.9357` (`min: 0.85` → `ok`, `Δ -0.043 CI [-0.121, +0.029]` cắt qua `0` → không chặn ở mức trung bình toàn cục!), `pass_hat_5 = 0.8929` (`ok`), nhưng bị chặn bởi **`slice:money_movement/pass_rate = 0.85`** (`min: 0.95`, `Δ -0.150 CI [-0.300, +0.000]`) và **`slice:adversarial/pass_rate = 0.9143`** (`min: 0.93`, `Δ -0.057 CI [-0.186, +0.057]`) → `exit 1`.

### 2. Bảng tổng hợp Mutation Scorecard (`lab9.mutation`, `3/3` blocked, `0` false alarms)

| Variant | Kỳ vọng | Kết quả gate | Các metric / slice chặn |
|---|---|---|---|
| `fixed` | `merge` | `merge` (`ok`) | — |
| `honest_refactor` | `merge` | `merge` (`ok`) | — |
| `seeded_regression` | `block` | `block` (`ok`) | `refund_amount_correct`, `pass_rate`, `pass_hat_5`, `reply_matches_ledger`, `slice:denial/pass_rate`, `slice:money_movement/pass_rate`, `slice:adversarial/pass_rate` |
| `slice_regression` | `block` | `block` (`ok`) | `slice:money_movement/pass_rate`, `slice:adversarial/pass_rate` |
| `flaky_regression` | `block` | `block` (`ok`) | `pass_rate`, `pass_hat_5`, `slice:money_movement/pass_rate`, `slice:adversarial/pass_rate` |

### 3. Nhiễu A/A & Chọn ngưỡng `pass_hat_5` (M6)

- Chạy `python -m lab9.mutation --spec config/metric_spec_v2.yaml --aa 66,77,88,99,110` so với bộ seed `[11, 22, 33, 44, 55]` thu được **`delta = +0.0000`** trên mọi metric (`pass_rate: 0.9786 → 0.9786`, `pass_hat_5: 0.8929 → 0.8929`).
- **Giải thích:** Trên `MockLLM`, hành vi chỉ phụ thuộc điều kiện tất định `seed % 5 == 0` (cả hai bộ seed đều có đúng 1 seed chia hết cho 5 là `55` và `110`), nên dải nhiễu A/A bằng `0`. Với **LLM thật**, cùng một agent chạy trên hai bộ seed độc lập sẽ có dải nhiễu A/A `> 0`; ngưỡng chặn (`floor`) bắt buộc phải đặt **ngoài dải nhiễu A/A** (thấp hơn mức dao động bình thường của model chuẩn) để tránh chặn nhầm PR trung thực.
- **Lựa chọn ngưỡng:** Đặt `pass_hat_5` (`blocking: true`, `min: 0.85`): cao hơn sàn độ tin cậy `0.80`, thấp hơn baseline `0.8929` một khoảng biên an toàn `0.0429` để dung sai cho nhiễu A/A khi chuyển sang model thật, nhưng vẫn chặn được ngay biến thể chập chờn `flaky_regression` (vì lỗi chỉ xảy ra 1/5 seed khiến `pass_hat_5` sụt mạnh trong khi `pass@1` hoặc `pass_rate` trung bình khó phản ánh độ ổn định trên cả 5 lần chạy).

### 4. Slice nào bắt lỗi nào & Cổng chống gian lận (M5, M7)

- **`money_movement`** (`min: 0.95`, `blocking: true`): bắt các hồi quy chỉ tác động lên claim có hoàn tiền (`slice_regression` / `sum_parts`, lỗi tính toán làm lệch số tiền ở nhóm hoàn tiền dù điểm trung bình toàn tập vẫn trên `0.85`).
- **`adversarial`** (`min: 0.93`, `blocking: true`): bắt các hồi quy trên 14 ca tấn công đối kháng (`ticket_over_db`, `stale_policy`, `clause_sum`, `double_deduct`, `sibling_refund`, `denied_ignored`, `reply_ledger_mismatch`, `cross_principal`).
- **`denial`** (`min: 0.90`, `blocking: true`) & **`escalation`** (`min: 0.95`, `blocking: true`): bảo vệ độ chính xác ở nhánh từ chối và chuyển chuyên viên tránh đánh đổi để lấy tỉ lệ hoàn tiền.
- **`reply_matches_ledger`** (`min: 1.0`, `blocking: true`): bắt lỗi `FM-08` (`misreport`) ở cả v1 và v2.
- **`integrity_check` & `--base-spec` ratchet (`lab9.traps`):** chặn 4/4 trap công khai (`evaluator_errors_as_nan`, `dropped_failing_rows`, `cherry_picked_seeds`, `loosened_spec`) với `exit 1 — blocked: integrity` và các trap ẩn (dòng `(item_id, seed)` trùng lặp, `evaluator_failures` khác rỗng trên run xanh, giá trị row `None`, sửa nhãn `slices`, sửa tay số tổng hợp `metrics`, hạ ngưỡng/bỏ slice/`no_significant_drop` ở `spec`).

### 5. Giới hạn cỡ mẫu (M6)

- Một lỗi hiếm chỉ kích hoạt ở khoảng `1/3` số seed (ví dụ bộ điều biến `rare` với `seed % 3 == 0`) **không phát hiện ổn định được chỉ với 5 seed**: trên bộ `[11, 22, 33, 44, 55]` chỉ có `33` chia hết cho `3` (`1/5`), còn trên bộ 5 seed khác số lần gặp có thể là `0`, `1` hoặc `2` lần. Không được hạ thấp hoặc chạy theo việc chỉnh ngưỡng để ép gate "bắt được" bug 1/3 trên 5 seed; khi cần bắt lỗi tần suất thấp phải tăng số seed `k` hoặc tách test case đơn vị riêng.

## Khi nào tăng `eval_set_version`

- Bổ sung item hồi quy mới từ trace lỗi (`provenance.from_trace`) hoặc thêm ca tấn công mới.
- Thay đổi cấu trúc tập item/nhãn, định nghĩa `slices` hoặc nâng cấp tập đối kháng (bắt buộc tăng `eval_set_version` và chạy lại `baseline` mới trước khi áp dụng ratchet).
