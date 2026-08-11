PACKAGE := ../anki-export-tags-as-text.ankiaddon

FILES := \
	__init__.py \
	export_tags_as_text.py \
	config.json \
	config.md \
	manifest.json \
	LICENSE

.PHONY: package clean

package: $(PACKAGE)

$(PACKAGE): $(FILES)
	rm -f "$@"
	zip -X -MM -T "$@" $(FILES)

clean:
	rm -f "$(PACKAGE)"
