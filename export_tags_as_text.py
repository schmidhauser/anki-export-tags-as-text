# Copyright (C) 2026 Andreas U. Schmidhauser
# SPDX-License-Identifier: AGPL-3.0-or-later

from datetime import date
from pathlib import Path

from aqt import mw
from aqt.qt import QAction, QApplication, QFileDialog, qconnect
from aqt.utils import showWarning, tooltip


def count_top_level_tags(tags: list[str]) -> int:
    return sum("::" not in tag for tag in tags)


def prepare_tags() -> tuple[str, int, int] | None:
    if mw.col is None:
        showWarning("No collection is open.", parent=mw)
        return None

    tags = sorted(mw.col.tags.all())

    if not tags:
        tooltip("The collection contains no tags.", parent=mw)
        return None

    total = len(tags)
    top_level = count_top_level_tags(tags)

    return "\n".join(tags), total, top_level


def result_message(verb: str, total: int, top_level: int) -> str:
    tag_word = "tag" if total == 1 else "tags"
    return f"{verb} {total} {tag_word} ({top_level} top-level)."


def on_copy() -> None:
    prepared = prepare_tags()

    if prepared is None:
        return

    text, total, top_level = prepared
    QApplication.clipboard().setText(text)

    tooltip(
        result_message("Copied", total, top_level),
        parent=mw,
    )


def on_save() -> None:
    prepared = prepare_tags()

    if prepared is None:
        return

    text, total, top_level = prepared

    default_filename = f"anki-tags-{date.today().isoformat()}.txt"
    default_path = Path.home() / default_filename

    filename, _selected_filter = QFileDialog.getSaveFileName(
        mw,
        "Save Tags as Text",
        str(default_path),
        "Text Files (*.txt)",
    )

    if not filename:
        return

    path = Path(filename)

    if not path.suffix:
        path = path.with_suffix(".txt")

    try:
        path.write_bytes(text.encode("utf-8"))
    except OSError as error:
        showWarning(
            f"Could not save the file:\n{error}",
            parent=mw,
        )
        return

    tooltip(
        result_message("Saved", total, top_level),
        parent=mw,
    )


def apply_shortcuts(config: dict) -> None:
    shortcut_copy = config.get("shortcut_copy", "")
    shortcut_save = config.get("shortcut_save", "")

    copy_action.setShortcut(
        shortcut_copy if isinstance(shortcut_copy, str) else ""
    )
    save_action.setShortcut(
        shortcut_save if isinstance(shortcut_save, str) else ""
    )


copy_action = QAction("Copy Tags as Text", mw)
save_action = QAction("Save Tags as Text…", mw)

qconnect(copy_action.triggered, on_copy)
qconnect(save_action.triggered, on_save)

config = mw.addonManager.getConfig(__name__) or {}
apply_shortcuts(config)

mw.addonManager.setConfigUpdatedAction(__name__, apply_shortcuts)

mw.form.menuTools.addAction(copy_action)
mw.form.menuTools.addAction(save_action)
