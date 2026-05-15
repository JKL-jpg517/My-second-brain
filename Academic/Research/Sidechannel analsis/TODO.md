
[[Sidechannel analsis/progress]]

# Coauthor C — Workflow Detection + Baseline Comparison + Dataset

  

> 你的任务: 闭合 G3 主体 (workflow hijacking 真评估), 闭合 G4 (dataset 升格为 C5

> contribution), 加方法学对比基线, 主导 paper level 重写。

> 工作量预估: 31.5 person-days (5–6 周内 ~25 active days, 含等待时段).

> 你也是 paper integration 的 czar: Week 5 全员 latex pass 由你主导。

  

---

  

## 你的任务清单

  

| 编号 | 任务 | Tier | 工时 | 闭合 |

|------|------|------|------|------|

| E4 | Stage-2 Edit-Distance Comparator 真实评估 | T1 关键路径 | 12–14 d | G3 主体 |

| E11 | Baseline 横向对比补全 | T2 | 7–10 d | 方法比较缺失 |

| P1 | 重写 Contributions (5 条, 含 Dataset C5) | T-B | 1 d | G4 (升格 C5) |

| P2 | 重新加回 V4 Caveat | T-B | 1.5 d | 诚实声明 |

| P6 | Dataset Release Plan | T-B | 4–6 d | G4 (C5 落地) |

| P7 | Skill Operation Detail Table | T-A→B | 2–3 d | reviewer ask |

  

---

  

## 启动前: Phase 0 资源定位 (你只需查这些)

  

任何动手前, 把发现写进 `_discovery_C.md`。**不要假设固定路径**——所有路径需通过搜索发现。

  

### C.0.1 论文核心文件 (你和 A、B 共用, 你是 paper czar 应该最熟)

  

```

搜索目标:

  - 终稿 PDF: 文件名形如 ndss27-summer-paper{NNNN}.pdf

  - 源 tex:   形如 main_revised.tex / main_ndss.tex / main_revised_v{N}.tex

  - bib:      reference.bib / refs.bib

  - 上一版 PDF (作 V4 caveat 措辞参考): main_revised_v{N}.pdf

  

工具优先级:

  1. Glob "**/ndss*paper*.pdf"

  2. Glob "**/main*.tex"

  3. Glob "**/*.bib"

  4. Glob "**/main*revised*.pdf"

  

如果找到多个候选, 按 mtime 取最新 + 文件大小最大者作为终稿;

旧版按 mtime 倒序列表 (P2 要逐段对照)。

```

  

### C.0.2 数据语料定位

  

你需要这些 corpus:

  

```

- focused3      ~3-cls,  ~123 records, ~8 GB raw IQ        ← E11 用

- big48         ~16-cls, ~1,529 records                    ← E4 confusability table 来源, P6 Tier 1 释放

- new-bands     ~22-cls at (80, 800) MHz                   ← E4 zero-shot recovery, E11 transfer

- attack_pilot  ~22-attack-cls                             ← P7 skill table 引用

- attack_v1     ~22-cls at (248, 800) MHz, ~155 records   ← P6 Tier 2

  

发现策略:

  Glob "**/focused3*"

  Glob "**/big48*"

  Glob "**/attack_pilot*", "**/attack_skills_pilot*"

  Glob "**/new_bands*", "**/new-bands*", "**/*80MHz*800MHz*"

  Glob "**/openclaw_attack*"

```

  

每个 corpus 报告: 路径, 总大小, 文件数, 子目录结构 (depth=2), modification time。

  

### C.0.3 代码定位

  

```

- V10 流水线: classify_v{NN}*.py (取最高版本号)

- 增强训练: _enhanced_train*.py

- 分析脚本: analyze_*.py

- Pi 端启动器: pi_load.py 或 _attack_skill_runner.py

- Skill 源码目录: _remote_mirror/skills/ 或 skills/   ← P7 列表对齐源

  

工具:

  Glob "**/classify_v*.py"

  Glob "**/_enhanced_train*.py"

  Glob "**/analyze_*.py"

  Glob "**/pi_load*.py"

  Glob "**/_remote_mirror/**"

```

  

### C.0.4 硬件可达性 (E4 启动前必查; E11 不需要硬件)

  

