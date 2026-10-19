---
title: RMSNorm
created: 2026-10-13
tags:
  - ml
  - deep_learning
  - normalization
links:
---
**Определение:** **RMSNorm** — метод нормализации активаций нейросети.

Основная идея: **отказаться от центрирования активаций (re-centering), сохранив нормализацию масштаба (re-scaling)**.

## Формула

Пусть $x\in\mathbb R^H$ — вектор активаций, где $H$ — количество признаков (_hidden size_).

Среднеквадратичное значение:

$$  
\operatorname{RMS}(x)=\sqrt{\frac1H\sum_{i=1}^{H}x_i^2}  
$$

Нормализация:

$$  
\boxed{  
\operatorname{RMSNorm}(x)_i=  
\gamma_i\frac{x_i}{\sqrt{\frac1H\sum_{j=1}^{H}x_j^2+\varepsilon}}  
}  
$$

Где:

- $H$ — размерность нормализуемого вектора;
    
- $\gamma_i$ — обучаемый коэффициент масштабирования;
    
- $\varepsilon$ — константа численной устойчивости.
    

В отличие от LayerNorm, RMSNorm не вычитает среднее $\mu$ и обычно не использует обучаемый сдвиг $\beta$.

## Математические свойства

**1. Инвариантность к масштабированию (re-scaling invariance)**

При $\varepsilon=0$ и $c>0$:

$$  
\operatorname{RMSNorm}(cx)=\operatorname{RMSNorm}(x)  
$$

Это следует из однородности евклидовой нормы:

$$  
\operatorname{RMS}(cx)=|c|\operatorname{RMS}(x)  
$$

Инвариантность выполняется при масштабировании **всего вектора одним коэффициентом**, но в общем случае не отдельных компонент.

**2. Отсутствие инвариантности к сдвигу (re-centering invariance)**

В общем случае:

$$  
\operatorname{RMSNorm}(x+c\mathbf{1})\neq\operatorname{RMSNorm}(x)  
$$

RMSNorm не гарантирует нулевое среднее нормализованных активаций.

**3. Геометрическая интерпретация**

При $\varepsilon=0$ и до применения $\gamma$:

$$  
\operatorname{RMSNorm}(x)=\sqrt H\frac{x}{|x|_2}  
$$

Таким образом, нормализация сохраняет направление вектора и приводит его евклидову норму к $\sqrt H$.