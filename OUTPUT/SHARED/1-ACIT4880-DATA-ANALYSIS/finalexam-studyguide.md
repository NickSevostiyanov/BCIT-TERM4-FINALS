# ACIT4880 — Final Exam Study Guide
> 60 min | Multiple choice + T/F | DTC 825 | April 20, 2026 @ 9:30 AM
> **Scope: Assume cumulative. Heavy focus on post-midterm ML content (Quiz 3 = "everything since mid-term, i.e. machine learning").**

---

## 1. NumPy Essentials

| Concept | Key Facts |
|---------|-----------|
| `arr = np.array([...])` | Homogeneous — all same type |
| `arr2 = arr1` | **Reference copy** — modifying arr2 ALSO modifies arr1 |
| `arr2 = arr1.copy()` | True independent copy |
| `arr[1:4]` | Returns indices 1, 2, 3 (NOT 4 — upper bound exclusive) |
| `arr[:, 1]` | All rows, column index 1 (2nd column) |
| `arr.reshape(r, c)` | Changes shape without changing data |
| `np.mean()` | Mean. NOT `np.avg()` |
| Element-wise ops | `arr1 + arr2` works without loops |
| Memory efficiency | NumPy arrays >> Python lists for numerics |

---

## 2. Pandas Essentials

| Concept | Key Facts |
|---------|-----------|
| `df.shape` | Returns **(rows, columns)** — tuple. TRUE. |
| `df.head()` | Returns first **5** rows by default (NOT 10) |
| `df.describe()` | Stats for numeric columns; **excludes NaN/None** — does NOT replace with 0 |
| `df.iloc[2:5, 1:3]` | Rows 2–4, columns 1–2 (exclusive upper bound) |
| `df.loc` | **Label-based** indexing |
| `df.iloc` | **Integer position** based (NOT label-based) |
| `df["Age"]` or `df.Age` or `df.loc[:, "Age"]` | All select column "Age" |
| `df.iloc[:, -1]` | Last column |
| `df.drop('col', inplace=True)` | Permanent change |
| `df.sort_values('col', inplace=True)` | Permanent change |
| `df.sort_values('col')` | Returns new df — does NOT modify original |
| **Series vs Array** | Series has an index, can hold mixed types; NumPy arrays are homogeneous |

---

## 3. Data Preprocessing & EDA

### Missing Values
- **GIGO** = Garbage In, Garbage Out — bad data → bad models
- Never always discard datasets with missing values — **impute instead**
- **Mean imputation**: simple, but **introduces bias** — distorts measures of spread
- **Median imputation**: better for skewed data
- **Random sample imputation**: preserves distribution
- **KNN imputation**: smart but expensive
- **Multiple imputation**: least biased overall
- Types of missingness: MCAR (Missing Completely At Random), MAR, MNAR

### Outliers
- NOT always errors — can be valid data points
- **Do NOT always remove** — context matters
- Effect: skews distribution, destabilizes statistical methods
- Graphical detection: **histogram**, box plot (NOT mean calculation alone)
- Z-score normalization: subtract mean, divide by std dev

### Data Transformation
- **Normalization (Min-Max)**: scales to [0,1]
- **Standardization (Z-score)**: mean=0, std=1
- **Log transformation**: best for highly skewed data (stabilizes variance)
- **Square root, inverse, log**: ALL stabilize variance / normalize distribution
- For highly skewed data → **logarithmic transformation** is most appropriate

