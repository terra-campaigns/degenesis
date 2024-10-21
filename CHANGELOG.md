---
layout: default
title: CHANGELOG
nav_exclude: TRUE

---

# CHANGELOG

<details close markdown="block">
  <summary id="index">
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## v0.4.1-deg

- Under the hood:
	- New href for redirect_to are dynamic

## v0.4.0-deg

- Named the system: **Primal Odd**, and new logo
- Added:
	- Ruin: New Sepsis infestation sub system, aligned with MOTO
	- Credits to Mark of the Odd
	- Attribute loss text
	- Include for PCs and NPCs to use metadata
	- Templated "connected_to" Obsidian function
- Changed:
	- Background (Cults and Clans) is also influenced by Culture
	- Scar 3 only adds 1d4 to HP (from Monolith)
	- Improved PC statblocks, and link to frontmatter
- Removed:
	- Inventory (Burdens)

## v0.3.1

- Added: Aesthetics modular settings
- Changed:
	- Updated modules' headings and TOC
	- General navigation set up in code

## v0.3.0

- **Modularisation**: Modules are now part of include files
- **Merged TerraOdd into Templates**:Templated folder structure and aesthetics
- Added:
	- 404.html
- Changed:
	- Separated Readme from Home
	- Fixed table colour in dark theme
	- Updated Gems
	- Folders with new structure with index files

## v0.2.1

- New:
	- Added placeholder for Systems
- Changed:
	- Saves - task resolution and adv/disadv
	- Sync gems and actions from [https://github.com/terra-campaigns/template](https://github.com/terra-campaigns/template) for aligned deployment.

## v0.2.0

- **Modularisation**: Backgrounds, Bonds, Ruin (Woes) and Creatures are modularised out of the SRD and will be maintained on each game repository.
	- Degenesis content is moved to [https://terra-campaigns.github.io/degenesis/](https://terra-campaigns.github.io/degenesis/).
- Updates from upstream Cairn

## v0.1.2

- Changed:
	- Reframed **Clans** **Potentials** (previously Feats) to Cairn's Spells Framework
	- Unrelated **Clans** to **Scars** for Spitalians and Scrapers
	- Improved the result of ingesting Burn for attribute increase
- Text improvements

## v0.1.1

- New:
	- Added mutation tables (**Woes**)
	- Exposed Cairn's procedures
	- Completed Anabaptists (new approach to rank and feats)
- Changed: Archetypes are now **Bonds**.
- Fixed: Broken navigation
- Removed: Changes on **Scars**, reinstated Cairn's
- Text improvements

## v0.1.0

**Forked [Cairn](https://cairnrpg.com/hacks/fork-this/).**

- New:
	- New landing page / `README`
	- Characters and Rules based on Cairn 2e
	- Added **Background**:
		- Spitalians
		- Scrapers
	- Added placeholders for remaining Borcan clans.
	- Added archetypes, to support behaviour choices
	- Tables for weapons and armour sizes and modifiers
	- Added **Woe** mechanic (not modularised yet)
- Changed:
	- **Attributes** roll 2d6+3
	- DEX is used for wits and coolness as well (mental DEX)
	- Inventory are treated as **Burdens**
	- **Backgrounds** have feats
	- Modified the scars table to take feats
- Removed:
	- Character traits, bonds and omens
	- Magic
- WIP:
	- Resources & GM material for my games
	- Cosmology of Terra Campaigns 
- Under the hood:
	- Hidden deleted files that are not necessary for Terra Odd
	- Changed site navigation
	- Updated `gemfiles` for website generation
	- Modularised config file, using includes
	- Added directions for localhosting
	- Adopted font choices from [Terra System](https://terra-campaigns.github.io/terraSystem/)
	- Added this Changelog
	- Copyright notes for Degenesis material, when needed
