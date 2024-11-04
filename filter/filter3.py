animals = {"pato", "águia", "galinha", "avestruz", "pinguim", "morcego", "ornitorrinco", "leão", "gato", "onça pintada", "baleia", "tubarão", "lambari", "enguia", "arraia"}
caracteristicas_animais = {
    "patas": {
        "bípede": ["pinguim", "morcego", "ornitorrinco"],
        "quadrúpede": ["gato", "leão"],
        "mais de quatro patas": ["galinha", "avestruz"],
    },
    "habitat": {
        "aquático": ["baleia", "tubarão", "arraia", "pinguim"],
        "terrestre": ["gato", "leão", "galinha", "avestruz", "morcego", "ornitorrinco"],
        "anfíbio": ["morcego", "ornitorrinco"],
    },
    "penas": {
        "possui penas": ["pato", "águia", "galinha", "avestruz", "pinguim"],
        "não possui penas": ["morcego", "ornitorrinco", "leão", "gato", "baleia", "tubarão", "lambari", "enguia", "arraia"],
    }
}
answerFinalOne = []
answerFinalTwo = []
answerFinalThree = []
answerOne = int(input("O animal que você está pensando é bípede[1], quadrúpede[2] ou possui mais de quatro patas[3]. Respoda 1,2 ou 3 para as respectivas respostas?"))
answerTwo = int(input("O animal que você está pensando possui penas[1] ou não possui penas[2]. Respoda 1 ou 2 para as respectivas respostas?"))
answerThree = int(input("O animal que você está pensando é aquático[1], terrestre[2] ou anfíbio[3]. Respoda 1,2 ou 3 para as respectivas respostas?"))
if answerOne == 1:
  answerFinalOne = ["pinguim", "morcego", "ornitorrinco"]
elif answerOne == 2:
  answerFinalOne = ["gato", "leão"]
else:
  answerFinal = ["galinha", "avestruz"]
if answerTwo == 1:
  answerFinalTwo = ["pato", "águia", "galinha", "avestruz", "pinguim"]
else:
  answerFinalTwo = ["morcego", "ornitorrinco", "leão", "gato", "baleia", "tubarão", "lambari", "enguia", "arraia"]
if answerThree == 1:
  answerFinalThree = ["baleia", "tubarão", "arraia", "pinguim"]
elif answerThree == 2:
  answerFinalThree = ["gato", "leão", "galinha", "avestruz", "morcego", "ornitorrinco"]
else:
  answerFinalThree = ["morcego", "ornitorrinco"]
print(set(answerFinalOne) & set(answerFinalTwo) & set(answerFinalThree))
