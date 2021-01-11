.PHONY: buildall
buildeach:
	for id in {1..3};
	do \
		pandoc -V geometry:margin=$$MARGIN -f markdown -o Chapter-$$CHID.pdf ch$$CHID/*_exercises.md ;
	done


CHID?=1
MARGIN?=1in
.PHONY: build
build:
	pandoc \
		-V geometry:margin=$$MARGIN \
		-f markdown \
		-o Chapter-$$CHID.pdf \
		--resource-path=.:./ch$$CHID:./ch$$CHID/img \
		ch$$CHID/*_exercises.md


MARGIN?=1in
.PHONY: build
buildall:
	pandoc \
		-V geometry:margin=$$MARGIN \
		-f markdown \
		-o solutions.pdf \
		--resource-path=.:./ch1:./ch1/img:./ch4:./ch4/img \
		ch1/*_exercises.md \
		ch2/*_exercises.md
