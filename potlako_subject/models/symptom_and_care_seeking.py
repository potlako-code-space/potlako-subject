from potlako_subject.choices import FACILITY

from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO_UNSURE, YES_NO

from ..choices import DATE_ESTIMATION, SYMPTOMS_CONCERN
from .list_models import Symptoms
from .model_mixins import CrfModelMixin


class SymptomAndcareSeekingAssessment(CrfModelMixin):

    first_visit_promt = models.TextField(
        verbose_name=('Can you please tell me about what first prompted you to'
                      'go to the clinic, nurse or doctor?'),
        max_length=100,)

    symptoms_description = models.TextField(
        verbose_name='Can you describe the symptoms a bit more?',
        max_length=100,
        help_text=('Try to identify all participant-reported symptoms first; '
                   'the checklist comes later.'))

    more_symptoms = models.TextField(
        verbose_name=('You mentioned (symptoms(s)),were there any more symptoms '
                      'that you noticed about this time?'),
        max_length=100)

    symptoms_cope = models.TextField(
        verbose_name=('What did you do to cope with/help these symptoms?'),
        max_length=75)

    symptoms_present = models.ManyToManyField(
        Symptoms,
        verbose_name=('Have you had any of the following symptoms?'),
        blank=True)

    symptoms_discussion = models.CharField(
        verbose_name=('Did you discuss your symptoms with anyone before going '
                      'to the clinic?'),
        choices=YES_NO_UNSURE,
        max_length=8)

    discussion_person = models.CharField(
        verbose_name=('If yes, who did you discuss with?'),
        choices=YES_NO_UNSURE,
        max_length=8,
        blank=True,
        null=True)

    discussion_person_other = OtherCharField()

    discussion_date = models.DateField(
        verbose_name='When did this discussion take place?',
        blank=True,
        null=True)

    discussion_date_estimated = models.CharField(
        verbose_name='Is the discussion date estimated?',
        choices=YES_NO,
        max_length=3,
        blank=True,
        null=True)

    discussion_date_estimation = models.CharField(
        verbose_name='Which part of the date is estimated?',
        choices=DATE_ESTIMATION,
        max_length=15,
        null=True,
        blank=True)

    medical_advice = models.CharField(
        verbose_name=('If yes, did they encourage you to seek advice from '
                      'clinic?'),
        choices=YES_NO_UNSURE,
        max_length=8,
        blank=True,
        null=True)

    clinic_visit_date = models.DateField(
        verbose_name=('When did you go to a clinic or hospital about these '
                      'symptoms?'),
        blank=True,
        null=True)

    clinic_visit_date_estimated = models.CharField(
        verbose_name='Is the hospital/clinic visit date estimated?',
        choices=YES_NO,
        max_length=3,
        blank=True,
        null=True,)

    clinic_visit_date_estimation = models.CharField(
        verbose_name='Which part of the date is estimated?',
        choices=DATE_ESTIMATION,
        max_length=15,
        null=True,
        blank=True,)

    clinic_visited = models.CharField(
        verbose_name='Which clinic or hospital did you go to?',
        choices=FACILITY,
        max_length=32,
        null=True,
        blank=True,)

    cause_assumption = models.TextField(
        verbose_name='What do you think is causing your symptoms?',
        max_length=100)

    symptoms_concern = models.CharField(
        verbose_name='How concerned are you about your symptoms?',
        choices=SYMPTOMS_CONCERN,
        max_length=25,
        null=True,
        blank=True,)

    class Meta(CrfModelMixin.Meta):
        app_label = 'potlako_subject'
        verbose_name = 'Symptom And Care Seeking Assessment'


class SymptomAssessment(BaseUuidModel):

    Symptom_care_seeking = models.ForeignKey(SymptomAndcareSeekingAssessment, on_delete=PROTECT)

    symptom = models.CharField(
        max_length=50)

    symptom_date = models.DateField(
        validators=[date_not_future, ])

    last_visit_date_estimated = models.CharField(
        verbose_name='Is the symptom date estimated?',
        choices=YES_NO,
        max_length=3,
        blank=True,
        null=True)

    last_visit_date_estimation = models.CharField(
        verbose_name='Which part of the date was estimated, if any?',
        choices=DATE_ESTIMATION,
        max_length=15,
        blank=True,
        null=True,)