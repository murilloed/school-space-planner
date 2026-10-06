# Decisões de engenharia

## Escopo
Alocação de turmas em salas com restrições de capacidade. O cenário é um benchmark sintético independente.

## Entregas atuais
Alocação de turmas com capacidade, acessibilidade, laboratório e conflitos de horário; baseline guloso; busca exata branch-and-bound; MCTS UCT com rollout; relatório de viabilidade e objetivo.

## Evolução
Planta real, métricas de deslocamento, integração ao produto escolar, instâncias maiores, solver de referência e política aprendida.

## Qualidade e colaboração
CI executa testes de comportamento. Revisões devem conferir contratos de entrada,
invariantes, divisão de dados e métricas. Evoluções de infraestrutura exigem avaliação
de custo, autorização e observabilidade. Não há recursos cloud provisionados.

## Limitações
Validar a hipótese com dados públicos licenciados ou dados autorizados antes de uso
operacional. Relatar baseline, várias sementes, intervalos de incerteza, consumo
de recursos e resultados negativos. O backlog não constitui funcionalidade implementada.
