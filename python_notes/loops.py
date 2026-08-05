'''countdown = 3

# Runs as long as countdown is greater than 0
while countdown > 0:
    print(f"T-minus {countdown}")
    countdown -= 1  # Crucial: decreases countdown by 1 each time

print("Blast off! 🚀")'''

'''
print("--- Testing Break ---")
for num in range(1, 6):
    if num == 4:
        break  # Stops the loop completely when num hits 4
    print(num)

print("--- Testing Continue ---")
for num in range(1, 6):
    if num == 3:
        continue  # Skips printing 3 and goes to 4
    print(num)
'''

for item in [1, 2, 3]:
    print(f"Item {item}")
else:
    print("Loop finished normally without interruption!")

