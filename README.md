![Logo](https://raw.githubusercontent.com/idealista/kafka-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/kafka-role.png)](https://travis-ci.org/idealista/kafka-role)

# Kafka Ansible role

This ansible role installs Apache Kafka in a debian environment. The server is installed using the sources.

- [Getting Started](#getting-started)
  - [Prerequisities](#prerequisities)
  - [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install a [Apache Kafka](https://kafka.apache.org/) distributed streaming platform in a Debian system.

### Prerequisities

Ansible 2.5.5.0
Python 3.6 or Python 2.7
Other combinations may work but they're not tested.

Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver.
See [test-requirements-27](test-requirements-27.txt) and [test-requirements-36](test-requirements-36.txt).

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```yml
- src: http://github.com/idealista/kafka-role.git
  scm: git
  version: 1.0.0
  name: kafka
```

Install the role with ansible-galaxy command:

```sh
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```yml
---
- hosts: someserver
  roles:
    - role: kafka
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

Kafka topics could be configured through the role. Just set the topics like:

```yml
kafka_topics:
  - name: 'test'
    partitions: '3'
    replicas: '3'
  - name: 'test2'
    partitions: '3'
    replicas: '1'
```

Enable delete topic var if you want to remove topics from the cluster.

The number of partitions can be modified but not the replicas. Please have this in mind when create the topics.

Also notice that you can't decrease the number of partitions of a created topic.

## Testing

```sh
pipenv install -r test-requirements-27.txt --python 2.7
pipenv run molecule test
```

and

```sh
pipenv install -r test-requirements-36.txt --python 3.6
pipenv run molecule test
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.5.5.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/kafka-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

- **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/kafka-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
