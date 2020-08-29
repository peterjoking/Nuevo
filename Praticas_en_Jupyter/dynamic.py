store_results={}
def sum_to_n(n):
    result =0
    for i in reversed(range(n)):
        result += i + 1
    stored_results[n] = result
    return result