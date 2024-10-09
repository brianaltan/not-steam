from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags


class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "description", "video_trailer", "rating", "quantity"]

        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)
    
        def clean_price(self):
            price = self.cleaned_data["price"]
            return strip_tags(price)
        
        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)
        
        def clean_video_trailer(self):
            video_trailer = self.cleaned_data["video_trailer"]
            return strip_tags(video_trailer)
        
        def clean_rating(self):
            rating = self.cleaned_data["rating"]
            return strip_tags(rating)
        
        def clean_quantity(self):
            quantity = self.cleaned_data["quantity"]
            return strip_tags(quantity)
