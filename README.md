# ContaBancaria.py
Exemplo de POO em Python com encapsulamento e herança

# ContaBancaria

Exemplo de Programação Orientada a Objetos em Python, com encapsulamento e herança.

## Exemplo de uso

```python
from ContaBancaria import ContaUniversitaria

conta = ContaUniversitaria("Danillo", 100)
conta.depositar(50)
conta.sacar(30)
conta.mostrar_info()
```

## Saída esperada

```
Depósito de R$50 realizado com sucesso.
Saque de R$30 realizado com sucesso.
Titular: Danillo
Saldo: R$120
Taxa de manutenção: R$0
```
