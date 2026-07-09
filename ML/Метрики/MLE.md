---
title: MLE
created: 2025-11-10
tags:
  - nlp
links:
---
**Определение:** Оценка максимального правдоподобия(Maximum Likehood Estimation) для $N$-грамной языковой модели равно
$$
P(w_{n}\ | \ w_{n-N+1:n-1})= \frac{C(w_{n-N+1:n-1},w_{n})}{C(w_{n-N+1:n-1})} 
$$