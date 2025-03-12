#!/usr/bin/env python3
import argparse
import subprocess
import sys

def list_gpg_keys():
    """Lists available GPG keys."""
    try:
        result = subprocess.run(
            ["gpg", "--list-secret-keys", "--keyid-format", "LONG"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        print("\nAvailable GPG keys:")
        print(result.stdout)
    except Exception as e:
        print("Error listing GPG keys:", e)

def set_git_config(key, value):
    """Sets a Git configuration value globally."""
    try:
        subprocess.run(
            ["git", "config", "--global", key, value],
            check=True
        )
        print(f"Set '{key}' to '{value}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting git config {key}: {e}")
        sys.exit(1)

def interactive_setup():
    # --- Merge Option ---
    print("Choose your merge option:")
    print("  1) Merge commit (default)")
    print("  2) Fast-forward only")
    print("  3) Rebase (for 'git pull')")
    merge_choice = input("Your choice (1/2/3): ").strip()
    if merge_choice == "1":
        merge_option = "merge"
    elif merge_choice == "2":
        merge_option = "fast-forward"
    elif merge_choice == "3":
        merge_option = "rebase"
    else:
        print("Invalid choice. Defaulting to merge commit.")
        merge_option = "merge"

    if merge_option == "merge":
        set_git_config("merge.ff", "true")
        set_git_config("pull.rebase", "false")
    elif merge_option == "fast-forward":
        set_git_config("merge.ff", "only")
        set_git_config("pull.rebase", "false")
    elif merge_option == "rebase":
        set_git_config("pull.rebase", "true")

    # --- Author Details ---
    name = input("Enter your Git user name: ").strip()
    email = input("Enter your Git email: ").strip()
    set_git_config("user.name", name)
    set_git_config("user.email", email)
    
    # --- Additional Attribute: Website ---
    website = input("Enter your website (optional): ").strip()
    if website:
        set_git_config("user.website", website)

    # --- Signing Method ---
    print("Choose your commit signing method:")
    print("  1) GPG signing")
    print("  2) No signing")
    sign_choice = input("Your choice (1/2): ").strip()
    if sign_choice == "1":
        # List available GPG keys so the user can decide
        list_gpg_keys()
        gpg_key = input("Enter your GPG key ID: ").strip()
        set_git_config("commit.gpgsign", "true")
        set_git_config("user.signingkey", gpg_key)
    elif sign_choice == "2":
        set_git_config("commit.gpgsign", "false")
    else:
        print("Invalid choice. Defaulting to no commit signing.")
        set_git_config("commit.gpgsign", "false")
    print("Git configuration updated successfully (interactive mode).")

def main():
    parser = argparse.ArgumentParser(
        description="Configure Git settings interactively or via command-line parameters."
    )
    parser.add_argument("--interactive", action="store_true", help="Run interactive setup")
    parser.add_argument("--merge-option", choices=["merge", "fast-forward", "rebase"],
                        help="Merge option to set")
    parser.add_argument("--name", help="Git user name")
    parser.add_argument("--email", help="Git email")
    parser.add_argument("--website", help="User website (optional)")
    parser.add_argument("--signing", choices=["gpg", "none"],
                        help="Commit signing method: 'gpg' for GPG signing, 'none' for no signing")
    parser.add_argument("--gpg-key", help="GPG key ID to use if signing is 'gpg'")

    args = parser.parse_args()

    # Run interactive mode if the flag is set or if no parameters were given.
    if args.interactive or (not args.merge_option and not args.name and not args.email and not args.signing):
        interactive_setup()
    else:
        # Non-interactive mode: set merge option if provided.
        if args.merge_option:
            if args.merge_option == "merge":
                set_git_config("merge.ff", "true")
                set_git_config("pull.rebase", "false")
            elif args.merge_option == "fast-forward":
                set_git_config("merge.ff", "only")
                set_git_config("pull.rebase", "false")
            elif args.merge_option == "rebase":
                set_git_config("pull.rebase", "true")

        if args.name:
            set_git_config("user.name", args.name)
        if args.email:
            set_git_config("user.email", args.email)
        if args.website:
            set_git_config("user.website", args.website)

        if args.signing:
            if args.signing == "gpg":
                if not args.gpg_key:
                    print("Error: --gpg-key must be provided when --signing is 'gpg'.")
                    sys.exit(1)
                set_git_config("commit.gpgsign", "true")
                set_git_config("user.signingkey", args.gpg_key)
            elif args.signing == "none":
                set_git_config("commit.gpgsign", "false")
        print("Git configuration updated successfully (non-interactive mode).")

if __name__ == "__main__":
    main()
