# Aceleração Internacional - Implementing Artificial Intelligence for Emotion Detection
------
-----


challenge 1
----------

Challenge
An institution decided to conduct research involving virtual assistants with the ability to identify people's emotions through their facial expressions, aiming to determine the most appropriate customer service approach based on their emotion. In this scenario, it was decided to develop a program that categorizes people's emotions based on this simplified facial analysis. Your task is to create a function that receives a list with the intensity of each facial feature of a person and returns the predominant emotion without using external libraries.

Input
The input will be a string with 4 numbers separated by commas (,) representing the intensity of 4 distinct emotions, where each index in this list represents, respectively, the emotions: Anger, Happiness, Sadness, and Surprise.

Output
The expected output is the name of the predominant emotion.


challenge 2
--------

Challenge
You are part of a development team at a financial institution. Recently, the team was given the important task of improving the fraud detection system in financial transactions. To do this, it is necessary to develop an algorithm, without the use of libraries, capable of identifying suspicious patterns in bank transactions equal to or greater than the corresponding fraud limit for that account.

Input
The input consists of: n, which corresponds to the number of transactions to be analyzed, followed by lists referring to the transactions, each consisting of three values: an id, the transaction value and the fraud threshold value.

Output
The expected output is the ids of the suspicious transactions.

challenge 3
-----------

Challenge
You are part of a team that is developing Machine Learning models to identify the probability of default on loans granted by a financial institution. After training the models, your task is to evaluate their performance using some evaluation metrics. In this context, the challenge is to create an algorithm that receives n confusion matrices and should return the index, accuracy, and precision of the matrix that performs best based on the calculation of these metrics. Remembering that:

• Accuracy is calculated by the formula: (TP + TN) / (TP + FP + FN + TN)
• Precision is calculated by the formula: TP / (TP + FP)

Where:

• TP (True Positive): Cases where the model correctly predicted the positive class.
• FP (False Positive or Type I Error): Cases where the model incorrectly predicted the positive class.
• FN (False Negative or Type II Error): Cases where the model incorrectly predicted the negative class.
• TN (True Negative): Cases where the model correctly predicted the negative class.

Input
The input consists of a string composed of: n, representing the number of confusion matrices, followed by the values that make up the n matrices.

Each matrix consists of four values, where the first two represent the first row of the matrix, composed of true positives (TP) and false positives (FP); the last two values represent the second row, which is formed by false negatives (FN) and true negatives (TN). The two rows and the values that compose them are separated by commas.

Output
The expected outcome includes the index value, accuracy, and precision (rounded to two decimal place) of the best-performing matrix based on the calculation of these metrics.



