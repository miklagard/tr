from django.core.management.base import BaseCommand
from django.conf import settings
from turkish_suffix_library.sample_verbs_list import VERBS
from ui.consonants import TENSES
from turkish_suffix_library.turkish import Turkish
from ui.utils import tr_slugify
import os
import json


class Command(BaseCommand):
    help = 'Create preconjuncted verbs'

    def handle(self, *args, **options):
        for verb in VERBS:
            conjunct = {
                'infinitive': Turkish(verb).infinitive().to_string(),
                'infinitive_negative': Turkish(verb).infinitive(negative=True).to_string()
            }

            conjunct['conjunctions'] = []

            for tense in TENSES:
                conjunct['conjunctions'].append(
                    {
                        'tense': tense,
                        'conjunct': {
                            'p1_poz_sng': Turkish(verb).__getattribute__(tense)(person=1, plural=False, negative=False, question=False).to_string(),
                            'p2_poz_sng': Turkish(verb).__getattribute__(tense)(person=2, plural=False, negative=False, question=False).to_string(),
                            'p3_poz_sng': Turkish(verb).__getattribute__(tense)(person=3, plural=False, negative=False, question=False).to_string(),
                            'p1_poz_pul': Turkish(verb).__getattribute__(tense)(person=1, plural=True, negative=False, question=False).to_string(),
                            'p2_poz_pul': Turkish(verb).__getattribute__(tense)(person=2, plural=True, negative=False, question=False).to_string(),
                            'p3_poz_pul': Turkish(verb).__getattribute__(tense)(person=3, plural=True, negative=False, question=False).to_string(),

                            'p1_neg_sng': Turkish(verb).__getattribute__(tense)(person=1, negative=True).to_string(),
                            'p2_neg_sng': Turkish(verb).__getattribute__(tense)(person=2, negative=True).to_string(),
                            'p3_neg_sng': Turkish(verb).__getattribute__(tense)(person=3, negative=True).to_string(),
                            'p1_neg_pul': Turkish(verb).__getattribute__(tense)(person=1, plural=True,
                                                                                negative=True).to_string(),
                            'p2_neg_pul': Turkish(verb).__getattribute__(tense)(person=2, plural=True,
                                                                                negative=True).to_string(),
                            'p3_neg_pul': Turkish(verb).__getattribute__(tense)(person=3, plural=True,
                                                                                negative=True).to_string(),

                            'p1_poz_sng_q': Turkish(verb).__getattribute__(tense)(person=1, question=True).to_string(),
                            'p2_poz_sng_q': Turkish(verb).__getattribute__(tense)(person=2, question=True).to_string(),
                            'p3_poz_sng_q': Turkish(verb).__getattribute__(tense)(person=3, question=True).to_string(),
                            'p1_poz_pul_q': Turkish(verb).__getattribute__(tense)(person=1, plural=True,
                                                                                  question=True).to_string(),
                            'p2_poz_pul_q': Turkish(verb).__getattribute__(tense)(person=2, plural=True,
                                                                                  question=True).to_string(),
                            'p3_poz_pul_q': Turkish(verb).__getattribute__(tense)(person=3, plural=True,
                                                                                  question=True).to_string(),

                            'p1_neg_sng_q': Turkish(verb).__getattribute__(tense)(person=1, negative=True,
                                                                                  question=True).to_string(),
                            'p2_neg_sng_q': Turkish(verb).__getattribute__(tense)(person=2, negative=True,
                                                                                  question=True).to_string(),
                            'p3_neg_sng_q': Turkish(verb).__getattribute__(tense)(person=3, negative=True,
                                                                                  question=True).to_string(),
                            'p1_neg_pul_q': Turkish(verb).__getattribute__(tense)(person=1, plural=True,
                                                                                  negative=True,
                                                                                  question=True).to_string(),
                            'p2_neg_pul_q': Turkish(verb).__getattribute__(tense)(person=2, plural=True,
                                                                                  negative=True,
                                                                                  question=True).to_string(),
                            'p3_neg_pul_q': Turkish(verb).__getattribute__(tense)(person=3, plural=True,
                                                                                  negative=True,
                                                                                  question=True).to_string(),

                        }
                     }
                )

            file_name = os.path.join(settings.BASE_DIR, 'data', f'{tr_slugify(verb)}.json')

            with open(file_name, 'w', encoding='utf-8') as json_file:
                json.dump(
                    conjunct,
                    json_file,
                    indent=4,
                    ensure_ascii=False
                )
