# ⚡ Advanced Algorithm Design: Divide-and-Conquer Maximum Subarray & Dynamic Dijkstra

Clean Python implementations of classic and dynamic optimization algorithms with step-by-step trace outputs and asymptotic complexity guarantees.

---

## 📌 Implemented Algorithms

### 1. Divide-and-Conquer Maximum Subarray (`Maximum Subarray Algorithm.py`)
- Solves the Maximum Contiguous Subarray problem in $O(n \log n)$ time by recursively partitioning the array and computing the optimal midpoint-crossing subarray.

### 2. Dynamic Single-Source Shortest Path (`Dynamic Shortest Path.py`)
- Implements a **Dynamic Graph Shortest-Path Tree (SPT)** engine on top of Dijkstra's algorithm that handles live edge mutations without recomputing the entire graph from scratch:
  - **`insert_edge(u, v, w)`**: Checks if $d(u) + w < d(v)$ and propagates shortest-path improvements only to affected downstream vertices.
  - **`delete_edge_dynamic(u, v)`**: Checks if $(u, v)$ belongs to the active Shortest-Path Tree (`parent[v] == u`) and selectively invalidates/recomputes only the affected subgraph.
  - **`update_weight_dynamic(u, v, new_w)`**: Dynamically handles both edge weight decreases (localized relaxation) and increases (partial SPT reconstruction).

---

## 🚀 Usage

```bash
python "Maximum Subarray Algorithm.py"
python "Dynamic Shortest Path.py"
```
