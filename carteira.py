acoes = {
    "BPAC11": {"nome": "Banco BTG Pactual", "setor": "Financeiro"},
    "ITUB4": {"nome": "Itaú Unibanco", "setor": "Financeiro"},
    "VALE3": {"nome": "Vale S.A.", "setor": "Mineração"},
    "PETR4": {"nome": "Petrobras", "setor": "Petróleo"},
    "B3SA3": {"nome": "B3 S.A.", "setor": "Financeiro"},
    "APPL34": {"nome": "Apple Inc.", "setor": "Tecnologia"},
    "SPXI11": {"nome": "S&P 500 Index", "setor": "Índice"}
}

minha_carteira = []

def _calcular_status(acao):
    """ 
    Calcula o status da acao baseado na quantidade atual vs meta.

    Retorna status da acao: 'Posição neutra', 'Posição comprada' ou 'Posição de venda'.
    """
    if 'meta' not in acao or acao['meta'] == 0:
        return 'Sem meta'
    elif acao['quantidade'] < acao['meta']:
        return 'Posição comprada'
    elif acao['quantidade'] == acao['meta']:
        return 'Posição neutra'
    else:
        return 'Posição de venda'
        
def _exibir_carteira():
    """
    Exibe todas as ações presentes na carteira do usuário.
    
    A função percorre a lista da carteira e mostra cada ação com sua quantidade,
    meta (se definida), status e progresso percentual.
    """
    if not minha_carteira:
        print("\nSua carteira está vazia.")
        return
        
    print("="*50)
    print("Sua Carteira de Ações:")
    print("="*50)
    for acao in minha_carteira:
        status = _calcular_status(acao)
        
        if 'meta' in acao and acao['meta'] > 0:
            progresso = (acao['quantidade'] / acao['meta']) * 100
            print(f"Ação: {acao['codigo']}, Quantidade: {acao['quantidade']}/{acao['meta']}, Status: {status} ({progresso:.0f}%)")
        else:
            print(f"Ação: {acao['codigo']}, Quantidade: {acao['quantidade']}, Status: {status}")

def comprar_acao(acao):
    """
    Permite que o usuário compre uma ação, adicionando à sua carteira.
    
    A função solicita o código da Ação e quantidade desejada.
    Se a ação existe na carteira, soma a nova quantidade e atualiza o status automaticamente.
    Se não existe, adiciona uma nova entrada.
    """
    
    print("="*30)
    print("Compra de Ações")
    print("="*30)
    for codigo, info in acoes.items():
        print(f"Código: {codigo}, Nome: {info['nome']}, Setor: {info['setor']}")
    
    codigo = input("\nDigite o código da ação que deseja comprar: ").upper()
    
    if codigo not in acoes:
        print("\n Ação indisponível")
        return
        
    try:
        quantidade = int(input(f"Quantas ações de {codigo} você deseja comprar? "))
        if quantidade <= 0:
            print("\n A quantidade deve ser um número positivo.")
            return
    except ValueError:
        print("\n A quantidade deve ser um número inteiro.")
        return
        
    acao_existente = None
    for acao in minha_carteira:
        if acao['codigo'] == codigo:
            acao_existente = acao
            break
    
    if acao_existente:
        acao_existente['quantidade'] += quantidade
        status_atual = _calcular_status(acao_existente)
        print(f"\n Compra realizada! Total de {codigo}: {acao_existente['quantidade']}")
        print(f" Status: {status_atual}")
        
        # Alerta se atingiu a posição neutra (meta exata)
        if 'meta' in acao_existente and acao_existente['quantidade'] == acao_existente['meta']:
            print("="*30)
            print(" Parabéns! Você atingiu sua meta para essa ação!")
            print("="*30)
    else:
        minha_carteira.append({'codigo': codigo, 'quantidade': quantidade})
        print(f"\n Compra realizada! Adicionadas {quantidade} ações de {codigo}")

def vender_acao():
    """
    Permite que o usuário venda uma ação, removendo TOTALMENTE ou parcialmente da carteira.
    
    O status da ação é automaticamente atualizado após a venda.
    """
    
    if not minha_carteira:
        print("\nSua carteira está vazia.")
        return
    
    print("="*30)
    print("Venda de Ações")
    print("="*30)
    
    _exibir_carteira()
    codigo = input("\nDigite o código da ação que deseja vender: ").upper()
    
    acao_existente = None
    for acao in minha_carteira:
        if acao['codigo'] == codigo:
            acao_existente = acao
            break
    
    if not acao_existente:
        print("\nAção não encontrada na sua carteira.")
        return
        
    try:
        quantidade = int(input(f"Quantas ações de {codigo} você deseja vender? (Disponível: {acao_existente['quantidade']}) "))
        if quantidade <= 0:
            print("\nA quantidade deve ser um número positivo.")
            return
    except ValueError:
        print("\nA quantidade deve ser um número inteiro.")
        return
        
    if quantidade > acao_existente['quantidade']:
        print("\nVocê não possui essa quantidade de ações.")
        return
        
    acao_existente['quantidade'] -= quantidade
    if acao_existente['quantidade'] == 0:
        minha_carteira.remove(acao_existente)
        print("\nVenda realizada com sucesso. Ação removida da carteira.")
    else:
        status_atual = _calcular_status(acao_existente)
        print(f"\nVenda realizada com sucesso. Status atual: {status_atual}")

def definir_meta():
    """
    Permite que o usuário defina ou altere a meta de quantidade para uma ação.
    
    O usuário pode definir quantas ações deseja ter como objetivo para cada posição.
    O status da ação é automaticamente calculado baseado na quantidade atual vs meta. 
    Retornando esse percentual na funcao _exibir_carteira()
    """
    
    print("="*30)
    print("Definir Meta de Investimento")
    print("="*30)
    
    if minha_carteira:
        _exibir_carteira()
        print("\nAções disponíveis para compra:")
    
    for codigo, info in acoes.items():
        print(f"Código: {codigo}, Nome: {info['nome']}")
    
    codigo = input("\nDigite o código da ação para definir meta: ").upper()
    
    if codigo not in acoes:
        print("\nAção indisponível.")
        return
    
    acao_existente = None
    for acao in minha_carteira:
        if acao['codigo'] == codigo:
            acao_existente = acao
            break
    
    try:
        nova_meta = int(input(f"Digite a meta de ações para {codigo}: "))
        if nova_meta <= 0:
            print("\nA meta deve ser um número positivo.")
            return
    except ValueError:
        print("\nA meta deve ser um número inteiro.")
        return
    
    if acao_existente:
        acao_existente['meta'] = nova_meta
        print(f"\nMeta atualizada para {codigo}: {nova_meta} ações")
    else:
        minha_carteira.append({'codigo': codigo, 'quantidade': 0, 'meta': nova_meta})
        print(f"\nMeta definida para {codigo}: {nova_meta} ações")
        print("Ação adicionada à sua lista de objetivos!")