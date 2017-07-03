# weixin_api
微信api的封装(部分，剩下的有时间补上)

## 使用方法(python版)
```
from wuest import wuest
resp = wuest.query_auth_acquired({ #参数包含了query参数和post_data参数，只要key能对应上就行
    "component_access_token": "xxx",
    "component_appid": "xxx",
    "authorization_code": "xxx"
})
print resp
```
