# atto-sublime

Sublime Text language support and editor integration for AttoLang.

## Naming migration and language authority

This repository is maintained at [atto-lang/atto-sublime](https://github.com/atto-lang/atto-sublime); use `https://github.com/atto-lang/atto-sublime.git` for Git remotes and canonical `.atto` source examples. The normative language contract is [atto-spec](https://github.com/atto-lang/atto-spec), with executable guest evidence tracked by [atto-platform-conformance](https://github.com/atto-lang/atto-platform-conformance). Follow current ownership, borrowing, effects, actor, and syntax rules there; do not infer implemented features from a README or unexecuted CI.

## Project scope

Syntax highlighting, editor configuration, and language-recognition tests.

## Development and validation

Use checked-in extension source and host-editor workflows for installation. Ensure `.atto` language registration and formatting/syntax support match the canonical specification.

## Status

This is a statement of intended scope, not a claim of completed implementation or production readiness. Source, CI, and checked-in examples are authoritative for actual supported features and commands.

## Ecosystem

- [AttoLang organization](https://github.com/atto-lang)
- [Language specification](https://github.com/atto-lang/atto-spec)
- [Platform conformance](https://github.com/atto-lang/atto-platform-conformance)

## Repository ownership and contribution routing

**Belongs here:** Sublime Text AttoLang package, syntax grammar, indentation settings, snippets and editor compatibility fixtures.

**Belongs elsewhere:** VS Code-specific UI and LSP integration belongs in atto-vscode; formatting engine in atto-format; language tokens in atto-spec.

**Security and portability boundary:** Validate .atto and supported legacy .ores file mappings without shell execution, arbitrary workspace commands or silent grammar drift.

AttoLang is the canonical project name; new source, examples and documentation use `.atto` and the `atto-lang` repository organization. This README defines scope, not feature readiness.

**Acceptance:** name exact source SHA/tree, runtime/toolchain, positive and negative checks and execution receipt before claiming support. Host-only tests and empty CI steps do not prove guest execution.
