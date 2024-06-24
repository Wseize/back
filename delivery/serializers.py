from rest_framework import serializers

from accounts.serializers import CustomUserSerializer
from .models import Category, CustomerDeliveryForm, CustomerStoreForm, NoticeStore, Rating, RatingStore, Store, Item, DeliveryPerson, Order, OrderItem, Publicity, SubCategory, Suppliment, TypeCategory


class RatingSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'user', 'item', 'rating']


class SupplimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliment
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True, source='rating_set')
    average_rating = serializers.SerializerMethodField(default=0)
    suppliments = SupplimentSerializer(many=True, read_only=True)
    suppliment_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Suppliment.objects.all(), write_only=True, source='suppliments'
    )    
    sub_category_name = serializers.SerializerMethodField()


    class Meta:
        model = Item
        fields = ['id', 'name', 'category', 'sub_category', 'sub_category_name', 'store', 'description', 'price', 'image', 'available', 'ratings', 'average_rating', 'suppliment_ids', 'personalized', 'suppliments']

    def get_average_rating(self, obj):
        ratings = [rating['rating'] for rating in obj.rating_set.values()]
        if ratings:
            return sum(ratings) / len(ratings)
        return 0
    
    def get_sub_category_name(self, obj):
        return obj.sub_category.name if obj.sub_category else None


class RatingStoreSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = RatingStore
        fields = ['id', 'user', 'store', 'rating']


class NoticeStoreSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = NoticeStore
        fields = ['id', 'user', 'store', 'notice']


class StoreSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    ratings = RatingStoreSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    favorited_by = CustomUserSerializer(many=True, read_only=True)
    notices = NoticeStoreSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['id', 'name', 'category', 'image', 'phone_number', 'password', 'available', 'country', 'governorate', 'latitude', 'longitude', 'items', 'ratings', 'average_rating', 'favorited_by', 'notices']

    def get_average_rating(self, obj):
        # Calculate store's own average rating
        store_average = obj.average_rating if obj.average_rating is not None else 0

        # Calculate the average rating of the store's items
        item_ratings = [item.average_rating for item in obj.items.all() if item.average_rating is not None]
        if item_ratings:
            items_average = sum(item_ratings) / len(item_ratings)
        else:
            items_average = 0

        # Combine the two averages
        combined_average = (store_average + items_average) / 2 if store_average and items_average else store_average or items_average
        return combined_average


class TypeCategorySerializer(serializers.ModelSerializer):
    stores = StoreSerializer(many=True, read_only=True)

    class Meta:
        model = TypeCategory
        fields = ['id', 'name', 'image', 'stores']

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'items']


class SubCategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'items']

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    delivery_person_name = serializers.SerializerMethodField() 
    delivery_person_password = serializers.SerializerMethodField()   
    user_mobile = serializers.CharField(source='user.mobile', read_only=True)
    user_address = serializers.CharField(source='user.adress', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'location', 'items', 'status', 'created_at', 'total_price', 'delivery_person', 'delivery_person_name', 'delivery_person_password', 'user', 'user_mobile', 'user_address', 'eat', 'latitude', 'longitude']

    def get_items(self, obj):
        ordered_items = OrderItem.objects.filter(order=obj)
        item_data = []
        for ordered_item in ordered_items:
            item = {
                'id': ordered_item.item.id,
                'item_name': ordered_item.item.name,
                'quantity': ordered_item.quantity,
                'suppliments': [suppliment.title for suppliment in ordered_item.suppliments.all()]
            }
            if ordered_item.store:
                item['store_name'] = ordered_item.store.name
                item['store_password'] = ordered_item.store.password  
            else:
                item['store_name'] = "Unknown Store"
                item['store_password'] = "No Password"  
            item_data.append(item)
        return item_data

    def get_delivery_person_name(self, obj):
        if obj.delivery_person:
            return obj.delivery_person.name
        return "Unknown Delivery Person"
    
    def get_delivery_person_password(self, obj):
        if obj.delivery_person:
            return obj.delivery_person.password
        return "Unknown Delivery Person"



class OrderDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivery_person']


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']


class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class PublicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicity
        fields = '__all__'


class CustomerDeliveryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDeliveryForm
        fields = '__all__'


class CustomerStoreFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerStoreForm
        fields = '__all__'