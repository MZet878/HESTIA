def calfp(frates, fac_rate):
    wt_factors = [
        [3, 4, 6],
        [4, 5, 7],
        [3, 4, 6],
        [7, 10, 15],
        [5, 7, 10],
    ]

    UFP = 0
    for i in range(5):
        for j in range(3):
            UFP += frates[i][j] * wt_factors[i][j]

    sumF = fac_rate * 14
    CAF = 0.65 + 0.01 * sumF
    FP = UFP * CAF

    print("Function Point Analysis :-")
    print(f"Unadjusted Function Points (UFP) : {UFP}")
    print(f"Complexity Adjustment Factor (CAF) : {CAF}")
    print(f"Function Points (FP) : {FP}")


frates = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 3, 0],
    [0, 1, 0],
    [0, 3, 0],
]
fac_rate = 2
calfp(frates, fac_rate)
