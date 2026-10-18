---
title: Reflection
created: 2026-10-05
tags:
  - ml
  - agentic
links:
  - "[[Агент]]"
---
**Определение:** *Reflection* - архитектура агента, состоящая из трех моделей: Actor, Evaluator, Self-reflection. Actor генерирует нужный текст и действия в зависимостей от наблюдений состояния, Evaluator генерирует награду, которая отражает производительность исходя из траектории, а также Self-reflection, используя награду и траекторию генерирует обратную связь, которая поможет действовать агенту лучше в будущих задачах.


![[Pasted image 20261005150526.png]]

```pseudo
\begin{algorithm}
\caption{Reinforcement via self-reflection}
\begin{algorithmic}

\State Initialize Actor, Evaluator, Self-Reflection:
\State $M_a, M_e, M_{sr}$

\State Initialize policy
\State $\pi_\theta(a_i \mid s_i), \quad \theta = \{M_a, mem\}$

\State Generate initial trajectory using $\pi_\theta$
\State Evaluate $\tau_0$ using $M_e$
\State Generate initial self-reflection $sr_0$ using $M_{sr}$

\State $mem \gets [sr_0]$
\State $t \gets 0$

\While{$M_e$ does not pass \textbf{and} $t < max\_trials$}
  \State Generate $\tau_t = [a_0, o_0, \ldots, a_i, o_i]$ using $\pi_\theta$
  \State Evaluate $\tau_t$ using $M_e$
  \State Generate self-reflection $sr_t$ using $M_{sr}$
  \State Append $sr_t$ to $mem$
  \State $t \gets t + 1$
\EndWhile

\end{algorithmic}
\end{algorithm}
```

| Benchmark + Language | Prev SOTA Pass@1 | SOTA Pass@1 | Reflexion Pass@1 |
|---|---:|---:|---:|
| HumanEval (PY) | 65.8 (CodeT [5] + GPT-3.5) | 80.1 (GPT-4) | **91.0** |
| HumanEval (RS) | – | 60.0 (GPT-4) | **68.0** |
| MBPP (PY) | 67.7 (CodeT [5] + Codex [6]) | 80.1 (GPT-4) | **77.1** |
| MBPP (RS) | – | 70.9 (GPT-4) | **75.4** |
| Leetcode Hard (PY) | – | 7.5 (GPT-4) | **15.0** |