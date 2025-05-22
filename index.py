def identificar_bandeira(numero_cartao: str) -> str:
    """
    Identifica a bandeira do cartão de crédito a partir do número informado.
    Suporta: Visa, MasterCard, American Express, Elo, Hipercard, Diners Club, Discover,
    EnRoute, JCB, Voyager, Aura.
    """
    numero = numero_cartao.replace(" ", "").replace("-", "")
    if not numero.isdigit():
        return "Número inválido"

    if (
        numero[:6] in [
            "507860", "507865", "507866", "507867", "507868", "507869", "507870", "507871", "507872", "507873",
            "507874", "507875", "507876", "507877", "507878", "507879", "507880", "507881", "507882", "507883",
            "507884", "507885", "507886", "507887", "507888", "507889", "507890", "507891", "507892", "507893",
            "507894", "507895", "507896", "507897", "507898", "507899"
        ]
        or numero[:5] in ["50786", "50787", "50788", "50789"]
        or numero[:4] == "5078"
        or numero[:4] == "6362"
    ):
        return "Aura"
    # Diners Club (prefixos 300-305, 36, 38, 39 e 14 dígitos)
    elif (numero[:3] in [str(i) for i in range(300, 306)] or numero[:2] in ["36", "38", "39"]) and len(numero) == 14:
        return "Diners Club"
    # Elo
    elif numero[:4] in [
        "4389", "4514", "5041", "6363", "6504", "6505", "6509", "6516", "6550"
    ]:
        return "Elo"
    # Visa
    elif numero.startswith("4") and len(numero) in [13, 16, 19]:
        return "Visa"
    # MasterCard
    elif numero[:2] in ["51", "52", "53", "54", "55"] and len(numero) == 16:
        return "MasterCard"
    # American Express
    elif numero[:2] in ["34", "37"] and len(numero) == 15:
        return "American Express"
    # Discover
    elif numero[:4] == "6011" or numero[:3] in ["644", "645", "646", "647", "648", "649"] or numero[:2] == "65":
        return "Discover"
    # Hipercard
    elif numero[:6] in ["606282", "384100", "384140", "384160"]:
        return "Hipercard"
    # EnRoute
    elif numero[:4] in ["2014", "2149"] and len(numero) == 15:
        return "EnRoute"
    # JCB
    elif (numero[:4].isdigit() and 3528 <= int(numero[:4]) <= 3589):
        return "JCB"
    # Voyager
    elif numero[:4] == "8699" and len(numero) == 15:
        return "Voyager"
    else:
        return "Bandeira desconhecida"

# Exemplo de uso:
if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    print("Bandeira:", identificar_bandeira(numero))

    #diners \ aura