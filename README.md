# Formal Semantics Implementation — Mandarin Comparative Sentences
# 形式語意學實作：漢語比較句歧義計算

A Python implementation of formal semantic analysis based on Liu (2025), modeling the three-way ambiguity of Mandarin comparative sentences using the Event Taxonomization Function B.

本專案以 Python 實作 Liu (2025) 論文中的形式語意分析，透過事件分類函數（Event Taxonomization Function B）計算漢語比較句的三重歧義現象。

***

## Background｜背景說明

This project translates abstract lambda expressions from a formal linguistics paper into executable Python code. The target sentence is:

本專案將語言學論文中的抽象 Lambda 表達式轉換為可執行的 Python 程式碼，目標例句為：

> 王姑媽比李姑媽多搓合了那六個年輕人。
> *(Aunt Wang matched more of those six young persons than Aunt Li did.)*

The sentence has three distinct semantic readings depending on how participants are counted:

此例句依據參與者的計算方式，產生三種不同的語意讀法：

| Reading 讀法 | n | Description 說明 |
|---|---|---|
| Internal 內部讀法 | 0 | All participants come from "those six young persons" 所有參與者均來自「那六個年輕人」 |
| External 外部讀法 | 3 | Each pair includes one participant from external context 每組配對包含一位來自語境的外部人士 |
| Mixed 混合讀法 | 1 | Combination of internal and external participants 內部與外部參與者混合計算 |

***

## Reference Paper｜參考論文

Liu, C.-S. L. (2025). A transitive comparative with the transitive verb *duō*: a comparison along the cardinality of taxonomic unit events. *Journal of East Asian Linguistics*, 34, 155–204.
[https://doi.org/10.1007/s10831-024-09291-z](https://doi.org/10.1007/s10831-024-09291-z)

Full paper is included as `Reference_Paper.pdf`.

完整論文請見 `Reference_Paper.pdf`。

***

## File Structure｜檔案結構

```
1218_Matching/
├── D_Calculator.py        # Main implementation 主程式
├── Function_Sheet.png     # Diagram mapping lambda expressions to functions
│                          # Lambda 表達式與函式對應圖
├── Reference_Paper.pdf    # Source linguistics paper 參考論文
├── code_01.jpg            # Code screenshot (part 1) 程式截圖（上）
└── code_02.jpg            # Code screenshot (part 2) 程式截圖（下）
```

***

## Key Components｜主要元件

### Knowledge Bases｜知識庫

- **`NormKG`** — Stores verb semantic constraints (minimal unit per event type)
  儲存動詞語意限制（每種事件類型的最小單位）
- **`FactDB`** — Stores entity facts (quantity of participants)
  儲存實體資料（參與者數量）

### Core Functions｜核心函式

- **`STANDARD(dimension)`** — Retrieves the minimal taxonomic unit `z` for a given verb
  取得指定動詞的最小分類單位 `z`
- **`FactAccess(key, dimension)`** — Retrieves entity data from `FactDB`
  從 `FactDB` 取得實體資料
- **`NamedEntity(entity)`** — Resolves entity name
  解析實體名稱
- **`MATCH_EVENT(d, entity, n)`** — Computes taxonomic unit count and outsider count
  計算分類單位事件數量與外部參與者數量

### Core Formula｜核心公式

```python
tu_count = (y / z) + n
outsiders = n * z
```

Where 其中：
- `y` = number of participants from the noun phrase 名詞片語中的參與者數量
- `z` = minimal unit size defined by the verb 動詞定義的最小單位大小
- `n` = number of externally-supplied groups 來自外部語境的組數

***

## How to Run｜執行方式

No external packages required. Requires Python 3.x.

不需要安裝額外套件，需要 Python 3.x。

```bash
python D_Calculator.py
```

Expected output｜預期輸出：

```
--- Internal Reading (n=0) ---
(3, 0)

--- External Reading (n=3) ---
(6, 6)

--- Mixed Reading (n=1) ---
(4, 2)
```

***

## Author｜作者

Maggie (Nientzu) Lin
National Yang Ming Chiao Tung University — Foreign Languages and Literatures
