cash = float(input())

print('NOTAS:')
print(f"{cash//100:.0f} nota(s) de R$ 100.00")
cash %= 100
print(f"{cash//50:.0f} nota(s) de R$ 50.00")
cash %= 50
print(f"{cash//20:.0f} nota(s) de R$ 20.00")
cash %= 20
print(f"{cash//10:.0f} nota(s) de R$ 10.00")
cash %= 10
print(f"{cash//5:.0f} nota(s) de R$ 5.00")
cash %= 5
print(f"{cash//2:.0f} nota(s) de R$ 2.00")
cash %= 2

print('MOEDAS:')
print(f"{cash//1:.0f} moeda(s) de R$ 1.00")
cash %= 1
print(f"{cash//0.50:.0f} moeda(s) de R$ 0.50")
cash %= 0.50
print(f"{cash//0.25:.0f} moeda(s) de R$ 0.25")
cash %= 0.25
print(f"{cash//0.10:.0f} moeda(s) de R$ 0.10")
cash %= 0.10
print(f"{cash//0.05:.0f} moeda(s) de R$ 0.05")
cash %= 0.05
cash *= 100
print(f"{cash:.0f} moeda(s) de R$ 0.01")