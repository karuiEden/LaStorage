---
title: TF-IDF
created: 2026-09-26
tags:
  - ml
  - nlp
links:
---
**Определение:** **TF-IDF (Term Frequency–Inverse Document Frequency)** - способ взвешивания слов, который повышает значимость редких для корпуса слов и снижает вес слишком частых.

Пусть $\mathcal{D}=\{ d_{1},\dots,d_{N} \}$ - корпус из $N$ документов. Для произвольного терма (слова) $t$ обозначим:
$n_{t,d}$ - число вхождений терма $t$ в документ $d$.
$n_{t}$ - число документов, в которых терм $t$ входит хотя бы один раз, $n_{t}=|d \in \mathcal{D}: n_{t,d}>0|$.

Тогда
$$
\mathrm{TF}(t,d)=n_{t,d}, \ \mathrm{TF}_{Norm}(t,d)= \frac{n_{t,d}}{\sum_{t'}n_{t',d}}
$$
$$
P(t)\approx \frac{n_{t}}{N}; \ \ \mathrm{IDF}(t)=-\log P(t)=-\log \frac{n_{t}}{N}=\log \frac{N}{n_{t}}.
$$
$$
w_{t,d}=\mathrm{TF}(t,d)\cdot \mathrm{IDF}(t).
$$
