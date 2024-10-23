# Commune Subnet Template

Subnet template built on top of [CommuneX][communex].

Learn how to structure, build and deploy a subnet on [Commune AI][commune-ai]!

## Dependencies

[CommuneX library / SDK][communex] is truly the only essential dependency.
Thought, in order enable some features out of the box we have some extra
dependencies in the [pyproject.toml](./pyproject.toml) file.

## Miner

To run the miner, you can just call **comx module serve**. For example:

```sh
comx module serve mysubnet.miner.model.Miner <name-of-your-com-key> [--subnets-whitelist <your-subnet-netuid>] \
  [--ip <text>] [--port <number>]
```

## Validator

To run the validator, just call the module in which you are executing
`validator.validation_loop()`. For example:

```sh
python3 -m mysubnet.cli <name-of-your-com-key>
```

[communex]: https://github.com/agicommies/communex
[commune-ai]: https://communeai.org/
