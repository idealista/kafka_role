# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/kafka-role/tree/develop)

## [1.13.0](https://github.com/idealista/kafka-role/tree/1.13.0) (2019-03-20)
## Added
- *[#70](https://github.com/idealista/kafka-role/issues/70) Provide list of not removable topics* @jmonterrubio

## [1.12.1](https://github.com/idealista/kafka-role/tree/1.12.1) (2019-02-19)
## Fixed
- *[#65](https://github.com/idealista/kafka-role/issues/65) Remove space before extra properties* @jmonterrubio

## [1.12.0](https://github.com/idealista/kafka-role/tree/1.12.0) (2019-02-12)
## [Full Changelog](https://github.com/idealista/kafka-role/compare/1.11.0...1.12.0)
## Added
- *[#62](https://github.com/idealista/kafka-role/issues/62) Provide the KAFKA_JVM_PERFORMANCE_OPTS* @jmonterrubio

## [1.11.0](https://github.com/idealista/kafka-role/tree/1.11.0) (2019-02-05)
## Fixed
- *[#59](https://github.com/idealista/kafka-role/issues/59) Fix scala version cannot be setted* @jmonterrubio
## Changed
- *[#59](https://github.com/idealista/kafka-role/issues/59) Set 2.12 as default scala version* @jmonterrubio

## [1.10.0](https://github.com/idealista/kafka-role/tree/1.10.0) (2019-01-30)
## Added
- *[#56](https://github.com/idealista/kafka-role/issues/56) Configure topic properties* @jmonterrubio
## Changed
- *[#56](https://github.com/idealista/kafka-role/issues/56) Remove compatibility with ansible < 2.7* @jmonterrubio

## [1.9.0](https://github.com/idealista/kafka-role/tree/1.9.0) (2018-12-18)
## Changed
- *Default kafka version 2.1.0* @jmonterrubio
## Fixed
- *[#53](https://github.com/idealista/kafka-role/issues/53) Fix problem removing topics in python 3* @jmonterrubio

## [1.8.1](https://github.com/idealista/kafka-role/tree/1.8.1) (2018-11-13)
## Fixed
- *[#51](https://github.com/idealista/kafka-role/issues/51) Fix alter kafka topics* @jmonterrubio
## [1.8.0](https://github.com/idealista/kafka-role/tree/1.8.0) (2018-10-31)

## Added
- *Add Kafka_OPTS hook* @john-delivuk
## Fixed
- *[#48](https://github.com/idealista/kafka-role/issues/48) Fix error creating topics in a second launch* @jmonterrubio

## [1.7.1](https://github.com/idealista/kafka-role/tree/1.7.1) (2018-10-29)
## Fixed
- *[#45](https://github.com/idealista/kafka-role/issues/45) Avoided remove all internal topics* @jmonterrubio

## [1.7.0](https://github.com/idealista/kafka-role/tree/1.7.0) (2018-10-29)
## Fixed
- *[#40](https://github.com/idealista/kafka-role/issues/40) Avoided remove __consumer_offsets internal topic* @jmonterrubio
## Added
- *[#39](https://github.com/idealista/kafka-role/issues/39) Add extra configuration properties* @jmonterrubio

## [1.6.0](https://github.com/idealista/kafka-role/tree/1.6.0) (2018-10-09)
## Added
- *[#33](https://github.com/idealista/kafka-role/issues/33) Enable or disable GC log by configuration* @jmonterrubio
- *[#35](https://github.com/idealista/kafka-role/issues/35) Remove old kafka installation* @jmonterrubio
- *[#36](https://github.com/idealista/kafka-role/issues/36) Configure topics from role* @jmonterrubio
## Changed
- *[#34](https://github.com/idealista/kafka-role/issues/34) Use goss instead of testinfra for molecule test* @jmonterrubio

## [1.5.0](https://github.com/idealista/kafka-role/tree/1.5.0) (2018-06-06)
## [Full Changelog](https://github.com/idealista/kafka-role/compare/1.4.0...1.5.0)
## Added
- *[#28](https://github.com/idealista/kafka-role/issues/28) Adding new variables to server.properties template* @amanzanotejon
- *[#30](https://github.com/idealista/kafka-role/issues/30) Kafka.service, log4j.properties and server.properties can be provided via playbooks* @jnogol

## [1.4.0](https://github.com/idealista/kafka-role/tree/1.4.0) (2018-06-06)
## [Full Changelog](https://github.com/idealista/kafka-role/compare/1.3.1...1.4.0)
## Changed
- *[#20](https://github.com/idealista/kafka-role/issues/20) Update to kafka v1.1* @eskabetxe
## Fixed
- *[#26](https://github.com/idealista/kafka-role/issues/26) Testinfra tests don't pass under Vagrant* @eskabetxe

## [1.3.1](https://github.com/idealista/kafka-role/tree/1.3.1) (2018-02-27)
## [Full Changelog](https://github.com/idealista/kafka-role/compare/1.3.0...1.3.1)
## Changed
- *[#23](https://github.com/idealista/kafka-role/issues/23) Using Vagrant hostmanager instead of Landrush* @dortegau
## Fixed
- *[#22](https://github.com/idealista/kafka-role/pull/22) Picking up Xms correctly from KAFKA_HEAP_OPTS environment variable* @didumgai

## [1.3.0](https://github.com/idealista/kafka-role/tree/1.3.0) (2018-02-01)
## [Full Changelog](https://github.com/idealista/kafka-role/compare/1.2.0...1.3.0)
## Added
- *[#13](https://github.com/idealista/kafka-role/issues/13) Enable delete topics property* @jmonterrubio
- *[#12](https://github.com/idealista/kafka-role/issues/12) Enable auto create topics property* @jmonterrubio
## Changed
- *Use uvigo's mirror to download Kafka* @jnogol
- *[#16](https://github.com/idealista/kafka-role/pull/16) Remove Java role dependency* @maqdev
## Fixed
- *Fix Kafka errored version* @jnogol
- *[#16](https://github.com/idealista/kafka-role/pull/16) Create data path if not exists* @maqdev

## [1.2.0](https://github.com/idealista/kafka-role/tree/1.2.0) (2017-05-19)
## [Full Changelog](https://github.com/idealista/kafka-role/compare/1.1.0...1.2.0)
## Changed
- *[#5](https://github.com/idealista/kafka-role/issues/5) Added kafka_hosts var to fix broker id issue* @jmonterrubio

## [1.1.0](https://github.com/idealista/kafka-role/tree/1.1.0) (2017-04-04)
## [Full Changelog](https://github.com/idealista/kafka-role/compare/1.0.0...1.1.0)
## Changed
- *[#2](https://github.com/idealista/kafka-role/issues/2) Change defaults vars and improve installation* @jmonterrubio

## [1.0.0](https://github.com/idealista/kafka-role/tree/1.0.0) (2017-02-28)
### Added
- *First release*
