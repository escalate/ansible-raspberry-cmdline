"""Role testing files using testinfra"""


def test_cmdline_file(host):
    """Check Linux kernel command line file"""
    f = host.file("/boot/firmware/cmdline.txt")

    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755
    assert (
        "console=serial0,115200 "
        "console=tty1 "
        "root=PARTUUID=ebbeb7e0-01 "
        "rootfstype=ext4 "
        "fsck.repair=yes "
        "rootwait"
    ) in f.content_string
