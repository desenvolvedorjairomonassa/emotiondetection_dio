n = int(input())
lines = []

for n in range(0, n):
    lines.append(input())

def detect_frauds(transactions):
  suspicious_transactions = []
  for transaction in transactions:
    evaluation = transaction.split(',')
    if  int(evaluation[1])>= int(evaluation[2]):
      suspicious_transactions.append(evaluation[0])

  #return suspicious_transactions
  return '\n'.join(suspicious_transactions)

print(detect_frauds(lines))
