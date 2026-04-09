#include <vector>
#include <chrono>
#include <iostream>
#include <random>
#include <algorithm>

int main() {
    const size_t N = 25'000'000;  // 200 MB – safe on Jetson Orin Nano
    std::vector<double> v(N);

    // Sequential touch
    auto start = std::chrono::high_resolution_clock::now();
    for (auto& x : v) x = 1.0;
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "Sequential: " << std::chrono::duration<double>(end - start).count() << " s\n";

    // Random touch (shuffle indices to force cache misses)
    std::vector<size_t> idx(N);
    std::iota(idx.begin(), idx.end(), 0);
    std::shuffle(idx.begin(), idx.end(), std::mt19937{std::random_device{}()});
    start = std::chrono::high_resolution_clock::now();
    for (auto i : idx) v[i] = 2.0;
    end = std::chrono::high_resolution_clock::now();
    std::cout << "Random:     " << std::chrono::duration<double>(end - start).count() << " s\n";

    return 0;
}
