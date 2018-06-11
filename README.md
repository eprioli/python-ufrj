# python-ufrj
# coding: utf-8
# autor: Eduardo Prioli Novaes
# Sexta-feira, Junho 8 de 2018

Aula de Python com o professor Igor

Trabalho a ser feito:

Dado um arquivo __repositorio.csv__ contendo uma listagem de nomes,e-mails e token, eu desejo que o meu programa em Python seja capaz de enviar notificação para cada e-mail da lista.

Todas as funções que irei criar ou de terceiros estarão no arquivo __func.py__.

O nome do arquivo principal que irá rodar o Python é __projeto.py__.

Eu possuo um arquivo .gitignore para esconder alguns arquivos usados pelo Python como o __pycache__. Aproveitei e criei um arquivo __credenciais.py__ para guardar o login e senha da minha conta do Google. Criei um outro chamado de __credenciais.exemplo.py__ para que outra pessoa que quiser fazer uso desse programa possa copiar esse arquivo retirando o .exemplo do nome e preenchendo com os seus dados nos valores de exemplos desse arquivo.   
Fiz o mesmo com o arquivo __repositorio.csv__, pois ele contem os meus emails pessoais. Listei ao menos quatro deles para fins de testes. Existe um arquivo __repositorio.exemplo.csv__ onde para cada linha separado por "tab", "," e ";" existem três colunas: nome_destinatario, email_destinatario e token.   
Para executar os textes substitua os e-mails falsos por qualquer outro real.

Exemplo:   
__credenciais.exemplo.py__ deve ser duplicado e renomeado para __credenciais.py__.
Em seguida deve-se preencher os campos requeridos.

__DEPENDÊNCIAS PARA RODAR O PROGRAMA:__  
  - __python3__: Para instalar no linux use o comando (_sudo apt install python3_);
  - __python3-tk__: Para instalar no linux use o comando (_sudo apt-get install python3-tk_);
  - E para terminar entre nesta página ative a opção Aplicativos menos seguros: [__CLIQUE AQUI!__](https://www.google.com/settings/security/lesssecureapps?hl=pt-BR "Clique e acesse agora!")

__PARA RODAR O PROGRAMA, FAÇA ASSIM:__   
  - Faça as configurações necessárias nos arquivos: __credenciais.py__ e __repositorio.csv__;
  - Vá até a raiz de seu projeto (pasta onde ele se encontra) pela linha de comando (terminal) e digite:   
  __python3 projeto.py__.
