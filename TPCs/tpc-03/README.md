
# TPC 03

Considere o formato Markdown, amplamente utilizado para escrever documentos estruturados de forma simples.
Usando o módulo re do Python, implemente um tradutor (**parcial**) de Markdown para HTML.

O tradutor deve reconhecer apenas os seguintes elementos, tudo o resto deve permanecer inalterado:

**Títulos**: Caracteres `#` definem um título se surgirem no início da linha e forem seguidos de espaços
```
# Título → <h1>Título</h1>
## Subtítulo → <h2>Subtítulo</h2>
```

**Ênfase (itálico e negrito)**: O texto entre asteriscos não pode começar nem terminar com espaços, e não pode estar colado a caracteres alfanuméricos (isto é, `a*b*c` ou `* x *` **não** é texto enfatizado)
```
*texto* → <em>texto</em>
**texto** → <strong>texto</strong>
```

**Listas (ordenadas e não ordenadas)**: Linhas consecutivas iniciadas por - seguido de espaço, ou `N.` seguido de espaço
```
- item 1
- item 2

→

<ul>
 <li>item 1</li>
 <li>item 2</li>
</ul>
```

```
1. item
2. outro item

→

<ol>
 <li>item</li>
 <li>outro item</li>
</ol>
```

## Pergunta 01

Considere o ficheiro `md1.md` em anexo. Converta-o para HTML usando o programa Python que desenvolveu. Quantas tags `<em>` tem o HTML resultante?

Resposta: 19

## Pergunta 02

Considere o ficheiro `md1.md` em anexo. Converta-o para HTML usando o programa Python que desenvolveu. Quantas tags `<li>` tem o HTML resultante?

Resposta: 44
