def top_three(s):
    counts = {}
    for ch in s:
        num = int(ch)
        counts[num] = counts.get(num, 0) + 1

    top3 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]

    top3_dict = dict(top3)

    top3_dict = dict(sorted(top3_dict.items()))

    return top3_dict

s = "1255539071595973019405391"
result = top_three(s)
print(result)
