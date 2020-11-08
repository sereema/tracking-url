import re

from .version import __version__

__all__ = ['__version__', 'guess_carrier', 'TrackingPattern', 'TrackingUrl', 'TRACKING_PATTERNS']


def guess_carrier(tracking_number):
    for tracking_pattern in TRACKING_PATTERNS:
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
            if number_pattern.fullmatch(number):
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
            r'1Z[0-9A-Z]{16}|[\dT]\d{10}'
        ]),
    TrackingPattern(
        'fedex',
        'https://www.fedex.com/apps/fedextrack/?tracknumbers={tracking_number}',
        [
            r'96\d{20}',
            r'61\d{18}',
            r'\d{12}',
            r'\d{15}',
            r'(98\d\d\d\d\d?\d\d\d\d|98\d\d)\d{8}(\d{3})?',
        ]),
    TrackingPattern(
        'usps',
        'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1={tracking_number}',
        [
            r'91\d+',
            r'9\d{15,21}',
            r'\d{20}',
            r'\d{26}',
            r'\d{30}',
            r'E\D{1}\d{9}\D{2}',
            r'[A-Za-z]{2}\d+US',
        ]
    ),
    TrackingPattern(
        'chronopost',
        'https://www.chronopost.fr/tracking-no-cms/suivi-page?listeNumerosLT={tracking_number}',
        [
            r'[A-Za-z]{2}\d{9}[A-Za-z]{2}',
            # These one seem to be when chronopost uses geodis :
            r'[A-Za-z]{2}\d{12}[A-Za-z]',
        ]
    ),
    TrackingPattern(
        'dhl',
        'http://www.dhl.com/en/express/tracking.html?AWB={tracking_number}&brand=DHL',
        [
            r'\d{10,11}'
        ])
]
