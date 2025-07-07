from string import Template
from dataclasses import dataclass


@dataclass(frozen=True)
class PairwiseJudgeTemplate:

    criteria: tuple[str] = (
        'comprehension',
        'structure',
        'prose_style',
        'creativity',
        'depth',
        'helpfulness',
        'overall',
    )
    template: Template = Template("""### 任務說明

你是一位精準、公正的寫作評審。你將基於給定的「使用者指令」，比較「助理回應」與「Baseline」的品質。

### 評分標準

- Baseline 的品質被定義為 5 分。這是你的錨點。
- 你需要為助理回應給出一個 0 到 10 分的整數分數，若你給助理：
    - 高於 5 分：代表助理回應優於 Baseline。分數越高，代表優勢越大（10分為大幅超越）。
    - 低於 5 分：代表助理回應劣於 Baseline。分數越低，代表劣勢越大（0分為完全失敗）。
    - 5 分：代表助理回應與 Baseline 的品質不相上下，難以區隔出優劣。

### 評分策略

請根據指令類型，適當選擇以下基準進行多維度評估：

1.  理解與切題性: 哪個回應更深刻地理解了指令的內涵與意圖？
2.  結構與連貫性: 哪個回應的結構更清晰、邏輯更流暢、文章用詞與段落轉折更為通順？
3.  文筆、風格與語氣: 哪個回應的語言運用更精準、如更具文采、或更貼近要求的風格？
4.  創意與原創性: 哪個回應展現了更新穎的想法、更獨特的視角或更巧妙的構思？
5.  深度與洞見: 哪個回應提供了更有深度的思考、或更獨到的見解？
6.  有幫助性: 哪個回應對於使用者更有幫助，綜合而言更能達成使用者的需求？

### 輸出格式

請先撰寫詳細的評分理由，解釋你是如何從比較分析導出這個最終分數的。你的理由必須清晰地闡述為何它比基準好/差，以及好/差的程度。

再採用以下格式輸出結果，清楚紀錄各個維度的評分結果，以及綜合而言，你認為助理於該指令的評分：

[START_OF_JUDGEMENT]
{
    "comprehension": {
        "judge": "說明對於理解與切題性的評判",
        "score": integer
    },
    "structure": {
        "judge": "說明對於結構與連貫性的評判",
        "score": integer
    },
    "prose_style": {
        "judge": "說明對於文筆、風格與語氣的評判",
        "score": integer
    },
    "creativity": {
        "judge": "說明對於創意與原創性的評判",
        "score": integer
    },
    "depth": {
        "judge": "說明對於深度與洞見的評判結果",
        "score": integer
    },
    "helpfulness": {
        "judge": "說明對於有幫助性的評判結果",
        "score": integer
    },
    "overall": {
        "judge": "說明整體而言，助理的回答相較於 Baseline 的評判結果",
        "score": integer
    }
}
[END_OF_JUDGEMENT]

請注意，**務必遵守此格式，將 JSON Object 包覆於 [START_OF_JUDGEMENT] 與 [END_OF_JUDGEMENT] 內** 
 
### 評分對象

以下將提供使用者指令，Baseline 回應與使用者回應。

**1. 使用者指令:**

```
$user_prompt
```

---

**2. Baseline Response - [品質定義為 5 分]:**

```
$baseline_response
```

---

**3. 助理回應 - [請為此回應評分]:**
```
$assistant_response
```""")