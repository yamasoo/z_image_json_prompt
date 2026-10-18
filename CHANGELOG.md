# Changelog

## [3.2.0] - 2026-10-18

### Added
- `seed` input: a fixed seed reproduces the same random picks; `0` keeps the old behaviour (new result every run).
- `template_mode` input: "Template overrides fields" (default) or "Fill empty fields only".
- `{a| b| c}` inline choices in option files and templates; the Chinese and English halves pick the same position.
- Console warning when a template uses a field name the node does not know.
- MIT `LICENSE` file and `CHANGELOG.md`.

### Changed
- The seven "Anime Manga –" templates now use the node's 15 real fields, so they actually change the prompt.
- The negative prompt is switched to the chosen language item by item, on both the JSON and the `negative_prompt` output.
- Templates are listed in file-name order and resolved by their ID, not by fuzzy name matching.
- README rewritten: git install, template format, field list, new inputs.

### Fixed
- Style templates had no effect with default settings: they only filled empty fields, and every field defaults to Random.
- Option files with fewer lines than the built-in defaults were silently rewritten on every run, discarding user edits.
- "Detailed" mode glued the adjective onto the text (`VividTreehouse village`, `生動的 | Vivid機械森林…`).
- "Extremely Detailed" in bilingual mode appended only the English suffix.
- Every prompt section started with a stray comma.
- English negative prompt came out as `Low quality, 模糊`; Chinese kept only the first term.
- Option lines written as `中文。| English` (no space before `|`) were not split by language.
- `Sad低头pose` option corrected to `Sad head-down pose`.

## [3.1.0] - 2025-12-06

### Added
- "Random Template" option.
- Seven "Anime Manga –" templates and an expanded option library.

## [3.0.0] - 2025-12-05

- First public release.
