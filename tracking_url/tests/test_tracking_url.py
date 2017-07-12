from unittest import TestCase

from tracking_url import guess_carrier


class GuessCarrierTestCase(TestCase):
    def check_carrier(self, expected_carrier, tracking_numbers):
        for tracking_number in tracking_numbers:
            match = guess_carrier(tracking_number)
            self.assertIsNotNone(match, tracking_number)
            self.assertEqual(expected_carrier, match.carrier)

    def test_ups(self):
        # from: https://docs.rocketship.it/php/1-0/tracking-shipments.html
        self.check_carrier('ups', [
            '1Z12345E0291980793',
            '1Z12345E6692804405',
            '1Z12345E0390515214',
            '1Z12345E0393657226',
            '1Z12345E1392654435',
            '1Z12345E6892410845',
            '1Z12345E1591910450'
        ])

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
            '070358180009382'
        ])

    def test_usps(self):
        # from: https://tools.usps.com/go/TrackConfirmAction!input.action
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
            '0300 0000 0000 0000 0000'
        ])

    def test_dhl(self):
        # from: https://xmlpi-validation.dhl.com/serviceval/jsps/main/Main_menu.jsp
        self.check_carrier('dhl', [
            '8564385550'
        ])
