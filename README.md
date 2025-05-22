# Validador de Bandeira de Cartão de Crédito

Este projeto consiste em um validador de bandeiras de cartões de crédito desenvolvido em Python. Ele identifica a bandeira do cartão a partir do número informado, suportando as principais bandeiras utilizadas no Brasil e no mundo.

## Bandeiras Suportadas

- **Visa**
- **MasterCard**
- **American Express**
- **Elo**
- **Hipercard**
- **Diners Club**
- **Discover**
- **EnRoute**
- **JCB**
- **Voyager**
- **Aura**

## Como funciona

O código utiliza os prefixos (primeiros dígitos) do número do cartão para identificar a bandeira. Cada bandeira possui um ou mais prefixos específicos, além de um tamanho de número característico. O algoritmo faz a limpeza do número (removendo espaços e traços) e, em seguida, verifica os prefixos e o tamanho para determinar a bandeira.

### Exemplo de uso

Ao executar o script, o usuário deve digitar o número do cartão. O programa irá exibir a bandeira correspondente ou informar se o número é inválido ou desconhecido.

```python
if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    print("Bandeira:", identificar_bandeira(numero))
```

### Exemplo de saída

```
Digite o número do cartão: 4111 1111 1111 1111
Bandeira: Visa
```

## Estrutura da Função

A função principal é `identificar_bandeira(numero_cartao: str) -> str`, que retorna uma string com o nome da bandeira ou mensagens de erro.

- **Limpeza do número:** Remove espaços e traços.
- **Validação:** Verifica se o número contém apenas dígitos.
- **Identificação:** Analisa os prefixos e o tamanho do número para identificar a bandeira.

## Prefixos Utilizados

- **Visa:** Começa com 4 (13, 16 ou 19 dígitos)
- **MasterCard:** Começa com 51-55 (16 dígitos)
- **American Express:** Começa com 34 ou 37 (15 dígitos)
- **Elo:** Diversos prefixos de 4 dígitos
- **Hipercard:** 606282, 384100, 384140, 384160
- **Diners Club:** 300-305, 36, 38, 39 (14 dígitos)
- **Discover:** 6011, 644-649, 65
- **EnRoute:** 2014, 2149 (15 dígitos)
- **JCB:** 3528-3589 (4 dígitos iniciais)
- **Voyager:** 8699 (15 dígitos)
- **Aura:** 5078, 6362, além de prefixos específicos de 5 e 6 dígitos

## Como executar

1. Certifique-se de ter o Python instalado.
2. Salve o código em um arquivo chamado `index.py`.
3. Execute no terminal:

```bash
python index.py
```

4. Digite o número do cartão quando solicitado.

## Observações

- O código não valida se o número do cartão é real, apenas identifica a bandeira pelo padrão dos dígitos.
- Para validação completa (incluindo dígito verificador), recomenda-se implementar o algoritmo de Luhn.

---

Desenvolvido para fins educacionais.
