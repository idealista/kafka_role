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

> [!IMPORTANT]
> From 3.0.0 Role version, Kafka v4.0.0 is installed in KRaft mode (without Zookeeper) and requires JDK 11 or higher, additionally the Log4j 2.x is used, see the [usage](#usage) section for more details.

### Prerequisities

Ansible >= 2.9 version installed.

Molecule >= 3.x.x version for testing purposes.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver and [Goss](https://github.com/aelsabbahy/goss) as verifier.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.kafka_role
  version: 3.0.0
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

This role supports Kafka in KRaft mode now and we made it the default mode, so if you were using this role before, please set the neccesary variables to keep your previous configuration working.

To maintian compatibility with previous versions of the role, if you set `kafka_use_kraft: false` the role will install Kafka in Zookeeper mode as before, and use the old templates for the configuration files.

This are an example of the minimum variables you may need to set get a working Kafka cluster in KRaft mode using the new template using the `kafka_cfg`, `broker_cfg` and `controller_cfg` variables (Check the [kafka-cfg](defaults/main/kafka-cfg.yml) for default cfg):

At broker level or host_vars level:

```yml
# Unique identifier for each Kafka node
kafka_node_id: 1

# We use the kafka_node_id to generate a unique uuid for each node, you can set the value of your choice
kafka_node_uuid: "{{ kafka_node_id | to_uuid | uuid_to_base64 }}".

# Controller URI for this node
kafka_controller_uri: "{{ kafka_node_id }}@{{ ansible_host }}:{{ kafka_controller_port }}"

# Initial controller for this node if the node acts as controller
kafka_initial_controller: "{{ kafka_controller_uri }}:{{ kafka_node_uuid }}"
```

At a general level or group_vars level:

```yml
# The use purpose in general for all the nodes, instead you can set it at host_vars level
kafka_process_roles: "broker,controller"  # broker, controller, or both

# A unique identifier for the Kafka cluster, you can set it to any value but it must be the same for all the nodes in the cluster
kafka_cluster_uuid: "{{ 'kafka_role' | to_uuid | uuid_to_base64 }}"

# List of all the controllers in the cluster with their node id and host/ip
# An example to generate the controller quorum voters value could be:
kafka_controller_quorum_voters: "{{  groups['brokers'] | map('extract', hostvars, 'kafka_controller_uri') | join(',') }}"

# List of all the listeners for the cluster
# An example to generate the listeners value could be:
kafka_listeners: >-
  {%- for listener in kafka_listeners_list -%}
    {{ listener.name }}://{{ listener.host }}
  {%- if not loop.last -%},{%- endif -%}
  {%- endfor -%}

# Where kafka_listeners_list looks like:
kafka_listeners_list:
  - name: BROKERS
    host: "0.0.0.0:{{ kafka_brokers_port }}"
    advertised_host: "{{ kafka_host_name }}:{{ kafka_brokers_port }}"
    protocol: PLAINTEXT
  - name: CLIENTS
    host: "0.0.0.0:{{ kafka_clients_port }}"
    advertised_host: "{{ kafka_host_name }}:{{ kafka_clients_port }}"
    protocol: PLAINTEXT
  - name: CONTROLLER
    host: "0.0.0.0:{{ kafka_controller_port }}"
    advertised_host: "{{ kafka_host_name }}:{{ kafka_controller_port }}"
    protocol: PLAINTEXT

# Kafka inter broker and controller listener names
kafka_inter_broker_listener_name: BROKERS
kafka_controller_listener_names: CONTROLLER

# Kafka listeners using the kafka_listeners_list variable
kafka_advertised_listeners: >-
  {%- for listener in kafka_listeners_list -%}
    {{ listener.name }}://{{ listener.advertised_host }}
  {%- if not loop.last -%},{%- endif -%}
  {%- endfor -%}

# Map of listener name to security protocol using the kafka_listeners_list variable
kafka_security_protocol_map: >-
  {%- for listener in kafka_listeners_list -%}
    {{ listener.name }}:{{ listener.protocol }}
  {%- if not loop.last -%},{%- endif -%}
  {%- endfor -%},SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL

# kafka controller quorum bootstrap servers using the inventory "brokers" group
kafka_controller_quorum_bootstrap_servers: "{{ groups['brokers'] | map('extract', hostvars, 'ansible_host') | product([':' + kafka_controller_port | string]) | map('join') | join(',') }}"

# If you want to customize the log4j configuration or if you are using kafka < 4.0.0 to set the log4j 1.x configuration
kafka_log4j_template_path: log4j2.yml.j2
kafka_log4j_file_name: log4j2.yml
```

> [!CAUTION]
> These were examples and should be adapted to your specific needs.

Additionally but not necessary, we recommend to set the following variables too:

```yml
kafka_xmx: "to_your_value"
kafka_xms: "to_your_value"
```

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

> [!NOTE]
> Ansible does not support generating base64 encoded UUIDs, so for this role we developed a custom filter plugin to do so. For this role it is included but, If you want to use this feature outside, you must copy the `filter_plugins` folder in this repo to your Ansible project.

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
