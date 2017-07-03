# -*- coding: utf-8 -*-

"""
微信接口集合
"""

import requests
import json

API_METHOD_GET = 'get'
API_METHOD_POST = 'post'

WEIXIN_API = {
	'update_component_access_token': {  # 获取第三方access_token
		'method': API_METHOD_POST,
		'url': 'https://api.weixin.qq.com/cgi-bin/component/api_component_token',
		'querys': [],
		'params': ['component_appid', 'component_appsecret', 'component_verify_ticket']
	},
	'update_authorizer_access_token': {  # 更新公众号access_token
		'method': API_METHOD_POST,
		'url': 'https://api.weixin.qq.com/cgi-bin/component/api_authorizer_token?component_access_token={}',
		'querys': ['component_access_token'],
		'params': ['component_appid', 'authorizer_appid', 'authorizer_refresh_token']
	},
	'get_pre_auth_code': {  # 获取pre_auth_code
		'method': API_METHOD_POST,
		'url': 'https://api.weixin.qq.com/cgi-bin/component/api_create_preauthcode?component_access_token={}',
		'querys': ['component_access_token'],
		'params': ['component_appid']
	},
	'query_auth_acquired': {  # 用户扫码同意授权
		'method': API_METHOD_POST,
		'url': 'https://api.weixin.qq.com/cgi-bin/component/api_query_auth?component_access_token={}',
		'querys': ['component_access_token'],
		'params': ['component_appid', 'authorization_code']
	},
	'get_authorizer_info': {  # 获取授权公众号的信息
		'method': API_METHOD_POST,
		'url': 'https://api.weixin.qq.com/cgi-bin/component/api_get_authorizer_info?component_access_token={}',
		'querys': ['component_access_token'],
		'params': ['component_appid', 'authorizer_appid']
	},
	'create_scene_qrcode': { #创建带参数二维码
		'method': API_METHOD_POST,
		'url': 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token={}',
		'querys': ['access_token'],
		'params': ['action_name', 'action_info'] #{"action_name": "QR_LIMIT_STR_SCENE", "action_info": {"scene": {"scene_str": "123"}}}
	},
	'get_member_info': { #获取微信用户详细信息
		'method': API_METHOD_GET,
		'url': 'https://api.weixin.qq.com/cgi-bin/user/info?access_token={}&openid={}&lang=zh_CN',
		'querys': ['access_token', 'openid']
	}
}

class Wuest(object):
	def __init__(self):
		global WEIXIN_API

		def wrapper(api):
			def inner(data):
				url = api['url']
				query_names = api['querys']
				query_data = [data.get(query_name, None) for query_name in query_names]
				full_url = url.format(*query_data)
				print 'request_weixin======================='
				print full_url

				if api['method'] == API_METHOD_POST:
					params = api['params']
					post_data = {param: data.get(param, None) for param in params}
					return Wuest.__post(full_url, post_data)

				elif api['method'] == API_METHOD_GET:
					return Wuest.__get(full_url)

			return inner

		for func_name, api in WEIXIN_API.items():
			setattr(self, func_name, wrapper(api))

	@staticmethod
	def __get(url):
		resp = requests.get(url)
		resp_data = resp.json()

		print resp_data
		return resp_data

	@staticmethod
	def __post(url, post_data):
		print 'post data==========='
		print post_data
		resp = requests.post(url, json.dumps(post_data))
		resp_data = resp.json()

		print resp_data
		return resp_data

wuest = Wuest()
