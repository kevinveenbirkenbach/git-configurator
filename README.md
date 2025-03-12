# Git Configurator ⚙️✨
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)


**Git Configurator** is a Python-based utility that simplifies setting up your global Git configuration. It interactively guides you through selecting merge strategies, setting author details (including website), and choosing your commit signing preferences. Alternatively, you can configure everything via command-line arguments for automated setup.

## Features 🚀

- **Interactive Setup:**  
  Follow step-by-step prompts to configure merge options, author name/email, website, and GPG signing settings.
- **Non-Interactive Mode:**  
  Use command-line arguments for quick, automated configuration.
- **Global Git Configuration:**  
  Easily set up your Git environment with a single command.
- **Integration with Kevin's Package-Manager:**  
  Installable via [Kevin's Package-Manager](https://github.com/kevinveenbirkenbach/package-manager) under the alias `gitconfig` for global access.

## Installation 📦

You can run the script directly:

```bash
python3 main.py --interactive
```

Or, if you have [Kevin Package-Manager](https://github.com/kevinveenbirkenbach/package-manager) installed, install **Git Configurator** with:

```bash
pkgmgr install --all
```

Then, use it globally via:

```bash
gitconfig --help
```

## Usage 💻

- **Interactive Mode:**

  ```bash
  gitconfig --interactive
  ```

  Follow the on-screen prompts to set your Git configuration.

- **Non-Interactive Mode:**

  ```bash
  gitconfig --merge-option rebase --name "John Doe" --email "john@example.com" --website "https://johndoe.com" --signing gpg --gpg-key YOUR_GPG_KEY
  ```

## License 📄

This project is licensed under the MIT License.

## Author 👤

**Kevin Veen-Birkenbach**  
[veen.world](https://www.veen.world/)

## Acknowledgements 🤖💡

This script was created with the help of **ChatGPT**.

---
Happy configuring! 🎉
