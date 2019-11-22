
from django.db import models


#======== 커스텀 바탕이 되는 기본 view 생성에 쓰일 테이블=========

# 상품 기본 단위
class BasicProducts(models.Model):
    product_name      = models.CharField(max_length=100)
    price             = models.DecimalField(max_digits=8, decimal_places=2)
    category          = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True)
    brand             = models.ForeignKey('Brands', on_delete=models.CASCADE, null=True)
    available_color   = models.ManyToManyField('Colors', through='AvailableColors', null=True)
    available_size_unit = models.ManyToManyField('SizeUnits', through='AvailableSizeUnits', null=True )
    available_part = models.ManyToManyField('Parts', through='AvailableParts', null=True)

    class Meta:
        db_table = 'basic_products'


# brand 마플, 챔피온 등
class Brands(models.Model) :
    brand = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'brands'


# category 후드, 아우터, 티셔츠 등
class Categories(models.Model):
    category = models.CharField(max_length=20)

    class Meta:
        db_table = 'categories'


# 사이즈를 기준으로한 상품 최소 분류단위가 의류는 상품명, 폰케이스는 기종임.
# 상품의 성격이 그 자신으로서 완전하면 상품명,  폰, 노트북 등 원형 제품이 있어야 유의미하면 원형 제품의 제원 참조
class SizeUnits(models.Model) :
    size_unit = models.CharField(max_length=20)

    class Meta:
        db_table = 'size_units'


class AvailableSizeUnits(models.Model) :
    basic_product = models.ForeignKey(BasicProducts, on_delete=models.CASCADE, null=True)
    size_unit = models.ForeignKey(SizeUnits, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'available_size_units'


# 전체 색상표
class Colors(models.Model) :
    color_name = models.CharField(max_length=20)
    hex_code = models.CharField(max_length=20)

    class Meta:
        db_table = 'colors'


# 상품명에 따라 사용 가능 색상이 달라짐
class AvailableColors(models.Model) :
    basic_product = models.ForeignKey(BasicProducts, on_delete=models.CASCADE, null=True)
    color         = models.ForeignKey(Colors, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 'available_colors'


# 커스텀 가능영역 이미지
# 의류 : 카테고리별 영역 명칭 * 상품명별 생김새 * 사용 가능 색상
# 폰케이스 : 전면 * 상품명별 생김새 * 사용 가능 색상

class SideNames(models.Model) :
    side_name = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'side_names'


class AvailableSideNames(models.Model) :
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    side_name = models.ForeignKey(SideNames, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'available_side_names'


class SideImages(models.Model) :
    basic_product = models.ForeignKey(BasicProducts, on_delete=models.CASCADE, null=True)
    side_name = models.ForeignKey(SideNames, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE, null=True)
    side_image      = models.URLField(max_length=3000)

    class Meta:
        db_table = 'side_images'


#==========상세 사이즈 조견표 view 생성에 쓰일 테이블=========

# part 사이즈 측정 위치
# 의류 : 상품명에 따라 측정 부위 다름
# 폰케이스 : 상품타입에 따라 가로, 세로로 고정적임.
class Parts(models.Model) :
    part = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'parts'


class AvailableParts(models.Model):
    basic_product = models.ForeignKey(BasicProducts, on_delete=models.CASCADE, null=True) 
    part = models.ForeignKey(Parts, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 'available_parts'


class SizeFiguresForProducts(models.Model) :
    basic_product = models.ForeignKey(BasicProducts, on_delete=models.CASCADE, null=True)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE, null=True)
    size_unit = models.ForeignKey(SizeUnits, on_delete=models.CASCADE, null=True )
    size_figure  = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'size_figures_for_products'


#==========제품 상세정보 view 생성을 위한 테이블 ======== 

#of 소재, by 회사, in 나라
# 상품명에 따라 상세 정보가 달라짐
class ProductInfo(models.Model) :
    basic_product  = models.ForeignKey(BasicProducts, on_delete=models.CASCADE, null=True)
    description    = models.CharField(max_length=100)
    made_of        = models.CharField(max_length=20)
    made_by        = models.CharField(max_length=20)
    made_in        = models.CharField(max_length=20)
    elasticity     = models.CharField(max_length=20)
    texture        = models.CharField(max_length=20)
    thickness      = models.CharField(max_length=20)
    care           = models.CharField(max_length=500)
    fitting_info   = models.CharField(max_length=200)

    class Meta:
        db_table = 'product_info'


class ModelImages(models.Model) :
    basic_product = models.ForeignKey(BasicProducts, on_delete=models.CASCADE, null=True)
    model_image   = models.URLField(max_length=3000)

    class Meta:
        db_table = 'model_images'
