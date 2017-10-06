origin_str = 'qwer'
codes = list(filter(lambda item: item > 50, map(ord, origin_str)))
print(codes)
