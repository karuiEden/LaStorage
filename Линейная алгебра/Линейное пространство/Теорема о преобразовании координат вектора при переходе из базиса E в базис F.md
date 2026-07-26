---
title: Теорема о преобразовании координат вектора при переходе из базиса E в базис F
created: 2025-06-03
tags:
  - linear-algebra
links:
  - "[[Матрица перехода от одного базиса к другому]]"
  - "[[Базис пространства]]"
---
**Теорема:** Пусть $\forall x\in V$ задан своими координатами:
- в базисе $E:x=(\alpha_{1}\dots\alpha_{n})=\alpha_{1}e_{1}+\dots+\alpha_{n}e_{n}=(e)\bar{\alpha}$ 
- в базисе $F:x=(\beta_{1}\dots\beta_{n})=\beta_{1}f_{1}+\dots+\beta_{n}f_{n}=(f)\bar{\beta}$
Тогда справедливо равенство:
$$\bar{\beta}=\begin{pmatrix}
\beta_{1} \\
\vdots \\
\beta_{n}
\end{pmatrix}=T^{-1}\cdot \begin{pmatrix}
\alpha_{1} \\
\vdots \\
\alpha_{n}
\end{pmatrix}= T^{-1} \bar{\alpha}$$
