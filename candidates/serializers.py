from rest_framework import serializers

from candidates.models import CandidateSkillScores


class CandidateSkillScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateSkillScores
        fields = ["score", "skill"]


class CandidateSkillSearchSerializer(serializers.Serializer):
    main_skill_score = serializers.CharField(read_only=True, source='score')
    candidate_name = serializers.CharField(max_length=200)
    related_skills = CandidateSkillScoresSerializer(many=True, read_only=True)
