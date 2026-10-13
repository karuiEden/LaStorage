---
title: Group Query Attention
created: 2026-10-12
tags:
  - ml
  - deep_learning
  - attention
links:
  - "[[Attention]]"
  - "[[Multi-head Attention]]"
  - "[[Multi-Query Attention]]"
---
**Определение:** Group Query Attention - механизм attention, который является гибридом MQA и MHA. Он обладает скоростью, сравнимой с MQA, но при этом не сильно уступает MHA.

Возникновение связано из-за того, что MQA хоть и сильно увеличивал скорость генерации токенов, но сильно ухудшал качество генерации.