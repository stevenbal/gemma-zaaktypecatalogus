import uuid
from datetime import timedelta

from django.test import TestCase

import requests_mock
from zds_schema.constants import Archiefnominatie

from .factories import ResultaatTypeFactory, ZaakTypeFactory

RESULTAAT_URL = 'https://ref.tst.vng.cloud/referentielijsten/api/v1/resultaten/{uuid}'


@requests_mock.Mocker()
class ResultaattypeTests(TestCase):

    def test_fill_in_default_archiefnominatie(self, m):
        """
        Assert that the archiefnominatie is filled in from the selectielijst
        """
        resultaat_url = RESULTAAT_URL.format(uuid=str(uuid.uuid4()))
        zaaktype = ZaakTypeFactory.create()
        resultaat = ResultaatTypeFactory.build(
            zaaktype=zaaktype,
            selectielijstklasse=resultaat_url,
            archiefnominatie='',
        )
        m.register_uri('GET', resultaat_url, json={
            'url': resultaat_url,
            'procesType': resultaat.zaaktype.selectielijst_procestype,
            'waardering': Archiefnominatie.blijvend_bewaren,
        })

        # save the thing, which should derive it from resultaat
        resultaat.save()

        resultaat.refresh_from_db()
        self.assertEqual(resultaat.archiefnominatie, Archiefnominatie.blijvend_bewaren)

    def test_explicitly_provided_archiefnominatie(self, m):
        """
        Assert that an explicit archiefnominatie is not filled in from the selectielijst
        """
        resultaat_url = RESULTAAT_URL.format(uuid=str(uuid.uuid4()))
        zaaktype = ZaakTypeFactory.create()
        resultaat = ResultaatTypeFactory.build(
            zaaktype=zaaktype,
            selectielijstklasse=resultaat_url,
            archiefnominatie=Archiefnominatie.vernietigen,
        )
        m.register_uri('GET', resultaat_url, json={
            'url': resultaat_url,
            'procesType': resultaat.zaaktype.selectielijst_procestype,
            'waardering': Archiefnominatie.blijvend_bewaren,
        })

        # save the thing, which should derive it from resultaat
        resultaat.save()

        resultaat.refresh_from_db()
        self.assertEqual(resultaat.archiefnominatie, Archiefnominatie.vernietigen)

    def test_fill_in_default_archiefactietermijn(self, m):
        """
        Assert that the archiefactietermijn is filled in from the selectielijst
        """
        resultaat_url = RESULTAAT_URL.format(uuid=str(uuid.uuid4()))
        zaaktype = ZaakTypeFactory.create()
        resultaat = ResultaatTypeFactory.build(
            zaaktype=zaaktype,
            selectielijstklasse=resultaat_url,
            archiefactietermijn=None,
        )
        m.register_uri('GET', resultaat_url, json={
            'url': resultaat_url,
            'procesType': resultaat.zaaktype.selectielijst_procestype,
            # TODO: use more precise P10Y instead, see lib used in
            # https://github.com/VNG-Realisatie/VNG-referentielijsten/pull/2
            'bewaartermijn': 'P3650D',
        })

        # save the thing, which should derive it from resultaat
        resultaat.save()

        resultaat.refresh_from_db()
        self.assertEqual(resultaat.archiefactietermijn, timedelta(days=3650))

    def test_explicitly_provided_bewaartermijn(self, m):
        """
        Assert that an explicit bewaartermijn is not filled in from the selectielijst
        """
        resultaat_url = RESULTAAT_URL.format(uuid=str(uuid.uuid4()))
        zaaktype = ZaakTypeFactory.create()
        resultaat = ResultaatTypeFactory.build(
            zaaktype=zaaktype,
            selectielijstklasse=resultaat_url,
            archiefactietermijn=timedelta(days=5 * 365),
        )
        m.register_uri('GET', resultaat_url, json={
            'url': resultaat_url,
            'procesType': resultaat.zaaktype.selectielijst_procestype,
            'bewaartermijn': 'P10Y',
        })

        # save the thing, which should derive it from resultaat
        resultaat.save()

        resultaat.refresh_from_db()
        self.assertEqual(resultaat.archiefactietermijn, timedelta(days=5 * 365))