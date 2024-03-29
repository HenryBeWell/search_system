from django.db import models


# Create your models here.
class CandidateSkillScores(models.Model):
    """
    Candidate Detail Information
    """
    score = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    skill = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'candidate_skill_scores'
        ordering = ['-score']


class Platform(models.Model):
    """
    Platform Information
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    sources = models.ManyToManyField(CandidateSkillScores, blank=True, related_name='sources')

    class Meta:
        db_table = 'platform'

    def __str__(self):
        return self.name
