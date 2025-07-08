# Zhiyin: Exploring the Frontier of Chinese LLM Writing
[**Website**](http://zake7749.github.io/Chinese-Writing-Bench/) &bull; [**GitHub**](https://github.com/zake7749/Chinese-Writing-Bench) &bull; [**Hugging Face**](https://huggingface.co/datasets/zake7749/chinese-writing-bench)

Zhiyin is an LLM-as-a-judge benchmark for Chinese writing evaluation. This V1 release features 280 test cases across 18 diverse writing tasks.

![462948315-d79b6a59-3bf4-4c12-93a7-96cac5f867ff](https://github.com/user-attachments/assets/46ce9ea3-951f-4e53-9544-657fea9eebd9)

---

## Benchmark Overview

Our evaluation method relies on **pairwise comparison**. A powerful language model (O3) acts as the judge, scoring a model's response relative to a fixed baseline (GPT-4.1), which is anchored at a score of 5.

### Scoring System
The judge assigns the model's response an integer score from 0 to 10, where:
- A score > 5 indicates the response is **superior** to the baseline.
- A score = 5 indicates the response is **on par** with the baseline.
- A score < 5 indicates the response is **inferior** to the baseline.

### Evaluation Dimensions
To ensure a comprehensive analysis, the final score is informed by a multi-dimensional assessment. The judge evaluates the response across six key criteria:

1.  **Comprehension & Relevance:** How well the response understands the prompt's intent and stays on topic.
2.  **Structure & Coherence:** How clear, logical, and well-organized the writing is.
3.  **Prose & Style:** The quality of the language, grammar, and adherence to the requested tone.
4.  **Creativity & Originality:** The novelty of the ideas and the uniqueness of the perspective.
5.  **Depth & Insight:** The level of detail, analysis, and substance provided.
6.  **Helpfulness:** How effectively the response fulfills the user's overall goal.

### Evaluation Scripts

Please refer to [Evaluation.md](https://github.com/zake7749/Chinese-Writing-Bench/blob/main/Evaluation.md) for more details.

---

## Leaderboard: All Writing Tasks

For the details of judgements, please refer to [zake7749/chinese-writing-bench-judgements](https://huggingface.co/datasets/zake7749/chinese-writing-bench-judgements)

Scores are averaged across all 280 writing prompts.

| Model | Overall | Comprehension | Coherence | Style | Creativity | Depth | Helpfulness |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **o3-2025-04-16** | **6.95** | 6.91 | 6.75 | 7.05 | 6.90 | 6.44 | 6.74 |
| **Deepseek-R1-0528** | **6.77** | 6.72 | 6.70 | 7.10 | 7.02 | 6.60 | 6.58 |
| **Qwen3-235B-Thinking** | **6.66** | 6.39 | 6.45 | 7.30 | 7.44 | 6.32 | 6.29 |
| **Qwen3-32B-Thinking** | **6.58** | 6.34 | 6.43 | 7.09 | 7.19 | 6.19 | 6.18 |
| **[Monomer-24B-Writer](https://huggingface.co/zake7749/Monomer-24B-Writer-Preview)** | **6.24** | 6.18 | 6.34 | 6.52 | 6.50 | 6.01 | 6.09 |
| **Deepseek-V3-0324** | **6.20** | 6.08 | 6.24 | 6.56 | 6.61 | 5.80 | 5.96 |
| **Qwen3-30B-A3B-Thinking** | **6.06** | 5.91 | 6.05 | 6.53 | 6.53 | 5.65 | 5.82 |
| **Gemini-2.5-Flash** | **6.01** | 6.20 | 6.22 | 6.00 | 5.83 | 5.75 | 6.03 |
| **[Monomer-8B-Writer](https://huggingface.co/zake7749/Monomer-8B-Writer-Preview)** | **5.70** | 5.66 | 5.96 | 6.00 | 5.95 | 5.57 | 5.63 |
| **Qwen3-235B** | **5.59** | 5.74 | 5.88 | 5.63 | 5.51 | 5.21 | 5.55 |
| **o4-mini-2025-04-16** | **5.54** | 5.80 | 5.70 | 5.59 | 5.44 | 5.10 | 5.58 |
| **Mistral-3.2-24B-2506** | **5.35** | 5.53 | 5.82 | 5.53 | 5.61 | 5.01 | 5.35 |
| **Qwen3-32B** | **5.22** | 5.46 | 5.63 | 5.29 | 5.08 | 4.88 | 5.31 |
| **gemma3-27b** | **5.08** | 5.43 | 5.54 | 5.03 | 5.12 | 4.85 | 5.22 |
| **gpt-4.1-2025-04-14** | **5.00** | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 |
| **gpt-4o-2024-11-20** | **4.99** | 5.28 | 5.35 | 5.21 | 5.08 | 4.75 | 5.01 |
| **Qwen3-8B** | **4.82** | 5.15 | 5.26 | 4.91 | 4.69 | 4.50 | 4.85 |
| **Qwen3-30B-A3B** | **4.81** | 5.15 | 5.29 | 4.85 | 4.71 | 4.53 | 4.93 |
| **gpt-4.1-mini-2025-04-14** | **4.44** | 5.04 | 4.94 | 4.68 | 4.34 | 4.20 | 4.56 |
| **gpt-4o-mini-2024-07-18** | **4.32** | 4.76 | 4.90 | 4.54 | 4.29 | 4.08 | 4.35 |
| **Phi-4-14B** | **4.30** | 4.74 | 4.89 | 4.46 | 4.24 | 4.18 | 4.32 |
| **Mistral-3.1-24B-2503** | **4.20** | 4.71 | 4.80 | 4.22 | 3.91 | 3.90 | 4.24 |

---
## Leaderboard: Complicated Writing Tasks
Scores for a subset of more complex, nuanced, and challenging writing prompts.

| Model | Overall | Comprehension | Coherence | Style | Creativity | Depth | Helpfulness |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **o3-2025-04-16** | **7.18** | 7.23 | 7.02 | 7.45 | 7.29 | 6.69 | 6.92 |
| **Deepseek-R1-0528** | **6.92** | 6.77 | 6.74 | 7.32 | 7.37 | 6.85 | 6.73 |
| **Qwen3-235B-Thinking** | **6.58** | 6.22 | 6.25 | 7.42 | 7.77 | 6.32 | 6.17 |
| **Qwen3-32B-Thinking** | **6.55** | 6.21 | 6.22 | 7.15 | 7.44 | 6.18 | 6.09 |
| **[Monomer-24B-Writer](https://huggingface.co/zake7749/Monomer-24B-Writer-Preview)** | **6.34** | 6.24 | 6.31 | 6.57 | 6.79 | 6.08 | 6.18 |
| **Deepseek-V3-0324** | **6.15** | 6.11 | 6.12 | 6.55 | 6.82 | 5.82 | 5.86 |
| **Qwen3-30B-A3B-Thinking** | **6.03** | 5.77 | 6.05 | 6.55 | 6.74 | 5.67 | 5.78 |
| **Gemini-2.5-Flash** | **5.94** | 6.20 | 6.14 | 5.92 | 5.80 | 5.71 | 6.00 |
| **[Monomer-8B-Writer](https://huggingface.co/zake7749/Monomer-8B-Writer-Preview)** | **5.68** | 5.56 | 5.86 | 5.92 | 6.16 | 5.53 | 5.59 |
| **Qwen3-235B** | **5.42** | 5.71 | 5.81 | 5.37 | 5.50 | 5.08 | 5.45 |
| **o4-mini-2025-04-16** | **5.13** | 5.51 | 5.48 | 5.33 | 5.26 | 4.79 | 5.24 |
| **Mistral-3.2-24B-2506** | **5.06** | 5.42 | 5.62 | 5.14 | 5.48 | 4.69 | 5.11 |
| **gpt-4.1-2025-04-14** | **5.00** | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 |
| **gpt-4o-2024-11-20** | **4.94** | 5.26 | 5.32 | 5.07 | 5.12 | 4.64 | 4.99 |
| **Qwen3-32B** | **4.80** | 5.23 | 5.39 | 4.92 | 4.91 | 4.61 | 5.04 |
| **gemma3-27b** | **4.78** | 5.26 | 5.33 | 4.59 | 4.82 | 4.58 | 5.07 |
| **Qwen3-30B-A3B** | **4.53** | 4.95 | 5.12 | 4.56 | 4.55 | 4.28 | 4.75 |
| **Qwen3-8B** | **4.46** | 4.86 | 5.02 | 4.56 | 4.43 | 4.18 | 4.57 |
| **gpt-4.1-mini-2025-04-14** | **4.33** | 4.98 | 4.88 | 4.51 | 4.28 | 4.02 | 4.51 |
| **gpt-4o-mini-2024-07-18** | **4.21** | 4.69 | 4.78 | 4.22 | 4.07 | 3.79 | 4.25 |
| **Phi-4-14B** | **4.10** | 4.62 | 4.69 | 4.09 | 3.99 | 3.86 | 4.20 |
| **Mistral-3.1-24B-2503** | **3.93** | 4.52 | 4.52 | 3.75 | 3.58 | 3.56 | 4.00 |

---

## Writing Tasks & Examples

Below are the tasks and data examples from our benchmark dataset. Due to space constraints, some paragraphs are abbreviated with “...”. The full instructions can be found in the original Hugging Face dataset.

### 1. Sentence/Paragraph Continuation
> 請繼續以下對話，並推展故事情節。描寫皇帝內心的掙扎與他最終做出的決定，保持緊張且凝重的歷史小說氛圍。
> 
> 「城牆外傳來的戰鼓聲越發急促，皇宮內燭光搖曳，映照出大殿上人們驚惶失措的面容。年幼的皇帝坐在龍椅上，臉色蒼白而無助，緊握著雙拳卻掩不住微微的顫抖。此刻，丞相徐鴻踏前一步，低聲但堅定地說道：『陛下，敵軍已近城門，您若不早做決斷，恐怕就無法挽回大局了。』話音剛落，旁邊的老將軍沉聲反駁：『臣願領兵死守，即使拼到最後一人，也絕不輕言投降！』皇帝的目光在兩人之間來回游移，殿內空氣緊繃得令人幾乎無法喘息……」

### 2. Short Essay Writing
> 有一種味道，吃一口就知道是「家」的味道。它可能來自媽媽的拿手菜，或奶奶的私房食譜。長大後，無論在外吃了多少山珍海味，最想念的還是那一味。寫一道菜，和那個為你做這道菜的人。那不僅是食物，更是愛與時光的記憶。

### 3. Creative Writing
> 城市有一座秘密倉庫，專門保存人們遺失或封存的「心跳」——某段激情、某種渴望、某次痛苦的愛。你意外地闖入了這座倉庫，發現每顆心跳都有聲音與故事。請描寫你在倉庫裡的所見所聞，並選擇其中一顆心跳去傾聽它的記憶。

### 4. Contextual Text Generation
> 我正在做上個月的業績報告，需要業務部的協助。你幫我寫封 Email 給業務部的窗口 Amy，請她提供一下上個月 A 產品的詳細銷售數據（例如數量和金額）。跟她說我這週五報告要交，希望能盡快拿到資料，謝謝她幫忙。

### 5. Paraphrasing
> 由於突如其來的暴雨，導致戶外音樂會被迫臨時取消。請用不同的措辭改寫以上句子，但保持其核心意思不變。

### 6. Style Transfer
> 現代人越來越依賴社群媒體獲取資訊和與人連結，但其背後的演算法機制，卻可能在無形中塑造著我們的認知。為了提升用戶黏著度，平台往往會優先推送使用者可能感興趣或認同的內容。當我們不斷點讚、分享、評論與自己觀點相符的貼文時，演算法便會學習我們的偏好，進而推薦更多同質性的資訊，同時減少我們接觸到不同聲音的機會...
>
> ---
>
> 用類似魯迅雜文的文風（冷靜觀察、帶有批判或反思意味、或許帶點諷刺）來重新書寫這段內容，探討這種現象背後可能反映的社會心態或個體焦慮。

### 7. Sentence  Simplification / Expansion
> 考量到現有資源的限制以及迫在眉睫的交付時程壓力，我們不得不做出一個艱難的決定，那就是暫時擱置部分次要功能的開發工作，以集中火力確保核心功能的穩定性與如期上線。
欸，上面這個寫得太繞口，你幫我把它改得簡單點，拆成幾句短的，讓人容易看懂，但意思不要跑掉。

### 8. Text Formatting
> 為推廣永續發展理念，市政府將於 8 月底舉辦為期兩天的「2025 綠能未來生活節」。活動地點位於大佳河濱公園，主舞台活動時間為每日 10:00–18:00。整體活動將分為五大展區，涵蓋教育、科技、藝術、飲食與親子體驗等面向...
> 
> ---
> 
> 可以幫我把這段活動資訊整理成 JSON 嗎？

### 9. Constrained Writing
> 我想請你寫一段話描述幸福的感覺，大概 50-80 字。但這裡有個限制：整段話裡面，絕對不能出現「幸福」或「快樂」這兩個詞。你試試看用其他方式表達那種感受。

### 10. Instructions & Information Integration
> 你幫我處理一下這幾封信...
> 
> 如果客戶滿意，草擬一封簡短的感謝信回覆他。
> 但如果客戶是抱怨，你就幫我草擬一封表示歉意、安撫他並請他提供訂單編號或更多細節以便處理的回信。
> 你要根據信件內容決定要寫哪一種喔。

### 11. Advertisement / Marketing
> 我們公司新推出一款強調『方便攜帶、隨時可用』的迷你行動電源，這是它的基本資料：「容量 5000mAh，重量僅 100 克，自帶 Type-C 和 Lightning 充電線，馬卡龍色系外殼，售價 699 元。」你幫我寫一則大約 80-100 字的社群媒體推廣貼文，要能打中常常手機沒電、又嫌行動電源很麻煩的年輕族群，強調它的小巧、方便、好看。

### 12. Machine Reading Comprehension
> 珊瑚礁被譽為「海底的熱帶雨林」，是地球上生物多樣性最豐富、結構最複雜的生態系之一...
> 
> 請根據以上文章回答下列問題：
> 
> RC-Q1: 這篇文章主要在談論什麼？
> (A) 詳細介紹珊瑚蟲的生物分類與生理結構。
> (B) 強調觀光旅遊對珊瑚礁地區經濟的重要性。
> (C) 說明珊瑚礁的生態價值、重要性、面臨的威脅及保護的必要性。
> (D) 比較珊瑚礁與熱帶雨林在生物多樣性上的差異。

### 13. Script Writting
> 幫我寫一場飯桌場景，家族裡的老大剛被刺殺未遂，現在輪到他的兒子出面主持會議。我要這場戲中沒有明說「你現在是新老大了」，但每個角色的語氣和反應都在確認這件事。場景中應該有沉默、視線交換、一點威脅語言的暗示，但一切都要在高教養的語境中進行。請用劇本格式書寫，三頁左右的篇幅。

### 14. Lyric Writting
> 我想寫首歌，主題是關於「思念家鄉」的。你幫我寫一段主歌（Verse）的歌詞，大概 4-6 行，表達那種在外地打拼時，想念家鄉食物或風景的心情。不一定要押韻，但希望有點畫面感。

### 15. Roleplay-Story Telling
> 你是一座飽經戰火的古老城市裡最後一位鐘樓守護人。今天，戰爭終於結束，和平協議已經簽訂。數十年來，你的鐘聲只為示警或報喪。今晚，市長請你敲響象徵和平的鐘聲。請以你的視角，描述在你攀上鐘樓時，撫摸著傷痕累累的牆壁與舊鐘的心情、你對過去歲月的追憶、敲響和平鐘聲那一刻的百感交集，以及你對這座城市未來重建之路的期盼與祝福。

### 16. Knowledge-Dependent Article Writing
> 請以1968年捷克布拉格之春前夕為背景，撰寫一則以哲學思辨與情感掙扎交織的故事。男主角安德烈是布拉格報社編輯，對政治冷淡卻對人生充滿疑惑；女主角塔瑪拉是前衛畫家，崇尚自由與即興主義。他們在咖啡館相識，展開了一段遊走於情感和哲學邊緣的對話與曖昧關係。情節中須有哲學辯論、細緻的咖啡廳場景描寫及大量心靈深處的反思，共計六段落。

### 17. Complicated Instruction Following
> 以「濾鏡下的真實」為題，探討社群媒體時代的身份焦慮與展演人生。主角是一位在 Instagram 上擁有數十萬粉絲的「生活風格」網紅，她的照片總是陽光、精緻、充滿正能量。不描寫她如何獲得成功，而聚焦於她關掉鏡頭後，在凌亂的租屋處獨自面對憂鬱症、催吐與帳單的時刻。透過她發文前後的內心獨白，以及與一位不知其真實身份的網友之間的真誠對話，呈現虛擬光環與真實自我之間的巨大裂痕，並詰問：當人生變成一場需要持續點讚的表演時，我們是否還有勇氣面對不完美的自己？

### 18. Brainstorming
> 我打算在台南開一家推廣台灣在地好茶的文創小店。除了傳統的店面銷售，還可以做哪些有創意、能吸引年輕人或觀光客注意的線上/線下行銷或體驗活動？想出 7 種適合這種在地文創茶店的行銷手法點子。

---

## Limitation

1. As noted in [Creative-Writing-Bench](https://eqbench.com/about.html#creative-writing-v3), LLM-judges may introduce various biases when evaluating creative writing. Since such evaluations are highly subjective, it’s wise to be skeptical of benchmark scores. The best way to assess a model is to try it yourself or review its sample outputs.
2. Currently, the benchmark focuses on Traditional Chinese in both raw queries and evaluation prompts, which means it may produce different results when assessing Simplified Chinese writing.

---

## Citation

If you found the benchmark useful, please cite our repository:
```
"Zhiyin: Exploring the Frontier of Chinese LLM Writing, Kai-Chou Yang, 2025. https://github.com/zake7749/Chinese-Writing-Bench"
```
