# ✍️ Zhiyin: Exploring the Frontier of Chinese LLM Writing
[**Website**](http://zake7749.github.io/Chinese-Writing-Bench/) &bull; [**GitHub**](https://github.com/zake7749/Chinese-Writing-Bench) &bull; [**Hugging Face**](https://huggingface.co/datasets/zake7749/chinese-writing-bench)

Zhiyin is an LLM-as-a-judge benchmark for Chinese writing evaluation. This V1 release features 280 test cases across 18 diverse writing tasks.

![462948315-d79b6a59-3bf4-4c12-93a7-96cac5f867ff](https://github.com/user-attachments/assets/46ce9ea3-951f-4e53-9544-657fea9eebd9)

---

## 🎯 Benchmark Overview

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

Please refer to [Evaluation.md](https://github.com/zake7749/Chinese-Writing-Bench/blob/master/Evaluation.md) for more details.

---

## 🏆 Leaderboard: All Writing Tasks
Scores are averaged across all 280 writing prompts.

| Model | Overall | Comprehension | Coherence | Style | Creativity | Depth | Helpfulness |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **o3-2025-04-16** | **6.95** | 6.91 | 6.75 | 7.05 | 6.90 | 6.44 | 6.74 |
| **Deepseek-R1-0528** | **6.77** | 6.72 | 6.70 | 7.10 | 7.02 | 6.60 | 6.58 |
| **Qwen3-235B-Thinking** | **6.66** | 6.39 | 6.45 | 7.30 | 7.44 | 6.32 | 6.29 |
| **Qwen3-32B-Thinking** | **6.58** | 6.34 | 6.43 | 7.09 | 7.19 | 6.19 | 6.18 |
| **Monomer-24B-Writer** | **6.24** | 6.18 | 6.34 | 6.52 | 6.50 | 6.01 | 6.09 |
| **Deepseek-V3-0324** | **6.20** | 6.08 | 6.24 | 6.56 | 6.61 | 5.80 | 5.96 |
| **Qwen3-30B-A3B-Thinking** | **6.06** | 5.91 | 6.05 | 6.53 | 6.53 | 5.65 | 5.82 |
| **Gemini-2.5-Flash** | **6.01** | 6.20 | 6.22 | 6.00 | 5.83 | 5.75 | 6.03 |
| **Monomer-8B-Writer** | **5.70** | 5.66 | 5.96 | 6.00 | 5.95 | 5.57 | 5.63 |
| **Qwen3-235B** | **5.59** | 5.74 | 5.88 | 5.63 | 5.51 | 5.21 | 5.55 |
| **o4-mini-2025-04-16** | **5.54** | 5.80 | 5.70 | 5.59 | 5.44 | 5.10 | 5.58 |
| **Mistral-3.2-24B-2506** | **5.35** | 5.53 | 5.82 | 5.53 | 5.61 | 5.01 | 5.35 |
| **Qwen3-32B** | **5.22** | 5.46 | 5.63 | 5.29 | 5.08 | 4.88 | 5.31 |
| **gemma3-27b** | **5.08** | 5.43 | 5.54 | 5.03 | 5.12 | 4.85 | 5.22 |
| **gpt-4o-2024-11-20** | **4.99** | 5.28 | 5.35 | 5.21 | 5.08 | 4.75 | 5.01 |
| **Qwen3-8B** | **4.82** | 5.15 | 5.26 | 4.91 | 4.69 | 4.50 | 4.85 |
| **Qwen3-30B-A3B** | **4.81** | 5.15 | 5.29 | 4.85 | 4.71 | 4.53 | 4.93 |
| **gpt-4.1-mini-2025-04-14** | **4.44** | 5.04 | 4.94 | 4.68 | 4.34 | 4.20 | 4.56 |
| **gpt-4o-mini-2024-07-18** | **4.32** | 4.76 | 4.90 | 4.54 | 4.29 | 4.08 | 4.35 |
| **Phi-4-14B** | **4.30** | 4.74 | 4.89 | 4.46 | 4.24 | 4.18 | 4.32 |
| **Mistral-3.1-24B-2503** | **4.20** | 4.71 | 4.80 | 4.22 | 3.91 | 3.90 | 4.24 |

---
## 👑 Leaderboard: Complicated Writing Tasks
Scores for a subset of more complex, nuanced, and challenging writing prompts.

| Model | Overall | Comprehension | Coherence | Style | Creativity | Depth | Helpfulness |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **o3-2025-04-16** | **7.18** | 7.23 | 7.02 | 7.45 | 7.29 | 6.69 | 6.92 |
| **Deepseek-R1-0528** | **6.92** | 6.77 | 6.74 | 7.32 | 7.37 | 6.85 | 6.73 |
| **Qwen3-235B-Thinking** | **6.58** | 6.22 | 6.25 | 7.42 | 7.77 | 6.32 | 6.17 |
| **Qwen3-32B-Thinking** | **6.55** | 6.21 | 6.22 | 7.15 | 7.44 | 6.18 | 6.09 |
| **Monomer-24B-Writer** | **6.34** | 6.24 | 6.31 | 6.57 | 6.79 | 6.08 | 6.18 |
| **Deepseek-V3-0324** | **6.15** | 6.11 | 6.12 | 6.55 | 6.82 | 5.82 | 5.86 |
| **Qwen3-30B-A3B-Thinking** | **6.03** | 5.77 | 6.05 | 6.55 | 6.74 | 5.67 | 5.78 |
| **Gemini-2.5-Flash** | **5.94** | 6.20 | 6.14 | 5.92 | 5.80 | 5.71 | 6.00 |
| **Monomer-8B-Writer** | **5.68** | 5.56 | 5.86 | 5.92 | 6.16 | 5.53 | 5.59 |
| **Qwen3-235B** | **5.42** | 5.71 | 5.81 | 5.37 | 5.50 | 5.08 | 5.45 |
| **o4-mini-2025-04-16** | **5.13** | 5.51 | 5.48 | 5.33 | 5.26 | 4.79 | 5.24 |
| **Mistral-3.2-24B-2506** | **5.06** | 5.42 | 5.62 | 5.14 | 5.48 | 4.69 | 5.11 |
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

## 📝 Writing Tasks & Examples

Below are the tasks and data examples from our benchmark dataset. Due to space constraints, some paragraphs are abbreviated with “...”. The full instructions can be found in the original Hugging Face dataset.

### 1. Sentence/Paragraph Continuation
> 秋天的午後，陽光篩過逐漸稀疏的枝葉，在老舊的木地板上投下斑駁的光影。空氣中飄浮著淡淡的桂花香氣，以及遠方隱約傳來的叫賣聲。我獨自坐在窗邊，手中捧著一本泛黃的舊書，指尖滑過書頁上那些被時光磨蝕的文字，心中湧起一股難以言喻的平靜與懷舊……
> 
> 請接續這段文字，保持抒情、感性的散文風格

### 2. Short Essay Writing
> 你有沒有想過，為什麼有些很厲害的人，心裡卻總覺得自己是個不配的騙子？但反過來，有些能力普通的人卻總是自信心爆棚？我想請你寫一篇文章，聊聊「冒牌者症候群」和「達克效應」這兩種有趣的心理現象。希望你可以用生活或職場上的小故事來解釋它們，分析這兩種心態會如何影響我們的學習和人際關係，最後給那些常常自我懷疑、或是需要更客觀認識自己的人一些溫暖的建議。

### 3. Creative Writing
> 想像一個顛倒的世界：人們在天花板上行走，雨水從地面往天上飄。請寫一則文章，描繪這個顛倒世界的某個生活場景或景象，著重於其中的奇特之處。

### 4. Contextual Text Generation
> 我明天家裡臨時有急事，得提早一小時下班。你幫我寫封簡短 Email 給我主管王經理，跟他說一下（不用提細節，就說家裡有事），請他批准。記得要客氣、正式一點喔。

### 5. Paraphrasing
> 由於突如其來的暴雨，導致戶外音樂會被迫臨時取消。請用不同的措辭改寫以上句子，但保持其核心意思不變。

### 6. Style Transfer
> 為維護場地秩序，敬請各位來賓依工作人員指示入座，並將手機調整為靜音模式。
請將以上這句比較正式的場合用語，改寫成更輕鬆、口語化的說法。

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
> 我們公司新推出一款強調『方便攜帶、隨時可用』的迷你行動電源，這是它的基本資料：「容量 5000mAh，重量僅 100 克，自帶 Type-C 和 Lightning 充電線，馬卡龍色系外殼，售價 699 元。」你幫我寫一則大約 80-100 字的社群媒體推廣貼文...

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
> 你幫我寫一段三個室友（小光、美玲、阿德）在廚房裡互相指責是誰沒洗碗的劇本對話。大概 10 行對話，要表現出三個人不同的個性（例如：小光可能有點潔癖，美玲比較健忘，阿德是和事佬）。記得用劇本格式標出人物和對白。

### 14. Lyric Writting
> 我想寫首歌，主題是關於「思念家鄉」的。你幫我寫一段主歌（Verse）的歌詞，大概 4-6 行，表達那種在外地打拼時，想念家鄉食物或風景的心情。不一定要押韻，但希望有點畫面感。

### 15. Roleplay-Story Telling
> 你是古羅馬的一位建築工程師，曾參與那座舉世聞名的圓形競技場的建造。多年後，當你帶著孫子重遊此地時，你向他講述當年的故事。請以你的視角，描述這座建築的宏偉設計、建造過程中的工程奇蹟與挑戰...

### 16. Knowledge-Dependent Article Writing
> 請以1968年捷克布拉格之春前夕為背景，撰寫一則以哲學思辨與情感掙扎交織的故事。男主角安德烈是布拉格報社編輯，對政治冷淡卻對人生充滿疑惑；女主角塔瑪拉是前衛畫家，崇尚自由與即興主義...

### 17. Complicated Instruction Following
> 以「濾鏡下的真實」為題，探討社群媒體時代的身份焦慮與展演人生。主角是一位在 Instagram 上擁有數十萬粉絲的「生活風格」網紅...

### 18. Brainstorming
> 一個喝完飲料的乾淨空寶特瓶，除了丟回收之外，還能拿來做什麼有創意或實用的事情？你幫我腦力激盪一下，列出 8 個空寶特瓶的再利用點子。

---

## Citation
If you use these results, please cite our paper:
```
"Zhiyin: Exploring the Frontier of Chinese LLM Writing, 2025. https://github.com/zake7749/Chinese-Writing-Bench"
```