Tags provide a many-to-many classification of the notes in an Anki collection: a note may carry several tags, and a tag may apply to many notes. In collections whose tags encode subject matter, the tag system can function as a lightweight ontology: top-level tags can identify domains, while hierarchical tags use `::` to represent subdivisions within those domains.

This add-on exports a collection’s complete tag list as sorted plain text, either to the clipboard or to a file. The result can be inspected directly, compared over time, or supplied to an LLM for analysis of the tag system or as context for assessing or generating notes.

**Export Tags as Text** is designed to complement **[Selected Notes to Structured Text](https://ankiweb.net/shared/info/1694585841)**. The former supplies collection-level context; the latter supplies the notes to be assessed or used as models.

<img src="https://raw.githubusercontent.com/schmidhauser/anki-export-tags-as-text/refs/heads/main/export-tags-as-text-tools-menu.png" align="right" width="232">

## Usage

Choose either of the following menu items:

* **Tools → Copy Tags as Text**
* **Tools → Save Tags as Text…**

Both commands export the same tag list: **Copy Tags as Text** places it on the clipboard; **Save Tags as Text…** writes it to a UTF-8 text file, by default named `anki-tags-YYYY-MM-DD.txt`. After copying or saving, Anki reports the total number of tags and the number of top-level tags.

Before exporting, you may wish to run **Tools → Check Database**. Anki retains unused tags in its tag list until that list is rebuilt; **Check Database** removes such entries.

## Configuration

The keyboard shortcuts can be changed under **Tools → Add-ons → Export Tags as Text → Config**. The default configuration is:

```json
{
    "shortcut_copy": "Meta+Ctrl+Shift+T",
    "shortcut_save": "Meta+Ctrl+Shift+E"
}
```

To disable a shortcut, set it to the empty string (`""`). No restart is required. On macOS, the default shortcuts are `⌃⇧⌘T` (copy) and `⌃⇧⌘E` (save).

## Format

Each tag is written exactly as stored by Anki, one per line. Hierarchical tags retain Anki’s `::` separator. An example:

```text
HTML
HTML::charref
HTML::charref::named
HTML::charref::numeric
```

The add-on exports Anki’s registered tag list, which may include unused tags. It does not modify the collection.

## Compatibility

Tested with Anki 26.08 on macOS Tahoe 26.5. Windows and Linux have not yet been tested.

Suggestions and bug reports are welcome. Please [open an issue on GitHub](https://github.com/schmidhauser/anki-export-tags-as-text/issues).