```

确认:

  - 两台 SDR (HackRF One 或同等) 在线: hackrf_info

  - DUT 主机 ssh 可达

  - 时间同步 (chrony) 正常

  - P7 测 skill resource mix 时需要 DUT 上 ps / iotop / nethogs 可用

  

如硬件未到位:

  E4 → blocked, 但可先把 30 类 workflow 实现 + comparator 算法写好

  E11 → 可立即开始 (零硬件)

  P1 / P2 / P6 / P7 (除 P7 resource mix 测量外) → 可立即开始

```

  

### C.0.5 工作目录

  

```

camera_ready_E4_workflow/

camera_ready_E11_baseline/

paper_camera_ready/

  main_camera_ready.tex     (复制终稿 tex 起步)

  fig/                      fig18-fig25 (新增, 每实验自产)

  table/                    Table V-XIII

  diff_to_submitted.md      与终稿的逐节 diff (你维护)

```

  

写一份 `_discovery_C.md` 记录 0.1–0.4 发现 + workspace 路径选择 + 任何 missing/blocker。

**特别记录**: V4 旧版 PDF 路径 (P2 必查), terminal 终稿 tex 与 V4 的章节差异。

  

---

  

## 你的工作要闭合的 Gap (Phase 1 摘录)

  

| ID | 漏洞 | 你的实验 |

|----|------|----------|

| **G3 主体** | 论文承诺检测 7 类 hijacking, 实际只评 binary fine-window detector, 覆盖 2 类; edit-distance comparator 从未量化评估。 | **E4** |

| **G4** | 7.82 TB / 38-skill 语料是论文最 underclaimed 的贡献, 应升级为 C5 dataset contribution。 | **P1, P6, P7** |

  

(G1 由 A 的 E1 闭合, G2 由 B 的 E2 闭合, G3 部分由 B 的 E3 闭合)

  

---

  

## Phase 6: 启动前 Sanity Check (E4 / E11 启动前必跑)

  

```

1. 主机空闲 (CPU < 30%, GPU/NPU 可用 — E11 多 baseline 训练吃 GPU)

2. 数据盘 free space ≥ 500 GB

3. 时间同步 (chronyc tracking) DUT-Win-Ext offset < 50 ms (E4 用)

4. SDR hackrf_info 都识别 (E4 用)

5. 温度 probe 有读数

6. E0 baseline: 用现有数据复现 AUC ≈ 0.9945 ± 0.005

   如复现不出 → 不要硬上, 先排查环境差异

```

  

任何 sanity check 失败 → 修复后再启动。

  

---

  

## E4 — Stage-2 Edit-Distance Comparator 真实评估 【Tier 1, 关键路径, 闭合 G3 主体】

  

**目的**: 让题目 "workflow hijacking" 站得住。

  

**Hypothesis**: confusability-weighted edit distance 在 5-template benchmark

上 AUC ≥ 0.85。

  

**Workflow templates** (5 × 6 variants = 30 classes, 5 instances each = 150 records):

  

```

W1 doc_summarize_email:    OpenFile→Summarize→ComposeEmail→SendEmail

W2 db_query_report:        db_analytics→Summarize→log_rotate_compress

W3 build_deploy_test:      git_dev→build_release→system_maintenance

W4 web_scrape_analyze:     browser_session→db_analytics→wiki_email

W5 iot_poll_log:           sensor_polling→db_analytics→log_rotate_compress

  

每 template 5 hijacked variants:

  H_INS: 中间插入 attack_third_party_rm

  H_OMI: 删最后一步

  H_SUB: 末步换 attack_bad_tool_result_wget_bash

  H_REO: 颠倒中间两步

  H_BR : 中间分支 attack_third_party_cp 后回主线

```

  

**Comparator** (`stage2_comparator.py`):

  

```python

def confusability_cost(s_a, s_b, pairwise_f1):

    return 1.0 - pairwise_f1.get((s_a, s_b), 0.0)

  

def edit_distance(W_int, W_rec, c_ins=0.5, c_del=0.5):

    # Wagner-Fischer DP, sub cost = confusability_cost

    ...

  

def hijacking_decision(D, delta):

    return "HIJACKED" if D > delta else "BENIGN"

```

  

**Procedure**:

