from django.db import models
from DjangoUeditor.models import UEditorField
from faker import Factory   #作假数据
import random
# Create your models here.

class TypeInfo(models.Model):       #index product info
    ttitle = models.CharField('TypeName',max_length=20)
    isDelete = models.BooleanField('IfDelete', default=False)   #if deleted 
    def __str__(self):
        return self.ttitle
    class Meta:
        db_table = "typeinfo"
        verbose_name = 'TypeInfo'
        verbose_name_plural = 'TypeInfo'

class GoodsInfo(models.Model):      # product Info
    gtitle = models.CharField('gtitle', max_length=20)
    gpic = models.ImageField('gpic',upload_to='df_goods', null=True, blank=True)      #product image
    gprice = models.DecimalField('gprice',max_digits=7, decimal_places=2)        
    gunit = models.CharField('unit',max_length=20, default='500g')     # unit for per product
    gclick = models.IntegerField('gclick')          # click by users and calculate popularity
    isDelete = models.BooleanField('ifdeleted',default=False)
    gjianjie = models.CharField('descrition',max_length=200)     #description for per product
    gkucun = models.IntegerField('stock')          #inventory
    grelated = models.CharField('grelated',max_length=1000)
    gcontent = UEditorField('detail', height=300, width=1000)                  #detail info for goods
    gtype = models.ForeignKey(TypeInfo, verbose_name='type', on_delete=models.CASCADE)     #type
    gasin = models.CharField('gasin',max_length=200) 
    # gadv = models.BooleanField(default=False)   #recommendation
    class Meta:
        db_table = "goodsinfo"
        verbose_name = 'productinfo'
        verbose_name_plural = 'productinfo'

class ReviewInfo(models.Model):      #Review for products from users
    reviewText = models.TextField('reviewText')     
    overall = models.CharField('orverall',max_length=10)          
    reviewerID = models.CharField('reviewerID', max_length=40)                 
    reviewerName = models.CharField('reviewerName', max_length=1000) 
    asin = models.CharField('asin',max_length=200) 
     
    class Meta:
        db_table = "Reviews_Movie"
        verbose_name = 'reviewinfo'
        verbose_name_plural = 'reviewinfo'

#
# TypeInfo_list = TypeInfo.objects.all()
# print(TypeInfo_list)
# fake = Factory.create()   #
# for i in range(0,300):
#     j = random.randint(0, 100)
#     s1 = random.randint(0, 100)
#     s2 = random.randint(0, 100)
#     k = random.randint(0, 5)
#     v = GoodsInfo(
#         gtitle=fake.text(max_nb_chars=10),
#         gpic='df_goods/goods.jpg',
#         gprice=j,
#         gunit='500g',
#         gclick=0,
#         isDelete=fake.pybool(),   #
#         gjianjie=fake.text(max_nb_chars=70),
#         gkucun=s2,
#         gcontent=fake.text(max_nb_chars=300),
#         gtype=TypeInfo_list[k],   #
#     )
#     v.save()

# INSERT INTO goodsinfo
# (gasin,gtitle,gpic,gprice,gunit,gclick,isDelete,gtype_id,brand,gsalesRank,grelated)
# select asin,title,imUrl,price,'set',0,0,1,brand,salesRank,related
# from Movie_TV
# where title is not null and price is not null and imUrl is not null;

# INSERT INTO goodsinfo
# (gasin,gtitle,gpic,gprice,gunit,gclick,isDelete,gtype_id,brand,gsalesRank,grelated)
# select asin,title,imUrl,price,'set',0,0,2,brand,salesRank,related
# from Music
# where title is not null and price is not null and imUrl is not null;

# INSERT INTO goodsinfo
# (gasin,gtitle,gpic,gprice,gunit,gclick,isDelete,gtype_id,brand,gsalesRank,grelated)
# select asin,title,imUrl,price,'set',0,0,5,brand,salesRank,related
# from Games
# where title is not null and price is not null and imUrl is not null;

# INSERT INTO goodsinfo
# (gasin,gtitle,gpic,gprice,gunit,gclick,isDelete,gtype_id,brand,gsalesRank,grelated)
# select asin,title,imUrl,price,'set',0,0,4,brand,salesRank,related
# from Tools
# where title is not null and price is not null and imUrl is not null;

# INSERT INTO goodsinfo
# (gasin,gtitle,gpic,gprice,gunit,gclick,isDelete,gtype_id,brand,gsalesRank,grelated)
# select asin,title,imUrl,price,'set',0,0,3,brand,salesRank,related
# from CDs
# where title is not null and price is not null and imUrl is not null;

# INSERT INTO goodsinfo
# (gasin,gtitle,gpic,gprice,gunit,gclick,isDelete,gtype_id,brand,gsalesRank,grelated)
# select asin,title,imUrl,price,'set',0,0,6,brand,salesRank,related
# from CellPhones
# where title is not null and price is not null and imUrl is not null;



# SELECT campaign_id, from_number, received_msg, date_received
#   FROM `received_txts`
#  WHERE `campaign_id` = '8'
 	
# ALTER TABLE goodsinfo MODIFY COLUMN ;
# ALTER TABLE users MODIFY address VARCHAR(255);
# ALTER TABLE tablename ADD columnname datatype
# ALTER TABLE tablename DROP COLUMN columname;
# ALTER TABLE users ADD uid INT UNSIGNED NOT NULL AUTO_INCREMENT,
# ADD UNIQUE (uid);
