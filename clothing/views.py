import json
import jwt

from django.http  import JsonResponse
from django.views import View

from django.db    import transaction
from django.db.models import Q, F
from .models      import (
    BasicProducts, 
    Brands, 
    Categories, 
    SizeUnits,
    AvailableSizeUnits,
    Colors,
    AvailableColors,
    SideNames,
    AvailableSideNames,
    SideImages, 
    Parts,
    AvailableParts,
    SizeFiguresForProducts,
    ProductInfo,
    ModelImages
)



#===============================

# 클론 사이트의 url 지정 방식 
# 의류 /clothing
# 의류 > 후디 /clothing/<int : category_id>/정렬 쿼리스트링
# 의류 > 후디 > 필터링 /clothing/<int : category_id>/정렬 쿼리스트링/필터별 쿼리스트링

# 필터링 지정 후 상품 선택할 시 /clothing/<int : product_id>/<int : color_id>
# 커스텀 foundation 상태 : 필터로 지정된 색상 반영

# 필터링 지정 하지 않고 상품 선택할 시 /clothing/<int : product_id>
# 커스텀 foundation 상태 : 무의미

#===============================


# 왼쪽 선택 항목 

class WhichCategory(View):
    def get(self, request) :
        res = list(Categories.objects.values())
        return JsonResponse({"category_set" : res}, status=200)
        #카테고리 id, 카테고리 내용

class WhichBrand(View):
    def get(self, request) :
        res = list(Brands.objects.values())
        return JsonResponse({"brand_set" : res}, status=200)
        #브랜드 id, 브랜드 내용

class WhichColor(View):
    def get(self, request) :
        res = list(Colors.objects.values())
        return JsonResponse({"color_set" : res}, status=200)
        #전체 색상표의 컬러 id, 색상명, 헥사코드 
        
class WhichSize(View):
    def get(self, request) :
        res = list(SizeUnits.objects.values())
        return JsonResponse({"size_set": res}, status=200)
        #전체 사이즈 단위의 id, 사이즈 단위명

# 의류 리스트
# url : /clothing

class AllItems(View):
    FILTER_NAMES = {
        "brand" : "brand_id",
        "color" : "available_color__hex_code",
        "size"  : "available_size_unit__size_unit__startswith"
    }

    def get(self, request) :
        search_filters  = {self.FILTER_NAMES[option] : request.GET[option] for option in request.GET} 
        res = [{
            "product_id"          : elem.id,  
            "product_name"        : elem.product_name,    
            "price"               : elem.price,           
            "category"            : elem.category.id,        
            "brand"               : elem.brand.id,          
            "available_color"     : list(elem.available_color.values()),
            "available_size_unit" : list(elem.available_size_unit.values()),
            "model_thumbnail"     : elem.modelimages_set.values_list('model_image' ,flat=True)[0]
        } for elem in BasicProducts.objects.filter(**search_filters)]
        
        return JsonResponse({"all_items": res}, status=200)


# # 의류 > 카테고리 리스트
# #url : /clothing/<int:category_id>

# class ItemsForCategory(View):
#     FILTER_NAMES = {
#         "brand" : "brand_id",
#         "color" : "available_color__hex_code",
#         "size"  : "available_size_unit__size_unit__startswith"
#     }

#     def get(self, request, category_id) :
#         search_filters  = {self.FILTER_NAMES[option] : request.GET[option] for option in request.GET} 
#         res = [{
#             "product_id"          : elem.id,  
#             "product_name"        : elem.product_name,    
#             "price"               : elem.price,           
#             "category"            : elem.category.id,        
#             "brand"               : elem.brand.id,          
#             "available_color"     : list(elem.available_color.values()),
#             "available_size_unit" : list(elem.available_size_unit.values()),
#             "model_thumbnail"     : elem.modelimages_set.values_list('model_image' ,flat=True)[0]
#         } for elem in BasicProducts.objects.filter(**search_filters, category_id=category_id)]
        
#         return JsonResponse({"items_for_category": res}, status=200)


#진입시 기본 세팅 : 앞면, 색상(이전페이지의 쿼리스트링 값)
#리스트 뷰에서 제공된 기본 정보를 프론트에서 계속 보유하고 있음을 가정