```

Step 1. 实现 workflows_v1/ 共 30 classes

Step 2. 采集 10 cycles × 30 × 1 = 300 records at new bands, ~6 h

Step 3. Stage 1 hierarchical recovery:

        - 先 binary attack/normal per fine-window

        - normal window 进 16-cls big48 classifier

        - attack window 标 "*"

        - 输出 ˆW = (skill_id 或 *) 序列

Step 4. 计算 D(W, ˆW): big48 pairwise F1 作 confusability table, c_ins=c_del=0.5

Step 5. 评估: 5 hijacked + 5 benign per template, sweep δ ∈ [0.1, 2.0]

        per-hijacking-type breakdown (INS/OMI/SUB/REO/BR)

Step 6. 与现有 binary fine-window detector 在同 300 records 上对比

```

  

**Acceptance**:

- 总 AUC ≥ 0.85 + 每类 ≥ 0.7 → 题目保留

- 总 AUC < 0.7 → 题目改为 "Detection of Malicious Sub-Skill Activity..."

- INS/SUB 高、OMI/REO 低也接受, 分类报告 (这是 honest result, 也是发表点)

  

**Failure pivot**: ˆW 太烂 (因 big48 macro-F1=0.146) → 16 类降到 8 super-class

(idle/build/data/web/file/dev/iot/email); pairwise F1 在 attack 类无数据 →

0.5 prior

  

**Time**: 12–14 天 (关键路径)

  

**Paper landing**: §V-D 重写"deferred to artefact"段; 新 §VI-D "Workflow-Level

Hijacking Detection" + Table XI + Fig.21; §IX 允许说 "ClawGuard detects

workflow hijacking" (if AUC ≥ 0.85)。

  

**协调**:

- 你产出的 big48 pairwise F1 confusability table 也给 A 的 E12 用 (诊断 NPU

  encoder 能否捞回 confusable skill)

- E4 结果决定题目是否改 — 跑完立刻全员通知

  

---

  

## E11 — Baseline 横向对比补全 【Tier 2, 7–10 天, 闭合"方法比较缺失"】

  

**目的**: 终稿只比 IsolationForest/OCSVM/CNN+LSTM 三个。审稿人会要求 ≥ 6

类同台对比。

  

**Baselines** (11 个, 实做 ≥ 6):

  

| 类别        | 方法                                  | 实现                       |

|-------------|---------------------------------------|----------------------------|

| Anomaly     | IsolationForest, OCSVM, Mahalanobis,  |                            |

|             | AutoEncoder reconstruction            | sklearn / scipy / torch    |

| Shallow Sup | LogReg L2, LDA, 5-NN                  | sklearn                    |

| Tree Sup    | RF, HGB, XGBoost, LightGBM            | (现有)                     |

| Deep Sup    | 1D CNN raw IQ, CNN+BiLSTM,            |                            |

|             | patchTST Transformer                  | torch                      |

| Cross-domain| EMMA-style template match             | reproduce from EMMA paper  |

| Host-baseline | bpftrace syscall histogram + RF     | NEW                        |

  

**Procedure**:

```

Step 1. 全部 baseline 在 1,797 cycle-disjoint split 跑 LOCO

Step 2. 全部 baseline 在 new-bands 550 records 跑 zero-shot transfer

Step 3. 报告 AUC ± 5-seed bootstrap CI, train time, inference latency

Step 4. host-based eBPF baseline 是关键 fair comparison:

        trust-degradation curve: x = host compromise level (0 → root → kernel)

        y = AUC

        ClawGuard 单调, host-based 在 root 处 cliff

```

  

**Acceptance**: ≥ 6 baseline 完成同 split 同 protocol; ClawGuard 在 ≥ 4

个 baseline 上 DeLong p < 0.05

  

**Failure pivot**: Transformer 在小样本不收敛 → 写 "Transformer needs more

data; future work"

  

**Paper landing**: §VII Related Work 末延伸为新 §VI-F "Baseline Comparison"

+ Table XIII + Fig.25 (trust-degradation)

  

**协调**: bpftrace host-baseline 是 G1 论证的同台 fair comparison, A 的 E1 跑完

后引用你的 trust-degradation 曲线在 §VI-E 收尾。

  

---

  

