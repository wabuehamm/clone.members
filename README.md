# Waldbühne Members area clone

## Introduction

This [Ansible](https://ansible.com) playbook clones the Waldbühne members area based on elgg to another environment and can also run update tasks and SQL scripts after cloning the environment.

## Inventory

The file inventory/sample.ini can be used as a template for new clone inventorys. The actual inventory files used on our systems aren't comitted to the repository for obvious safety reasons.

## Usage

    ansible-playbook -i <inventory-file>.ini --ask-vault-pass playbook.yaml