DTC?=dtc
DTC_OPTIONS?=-@

%.dtbo: %.dts
	$(DTC) $(DTC_OPTIONS) -I dts -O dtb -o $@ $^

all: $(patsubst %.dts,%.dtbo,$(wildcard */*.dts))
