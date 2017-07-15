# WIKI

## PAGE

1. 首页
2. 文章列表
3. 文章
4. 文章添加页
5. 关于       // 静态页

## API

title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'作者', on_delete=models.CASCADE)
    digest = models.TextField(blank=True, null=True)  # 文章摘要
    pub_time = models.DateField(auto_now_add=True)  # 发布日期
    content = models.TextField(blank=True, null=True)  # 文章正文
    view = models.BigIntegerField(default=0)  # 阅读数


>
    获取文章列表
    url: /article/get_articles
    params:
    return: {
        rtnCode: 0,
        rtnMsg: 'ok',
        data: {
            articles: [
                {
                    id: 'id',
                    title: '标题1',
                    author: '周智'，
                    digest: '文章摘要文章摘要文章摘要'，
                    pub_time: 1499497266249,            // 发布时间 long
                    content: '段落1\n段落2',
                    view: 0                             // 阅读数
                }
                ...
            ]
        }
    }

    文章
    url: /article/get_article
    params: id
    return: {
        rtnCode: 0,
        rtnMsg: 'ok',
        data: {
            id: 'id',
            title: '标题1',
            author: '周智'，
            digest: '文章摘要文章摘要文章摘要'，
            pub_time: 1499497266249,            // 发布时间 long
            content: '段落1\n段落2',
            view: 0
        }
    }

    文章添加
    url: /article/add_article
    params: {
        title: 'xxx',
        digest: '摘要'
        content: [
            '段落一内容',
            '段落二内容',
            '段落三内容',
            ....
        ]
    }