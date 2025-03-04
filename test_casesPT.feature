Feature: Testes do E-commerce Advantage Online Shopping

  Scenario: Cadastro de novo usuário
    Given que o usuário acessa a página de cadastro
    When ele preenche os campos obrigatórios corretamente
    And clica no botão "Registrar"
    Then a conta deve ser criada com sucesso
    And o usuário deve ser redirecionado para a página inicial logado

  Scenario: Login com credenciais válidas
    Given que o usuário tem uma conta válida
    When ele insere seu usuário e senha corretamente
    And clica no botão "Entrar"
    Then ele deve ser redirecionado para a página inicial logado
    And deve visualizar seu nome de usuário no canto superior da tela

  Scenario: Login com credenciais inválidas
    Given que o usuário está na página de login
    When ele insere um usuário ou senha incorretos
    And clica no botão "Entrar"
    Then uma mensagem de erro deve ser exibida
    And o usuário deve permanecer na página de login

  Scenario: Adicionar um produto ao carrinho
    Given que o usuário acessa a página de um produto
    When ele clica no botão "Adicionar ao carrinho"
    Then o produto deve aparecer no carrinho de compras
    And a quantidade do produto no carrinho deve ser "1"

  Scenario: Remover um item do carrinho
    Given que o usuário tem um item no carrinho
    When ele clica no botão "Remover"
    Then o item deve ser removido do carrinho
    And a mensagem "Seu carrinho está vazio" deve ser exibida

  Scenario: Atualizar quantidade de um item no carrinho
    Given que o usuário tem um item no carrinho
    When ele altera a quantidade do item
    And confirma a atualização
    Then a quantidade do item no carrinho deve ser atualizada
    And o preço total deve ser atualizado corretamente

  Scenario: Finalizar uma compra com sucesso
    Given que o usuário tem itens no carrinho
    And está logado na conta
    When ele clica no botão "Finalizar Compra"
    And preenche os dados de pagamento e envio corretamente
    And confirma a compra
    Then a compra deve ser concluída com sucesso
    And um e-mail de confirmação deve ser enviado ao usuário

  Scenario: Tentar finalizar compra sem estar logado
    Given que o usuário adicionou itens ao carrinho
    When ele tenta finalizar a compra sem estar logado
    Then o sistema deve solicitar o login antes da finalização
    And deve exibir uma mensagem informativa

  Scenario: Aplicar um cupom de desconto válido
    Given que o usuário está na página do carrinho
    When ele insere um cupom de desconto válido
    And confirma a aplicação do cupom
    Then o desconto deve ser aplicado ao total da compra
    And o novo valor total deve ser atualizado corretamente

  Scenario: Aplicar um cupom de desconto inválido
    Given que o usuário está na página do carrinho
    When ele insere um cupom de desconto inválido
    And confirma a aplicação do cupom
    Then uma mensagem de erro deve ser exibida
    And o valor total da compra não deve ser alterado

  Scenario: Verificar detalhes do pedido na página de perfil
    Given que o usuário realizou uma compra
    When ele acessa a página de pedidos no perfil
    Then os detalhes da compra devem ser exibidos corretamente
    And o status do pedido deve estar atualizado

  Scenario: Logout do usuário
    Given que o usuário está logado
    When ele clica no botão "Logout"
    Then ele deve ser deslogado e redirecionado para a página inicial
    And o nome de usuário não deve mais ser exibido no topo da tela

  Scenario: Recuperar senha
    Given que o usuário esqueceu a senha
    When ele acessa a opção "Esqueci minha senha"
    And insere seu e-mail cadastrado
    Then o sistema deve enviar um link de recuperação para o e-mail
    And uma mensagem informativa deve ser exibida

  Scenario: Filtrar produtos por categoria
    Given que o usuário está na página de produtos
    When ele seleciona uma categoria
    Then apenas produtos da categoria selecionada devem ser exibidos
    And nenhuma outra categoria deve aparecer nos resultados

  Scenario: Alterar endereço de entrega no perfil
    Given que o usuário está na página de perfil
    When ele edita o endereço de entrega
    And salva as alterações
    Then o novo endereço deve ser atualizado corretamente
    And uma mensagem de confirmação deve ser exibida
