# Manager:

Manager is a wrapper to easily perform administrative tasks on a machine in an interactive CLI. I wrote it so I could more easily do package or service management on Unix-like operating systems from a device like my phone where typing commands is not nearly as convenient. I designed it to be relatively cross-platform, with some opinionated choices on what OS-es or package managers I would support. Feel free to add a PR if you want to add additional package managers or operating systems.


### Supported Operating Systems:
MacOS

Linux (systemd only):
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
