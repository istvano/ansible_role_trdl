import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dir(host):
    dir = host.file('/usr/local/bin')
    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'root'


def test_file(host):
    installed_file = host.file('/usr/local/bin/trdl')
    assert installed_file.exists
    assert installed_file.is_file
    assert installed_file.user == 'root'
    assert installed_file.group == 'root'
