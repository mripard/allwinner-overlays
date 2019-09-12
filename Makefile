GCC?=gcc
DTC?=dtc
DTC_OPTIONS?=-@

OBJECTS:= $(patsubst %.dts,%.dtbo,$(wildcard **/*.dts))

%.dtbo: %.dts
	@echo "DTC	$@"
	@$(GCC) -E -nostdinc -I$(CURDIR)/include -I$(CURDIR) -x assembler-with-cpp -undef -o $^.tmp $^; \
	$(DTC) $(DTC_OPTIONS) -I dts -O dtb -o $@ $^.tmp ; \
	rm $^.tmp

all: $(OBJECTS)

clean:
	rm -f $(OBJECTS)
