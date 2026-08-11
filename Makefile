PACKAGE := ../anki-export-tags-as-text.ankiaddon

FILES := \
	__init__.py \
	export_tags_as_text.py \
	config.json \
	config.md \
	manifest.json \
	LICENSE

.PHONY: package clean

package:
	rm -f "$(PACKAGE)"
	zip -X -MM -T "$(PACKAGE)" $(FILES)
	unzip -l "$(PACKAGE)"

clean:
	rm -f "$(PACKAGE)"
