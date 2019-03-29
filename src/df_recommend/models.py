from django.db import models
from DjangoUeditor.models import UEditorField
from faker import Factory   
import random
# Create your models here.

class TypeInfo(models.Model):       
    ttitle = models.CharField('TypeName',max_length=20)
    isDelete = models.BooleanField('IfDelete', default=False)   
    def __str__(self):
        return self.ttitle
    class Meta:
        db_table = "typeinfo"
        verbose_name = 'TypeInfo'
        verbose_name_plural = 'TypeInfo'

class GoodsInfo(models.Model):     
    gtitle = models.CharField('name', max_length=20)
    gpic = models.ImageField('image',upload_to='df_goods', null=True, blank=True)    
    gprice = models.DecimalField('price',max_digits=7, decimal_places=2)        
    gunit = models.CharField('unit',max_length=20, default='500g')    
    gclick = models.IntegerField('countclick')          
    isDelete = models.BooleanField('ifdeleted',default=False)
    gjianjie = models.CharField('descrition',max_length=200)    
    gkucun = models.IntegerField('stock')         
    grelated = models.CharField('grelated',max_length=1000)
    galso_buy = models.CharField('galso_buy',max_length=1000)
    galso_view = models.CharField('galso_view',max_length=1000)
    gbuy_after = models.CharField('gbuy_after',max_length=1000)
    gbuy_together = models.CharField('gbuy_together',max_length=1000)
    gcontent = UEditorField('detail', height=300, width=1000)                 
    gtype = models.ForeignKey(TypeInfo, verbose_name='type', on_delete=models.CASCADE)    
    gasin = models.CharField('gasin',max_length=200) 
    # gadv = models.BooleanField(default=False)  
    class Meta:
        db_table = "goodsinfo"
        verbose_name = 'productinfo'
        verbose_name_plural = 'productinfo'

#
# TypeInfo_list = TypeInfo.objects.all()
# print(TypeInfo_list)
# fake = Factory.create()   
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
#         isDelete=fake.pybool(),   
#         gjianjie=fake.text(max_nb_chars=70),
#         gkucun=s2,
#         gcontent=fake.text(max_nb_chars=300),
#         gtype=TypeInfo_list[k],   
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
