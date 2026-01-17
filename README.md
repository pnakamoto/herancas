# 🐍 Projeto Python – Programação Orientada a Objetos (POO)

Este projeto demonstra conceitos fundamentais de **Programação Orientada a Objetos em Python**, incluindo:

* Herança simples e múltipla
* Uso de `super()` e **MRO (Method Resolution Order)**
* Mixins
* Sobrescrita de métodos (`__str__`)
* Encapsulamento de comportamento em classes

O código está dividido em **dois grandes exemplos**: um sistema de **Animais** e um sistema de **Veículos**.

---

## 📁 Estrutura do Projeto

```
├── animais.py   # Classes Animal, Mamífero, Ave, Ornitorrinco, etc.
├── veiculos.py  # Classes Veiculo, Carro, Moto e Caminhão
└── README.md
```

*(Os arquivos podem estar em um único script, mas a separação é recomendada.)*

---

## 🐾 Exemplo 1: Sistema de Animais

### 🔹 Classe `Animal`

Classe base que define atributos comuns:

* `nro_patas`
* Método `__str__` que imprime dinamicamente os atributos do objeto

```python
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
```

---

### 🔹 Classe `Mamifero`

Herda de `Animal` e adiciona:

* `cor_pelo`
* Uso de `**kw` para permitir herança múltipla cooperativa

```python
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
```

---

### 🔹 Classe `Ave`

Herda de `Animal` e adiciona:

* `cor_bico`

---

### 🔹 Classe `Gato`

Herança simples de `Mamifero`.

```python
class Gato(Mamifero):
    pass
```

---

### 🔹 Mixin `FalarMixin`

Mixin reutilizável que adiciona comportamento de fala:

```python
class FalarMixin:
    def falar(self):
        return "oi estou falando"
```

---

### 🔹 Classe `Ornitorrinco`

Exemplo avançado de **herança múltipla**:

```python
class Ornitorrinco(Mamifero, Ave, FalarMixin):
```

Características:

* É mamífero
* É ave
* Pode falar (mixin)
* Usa `super()` respeitando o **MRO**

Durante a inicialização, o MRO é exibido:

```python
print(Ornitorrinco.__mro__)
```

📌 Isso ajuda a entender a ordem de execução dos construtores.

---

### ▶️ Exemplo de Uso

```python
gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="Vermelho", cor_bico="Laranja")
print(ornitorrinco)
print(ornitorrinco.falar())
```

---

## 🚗 Exemplo 2: Sistema de Veículos

### 🔹 Classe `Veiculo`

Classe base com atributos comuns:

* `cor`
* `placa`
* `numero_rodas`
* Método `ligar_motor()`

---

### 🔹 Classes Derivadas

#### 🏍️ `Motocicleta`

Herda tudo de `Veiculo` sem modificações.

#### 🚗 `Carro`

Herda tudo de `Veiculo` sem modificações.

#### 🚛 `Caminhao`

Extende `Veiculo` adicionando:

* `carregado` (boolean)
* Método `esta_carregado()`

```python
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
```

---

### ▶️ Exemplo de Uso

```python
moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "cab-4321", 4)
carro.ligar_motor()

caminhao = Caminhao("Verde", "vou-0420", 8, False)
caminhao.esta_carregado()
```

---

## 🎯 Conceitos Demonstrados

✅ Herança simples

✅ Herança múltipla

✅ Mixins

✅ MRO (Method Resolution Order)

✅ Reutilização de código

✅ Sobrescrita de métodos

✅ Boas práticas com `super()`

---

## 🧠 Observações Importantes

* Em herança múltipla, **sempre use `super()`**
* Use `**kwargs` para permitir inicialização cooperativa
* Mixins devem conter **apenas comportamento**, nunca estado

---

## 📌 Requisitos

* Python 3.8+

---

## 👨‍💻 Autor

Projeto criado para fins educacionais, focado no aprendizado de **POO em Python**.

---

Se quiser, posso:

* Refatorar o código para padrão profissional
* Separar em módulos
* Criar testes unitários
* Explicar o MRO passo a passo
