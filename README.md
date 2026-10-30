# Echo — Resonance Regulator for Anomaly on Android

[Español](README.es.md) · [Русский](README.ru.md) · [Installation](INSTALL.md) · [Downloads](https://github.com/SidorovichsWork/echo-anomaly-android/releases/tag/v0.8.1)

<p align="center"><img src="assets/echo-regulator.png" alt="Echo: battered olive regulator with an amber artifact, protective cage and rotary switch" width="440"></p>

**For the ANDROID port of S.T.A.L.K.E.R. Anomaly: Stalker Mobile.** Echo is a reusable device that toggles slow motion from the existing medical/food quick slots. No flashlight gesture, keyboard shortcut or original Slow Motion installation is needed at runtime.

**Free public beta: ready-to-import ZIPs for Android. No PC or Python required.** Install MCM separately, then our small mobile compatibility fix and Echo. See [installation instructions](INSTALL.md).

## Field notes from Yantar

A recovered detector recorded the same anomalous discharge twice, a fraction of a second apart. The first report blamed faulty wiring. The second carried a handwritten note: **“The detector was disconnected.”**

The scientists at Yantar rebuilt the circuit around a caged Sparkler fragment. Their regulator briefly couples the operator's perception to that resonance. Test subjects described hanging bullets and movements that seemed impossibly slow. Whether the world slows down or the mind races ahead remains disputed.

The fatigue is not. Repeated activation and prolonged exposure can leave the operator disoriented, with blurred vision and an unsteady head. Sakharov keeps the surviving devices under his supervision—and sometimes has one available for a suitably motivated stalker.

*Original fan fiction for this addon, not official S.T.A.L.K.E.R. canon. The illustration is promotional artwork of the inventory device; it is not a screenshot or a new world model.*

## What it does

- Reusable quick-slot controller: use once to activate and again to deactivate.
- Sold by **Professor Sakharov**. All supply tiers stock one; close/reopen trade if delivery is not immediately visible.
- **No crafting recipe** and no Hermann stock override. The **MCM grant button remains available**.
- Configurable slow-motion speed, stamina drain and optional screen effects.
- Overload using the game's drunken camera sway and alcohol screen effect, without adding actual alcohol.
- Default overload: **8 seconds of continuous use OR 4 activations within 30 gameplay seconds**; recovery takes **20 seconds after the last trigger**. Continued prolonged use refreshes recovery.
- Separate MCM switches for repeated-use overload, continuous-use overload, camera and screen; adjustable thresholds, recovery and screen intensity.
- English, Spanish and Russian text. Existing Echo item/settings/save identifiers are retained.

## MCM mobile compatibility fix

The companion **MCM Mobile Compatibility 1.0.0** ZIP contains only our small runtime shim. It handles ports without `key_state` by tracking modifier press/release events and preserves MCM's original callbacks. **It does not contain or replace `ui_mcm.script`, and is not MCM itself.** [Download MCM separately from its author](https://www.moddb.com/mods/stalker-anomaly/addons/anomaly-mod-configuration-menu). Logic-tested against MCM **1.7.2fix**; other versions need verification. Disable the older full-file mobile correction before enabling this one.

## Install and upgrade

Download **Echo_0.8.1_Standalone.zip** and **MCM_Mobile_Compatibility_1.0.0.zip** from [Releases](https://github.com/SidorovichsWork/echo-anomaly-android/releases/tag/v0.8.1). In Sidorovich's Mod Manager, import each ZIP and choose **gamedata**. Follow [INSTALL.md](INSTALL.md) for the complete order.

Before upgrading: deactivate slow motion, save, and close the game. Disable the original Slow Motion / SlowMoMod, older Echo versions and the separate icon patch. Keep original MCM and the new standalone MCM fix enabled, then enable Echo. Keep unrelated weapon fixes enabled if your installation needs them. Do not load saves containing the device with Echo disabled. Existing MCM values take precedence: if yours still says 15 seconds, change it to 8 manually.

The common icon atlas and Sakharov trade configuration are conflict points: load Echo after other replacements or merge changes. No universal modpack compatibility is claimed. The compatibility fix is intended for the tested MCM version; report other-version results separately.

## Validation and support

Echo 0.8.0 was confirmed working in-game by the tester. Public **0.8.1** keeps its gameplay and replaces the two third-party sounds with newly synthesized original audio. The earlier core passed 57 Lua 5.1 checks. The new standalone MCM shim passed 22 checks against the original MCM handlers in both startup orders; **device testing of these two public packages is still pending**. No universal phone, port or modpack compatibility is claimed. See [validation notes](VALIDATION.md).

[Report an issue](https://github.com/SidorovichsWork/echo-anomaly-android/issues) with your port version, addon versions, load order and relevant error text. Remove personal information from logs before sharing them.

## Downloads and optional support

- [Public beta downloads](https://github.com/SidorovichsWork/echo-anomaly-android/releases/tag/v0.8.1)
- [Stalker Mobile port](https://stalker-mobile.ru)
- [Sidorovich's Mod Manager](https://github.com/SidorovichsWork/sidorovich-mod-manager)
- [Sidorovich's Workshop on Patreon](https://www.patreon.com/c/SidorovichsWorkshop)

**No payment or paid membership is required.** Donations are optional and support maintenance and testing.

## Credits

Sidorovich's Workshop: Echo device, original lore and artwork, Android control implementation and mobile compatibility changes. Inspiration: [**Bullet Time Enhanced** by **pitAlex**](https://www.moddb.com/mods/stalker-anomaly/addons/bullet-time-enhanced), based on **exDeMODER**'s Legend Returns skills script. The original addon's audio is not included; Echo 0.8.1 uses its own synthesized sounds. MCM: **RavenAscendant**, **Tronex** and contributors. S.T.A.L.K.E.R. and game assets belong to their respective owners.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [license scope](LICENSE_SCOPE.md). MCM is not redistributed. The modified game icon atlas remains third-party fan-mod content, not public-domain material. Echo is an unofficial fan-created derivative modification for S.T.A.L.K.E.R., developed and owned by GSC Game World, and has no affiliation with GSC. [Official game store](https://store.steampowered.com/franchise/stalker).
