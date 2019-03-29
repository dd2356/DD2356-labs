CC = CC
CFLAGS = -Wall -O3
$(eval REMAINDER := $$$(USER))
USERNAME_PREFIX = $(subst $(REMAINDER),,$(USER))
OUT := /cfs/klemming/nobackup/$(USERNAME_PREFIX)/${USER}

%: %.c
	echo $(USERNAME_PREFIX)
	$(CC) $(CFLAGS) $^ -o $(OUT)/$@
