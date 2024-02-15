n = int(input())
matrices = []

for n in range(0, n):
    matrix = input()
    matrices.append(matrix.split(','))

def best_performance(matrices):
  
  best_index = 0
  best_accuracy = 0
  best_precision = 0
  for index, matrix in enumerate(matrices):
    # Ensure valid integers representing confusion matrix values
    tp, fp, fn, tn = [int(value) for value in matrix]
    accuracy = round((tp + tn) / (tp + fp + fn + tn),2)
    precision = round(tp / (tp + fp),2)
    if accuracy > best_accuracy:
      best_accuracy = accuracy
      best_index = index + 1
      best_precision = precision

  return  f'Index: {best_index}\nAccuracy: {best_accuracy}\nPrecision: {best_precision}'

print(best_performance(matrices))
