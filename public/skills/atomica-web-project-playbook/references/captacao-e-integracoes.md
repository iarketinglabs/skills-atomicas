# Captação e integrações

## Contrato de dados

1. Para cada campo, registe finalidade, obrigatoriedade, formato, persistência e dependências. Determine com o responsável qual base legal e aviso correspondem a cada finalidade. Se depender de consentimento, defina em que ponto ele deve ser obtido e como comprová-lo. Modele a retenção, exclusão e retomada de rascunhos antes de habilitar gravação progressiva.
2. Modele estados de carregamento, erro de campo, falha de rede, reenvio, sucesso e alternativa acessível. Valide no servidor mesmo com validação cliente. Use label associado, grupos semânticos e instruções. Mantenha apenas os valores permitidos ao apresentar erro. [W3C WAI, formulários](https://www.w3.org/WAI/tutorials/forms/).
3. Use uma chave de idempotência estável por operação e uma restrição no armazenamento para lidar com repetição concorrente. Separe gravação do envio a integrações. Defina o estado observável de cada integração e o que pode ser reexecutado sem duplicar notificações ou agendamentos.
4. Em bases partilhadas, confira projeto, esquema, papéis e políticas antes de migrar. Teste acessos permitidos e negados em cada papel e confirme minimização no payload. Em implementações Supabase, confira RLS e mantenha credenciais elevadas apenas no servidor. [Supabase, Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security).

## Integrações e medição

- Para CRM, chat ou calendário, mapeie campos e destinos autorizados. Registe propriedade, retentativa, falha parcial e modo manual. Na agenda, defina quando a interface pode confirmar uma marcação e o comportamento se o serviço cair.
- Defina uma lista de eventos e parâmetros admitidos para o analytics. Teste que tags, URLs, parâmetros e payloads não transportam e-mails, telefones ou texto submetido. Respeite a configuração de privacidade acordada. [Google Analytics, evitar dados de identificação pessoal](https://support.google.com/analytics/answer/6366371?hl=pt).
- Teste com dados sintéticos em homologação e integrações simuladas ou namespaces reservados. Faça um teste real apenas com autorização específica e documente destino e limpeza conforme política.
