# Dicionário de Palavras Reservadas de Python

## print (imprimir/escrever)

**Linguagem natural**
```
escreva: "Ensine coragem às meninas, não perfeição."
```

**Python**
```python
>>> print("Ensine coragem às meninas, não perfeição.")
Ensine coragem às meninas, não perfeição.
```

## if (se)

**Linguagem natural**
```
Se a pessoa é uma mulher, então, 
um homem não te define, 
sua casa não te define, 
sua carne não te define,
você é seu próprio lar.
```
**Python**
```python
>>> pessoa = "Mulher"
>>> if(pessoa == "Mulher"):
...     print("Um homem não te define")
...     print("Sua casa não te define")
...     print("Sua carne não te define") 
...     print("Você é seu próprio lar")
... 
Um homem não te define
Sua casa não te define
Sua carne não te define
Você é seu próprio lar
```

## else (senão)

**Linguagem natural**
```
Se mexeu com uma for verdadeiro, 
escreva: "Mexeu com todas".
Senão,
escreva: "Vamos nos empoderar mesmo assim".
```
**Python**
```python
>>> mexeu_com_uma = False
>>> if(mexeu_com_uma == True):
...     print("Mexeu com todas")
... else:
...     print("Vamos nos empoderar mesmo assim.")
... 
Vamos nos empoderar mesmo assim.
```

## while (enquanto)

**Linguagem natural**
```
enquanto o número de mulheres for diferente do número de homens, 
escreva: "precisamos de mais empoderamento".
```
**Python**
```python
>>> numero_mulheres = 0
>>> numero_homens = 100
>>> while(numero_mulheres != numero_homens):
...     print("precisamos de mais empoderamento.")
...     break
... 
precisamos de mais empoderamento.
```

## for (para)

**Linguagem natural**
```
Para cada mulher em uma lista de mulheres,
escreva "Essa mulher é uma inspiração!"
```
**Python**
```python
>>> mulheres = ["Sil Bahia", "Camila Achutti", "Buh D'Angelo"]
>>> for mulher in mulheres:
...     print(mulher, "é uma inspiração!")
... 
Sil Bahia é uma inspiração!
Camila Achutti é uma inspiração!
Buh D Angelo é uma inspiração!
```

___

Os exemplos deste material foram retirados/adaptados do [Manifesto literário Poesia Compilada](http://poesiacompilada.com/).