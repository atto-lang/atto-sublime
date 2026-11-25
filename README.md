> **AI agent instructions (organization-wide):** Before working on code, issues, or pull requests, read and follow the [organization `AGENTS.md`](https://github.com/atto-lang/.github/blob/main/AGENTS.md), including its **merge-first stealth-development policy**. Honor any repository-local `AGENTS.md`, explicit holds, and GitHub-enforced rules.

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

## Legacy migration and verification gates

The historical predecessor was `ores-truffle-oreslang/sublime-text-plugins`. This repository is now maintained in `atto-lang`; a similarly named repository or imported history does not by itself establish preservation of the original numeric repository ID, source parity or compiler support. Preserve working legacy `.ores` inputs, old package names and CLI references until compatibility and replacement paths have been verified; new source follows the canonical `.atto` specification.

Sublime grammar and editor integration belong here; runtime implementation and cloud billing do not. [atto-lang](https://github.com/atto-lang) owns language, tooling and portable examples/libraries; [atto-co](https://github.com/atto-co) owns separately governed hosted deployment, tenant infrastructure, registry, identity and billing. Any further original-ID transfer or managed-product carve-out requires separate owner authorization; no direct legacy-org move to atto-co is authorized by this document.

Before an actual transfer, coordinate with the [migration issue](https://github.com/ores-truffle-oreslang/.github/issues/26) and authorized reviewers; inventory numeric ID, exact HEAD/tree, history, access, branch protections/rulesets, open PRs, packages, releases, CI/runners, secrets, webhooks, apps, Pages, dependencies and rollback ownership. Never disclose or mirror private code without authorization. After transfer, verify ID/tree/history and security controls, then execute exact-head tests before changing consumer references. Empty CI steps are NOT_EXECUTED; host-only checks are not compiled guest evidence.

## Standalone lexical grammar preview

`AttoLang.sublime-syntax` is a standalone lexical grammar preview for `.atto` and `.ores`, not a compiler or runtime guarantee. Install the pinned `requirements-dev.txt` and run `python -m unittest discover -s tests -p test_syntax.py` for the structural smoke tests. Contextual spellings such as `critical-read` remain non-reserved.
