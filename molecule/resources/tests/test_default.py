import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def named_is_running(host):
    assert host.service("named").is_running is False


def named_example_com_dig(host):
    command = host.run('dig www.example.com @127.0.0.1 +short')
    assert command.stdout != '127.0.0.1'
