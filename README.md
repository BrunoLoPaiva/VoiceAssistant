# Reconhecimento de Fala

Este é um programa em Python que utiliza a biblioteca SpeechRecognition para reconhecer a fala do usuário e responder a comandos específicos.<br> 
Ele usa a API do Google para reconhecimento de fala e a biblioteca pyttsx3 para sintetizar a fala de resposta.


## Instalação

1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale as dependências necessárias executando o seguinte comando:
  ```
  pip install SpeechRecognition pyttsx3
  ```
  
  
## Uso

1. Abra um terminal e navegue até o diretório onde o código está localizado.
2. Execute o seguinte comando para iniciar o programa:
```
  python index.py
```
3. Após a execução, o programa estará pronto para receber comandos de fala.


## Funcionalidades

- O programa inicia saudando o usuário.
- O usuário pode fazer um pedido de ajuda, e o programa responderá com uma mensagem de assistência.
- O usuário pode informar o seu nome, e o programa o cumprimentará pelo nome fornecido.
- Se a fala do usuário não for reconhecida, o programa enviará uma mensagem indicando que não conseguiu entender.


## Personalização

- É possível personalizar a voz usada para a resposta, alterando a propriedade 'voice' no código para uma voz disponível em seu sistema.


## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou novos recursos, sinta-se à vontade para criar um pull request.


## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

