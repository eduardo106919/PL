# TPC 05

### Pergunta 01

O que pode concluir sobre a condição LL(1) relativamente à gramática abaixo?

```
S → X Y
X → 'p' A | ε
Y → 'q' B | 'r'
A → 's' | ε
B → 't' | ε
```

- [x] Não tem conflitos
- [ ] Tem conflitos FIRST/FIRST
- [ ] Tem conflitos FIRST/FOLLOW

### Pergunta 02

O que pode concluir sobre a condição LL(1) relativamente à gramática abaixo?

```
S → A B
A → 'h' | ε
B → C D
C → E | j
E → 'h' | 'k'
D → 'l'
```

- [ ] Não tem conflitos
- [ ] Tem conflitos FIRST/FIRST
- [x] Tem conflitos FIRST/FOLLOW
