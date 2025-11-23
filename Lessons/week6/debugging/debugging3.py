numbers = [1, 2, 3, 4, 5, 6]
even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers: ", even_count)
print("Odd numbers: ", odd_count)
if even_count > odd_count:
    print("More odds than evens!")
elif even_count == odd_count:
    print("Same amount of evens and odds")
else:
    print("More evens than odds!")