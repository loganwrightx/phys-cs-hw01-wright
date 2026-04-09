# Derivation of the Efficiency of my Gravitational Force Function

The efficiency of the naive solution to the problem of computing gravitational forces for every pair interaction can be depicted by the worst-case scenario–every pair interacts equally and no pairs can be omitted.

Using this worst case, we can see that _every_ mass must be evaluated once against _every_ other mass in space (except for itself). Using a double for-loop over the same mass array, we can see that we iterate over $N^2$ interactions. Technically, we actually only perform the force calculation $N \cdot (N - 1)$ times since masses don't interact with themselves, gravitationally. However as we evaluate that expression in the limit as N approaches infinity, the $N^2$ term grows _much_ faster than the $N$ term ($N \cdot (N - 1) = N^2 - N$).

According to the laws of physics, a nice optimization may be made by using Newton's Third Law–every action has an equal and opposite reaction experienced by the other mass in space ($\vec{F}_{a,b} = -\vec{F}_{b,a}$. In a future development, this would reduce time complexity from $O(N^2)$ to $O(\sum_{k=1}^{k=N-1} (N-k))$.
