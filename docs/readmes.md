# README requirements

Collection READMEs should follow the [certified collection README template](readme-template.md) to provide a consistent experience.

## Required content

At minimum, the README must include:

- A clear description of the collection's purpose and use case.
- A **Requirements** section listing the minimum Python version and any external dependencies.
- An **Installation** section focused on installing from [Red Hat Ansible Automation Hub](https://console.redhat.com/ansible/automation-hub).
- A **Changelog** or **Release notes** section that links to the collection's changelog.
- A **License** section or link to the license file.

## Links

All links in the README must be valid and use full URLs.
Do not use relative links, as READMEs are rendered outside the repository on Automation Hub.

## Installation section

The installation section must not include `pip install ansible` or `pip install ansible-core` commands.
Red Hat customers use execution environments to run `ansible-core` and do not install it with pip.

There is no need to list `ansible-core` as a requirement because the minimum version is declared in `meta/runtime.yml`.

If a collection contains validated content and it requires community packages, state those requirements in a **Requirements** section and indicate they apply when installing from Galaxy or other sources.

## Support section

Collections in the `ansible` or `redhat` namespaces, or collections managed by Red Hat teams, must include a **Support** section that identifies:

- Which Red Hat group maintains the collection (for example, Ansible, OpenShift, RHEL).
- How customers can open support issues using the **Create issue** link on Automation Hub

The following is an example support statement:

```text
This collection is maintained by Red Hat <product team name>.

As Red Hat Ansible Certified Content, this collection is entitled
to support through the Ansible Automation Platform (AAP) using the
Create issue button on the top right corner.
If a support case cannot be opened with Red Hat and the collection
has been obtained either from Galaxy or GitHub, there may be community
help available on the Ansible Forum (https://forum.ansible.com/).
```

Third-party vendor collections should also include a support statement.
The [certified collection README template](https://access.redhat.com/articles/7068606) provides guidance on structure and content.
