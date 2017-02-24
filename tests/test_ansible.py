import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/kafka.yml")["ansible_facts"]


@pytest.fixture()
def Hostname(TestinfraBackend):
    return TestinfraBackend.get_hostname()


def test_kafka_user(User, Group, AnsibleDefaults, Hostname):
    if "kafka" in Hostname:
        assert User(AnsibleDefaults["kafka_user"]).exists
        assert Group(AnsibleDefaults["kafka_group"]).exists
        assert User(AnsibleDefaults["kafka_user"]).group == AnsibleDefaults["kafka_group"]


def test_kafka_conf(File, AnsibleDefaults, Hostname):
    if "kafka" in Hostname:
        conf_dir = File(AnsibleDefaults["kafka_conf_path"])
        conf_file = File(AnsibleDefaults["kafka_conf_path"] + "/server.properties")
        assert conf_dir.exists
        assert conf_dir.is_directory
        assert conf_dir.user == AnsibleDefaults["kafka_user"]
        assert conf_dir.group == AnsibleDefaults["kafka_group"]
        assert conf_file.exists
        assert conf_file.is_file
        assert conf_file.user == AnsibleDefaults["kafka_user"]
        assert conf_file.group == AnsibleDefaults["kafka_group"]


def test_kafka_log(File, AnsibleDefaults, Hostname):
    if "kafka" in Hostname:
        log_dir = File(AnsibleDefaults["kafka_log_path"])
        assert log_dir.exists
        assert log_dir.is_directory
        assert log_dir.user == AnsibleDefaults["kafka_user"]
        assert log_dir.group == AnsibleDefaults["kafka_group"]


def test_kafka_service(File, Service, Socket, AnsibleVars, Hostname):
    if "kafka" in Hostname:
        host = AnsibleVars["kafka_host_name"]
        port = AnsibleVars["kafka_port"]
        assert File("/lib/systemd/system/kafka.service").exists
        assert Service("kafka").is_enabled
        assert Service("kafka").is_running
        assert Socket("tcp://" + host + ":" + str(port)).is_listening
