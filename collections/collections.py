#   Range objects implement the collections.abc.Sequence ABC, and provide features
#   such as containment tests, element index lookup, slicing and support
#   for negative indices. The advantage of the range type over a regular list or
#   tuple is that a range object will always take the same (small) amount of memory,
#   no matter the size of the range it represents

#   A 'Range' of SignalFrame (a 'SignalFrameArray')
# -- would this be better as a list? is there a need to sort these, given they
#       are inserted sequentially in time?
# -- does it make better sense to sort this synthetically via internal/external method?
# -- equals: Same timestamp, carrier_freq and domain.

# Lists: mutable sequences, typically used to store collections of homogeneous items.
#       NATIVELY SORTABLE
# Tuples: immutable sequences, typically used to store collections of heterogeneous
#       data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also
#       used for cases where an immutable sequence of homogeneous data is needed
#       (such as allowing storage in a set or dict instance)

# A 'List' of TimeFrequencyFrame (a 'TimeFrequencyFrameList')
# A 'Tuple' of TimeFrequencyFrame (a 'TimeFrequencyFrameSet')
# -- does this need to be sortable

# EmitterGroup? equals is: Same id and platform_type.
# EMFieldArray: equals is: Same timstamp, location and domain.

# A 'List' of SignalEvent (a 'SignalEventList')
# A 'Range' of SignalEvent (a 'SignalEventRange')
# -- would this be better as a range? events have timing. I can see a scanario where
#       I want events occurring within a range od time
# -- equals: Same EMField AND carrier_freq.

# A 'List' of SignalMessage (a 'SignalMessageList')
# -- would this be better as a 'range'? events have timing. I can see a scanario where
#       I want messages within a range od time
# -- equals: Same SignalEvent AND semantics.


