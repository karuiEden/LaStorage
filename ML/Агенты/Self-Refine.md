---
title: Self-Refine
created: 2026-10-01
tags:
  - ml
  - llm
links:
  - "[[Агент]]"
  - "[[LLM]]"
---
**Определение:** *Self-Refine* - алгоритм улучшения результата LLM с использованием одной модели, которая дает обратную связь по ответу и улучшает на её основе свой ответ. Заканчивается алгоритм при достижения количества итераций или выполнения какого-то условия.

```pseudo
\begin{algorithm}
\caption{Self-Refine algorithm}
\begin{algorithmic}
\Require input $x$, model $\mathcal{M}$, prompts $\{p_{\text{gen}}, p_{\text{fb}}, p_{\text{refine}}\}$, stop condition $\text{stop}(\cdot)$

\State $y_0 \gets \mathcal{M}(p_{\text{gen}} \| x)$ \Comment{Initial generation (Eqn.~1)}
\For{iteration $t \in 0, 1, \dots$}
    \State $fb_t \gets \mathcal{M}(p_{\text{fb}} \| x \| y_t)$ \Comment{Feedback (Eqn.~2)}
    \If{$\text{stop}(fb_t, t)$}
        \State break \Comment{Stop condition}
    \Else
        \State $y_{t+1} \gets \mathcal{M}(p_{\text{refine}} \| x \| y_0 \| fb_0 \| \dots \| y_t \| fb_t)$ \Comment{Refine (Eqn.~4)}
    \EndIf
\EndFor
\State \Return $y_t$
\end{algorithmic}
\end{algorithm}
```
## Таблица результатов

| Task                   | GPT-3.5 Base | GPT-3.5 +SELF-REFINE | ChatGPT Base | ChatGPT +SELF-REFINE | GPT-4 Base | GPT-4 +SELF-REFINE |
| ---------------------- | ------------ | -------------------- | ------------ | -------------------- | ---------- | ------------------ |
| Sentiment Reversal     | 8.8          | **30.4** (↑21.6)     | 11.4         | **43.2** (↑31.8)     | 3.8        | **36.2** (↑32.4)   |
| Dialogue Response      | 36.4         | **63.6** (↑27.2)     | 40.1         | **59.9** (↑19.8)     | 25.4       | **74.6** (↑49.2)   |
| Code Optimization      | 14.8         | **23.0** (↑8.2)      | 23.9         | **27.5** (↑3.6)      | 27.3       | **36.0** (↑8.7)    |
| Code Readability       | 37.4         | **51.3** (↑13.9)     | 27.7         | **63.1** (↑35.4)     | 27.4       | **56.2** (↑28.8)   |
| Math Reasoning         | **64.1**     | **64.1** (0)         | 74.8         | **75.0** (↑0.2)      | 92.9       | **93.1** (↑0.2)    |
| Acronym Generation     | 41.6         | **56.4** (↑14.8)     | 27.2         | **37.2** (↑10.0)     | 30.4       | **56.0** (↑25.6)   |
| Constrained Generation | 28.0         | **37.0** (↑9.0)      | 44.0         | **67.0** (↑23.0)     | 15.0       | **45.0** (↑30.0)   |

Был разработан, чтобы локально улучшать результат выполнения задачи