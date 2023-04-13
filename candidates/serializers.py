from rest_framework.serializers import ModelSerializer

from candidates.models import CandidateSkillScores


class CandidateSkillScoresSerializer(ModelSerializer):
    class Meta:
        model = CandidateSkillScores
        fields = '__all__'
