from django.db import models
from django.contrib.auth.models import Group
import random



class asset(models.Model):
    '''
        add item
        '''
    assetuid = models.CharField(max_length=64, verbose_name='唯一号', unique=True, default="1")  # add
    sn = models.CharField(max_length=64, verbose_name='序列号', unique=True)  # use
    asset_number = models.CharField(max_length=64, verbose_name='资产编号', null=True, blank=True)  # add
    asset_type_choices = (
        ("服务器", "服务器"),
        ("交换机", "交换机"),
    )
    asset_type = models.CharField(max_length=64, choices=asset_type_choices, verbose_name='资产类型', default="服务器")  # add
    asset_brand_choices = (
        ("SystemX 3650M5", "SystemX 3650M5"),
        ("ThinkSystem SR650", "ThinkSystem SR650"),
        ("ThinkSystem SR358F", "ThinkSystem SR358F"),
        ("ThinkServer RD630", "ThinkServer RD630"),
        ("ThinkServer RD640", "ThinkServer RD640"),
        ("ThinkServer RD650", "ThinkServer RD650"),
        ("ThinkServer RD430", "ThinkServer RD430"),
        ("ThinkServer RD530", "ThinkServer RD530"),
        ("ThinkServer RD550", "ThinkServer RD550"),
        ("ThinkServer RD350", "ThinkServer RD350"),
        ("HuaWei 2288H V5", "HuaWei 2288H V5"),
        ("万全 R520", "万全 R520"),
        ("万全 R510", "万全 R510"),
    )
    asset_brand = models.CharField(max_length=64, choices=asset_brand_choices, verbose_name='资产品牌',
                                   default="SystemX 3650M5")  # add
    room_choices = (
        ("A1", "A1"),
        ("D2", "D2"),
        ("B201", "B201"),
        ("B211", "B211"),
        ("C1", "C1"),
        ("G6", "G6"),
    )
    room = models.CharField(max_length=64, choices=room_choices, verbose_name='机房', null=True)  # add
    position = models.CharField(max_length=64, verbose_name='位置', null=True)  # use
    status_choices = (
        ("闲置", "闲置"),
        ("在用", "在用"),
    )
    status = models.CharField(max_length=64, choices=status_choices, verbose_name='状态', default="闲置")  # add
    buy_time = models.DateField(verbose_name="购买时间", default="1970-01-01")  # add
    free_repair = models.CharField(max_length=64, verbose_name='保修期', null=True, blank=True)  # add
    person_incharge_choices = (
        ("崔先锋", "崔先锋"),
        ("邓建", "邓建"),
        ("方方", "方方"),
        ("付义展", "付义展"),
        ("高瞻", "高瞻"),
        ("韩晓磊", "韩晓磊"),
        ("孙雷", "孙雷"),
        ("汤文军", "汤文军"),
        ("冷显慧", "冷显慧"),
        ("高绍阳", "高绍阳"),
        ("李福鑫", "李福鑫"),
        ("于晓辉", "于晓辉"),
        ("常井志", "常井志"),
        ("高菁华", "高菁华"),
        ("外借", "外借"),
        ("无法查找", "无法查找"),
    )
    person_incharge = models.CharField(max_length=64, choices=person_incharge_choices, verbose_name='挂账人',
                                       default="冷显慧")  # add
    # person_ops = models.CharField(max_length=64, verbose_name='运维负责人', null=True, blank=True)  # add
    project = models.CharField(max_length=64, verbose_name='项目', null=True, blank=True)  # add
    team_choices = (
        ("高瞻", "高瞻"),
        ("刘军", "刘军"),
        ("马亮亮", "马亮亮"),
        ("Betty", "Betty"),
        ("张剑鸣", "张剑鸣"),
        ("吴娟", "吴娟"),
        ("AI", "AI"),
        ("段立功", "段立功"),
        ("谢刚", "谢刚"),
        ("李曈", "李曈"),
        ("李蕾", "李蕾"),
        ("杨杰", "杨杰"),

    )
    team = models.CharField(max_length=64, choices=team_choices, verbose_name='团队', null=True, blank=True)  # add
    role = models.CharField(max_length=64, verbose_name='角色', null=True, blank=True)  # add
    use_man_choices = (
        ("王正浩", "王正浩"),
        ("宋晓丽", "宋晓丽"),
        ("马亮亮", "马亮亮"),
        ("高瞻", "高瞻"),
        ("张浩南", "张浩南"),
        ("杨碧波", "杨碧波"),
        ("吴娟", "吴娟"),
        ("张剑鸣", "张剑鸣"),
        ("高绍阳", "高绍阳"),
        ("高菁华", "高菁华"),
        ("段立功", "段立功"),
        ("崔先锋", "崔先锋"),
        ("吴刚", "吴刚"),
        ("刘军", "刘军"),
        ("李蕾", "李蕾"),
        ("刘峰", "刘峰"),
        ("张志正", "张志正"),
        ("谢刚", "谢刚"),
        ("胡伟", "胡伟"),
        ("陶光庆", "陶光庆"),
        ("郭振辉", "郭振辉"),
        ("胡伟", "胡伟"),
        ("孙雷", "孙雷"),
        ("萧曙光", "萧曙光"),
        ("郭庆萍", "郭庆萍"),


    )
    use_man = models.CharField(max_length=64, choices=use_man_choices, verbose_name='使用人', null=True, blank=True)  # add
    remark = models.CharField(max_length=64, verbose_name='备注', null=True, blank=True)  # add

    give_time = models.DateField(verbose_name="外借时间", null=True, blank=True)  # add
    back_time = models.DateField(verbose_name="归还时间", null=True, blank=True)  # add

    #################

    hostname = models.CharField(max_length=64, verbose_name='主机名', null=True,blank=True)
    network_ip = models.GenericIPAddressField(verbose_name='外网IP',unique=True)
    manage_ip = models.GenericIPAddressField(verbose_name='管理IP', null=True,blank=True)
    inner_ip = models.GenericIPAddressField(verbose_name='内网IP', null=True,blank=True)
    port = models.IntegerField(verbose_name='ssh端口', null=True,blank=True,default="22")
    model = models.CharField(max_length=128, verbose_name='型号', null=True,blank=True)
    system = models.CharField(max_length=128,verbose_name='系统版本',null=True,blank=True)

    eth0 = models.CharField(max_length=64, verbose_name="网卡1mac地址", null=True, blank=True)
    eth1 = models.CharField(max_length=64, verbose_name="网卡2mac地址", null=True, blank=True)
    eth2 = models.CharField(max_length=64, verbose_name="网卡3mac地址", null=True, blank=True)
    eth3 = models.CharField(max_length=64, verbose_name="网卡4mac地址", null=True, blank=True)


    system_user = models.ForeignKey(to="system_users",to_field='id',on_delete=models.SET_NULL, null=True,verbose_name='登陆用户',blank=True)
    data_center =  models.ForeignKey(to="data_centers",to_field='id',on_delete=models.SET_NULL, null=True,verbose_name='数据中心')
    cabinet = models.CharField(max_length=64,verbose_name='机柜',null=True,blank=True)
    # position = models.CharField(max_length=64,verbose_name='位置',null=True,blank=True)


    # sn = models.CharField(max_length=64,verbose_name='序列号',null=True,blank=True)
    cpu = models.CharField(max_length=64,verbose_name='CPU',null=True,blank=True)
    memory = models.CharField(max_length=64, verbose_name='内存', null=True,blank=True)
    disk = models.CharField(max_length=256,verbose_name="硬盘",null=True,blank=True)
    uplink_port = models.CharField(max_length=256,verbose_name="上联端口",null=True,blank=True)

    ship_time = models.DateField(verbose_name="出厂时间",default="1970-01-01")
    end_time = models.DateField(verbose_name="到保时间",default="1970-01-01")

    product_line =  models.ForeignKey(to=Group,to_field='id',on_delete=models.SET_NULL,verbose_name='产品线',null=True)


    is_active = models.BooleanField(default=True, verbose_name=('是否启用'))
    ps = models.CharField(max_length=1024,verbose_name="备注",null=True,blank=True)
    file = models.FileField(upload_to = 'assets/%Y%m%d{}'.format(random.randint(0,99999)),verbose_name="文件",null=True,blank=True,default=None)

    ctime= models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间',blank=True)
    utime = models.DateTimeField(auto_now=True, null=True,verbose_name='更新时间',blank=True)


    class  Meta:
        db_table ="asset"
        verbose_name="资产管理"
        verbose_name_plural = '资产管理'
        permissions = {
            ('read_asset',u"只读资产管理"),
            ('task_asset', u"执行资产"),
        }


    def __str__(self):
        return self.network_ip


