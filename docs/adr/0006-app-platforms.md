# ADR-0006: Build the app for iOS and iPadOS only

Status: Accepted / 2026-11-09

## Context

ADR-0001 describes the SwiftUI app as iOS, iPadOS, and macOS 27.0 or later. The app target listed iOS, macOS, and visionOS as supported platforms, and VinoGuessrKit declared macOS and iOS, but only iOS was ever built and checked. VinoGuessrKit uses SwiftUI APIs that do not exist on the other platforms, so it does not compile for macOS (the `insetGrouped` list style and the `tabBar` toolbar placement; [vinoguessr-app#16](https://github.com/vinoguessr/vinoguessr-app/issues/16)) or for visionOS (`scrollEdgeEffectStyle(_:for:)`).

Each platform the app targets has to be designed for, built in CI, and checked on every change. There are no users yet, and nothing currently requires a native Mac or Apple Vision Pro app.

## Decision

- The app targets iOS and iPadOS 27.0 or later only. The app target supports only `iphoneos` and `iphonesimulator`, with the iPhone and iPad device families, and VinoGuessrKit declares only `.iOS(.v27)`.
- macOS and visionOS are deferred, not rejected. Re-adding one takes a new ADR, together with the platform-specific code, a CI build for that platform, and checks on it.
- CI builds and tests the targeted platforms only. VinoGuessrKit no longer builds for the macOS host, so its tests run with `xcodebuild test` on an iOS Simulator instead of `swift test` ([vinoguessr-app#9](https://github.com/vinoguessr/vinoguessr-app/issues/9)).
- Offering the iPad app on Apple silicon Macs and Apple Vision Pro as "Designed for iPad" remains an App Store Connect availability option, not a build target. It is decided when the app is first distributed.

## Alternatives

- Keep macOS and visionOS and guard the platform-specific APIs with `#if os(...)`: visionOS needs only one guard today, but each platform still needs its own design, CI build, and checks, which no current requirement justifies.
- Mac Catalyst instead of a native macOS target: it is still a macOS build that needs its own adjustments and checks. Weigh it against a native target when macOS is re-added.

## Consequences

The app's SwiftUI code may use iOS-only APIs without platform guards. Re-adding macOS or visionOS later means revisiting the iOS-only APIs that accumulated in the meantime.

`swift test` on a Mac no longer works for VinoGuessrKit; the vinoguessr-app README lists the `xcodebuild` commands that replace it. The shared rules and the foundation sync in `.github` still describe the app as iOS, iPadOS, and macOS until [.github#7](https://github.com/vinoguessr/.github/issues/7) updates them.

## References

- https://github.com/vinoguessr/vinoguessr-app/issues/16
- https://github.com/vinoguessr/vinoguessr-app/issues/9
- https://developer.apple.com/documentation/apple-silicon/running-your-ios-apps-in-macos
- https://developer.apple.com/documentation/visionos/determining-whether-to-bring-your-app-to-visionos
- ADR-0001: [The API and PostgreSQL are the source of truth for business data](0001-architecture.md)
