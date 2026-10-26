# Camadas da aplicação

- `domain`: entidades e regras de negócio puras.
- `application`: casos de uso que coordenam o domínio.
- `services`: fachada compatível para os consumidores atuais.
- `presentation`: adaptadores de entrada e saída.
- `infrastructure`: frameworks, configuração, banco e integrações externas.

As dependências devem apontar para dentro: o domínio não conhece FastAPI,
persistência ou detalhes de transporte.
