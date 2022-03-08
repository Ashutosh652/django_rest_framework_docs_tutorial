from rest_framework import serializers
from .models import Snippet, STYLE_CHOICES, LANGUAGE_CHOICES
from django.contrib.auth.models import User


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)

#     def update(self, snippet, validated_data):
#         snippet.title = validated_data.get('title', snippet.title)
#         snippet.code = validated_data.get('code', snippet.code)
#         snippet.linenos = validated_data.get('linenos', snippet.linenos)
#         snippet.language = validated_data.get('language', snippet.language)
#         snippet.style = validated_data.get('style', snippet.style)

#         snippet.save()

#         return snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name="snippets:snippet-detail")
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippets:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'highlight',
                  'linenos', 'language', 'style', 'owner', ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="snippets:user-detail")
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippets:snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
