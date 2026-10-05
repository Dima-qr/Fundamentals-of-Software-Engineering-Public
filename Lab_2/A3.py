import sys

bytes_given = 1921000
mb_calculated = bytes_given / (1024 * 1024)
print(mb_calculated)

huge_number = 3 ** 9090001
real_bytes = sys.getsizeof(huge_number)
real_mb = real_bytes / (1024 * 1024)
print(real_mb)
