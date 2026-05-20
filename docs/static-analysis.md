# Static analysis requirements

Certification requires collections to pass Ansible Lint scans with the [production profile](https://docs.ansible.com/projects/lint/profiles/#production).

## Rules that cannot be skipped

The following rules are enforced during certification and must not appear in `skip_list` or `.ansible-lint-ignore`:

- `risky-shell-pipe`
- `command-instead-of-shell`
- `meta-no-info`
- `package-latest`
- `no-handler`
- `no-log-password`
- `meta-runtime[unsupported-version]`
- `no-changed-when`
- `risky-file-permissions`
- `command-instead-of-module`
- `unnamed-task`

Skipping these rules can mask issues that affect reliability or security in production environments.

## Rules that should be addressed

The following rules do not block certification but should be resolved in subsequent releases:

- `var-spacing`
- `empty-string-compare`
- `role-name`
- `fqcn-builtins`
- `var-naming[no-role-prefix]`
- `key-order`
- `fqcn[action]`
- `name`

Violations in the [min](https://docs.ansible.com/projects/lint/profiles/#min) and [basic](https://docs.ansible.com/projects/lint/profiles/#basic) profiles generally relate to code quality and formatting and are treated similarly.

### Skipping `var-naming`

Older collections frequently include `var-naming` in their skip lists.
This is generally acceptable for collections past version `1.0.0`.
For new collections, consider addressing the underlying naming issues instead.

If you need to customize variable naming conventions, you can configure the rule in `.ansible-lint` as described in the [var-naming documentation](https://docs.ansible.com/projects/lint/rules/var-naming/#settings).

## Notable rule violations

Some rule violations are particularly significant:

- [ignore-errors](https://docs.ansible.com/projects/lint/rules/ignore-errors/): Can hide failures and cause unpredictable behavior. Replace `ignore_errors` directives with `failed_when` or `changed_when` error handling.
- [schema](https://docs.ansible.com/projects/lint/rules/schema/): Can cause runtime failures. The `schema[meta]` violation in particular affects the integrity of collection metadata.

## Ansible Lint configuration

Including an `.ansible-lint` configuration file in a collection tarball is allowed but not recommended.
Consider using `.ansible-lint` in development environments only and excluding it from tarballs via the `build_ignore` list in `galaxy.yml`.

When configuring `.ansible-lint`, keep the following in mind:

- **`skip_list`**: Must not include any of the enforced rules listed above.
- **`exclude_paths`**: Must not exclude content directories such as `plugins/`, `roles/`, or `extensions/`. Excluding non-content directories such as `changelogs/`, `extensions/molecule/`, `.github/`, and `docs/` is acceptable.
- **`profile`**: Must be set to `production` or omitted.

### Example `.ansible-lint` configuration

```yaml
---
exclude_paths:
  - changelogs
  - .github

skip_list:
  - yaml[indentation]
  - yaml[empty-lines]
```

Only skip cosmetic rules such as YAML formatting.
If your collection has a large number of cosmetic failures, this approach is preferable to leaving them unaddressed.

## Excluding directories from collection builds

You can use the `build_ignore` section in `galaxy.yml` to exclude directories that do not contain user-facing content from collection tarballs:

- `tests/integration/`
- `tests/unit/`
- `changelogs/`
- `.github/`
- `docs/`
