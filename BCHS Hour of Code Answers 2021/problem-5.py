layers = int(input("How many layers? "))
for layer in range(0, layers):
    print(" " * (layers - 1 - layer) + "*" * (1 + 2 * layer))
for trunk in range(0, 1 + int(layer / 2)):
    print(" " * (layers - 1) + "|")
