# Versioning requirements

Collections must follow [Semantic Versioning 2.0.0](https://semver.org/) using the **MAJOR.MINOR.PATCH** format.

Collections must be at minimum version `1.0.0` to be submitted for certification.
Pre-release versions, such as alpha, beta, or release candidates, are not eligible.

For full details, see the [versioning strategy for Ansible certified collections](https://access.redhat.com/articles/4993781) and the [collection releasing guide](https://docs.ansible.com/projects/ansible/latest/community/collection_contributors/collection_releasing.html).

## Version components

- **MAJOR**: Incompatible API changes such as breaking argspec changes, removal of plugins, or changes that alter outcomes from previous versions.
- **MINOR**: New features or functionality added in a backward-compatible manner, including new modules, plugins, or roles. Also covers updates to testing matrix and metadata such as deprecation notices.
- **PATCH**: Backward-compatible bug fixes, security fixes, and documentation-only changes. Patch releases must not add new features or deprecate existing functionality.

Bug fixes do not require a dedicated patch release and can be included in a minor or major release.
