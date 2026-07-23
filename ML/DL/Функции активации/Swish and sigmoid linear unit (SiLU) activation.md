---
title: Swish and sigmoid linear unit (SiLU) activation
created: 2026-07-23
tags:
  - deep_learning
links:
  - "[[Функция активации]]"
---
**Определение:** Пусть $\beta \in \mathbb{R}$. $a(x)$ - swish activation с параметром $\beta$, если
$$
a(x)= \frac{x}{1+\exp(-\beta x)}.
$$


```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  width=8cm,height=5cm,
  xmin=-6,xmax=6,
  ymin=-1.5,ymax=6,
  xlabel={$x$},ylabel={$f(x)$},
  samples=150,
  domain=-6:6
]
\def\beta{2.0}
\addplot[thick] {x/(1+exp(-\beta*x))};
\end{axis}
\end{tikzpicture}
\end{document}
```

**Определение:** $a(x)$ - SiLU функция активации, если
$$
a(x)= \frac{x}{1+\exp(-x)}
$$

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  width=8cm,height=5cm,
  xmin=-6,xmax=6,
  ymin=-1.5,ymax=6,
  xlabel={$x$},ylabel={$f(x)$},
  samples=150,
  domain=-6:6
]
\addplot[thick] {x/(1+exp(-x))};
\end{axis}
\end{tikzpicture}
\end{document}
```

**Лемма:** При $\beta$ swish активация и SiLU совпадают.

