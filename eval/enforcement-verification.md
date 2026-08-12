\# Enforcement Verification



\## Layer 1: Container Permissions



\*\*Role:\*\* documentation-writer



\*\*Workspace check\*\*



\*\*Command:\*\*

`touch /workspace/should-fail.txt`



\*\*Output:\*\*

`touch: cannot touch '/workspace/should-fail.txt': Read-only file system`



\*\*Memory volume check\*\*



\*\*Command:\*\*

`if grep -q ' /memory ' /proc/mounts; then echo "unexpected: /memory is mounted"; else echo "OK: /memory is not mounted"; fi`



\*\*Output:\*\*

`OK: /memory is not mounted`



\*\*Result:\*\* Blocked as expected. The documentation-writer has a read-only workspace and no memory volume, matching its governance policy.

