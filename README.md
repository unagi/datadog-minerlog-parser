[![Build Status](https://travis-ci.org/unagi/datadog-minerlog-parser.svg?branch=master)](https://travis-ci.org/unagi/datadog-minerlog-parser)

# datadog-minerlog-parser
minerlog parser for datadog (using 'dogstream')
https://docs.datadoghq.com/agent/logs/

# Usage
1. Put 'miner_parser.py' into your PYTHONPATH
2. Fix yoru Datadog Agent configuration file
3. Restart datadog agent

## Configuration sample
```dogstreams: /var/log/ccminer:miner_parser:parse_miner```

## Notes
If you cannot find log file of `xxxminer`(like `ccminer`), use `-S` option in `xxxminer`.