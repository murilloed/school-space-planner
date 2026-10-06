# Espaços escolares otimizados

Alocação de turmas em salas com restrições de capacidade.

**Status: MVP de pesquisa, v0.1.0.** Estudo de caso independente inspirado
em desafios dos setores relacionados à trajetória do autor (Keduka · Caeduca).
Não representa entrega contratada, resultado real ou endosso dessas organizações.
Todos os exemplos desta versão são sintéticos e reproduzíveis.

## Executar

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
python -m schoolplan.demo --iterations 300 --seed 7
python -m unittest discover -s tests -v
```

## Implementado

Alocação de turmas com capacidade, acessibilidade, laboratório e conflitos de horário; baseline guloso; busca exata branch-and-bound; MCTS UCT com rollout; relatório de viabilidade e objetivo.

## Próximas etapas

Planta real, métricas de deslocamento, integração ao produto escolar, instâncias maiores, solver de referência e política aprendida.

## Reprodutibilidade e avaliação

A demonstração grava `artifacts/report.json`, com parâmetros e métricas.
Resultados de dados sintéticos validam o fluxo; não demonstram desempenho em produção.
Use a mesma semente e orçamento computacional para comparar abordagens.
Consulte `docs/design.md` para decisões e limitações.

## Contribuição

Abra uma issue com objetivo e critério de aceite. Entregue mudanças pequenas,
revisadas e acompanhadas de testes de comportamento. Não inclua dados de clientes,
credenciais ou resultados sem proveniência. Licença MIT para código e dados sintéticos próprios.
