# Fila de Carros e Drones em Python

Este é um software simples em Python que implementa uma Fila de Carros e uma Fila de Drones. As classes `Carro` e `Drone` representam os veículos, enquanto as classes `FilaCarros` e `FilaDrones` gerenciam as filas.

## Classes

### Carro

A classe `Carro` representa um carro com atributos como marca, modelo e quantidade de portas.

### Drone

A classe `Drone` representa um drone com atributos como marca, modelo e quantidade de hélices.

### FilaCarros

A classe `FilaCarros` gerencia a fila de carros, oferecendo operações como adicionar e remover carros, além de imprimir a fila.

### FilaDrones

A classe `FilaDrones` gerencia a fila de drones, oferecendo operações como adicionar e remover drones, além de imprimir a fila.

**Funcionalidades Principais:**

✅ **Adição e Remoção de Veículos:** O sistema permite adicionar carros e drones à fila, fornecendo uma interface intuitiva para inserir informações como marca, modelo, portas (para carros) e quantidade de hélices (para drones).

🔄 **Operações de Fila:** As operações básicas de fila, como adicionar e remover, foram implementadas de forma eficiente para garantir uma experiência de usuário suave.

📊 **Visualização das Filas:** O software oferece a capacidade de visualizar as filas de carros e drones, proporcionando uma visão instantânea do estado atual.

**Exemplo de Uso:**

```python
# Exemplo de código de uso
# ...

# Adicionando um carro à fila
marca = input("Marca do carro: ")
modelo = input("Qual o modelo do carro: ")
portas = input("Quantidade de portas: ")
carro = Carro(marca, modelo, portas)
filaCarros.add(carro)

# ...
```

O código principal cria instâncias de carros e drones, em seguida, entra em um loop de menu interativo para realizar operações na fila. O menu oferece opções para adicionar e remover carros e drones, bem como imprimir as filas.