## P1 — 重写 Contributions (5 条, 含 Dataset C5) 【Tier-B, 1 天】

  

```

C1 Skill-Level EM Granularity (理论分层)

C2 Out-of-Band Architecture (drift-compensated 系统设计)

C3 Methodological Insight on RF Artifacts (governor-driven AFM 揭露)

C4 Workflow-Hijacking Detection (评测主结果)

C5 The ClawGuard Skill-EM Dataset:

   First-of-its-kind 8 TB-scale skill-level EM corpus spanning 38 skills

   (16 benign + 22 attack), 12,232 records, dual-band synchronized SDR +

   thermal + event metadata. Released under CC-BY-4.0. (See P6.)

```

  

摘要末尾加: "We release the 7.82 TB corpus and reference V10 pipeline at

https://anonymous.4open.science/r/clawguard-{anon-id}."

  

题目可能改动:

- E4 通过 (AUC ≥ 0.85): 保持当前题目

- E4 不通过: 改 "Out-of-Band Detection of Malicious Sub-Skill Activity in

  LLM Agent EM Emanations"

  

**依赖**:

- A 的 E5 5-seed CI + DeLong p-value (摘要的 AUC 数字带 CI)

- B 的 E3 mimicry detection rate (摘要倒二句)

- B 的 E2 governor 数字 (§IX 88.3% 升级)

- 你自己的 E4 结果 (题目是否改)

  

E5/E3/E2/E4 任一未到位前, P1 别 finalize。

  

---

  

## P2 — 重新加回 V4 Caveat 【Tier-B, 1.5 天】

  

| V4 段                                              | 加到终稿哪里                          |

|----------------------------------------------------|---------------------------------------|

| §III-B "Label provenance & event-anchor provenance"| §IV-A 末尾, 1 段, 链 E1 结果         |

| §VI-D "Three caveats on AUC headline"             | §VI-C 末尾, 简化 1 段                |

| §VIII limitations 8 条                            | §VIII 重组为编号 L1–L8                |

| §V-E governor reconciliation                       | 至少 ondemand vs userspace 表加回    |

  

**前置**: 必须先找到 V4 旧版 PDF (Phase 0.1)。逐段对照, 不要全文 copy-paste —

只加回终稿砍掉的诚实段。

  

**依赖**: A 的 E1 主结果 (label-provenance 段引用); B 的 E2 主结果 (§V-E

governor reconciliation 表)。

  

---

  

## P6 — Dataset Release Plan 【Tier-B, 4–6 天】

  

**目标**: 把 corpus 升格为 NDSS Artifact Evaluation 可申请的独立资源。

  

**释放分层**:

  

```

Tier 1 (rebuttal 期间, 评审可访问):

  big48 16-cls 完整 1,529 records (~120 GB)

  focused3 完整 (~8 GB)

  全部 V10 feature CSV (跨所有 corpus, ~1 GB)

  reference V10 + RF 代码

  托管: anonymous.4open.science (双盲) 或 Zenodo sandbox

  README + checksum + 5 分钟跑通的 reference notebook

  

Tier 2 (中稿后):

  全部 raw IQ 7.82 TB

  new-bands 550 IQ files

  attack_v1 155 records

  attack skill source code

  托管: Zenodo (DOI), 镜像到 OpenClaw GitHub Releases

  License: CC-BY-4.0 for data, MIT for code

  

Tier 3 (社区维护):

  Croissant metadata schema 描述

  HuggingFace Datasets 集成

  load_dataset("openclaw/clawguard-em", "big48_v10")

```

  

**先结合 big48 起步**: big48 (1,529 records, 16-cls, 48 cycles) 是

EM-side-channel 文献中规模最大的 single-class-per-record 语料, 单独抽出做

dataset descriptor 即一篇可独立引用的资源。

  

**Acceptance**: 至少 Tier 1 在投出 rebuttal 前可下载, 附 README +

checksum + reference notebook (5 min 跑通最小 LOCO)

  

**Paper landing**: 摘要 + §I C5 + §VI-A 末尾段 + 新 §X "Dataset and

Reproducibility" (如章节空间允许)

  

---

  

## P7 — Skill Operation Detail Table 【Tier-A 起步, 2–3 天完成】

  

