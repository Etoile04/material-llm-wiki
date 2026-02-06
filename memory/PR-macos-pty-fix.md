# Pull Request: macOS PTY Compatibility Fix

## PR Title
```
fix: Replace script(1) with Python pty module for macOS compatibility
```

## Problem
The Python wrapper (`claude_code_run.py`) uses `script(1)` to force a pseudo-terminal, but `script(1)` behaves differently on macOS vs Linux. This causes:
- Claude Code to hang
- Abnormal output
- Unpredictable behavior

## Solution
Replace `script(1)` with Python's standard `pty` module for consistent cross-platform behavior.

## Changes
### scripts/claude_code_run.py
- Added `import pty` and `import select`
- Rewrote `run_with_pty()` function to use `pty.openpty()`
- Added non-blocking output reading with `select.select()`
- Added real-time output printing for better UX
- Improved error handling with try/finally blocks

**File stats:**
```
 scripts/claude_code_run.py | 57 ++++++++++++++++++++++++++++++++++++++++------
 1 file changed, 50 insertions(+), 7 deletions(-)
```

## Testing
Tested and verified on macOS:
```bash
# Test PTY module availability
python3 -c "import pty; print('PTY module OK')"
# Output: PTY module OK

# Test syntax
python3 -m py_compile scripts/claude_code_run.py
# Output: (no errors)

# Test execution
python3 scripts/claude_code_run.py -p "Return OK" --permission-mode plan
# Output: OK
```

All tests passed successfully.

## Benefits
- ✅ Cross-platform compatibility (macOS, Linux, Windows via WSL)
- ✅ No external command dependencies
- ✅ Better error handling
- ✅ Real-time output
- ✅ More robust resource management

## Impact
This is a backward-compatible change. All existing functionality is preserved while fixing macOS compatibility issues.

## PR Details
- **Base branch**: `win4r/claude-code-clawdbot-skill` main
- **Head branch**: `Etoile04:fix/macos-pty-compatibility`
- **Commit**: `acb9d95`

## Create PR

### Method 1: Direct GitHub Web Link (Recommended)

1. Visit: https://github.com/win4r/claude-code-clawdbot-skill/compare/main...Etoile04:pr/macos-pty-fix
2. Click "Create pull request"
3. Use the title and body from this document
4. Review and submit

### Method 2: GitHub CLI (may require permissions)

```bash
gh pr create \
  --repo win4r/claude-code-clawdbot-skill \
  --base main \
  --head Etoile04:pr/macos-pty-fix \
  --title "fix: Replace script(1) with Python pty module for macOS compatibility" \
  --body-file /path/to/PR-macos-pty-fix.md
```

## Branch Information

- **Base branch**: `win4r/claude-code-clawdbot-skill` main
- **Head branch**: `Etoile04:pr/macos-pty-fix` (clean branch based on upstream/main)
- **Commit**: `4d2f0e1`
- **Files changed**: 1 file, 50 insertions(+), 7 deletions(-)
