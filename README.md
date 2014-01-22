Mibbit IRC log cleaner plugin for Sublime
===
This will add an item to your Edit menu to clean Mibbit IRC logs into a "traditional IRC" format that's nicer to read in plain text (e.g. when copy-pasting into another chat).

Known Issues
---
* The position of the item in the Edit menu is not great. I will try to fix this in a future release as soon as I understand the Sublime menu structure better.
* It expects a buffer of just IRC logs; bad things may happen if something is more complicated
* It might not understand timestamps inside IRC log lines. This has not been tested excessively. Sublime doesn't seem to distinguish line-by-line as the regex ^ wording doesn't work the way I expected it to.