**目标**: 当前论文只列 skill 名字, 未说明每个 skill 实际操作。审稿人会

要求知道 "db_analytics 到底跑什么 SQL"。

  

**Table V 字段**:

  

```

| Skill ID | Category | Description | Typical Duration | Resource Mix | Source / UUID |

```

  

**示例行** (全 38 行需对齐 _remote_mirror/skills/* 源码):

  

```

db_analytics  | benign | sqlite3+numpy 在 50k-row TPC-H lineitem 表

                         GROUP BY 聚合 5 次              | 10–14s | DRAM-heavy + CPU | OpenClaw v1.2

build_release | benign | git clone+cmake+make -j4 编译

                         50KLOC C++                       | 18–22s | CPU-heavy        | OpenClaw v1.2

log_rotate_compress | benign | gzip + logrotate 压缩 200MB

                                日志                       | 8–12s  | DRAM + IO storage| OpenClaw v1.2

file_sync_backup | benign | rsync --checksum 同步 1.2 GB

                            目录                          | 12–18s | IO + network     | OpenClaw v1.2

attack_third_party_rm | attack | rm -rf /tmp/openclaw_skills/

                                  payload/{1..50}         | 0.4–0.8s | IO syscalls    | m4p1e UUID:abcd...

attack_bad_tool_result_wget_bash | attack | wget 返回伪

                                  造 .sh, agent 执行       | 1.2–2.0s | network+CPU exec| m4p1e UUID:efgh...

... (剩余 32 行)

```

  

**Procedure**:

```

Step 1. 列出 _remote_mirror/skills/ 全部 38 路径

Step 2. 每 skill 执行 5 次, time + ps + iotop 测 resource mix:

  CPU%: ps aux 取 max

  DRAM peak: /proc/<pid>/status VmPeak

  storage IO: iotop -p <pid>

  network: ss / nethogs

  Resource Mix 量化为四档: CPU-heavy / DRAM-heavy / IO-heavy /

                          Network-heavy / Mixed

Step 3. LaTeX longtable, ~2 页

Step 4. 检查 attack 的 ATTACK_ID UUID 与 m4p1e/agent-sentinel 原始 entry

        1:1 对应

```

  

**Acceptance**: 38 行齐全, attack UUID 与 origin 1:1, 同 skill 5 次

duration std ≤ 20%

  

**Paper landing**: 新 Table V at §VI-A, 替代当前 "16-skill big48 catalog

... 22-class attack catalog comprises 11 third-party shell utilities..."

一段散文描述

  

**协调**: Step 2 测 resource mix 需要 DUT — 与 B (E2/E3/E6) 排好不冲突的时段。

  

---

  

## 输出与报告约定 (每实验目录的 report.md 模板)

  

```markdown

# E{N}: {name}

  

## Status: [planned | running | done | failed-pivot]

  

## Hypothesis: ...

  

## Data collected:

- carrier pair: ...

- cycles: ...

- records: ...

- raw IQ size: ... GB

- collection wall time: ...

  

## Headline metric:

{metric_name}: {value} ± {ci}

  

## Acceptance criterion: {pass | fail | pivot}

  

## Paper landing:

- 修改了 §X.Y 的第 Z 段

- 新增 Fig.{NN}, Table.{NN}

  

## Reproducibility:

- 训练 seed: ...

- code commit: ...

- data hash: SHA-256 of .npz

```

  

每 Tier 1 实验完成后 ≤ 200 字总结:

  

```

[E{N}] {name}: {pass | fail | pivot}

  Headline:    {1 行核心数字}

  vs hypothesis: {正/反向多少}

  Paper impact: {section, strengthen / weaken claim}

  Time spent:   X 天 (estimated Y)

  Next:         {继续 / 等用户决策}

```

  

Tier 2/3 实验: 1 行写完即可。

  

---

  

## 你的时间表 (5–6 周内 ~25 active days, 你也是 paper czar)

  

```

Week 1:

  - P7 起步: 列 38 skill, 写 LaTeX longtable 骨架

  - E4 workflows_v1/ 30-class 实现

  - E11 Anomaly 4 类 baseline 在 1,797 split 起步

  - 找 V4 旧版 PDF, 起 P2 段落映射表

  

Week 2:

  - E4 采集 300 records (new bands, ~6 h)  — 与 B 协调 SDR 排期

  - E11 Shallow Sup + Tree Sup 跑完

  - P7 测 38 skill resource mix (DUT 排期)

  

Week 3:

  - E4 stage-1 hierarchical recovery 实现

  - E4 confusability table 计算 (big48 pairwise F1)  — 同步给 A (E12 复用)

  - E11 Deep Sup (1D CNN, BiLSTM, Transformer)

  - P6 Tier 1 释放包打包 (anonymous.4open.science)

  

Week 4:

  - E4 comparator 完成 + AUC sweep δ + 分类报告 (停下汇报, 题目决定点)

  - E11 host-baseline (bpftrace) + trust-degradation 曲线

  - P1 contribution 重写 (依赖 A 的 E5, B 的 E2/E3, 你的 E4)

  

Week 5:

  - P2 V4 caveat 逐段加回 (依赖 A 的 E1, B 的 E2)

  - P6 Tier 1 README + reference notebook 5 min 跑通验证

  - 全员 latex pass: 你召集 A、B 一起做 \ref / \cite 验, 章节合并

  

Week 6 (camera-ready 截止前):

  - 整合所有 metric, 重写 §VI / §VIII (paper czar 主导)

  - diff_to_submitted.md 最终化

  - 投出 rebuttal 包前最终 sanity (色盲检查由你做的话: Coblis 在线工具)

```

  

---

  

## Phase 8: Anti-Patterns (你别做这些)

  

- 7.82 TB 不要改回 1.82 TB, 但要在 Table IV 拆透明

- 不要删 §VIII limitations

- 不要追加新 baseline 之外的 scope creep — E11 11 类列表已是上限

- 不要在 camera-ready 加新作者贡献

- E4 不通过强制题目改时**不要硬扛** — 接受降级题目, 数据继续诚实写

- E11 Transformer 不收敛**不要藏** → 写 future work, 不算 fail

- **不要在 E4 主结果 + E1 (A) + E2/E3 (B) 都到位之前 finalize P1 摘要**

- 不要在 P2 重新加 V4 caveat 时全文 copy-paste — 只加回终稿砍掉的诚实段

- 不要在没跑 sanity check (Phase 6) 时启动任何采集

- Tier 1 实验 (E4) 交付时**停下汇报**, 等用户确认再开下一个

  

---

  

## Phase 9: 执行原则

  

- **E4 (你的 Tier 1) 交付时停下汇报**, 等用户确认再开下一个

- E11 (Tier 2) + paper revisions (P1/P2/P6/P7) 可批量执行后一次性汇报

- 每实验目录维护 report.md, 含上方全部字段

- 验证再 loop: surgical changes, simplicity first, goal-driven

- 如发现 Phase 0 资源定位结果与预设有出入, 在 _discovery_C.md 记录

- **作为 paper czar**: 你负责 maintain `paper_camera_ready/diff_to_submitted.md`,

  逐节记录 A/B/你 各自做了什么改动, 在 Week 5 整合前给全员看 1 次

  

---

  

## 关键 Hand-off

  

| 你产出 | 谁需要 |

|-------|-------|

| big48 pairwise F1 confusability table (E4 副产) | A (E12 NPU encoder 诊断) |

| E4 题目决定 (pass/fail) | 全员 (题目是否改) |

| E11 trust-degradation 曲线 | A (E1 §VI-E 收尾引用) |

| P1 重写后的 5 contributions | 全员 (大家段落措辞要对齐) |

| P7 Table V skill-level 描述 | A (E12 数据上传 manifest 需要 skill ID) |

  

| 你需要等 | 谁产出 |

|---------|-------|

| 5-seed CI + DeLong p-value (P1 摘要用) | A 的 E5 |

| OOB anchor AUC (P2 §IV-A 段引用) | A 的 E1 |

| Mimicry detection rate (P1 摘要倒二句) | B 的 E3 |

| Governor M3/M4 AUC (P1 §IX deployment number) | B 的 E2 |

| feature-space bottleneck 诊断 (P1 §VIII 措辞) | A 的 E12 |

  

**你的 P1 是全员论文修订的合流点 — 等 A/B Tier-1 实验数据齐了再 finalize**。