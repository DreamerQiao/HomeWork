def mean(data):
    if not data:
        raise ValueError("data must not be empty")
    return sum(data) / len(data)


def median(data):
    if not data:
        raise ValueError("data must not be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def variance(data):
    if not data:
        raise ValueError("data must not be empty")
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def std_dev(data):
    return variance(data) ** 0.5


def analyze(data):
    if not data:
        raise ValueError("data must not be empty")
    return {
        "count": len(data),
        "mean": mean(data),
        "median": median(data),
        "variance": variance(data),
        "std_dev": std_dev(data),
        "min": min(data),
        "max": max(data),
    }


def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    data = fibonacci(10)
    print("Fibonacci sequence:", data)
    stats = analyze(data)
    for key, value in stats.items():
        print(f"  {key}: {value}")
