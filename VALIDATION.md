# Validation

- Echo 0.8.0 standalone: confirmed working in-game by the user on 2026-10-29; 57 Lua 5.1 regression checks passed.
- Public Echo 0.8.1: identical gameplay files apart from version strings; replaces only the two third-party sounds with newly synthesized audio. Audio decodes successfully as mono 44.1 kHz Vorbis; peak level and duration checked. No original Bullet Time Enhanced sounds are included.
- New standalone MCM runtime shim: 22 Lua 5.1 checks against the original MCM 1.7.2fix handlers, with both MCM-first and shim-first registration. Checked missing/native numeric/native boolean key_state, modifiers, original hold cleanup, startup reentry, and no native global replacement. No ui_mcm.script is distributed.
- Public package device testing is pending; they are released as a beta, not universally certified for all ports or MCM versions.
- Both ZIPs passed archive integrity checks. Echo has no crafting file, Hermann override or keyboard-menu replacement. Item, MCM and saved-state IDs remain compatible.
- Release SHA256SUMS.txt identifies the downloadable ZIPs.
