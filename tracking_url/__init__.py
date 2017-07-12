import re

from .version import __version__

__all__ = ['__version__', 'guess_carrier', 'TrackingPattern', 'TrackingUrl', 'TRACKING_PATTERNS']


def guess_carrier(tracking_number):
    for tracking_pattern in TRACKING_PATTERNS:
        # XXX: I'm not a big fan of the replace,
        # we should use a space-friendly matcher for usps instead.
        match = tracking_pattern.match(tracking_number.replace(' ', ''))
        if match is not None:
            return match


class TrackingPattern:
    def __init__(self, carrier, url_pattern, number_patterns):
        self.carrier = carrier
        self.url_pattern = url_pattern
        self.number_patterns = [re.compile(number_pattern) for number_pattern in number_patterns]

    def match(self, number):
        for number_pattern in self.number_patterns:
            if number_pattern.match(number):
                return TrackingUrl(self.url_pattern.format(tracking_number=number), self.carrier, number)


class TrackingUrl:
    def __init__(self, url, carrier, number):
        self.url = url
        self.carrier = carrier
        self.number = number


TRACKING_PATTERNS = [
    TrackingPattern(
        'ups',
        'http://wwwapps.ups.com/WebTracking/track?track=yes&trackNums={tracking_number}',
        [
            r'\b(1Z ?[0-9A-Z]{3} ?[0-9A-Z]{3} ?[0-9A-Z]{2} ?[0-9A-Z]{4} ?[0-9A-Z]{3} ?[0-9A-Z]|[\dT]\d\d\d ?\d\d\d\d ?\d\d\d)\b'
        ]),
    TrackingPattern(
        'fedex',
        'https://www.fedex.com/apps/fedextrack/?tracknumbers={tracking_number}',
        [
            r'(\b96\d{20}\b)|(\b\d{15}\b)|(\b\d{12}\b)',
            r'\b((98\d\d\d\d\d?\d\d\d\d|98\d\d) ?\d\d\d\d ?\d\d\d\d( ?\d\d\d)?)\b',
            r'^[0-9]{15}$'
        ]),
    TrackingPattern(
        'usps',
        'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1={tracking_number}',
        [
            r'(\b\d{30}\b)|(\b91\d+\b)|(\b\d{20}\b)',
            r'^E\D{1}\d{9}\D{2}$|^9\d{15,21}$',
            r'^91[0-9]+$',
            r'^[A-Za-z]{2}[0-9]+US$'
        ]
    ),
    TrackingPattern(
        'dhl',
        'http://www.dhl.com/en/express/tracking.html?AWB={tracking_number}&brand=DHL',
        [
            r'^\d{10,11}$'
        ])
]
