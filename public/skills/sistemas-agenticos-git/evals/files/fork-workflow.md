# Workflow sintético recebido para revisão

O workflow abaixo foi proposto para testar código submetido por forks. O PR pode ser aberto por uma pessoa sem acesso de escrita ao repositório.

    name: Validate external pull requests
    on: pull_request_target
    permissions:
      contents: write
    jobs:
      test:
        steps:
          - checkout the fork's pull request head
          - install dependencies from the checked-out branch
          - run the repository test command
        environment:
          PACKAGE_REGISTRY_TOKEN: secret stored in the repository
