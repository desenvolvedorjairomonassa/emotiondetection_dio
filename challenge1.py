input_str = input()
pairs = input_str.split(",")
# TODO: Split the input into a list of strings and convert it to a new list of integers

# TODO: Define a function to analyze the predominant emotion based on the list of integers representing the intensity and a list of strings representing the emotions
def analyze_emotion(facial_features):
    indice_maior_valor = facial_features.index(max(facial_features))
    emotions = ["Anger", "Happiness", "Sadness", "Surprise"]
    return emotions[indice_maior_valor]

print(analyze_emotion(pairs))
