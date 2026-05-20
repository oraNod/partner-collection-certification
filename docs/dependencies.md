# Dependency requirements

## Python dependencies

Collections with external Python dependencies must include a `requirements.txt` file.

### No `ansible` or `ansible-core` packages

The `requirements.txt` file must not list `ansible` or `ansible-core` as dependencies.

Ansible Automation Platform provides `ansible-core` through execution environments.
Modules and plugins have access to the `ansible` Python namespace at runtime, including `ansible.module_utils.basic`, without declaring it as a dependency.

The `ansible` package is a community distribution that bundles 80+ community collections and is not supported in certified collections.

!!! note
    References to `ansible-core` in `pyproject.toml` for development tooling, such as [this example](https://github.com/ansible-collections/amazon.aws/blob/main/pyproject.toml#L33), are acceptable because they do not affect package installation.

### Version specifiers

Dependency versions in `requirements.txt` must not use upper bounds or pinned versions.
Use `>=` or leave the version unspecified:

| Allowed | Not allowed |
| --- | --- |
| `requests` | `requests==2.31.0` |
| `requests>=2.28.0` | `requests<=2.31.0` |

Pinned or capped versions can cause conflicts when multiple collections in an execution environment depend on different versions of the same package.

An exception applies when both the collection and its dependency are provided by the same vendor.

## Binary dependencies

Collections with binary dependencies must include a `bindep.txt` file.
This file is used by `ansible-builder` when creating execution environments.

## Collection dependencies

Collection dependencies declared in `galaxy.yml` must be certified collections available on [Red Hat Ansible Automation Hub](https://console.redhat.com/ansible/automation-hub).
Community collections are not permitted as dependencies in certified collections.
Only validated collections can declare community collections as dependencies.
