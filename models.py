class Category(peewee.Model): #класс расширяет функционал
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length = 100, unique=True)
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'category'


class Product(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=100)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=10) #99999999,99 primer
    amount = peewee.IntegerField(null=False)
    category = peewee.ForeignKeyField(Category, related_name='products', to_field='id', on_delete='cascade')

    class Meta:
        database = db
        db_table = 'product'



# Category.create_table()
# Product.create_table()

# category = Category(name='game')
# category.save()