class CustomFoundation(View) :
    def get(self, request, product_id) :
        f_color = request.GET.get('color',None)
        a = SideImages.objects.select_related('basic_product').prefetch_related('side_name', 'color')
        
        if f_color == None :
            res = list(a.annotate(
                color_name = F('color__color_name'),
                hex_code = F('color__hex_code'),
                side = F('side_name__side_name')).filter(basic_product_id = product_id).values())
        
        else :
            res = list(a.annotate(
                color_name = F('color__color_name'),
                hex_code = F('color__hex_code'),
                side = F('side_name__side_name')).filter(
                    basic_product_id = product_id,
                    color__hex_code = f_color).values())
        return JsonResponse({"custom_foundation":res}, status=200)

class ProductDetailView(View) : 
    def get(self, request, product_id) :
        b = ProductInfo.objects.select_related('basic_product').prefetch_related('basic_product__modelimages_set')
        res = [{
            "product_id"          : a.basic_product_id,  
            "product_name"        : a.basic_product.product_name,    
            "price"               : a.basic_product.price,                   
            "available_color"     : list(a.basic_product.available_color.values()),
            "available_size_unit" : list(a.basic_product.available_size_unit.values()),    
            "description"         : a.description,
            "made_of"             : a.made_of,
            "made_by"             : a.made_by,
            "made_in"             : a.made_in,
            "elasitcity"          : a.elasticity,
            "texture"             : a.texture,
            "thickness"           : a.thickness,
            "care"                : a.care,
            "fitting_info"        : a.fitting_info,
            "model_images"        : list(a.basic_product.modelimages_set.values())
        } for a in b.filter(basic_product_id=product_id)]
        print(res)    
        return JsonResponse({'product_info':res}, status=200)

class SizeDetailView(View) :
    def get(self, request, product_id) :
        res = list(
            SizeFiguresForProducts.objects.annotate(
                unit_name = F('size_unit__size_unit'),
                part_name = F('part__part')).filter(
                basic_product_id=product_id).values())
        return JsonResponse({'size_detail':res}, status=200)


# class ProtoSet(View) :
#     def get(self, request, product_id) :
#         proto_color=request.GET.get('color', None)
#         if proto_color == None :
#             proto_set = SideImages.objects.annotate(
#                 side=F('side_name__side_name'),
#                 color_name=F('color__color_name'), 
#                 hex_code=F('color__hex_code')).filter(basic_product_id=product_id).values(
#                         'id','side_name','color_name', 'hex_code', 'side_image'
        
#         else : 
#             proto_color = request.GET['color']
#             proto_set = SideImages.objects.annotate(
#                 side=F('side_name__side_name'),
#                 color_name=F('color__color_name'), 
#                 hex_code=F('color__hex_code')).filter(
#                     basic_product_id=product_id,
#                     hex_code=proto_color).values(
#                         'id','side_name','color_name', 'hex_code', 'side_image')
        
#         return JsonResponse({'proto_set':list(proto_set)}, status=200)

# # 커스텀 화면의 기본 상품 사용 가능 색상표
# class ColorSet(View) :
#     def get(self, request, product_id) :
#         color_set = SideImages.objects.annotate(
#             name = F('color__color_name'), 
#             hex_code = F('color__hex_code')).filter(
#                 basic_product_id=product_id, 
#                 side_name_id=1).values('name', 'hex_code')
#         return JsonResponse({"color_set" : list(color_set)}, status=200)
 
# class FoundationSet(View) : 
#     def get(self, request, product_id) :
#         foundation = json.loads(request.body) 
#         foundation_set = SideImages.objects.annotate(
#             side = F('side_name__side_name'),
#             color_name = F('color__color_name'), 
#             hex_code = F('color__hex_code')).filter(
#                 basic_product_id = product_id,
#                 hex_code = foundation['hex_code']
#                 side = foundation['side_name']).values(
#                         'id','side_name','color_name', 'hex_code', 'side_image')
 
#         return JsonResponse({'foundation_set':list(foundation_set)}, status=200)

# class AvailableSizeUnitsView(View) :
#     def get(self, request, product_id) :
#         res = list(AvailableSizeUnits.objects.filter(basic_product_id=product_id).values())
#         return JsonResponse({'available_size_units':res}, status=200)

