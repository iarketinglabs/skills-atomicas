#!/usr/bin/env bash
# Stage explicitly selected static files on a clean review branch.
# This helper never clones, commits, or pushes a public repository.

set -euo pipefail

SOURCE_ROOT="$(pwd -P)/docs"

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <existing-mirror-clone> <docs/file> [more docs/files...]" >&2
  exit 1
fi

WORKDIR="$1"
shift

if [ ! -d "$SOURCE_ROOT" ]; then
  echo "Run this helper from the project root containing docs/." >&2
  exit 1
fi
SOURCE_ROOT="$(cd "$SOURCE_ROOT" && pwd -P)"

if [ ! -d "$WORKDIR" ] || ! git -C "$WORKDIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "The mirror clone must already exist and be a Git worktree." >&2
  exit 1
fi
WORKDIR="$(cd "$WORKDIR" && pwd -P)"

BRANCH="$(git -C "$WORKDIR" branch --show-current)"
case "$BRANCH" in
  ""|main|master)
    echo "Check out a dedicated review branch before staging files." >&2
    exit 1
    ;;
esac

if [ -n "$(git -C "$WORKDIR" status --porcelain)" ]; then
  echo "The mirror worktree must be clean before staging." >&2
  exit 1
fi

if ! command -v realpath >/dev/null 2>&1; then
  echo "Install realpath (GNU coreutils) to validate selected paths." >&2
  exit 1
fi

STAGED=()
for path in "$@"; do
  if [[ "$path" = /* ]]; then
    candidate="$path"
  else
    candidate="$(pwd -P)/$path"
  fi

  if [ -L "$candidate" ] || [ ! -f "$candidate" ]; then
    echo "Only existing regular files may be staged: $path" >&2
    exit 1
  fi

  source_file="$(realpath -- "$candidate")"
  case "$source_file" in
    "$SOURCE_ROOT"/*) relative="${source_file#"$SOURCE_ROOT"/}" ;;
    *)
      echo "Selected file must be inside docs/: $path" >&2
      exit 1
      ;;
  esac

  destination="$WORKDIR/$relative"
  destination_parent="$(dirname "$destination")"
  mkdir -p "$destination_parent"
  destination_parent_real="$(cd "$destination_parent" && pwd -P)"
  case "$destination_parent_real/" in
    "$WORKDIR/"*) ;;
    *)
      echo "Destination escapes the mirror worktree: $relative" >&2
      exit 1
      ;;
  esac
  if [ -L "$destination" ] || [ -d "$destination" ]; then
    echo "Destination must be a regular file or absent: $relative" >&2
    exit 1
  fi

  cp -- "$source_file" "$destination"
  git -C "$WORKDIR" add -- "$relative"
  STAGED+=("$relative")
done

git -C "$WORKDIR" diff --cached --check
echo "Files staged for review: ${#STAGED[@]}"
git -C "$WORKDIR" diff --cached --stat
echo "No commit or push was performed. Review with: git -C \"$WORKDIR\" diff --cached"
echo "Open a pull request after review; merge through the repository's approval checks."
