# GitCon ⚙️✨
*A simple, interactive way to configure your global Git setup*
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)
[![PyPI](https://img.shields.io/pypi/v/gitcon.svg)](https://pypi.org/project/gitcon/)
[![Python Versions](https://img.shields.io/pypi/pyversions/gitcon.svg)](https://pypi.org/project/gitcon/)
[![License](https://img.shields.io/pypi/l/gitcon.svg)](https://pypi.org/project/gitcon/)
[![Tests](https://github.com/kevinveenbirkenbach/git-configurator/actions/workflows/tests.yml/badge.svg)](https://github.com/kevinveenbirkenbach/git-configurator/actions)

---

## Overview

**GitCon** is a small command-line tool that helps you **set up your global Git configuration quickly and consistently**.

Instead of remembering dozens of Git commands, GitCon guides you through the most important settings or lets you configure everything in one command. It is especially useful when setting up a **new machine**, a **fresh user account**, or when you want to **standardize your Git configuration**.

---

## What you can do with GitCon

* Configure global Git settings in minutes
* Choose how `git pull` and merges behave
* Set your name, email, and optional website
* Enable or disable GPG signing for commits
* Automatically sign Git tags
* Run interactively or fully automated in scripts

---

## Installation 📦

Install GitCon using **pip**:

```bash
pip install gitcon
```

After installation, the `gitcon` command is available globally:

```bash
gitcon --help
```

---

## Usage 💻

### Interactive setup (recommended)

Run GitCon in interactive mode to be guided step by step:

```bash
gitcon --interactive
```

You will be asked about:

* Merge and pull behavior
* Your Git user name and email
* Optional website
* Commit signing preferences
* GPG key selection
* Automatic tag signing

This is ideal for first-time setup.

---

### Non-interactive (scripted) usage

You can also configure everything directly using command-line arguments:

```bash
gitcon \
  --merge-option rebase \
  --name "John Doe" \
  --email "john@example.com" \
  --website "https://johndoe.com" \
  --signing gpg \
  --gpg-key ABCDEF123456 \
  --tag-signing auto
```

This mode is useful for:

* Automation scripts
* CI environments
* Reproducible workstation setups

---

## Commit & Tag Signing with GPG 🔐

GitCon can configure Git to **sign commits and tags using GPG**.

### 1. Find your GPG key ID

List your secret keys:

```bash
gpg --list-secret-keys --keyid-format LONG
```

Example output:

```
sec   rsa4096/DEADBEEF12345678 2020-01-01 [SC]
uid                 John Doe <john@example.com>
```

The key ID is the part after `rsa4096/`, for example:

```
DEADBEEF12345678
```

---

### 2. Configure Git signing with GitCon

```bash
gitcon --signing gpg --gpg-key DEADBEEF12345678 --tag-signing auto
```

This will:

* Enable commit signing
* Set your signing key
* Automatically sign Git tags

---

## Typical use cases

* Setting up Git on a new laptop or server
* Ensuring consistent Git configuration across multiple machines
* Quickly enabling GPG signing without memorizing Git commands
* Automating Git setup in provisioning scripts

---

## License 📄

MIT License

---

## Author 👤

**Kevin Veen-Birkenbach**
[https://www.veen.world](https://www.veen.world)
