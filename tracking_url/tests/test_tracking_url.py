from unittest import TestCase

from tracking_url import guess_carrier


class GuessCarrierTestCase(TestCase):
    def check_carrier(self, expected_carrier, tracking_numbers):
        for tracking_number in tracking_numbers:
            match = guess_carrier(tracking_number)
            self.assertIsNotNone(match, msg='`{}` did not match {}'.format(tracking_number, expected_carrier))
            self.assertEqual(
                expected_carrier, match.carrier,
                msg='`{}` matched {} instead of {}'.format(tracking_number, match.carrier, expected_carrier))

    def test_ups(self):
        # from: https://docs.rocketship.it/php/1-0/tracking-shipments.html
        self.check_carrier('ups', [
            '1Z12345E0291980793',
            '1Z12345E6692804405',
            '1Z12345E0390515214',
            '1Z12345E0393657226',
            '1Z12345E1392654435',
            '1Z12345E6892410845',
            '1Z12345E1591910450',
        # Based on https://www.ups.com/ci/en/help-center/sri/tracking-number.page
            'T1234567890',
            '123456789',
            '123456789012345678',
        ] + [ 'MI123456' + 'A'*i for i in range(1, 23) ])

    def test_fedex(self):
        # from: https://stackoverflow.com/questions/11049025/how-can-i-get-fedex-testing-tracking-number
        self.check_carrier('fedex', [
            '449044304137821',
            '149331877648230',
            '020207021381215',
            '403934084723025',
            '920241085725456',
            '568838414941',
            '039813852990618',
            '231300687629630',
            '797806677146',
            '377101283611590',
            '852426136339213',
            '797615467620',
            '957794015041323',
            '076288115212522',
            '581190049992',
            '122816215025810',
            '843119172384577',
            '070358180009382',
            '6129 0985 1490 2043 8000'
        ])

    def test_usps(self):
        # from: https://tools.usps.com/go/TrackConfirmAction!input.action
        # and: https://www.trackingmore.com/usps-tracking.html
        # and: https://github.com/sereema/tracking-url/issues/1
        self.check_carrier('usps', [
            '9407 1000 0000 0000 0000 00',
            '7000 0000 0000 0000 0000',
            '9303 3000 0000 0000 0000 00',
            'EC 000 000 000 US',
            '9270 1000 0000 0000 0000 00',
            'EA 000 000 000 US',
            'CP 000 000 000 US',
            '9205 5000 0000 0000 0000 00',
            '1400 0000 0000 0000 0000',
            '9208 8000 0000 0000 0000 00',
            'RA 000 000 000 US',
            '9202 1000 0000 0000 0000 00',
            '2300 0000 0000 0000 0000',
            '9400 1000 0000 0000 0000 00',
            '0300 0000 0000 0000 0000',
            '92748999984327000003259997',
            '924 199 021 185 965 130 000 532 72',
        ])

    def test_dhl(self):
        # from: https://xmlpi-validation.dhl.com/serviceval/jsps/main/Main_menu.jsp
        self.check_carrier('dhl', [
            '8564385550'
        ])

    def test_purolator(self):
        # from: https://www.trackingmore.com/tracking-status-detail-en-254.html
        self.check_carrier('purolator', [
            '332359073811',
            '331426749957',
            'KYV009956937',
            'CGK002986959',
            '331434972567',
            '331435738942',
            'JFV247545960',
            'JFV247698458',
            '331434463120',
            '331432270063',
            '331433946802',
            'TLR000083964',
            '331432012770',
        ])

    def test_australia_post(self):
        # from: https://www.trackingmore.com/australia-post-tracking.html
        # and: D2D test orders
        self.check_carrier('australia_post', [
            'LH211265976AU',  # normal Australia Post tracking ID
            'PF8102906901000935003',  # shipped by Parcel Freight Logistics, URL works the same
            'PF8102748601000935000',
            'PF8102773201000965005',
        ])

    def test_royal_mail(self):
        # from: https://www.royalmail.com/royal-mail-you/intellectual-property-rights/linking-our-website
        # and: https://www.trackingmore.com/royal-mail-tracking.html
        self.check_carrier('royal_mail', [
            'ZW924750388GB',
            'QP922433396GB',
        ])
