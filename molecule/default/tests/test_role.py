import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dir(host):
    dir = host.file('/root/bin')
    assert dir.exists
    assert dir.is_directory


def test_file(host):
    installed_file = host.file('/root/bin/trdl')
    assert installed_file.exists
    assert installed_file.is_file