class   data_centers(models.Model):
    data_center_list = models.CharField(max_length=128, verbose_name='数据中心', null=True)


    class Meta:
        db_table = "data_centers"
        verbose_name = "数据中心"
        verbose_name_plural = '数据中心'

    def __str__(self):
        return self.data_center_list


class  system_users(models.Model):

    name = models.CharField(max_length=255, unique=True,verbose_name='名称')
    username = models.CharField(max_length=64,null=True,blank=True, verbose_name=('登陆用户'),default='root')
    password = models.CharField(max_length=255, blank=True,null=True,verbose_name=('登陆密码'))
    product_line = models.ForeignKey(to=Group, to_field='id', on_delete=models.SET_NULL, verbose_name='产品线',null=True)
    ps = models.CharField(max_length=1024,verbose_name="备注",null=True,blank=True)
    ctime= models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间',blank=True)
    utime = models.DateTimeField(auto_now=True, null=True,verbose_name='更新时间',blank=True)

    def __str__(self):
        return self.name

    class  Meta:
        db_table ="system_users"
        verbose_name="系统登陆用户"
        verbose_name_plural = '系统登陆用户'
        permissions = {
            ('read_system_users',u"只读系统登陆用户"),
        }



class performance(models.Model):

    cpu_use = models.CharField(verbose_name='CPU使用率', null=True,blank=True,max_length=32)
    mem_use = models.CharField(verbose_name='内存使用率', max_length=32, null=True,blank=True)
    in_use = models.CharField(verbose_name='进流量', max_length=32, null=True,blank=True)
    out_use = models.CharField(verbose_name='出流量', max_length=32, null=True,blank=True)
    server = models.ForeignKey('asset',on_delete=models.CASCADE,)



    cdate = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    udate = models.DateTimeField(auto_now=True, verbose_name='更新时间')


    class Meta:
        db_table = 'performance'
        verbose_name = '监控状态'
        verbose_name_plural = verbose_name
        ordering = ["cdate"]

    def __str__(self):
        return self.cpu_use


class web_history(models.Model):
    user = models.CharField(max_length=32, verbose_name='登录用户', null=True)
    ip = models.GenericIPAddressField(verbose_name='用户地址',null=True)
    login_user = models.CharField(max_length=32,verbose_name='所用账号',null=True)
    host = models.CharField(max_length=32,verbose_name='登录主机',null=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    class  Meta:
        db_table ="web_history"
        verbose_name="历史登录"
        verbose_name_plural = '历史登录'


    def __str__(self):
        return self.user
