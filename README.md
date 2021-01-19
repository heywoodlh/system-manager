# system-manager:

System-manager is a wrapper to easily perform administrative tasks on a machine in an interactive CLI. I wrote it so I could more easily do package or service management on Unix-like operating systems from a device like my phone where typing commands is not nearly as convenient. I designed it to be relatively cross-platform, with some opinionated choices on what OS-es or package managers I would support. Feel free to add a PR if you want to add additional package managers or operating systems.

## Installation:

```bash
sudo pip3 install system-manager
```

## Usage:

### Packages:

Install the foo package, upgrade the bar package and remove the cow package:

```bash
sudo system-manager packages --install foo --upgrade bar --remove cow
```

Usage:

```bash
$ system-manager packages --help
usage: system-manager packages [-h] [-i PKG [PKG ...]] [-u PKG [PKG ...]]
                               [-r PKG [PKG ...]]

optional arguments:
  -h, --help            show this help message and exit
  -i PKG [PKG ...], --install PKG [PKG ...]
                        packages to install
  -u PKG [PKG ...], --upgrade PKG [PKG ...]
                        packages to upgrade
  -r PKG [PKG ...], --remove PKG [PKG ...]
                        packages to uninstall
```


### Services:

Start the foo service, restart the bar service and stop the cow service:

```bash
sudo system-manager services --start foo --restart bar --stop cow
```

Usage:

```bash
$ system-manager services --help
usage: system-manager services [-h] [--restart NAME [NAME ...]]
                               [--stop NAME [NAME ...]]
                               [--start NAME [NAME ...]]

optional arguments:
  -h, --help            show this help message and exit
  --restart NAME [NAME ...]
                        service(s) to restart
  --stop NAME [NAME ...]
                        service(s) to stop
  --start NAME [NAME ...]
                        service(s) to start
```

### Supported Operating Systems:
MacOS

Linux:
  - Alpine
  - Arch
  - Debian (and derivatives)
  - RHEL (and derivates)

FreeBSD


### Supported Package Managers:

MacOS:
- [Homebrew](brew.sh)
- [Nix](https://nixos.org/download.html#nix-quick-install)

Linux:
- apk
- apt
- dnf
- [Homebrew](brew.sh)
- [Nix](https://nixos.org/download.html#nix-quick-install)
- pacman

FreeBSD:
- pkg