### EDA
- Purpose: uncover patterns, relationships, interrelationships between features
- EDA is for: developing initial ideas of associations, examining interrelationships, identifying subsets
- EDA does **NOT** test specific statistical hypotheses (that's inferential stats)
- Visual tools: graphs/plots help uncover patterns — NOT just for presentation
- Dimensionality reduction: **reduces** features (not increases)

### Feature Selection
- **Constant features**: same value for all rows — drop them
- **Quasi-constant**: >99% same value — drop
- **Correlation**: highly correlated features = redundant; drop one
- **Chi-square**: categorical features vs target
- **Mutual information**: non-linear relationships

---

## 4. Supervised Learning — Regression

### Linear Regression
- Predict continuous values
- **Evaluation Metrics:**
  - **MAE** (Mean Absolute Error): average of absolute errors
  - **MSE** (Mean Squared Error): penalizes large errors more
  - **RMSE** (Root MSE): same units as target
  - **R²** (Coefficient of Determination): 1 = perfect, 0 = baseline. Can be negative (worse than baseline)

### Train/Test Split
- Typical: 80/20 or 70/30
- **Cross-validation (k-fold)**: splits data k times, averages performance — more robust

---

## 5. Supervised Learning — Classification

### Confusion Matrix
| | Predicted Positive | Predicted Negative |
|--|--|--|
| **Actual Positive** | TP | FN |
| **Actual Negative** | FP | TN |

- **Accuracy** = (TP + TN) / total — misleading on imbalanced data
- **Precision** = TP / (TP + FP) — of all predicted positive, how many were right
- **Recall (Sensitivity)** = TP / (TP + FN) — of all actual positives, how many caught
- **F1 Score** = 2 × (Precision × Recall) / (Precision + Recall) — harmonic mean
- Use F1 / Recall when classes are imbalanced

### kNN (k-Nearest Neighbors)
- Non-parametric, lazy learner (no training phase)
- Classifies based on majority vote of k nearest neighbors
- Distance: Euclidean (default), Manhattan
- **Low k**: overfitting (too sensitive to noise)
- **High k**: underfitting (too smooth)
- **Curse of dimensionality**: performance degrades with many features
- Feature scaling required (distance-sensitive)

### SVM (Support Vector Machine)
- Finds **optimal hyperplane** that maximizes margin between classes
- **Support vectors**: data points closest to hyperplane
- **Kernel trick**: maps data to higher dimensions (RBF, polynomial, linear)
- **Soft margin (C parameter)**: allows some misclassifications — prevents overfitting
- Works well in high dimensions

### Decision Trees
- Splits data using **information gain** (entropy-based) or **Gini impurity**
- **Entropy** = measure of impurity/disorder
- **Information gain** = reduction in entropy after split
- **Gini impurity** = probability of misclassifying randomly chosen element
- Prone to **overfitting** — combat with pruning or max_depth
- Interpretable — human-readable rules

### Random Forest
- **Ensemble** of decision trees using **bagging** (Bootstrap Aggregating)
- Each tree trained on random subset of data AND features
- Final prediction = majority vote (classification) or average (regression)
- More robust than single tree — reduces overfitting
- Provides **feature importance** scores
- Less interpretable than single tree

---

## 6. Model Tuning

### Hyperparameter Tuning
- **GridSearchCV**: tries all combinations of parameter grid — exhaustive
- **RandomizedSearchCV**: random subset of combinations — faster
- **Cross-validation** used inside GridSearchCV (cv=5 means 5-fold)

### Bias-Variance Tradeoff
- **High bias (underfitting)**: model too simple, poor on train AND test
- **High variance (overfitting)**: model memorizes training data, poor on test
- Goal: find sweet spot

### Imbalanced Data
- Accuracy is misleading — 90/10 split, always predict majority = 90% accuracy
- Solutions:
  - **SMOTE** (Synthetic Minority Oversampling Technique): generates synthetic samples
  - **Undersampling**: remove majority class samples
  - **Class weights**: penalize misclassification of minority more (e.g., `class_weight='balanced'`)
  - Use **F1, Recall, AUC-ROC** instead of accuracy

---

## 7. Unsupervised Learning

### K-Means Clustering
- Partitions data into **k clusters** based on centroid proximity
- **Algorithm:**
  1. Initialize k centroids (randomly)
  2. Assign each point to nearest centroid
  3. Recompute centroids
  4. Repeat until convergence
- **Elbow Method**: plot inertia (WCSS) vs k — pick the "elbow" point
- **Inertia**: sum of squared distances from each point to its centroid (lower = tighter)
- Sensitive to: initial centroid placement, outliers, feature scale

### Hierarchical Clustering
- Builds a **dendrogram** (tree structure)
- **Agglomerative** (bottom-up): each point starts as own cluster, merge up
- **Divisive** (top-down): start as one cluster, split down
- **Linkage methods:**
  - Single: distance between closest points
  - Complete: distance between farthest points
  - Average: average of all pairwise distances
  - Ward: minimizes variance (most common)
- Cut dendrogram at desired number of clusters
- No need to specify k upfront

---

## 8. Quick-Fire Tricky Topics (Common Mistakes)

| Statement | Answer |
|-----------|--------|
| `df.head()` returns 10 rows by default | **FALSE** — returns 5 |
| `iloc` is label-based | **FALSE** — it's integer position-based |
| Outliers should always be removed | **FALSE** — context-dependent |
| Mean substitution doesn't affect measures of spread | **FALSE** — it does affect spread |
| Dimensionality reduction increases features | **FALSE** — reduces them |
| Histogram is a graphical method for detecting outliers | **TRUE** |
| Z-score subtracts mean and divides by std | **TRUE** |
| GIGO = Garbage In, Garbage Out | **TRUE** |
| Supervised learning target = dependent variable | **TRUE** |
| All variance-stabilizing transforms: log, sqrt, inverse | **TRUE — all of the above** |
| `arr2 = arr1` creates independent copy | **FALSE** — reference copy |
| `df.describe()` includes NaN in calculations | **FALSE** — excludes NaN |
| EDA tests specific statistical hypotheses | **FALSE** |
| Mode is a measure of center | **TRUE** (mean, median, mode all are) |
| Bars are same-sized in normalized charts | **TRUE** |
| Mean imputation is most susceptible to introducing bias | **TRUE** |
| Log transformation is best for highly skewed data | **TRUE** |
| Target variable = dependent variable | **TRUE** |

---

## 9. Exam Tips

- **60 minutes** — don't dwell on any one question
- Watch for "NOT", "ALWAYS", "NEVER" in questions — these are usually traps
- "All of the above" is frequently correct in this course (Quiz 1 Q11, Quiz 2 Q17, Q20)
- `inplace=True` = permanent modification — key concept tested
- Know the difference between `loc` (label) vs `iloc` (integer position)
- For classification problems: **dependent variable = target variable**
- Random Forest > Decision Tree for robustness (less overfitting)
- kNN requires **feature scaling** — it's distance-based
