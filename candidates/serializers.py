from django.db.models import Q, Avg
from rest_framework import serializers

from candidates.models import Platform, CandidateSkillScores


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('name',)

    def to_representation(self, instance):
        return instance.name


class CandidateSkillScoresSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, source='skill')
    score = serializers.CharField(max_length=200, )
    sources = PlatformSerializer(many=True)
    average = serializers.SerializerMethodField()

    def get_average(self, obj):
        average = CandidateSkillScores.objects.filter(skill=obj.skill).aggregate(Avg('score'))['score__avg']
        return average

    class Meta:
        model = CandidateSkillScores
        fields = ['name', 'score', 'sources', 'average']


class CandidateSkillSearchSerializer(serializers.ModelSerializer):
    main_skill_score = serializers.CharField(source='score')
    candidate_name = serializers.CharField(max_length=200, )
    related_skills = serializers.SerializerMethodField()

    def get_related_skills(self, obj):
        queryset = CandidateSkillScores.objects.filter(Q(candidate_name=obj.candidate_name) & ~Q(skill=obj.skill))
        serializer = CandidateSkillScoresSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = CandidateSkillScores
        fields = ('main_skill_score', 'candidate_name', 'related_skills')
