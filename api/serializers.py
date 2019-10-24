from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = 'item-detail',
		lookup_field = 'id',
		lookup_url_kwarg = 'item_id'
		)
	added_by = UserSerializer()
	fave_item = serializers.SerializerMethodField()
	

	class Meta:
		model = Item
		fields = ['id','image', 'name', 'description', 'detail', 'added_by', 'fave_item']

	def get_fave_item(self, obj):
		return obj.favoriteitem_set.all().count()



class ItemDetailSerializer(serializers.ModelSerializer):
	
	fave_user = serializers.SerializerMethodField()


	class Meta:
		model = Item
		fields = ['image', 'name', 'description','fave_user']
		
	def get_fave_user(self, obj):
		faves = obj.favoriteitem_set.all()
		users = []

		for fave in faves:
			users.append(fave.user)
		return UserSerializer(users, many=True).data



