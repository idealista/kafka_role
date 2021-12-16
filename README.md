![Logo](https://raw.githubusercontent.com/idealista/kafka_role/master/logo.gif)

[![Build Status](https://travis-ci.com/idealista/kafka_role.svg?branch=develop)](https://travis-ci.com/idealista/kafka_role)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-idealista.kafka--role-B62682.svg)](https://galaxy.ansible.com/idealista/kafka_role)

# Kafka Ansible role

This Ansible role installs Apache Kafka in a Debian Environment. The server is installed using the sources.

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

These instructions will get you a copy of the role for your Ansible Playbook. Once launched, it will install a [Apache Kafka](https://kafka.apache.org/) distributed streaming platform in a Debian Environment.

### Prerequisities

Ansible 2.8.8 version installed.

Molecule 3.x.x version installed.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver and [Goss](https://github.com/aelsabbahy/goss) as verifier.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.kafka_role
  version: 1.15.0
  name: kafka_role
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - role: kafka_role
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

### Install dependencies

```sh
$ pipenv sync
```

For more information read the [pipenv docs](ipenv-fork.readthedocs.io/en/latest/).

### Testing

```sh
$ pipenv run molecule test 
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.7.5.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/kafka_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

- **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/kafka_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
