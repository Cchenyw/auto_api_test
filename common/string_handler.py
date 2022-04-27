import json


class StringHandler:
    def __init__(self, string):
        self.d_string = json.loads(string)
        self.keys = []

    def get_dict(self):
        return self.d_string

    def get_keys(self):
        return list(self.d_string.keys())

    def get_items(self, t_string=None, t_list=None):
        if t_string:
            for key, value in t_string.items():
                print(key, value)
                if isinstance(t_string[key], dict):
                    print('is dict')
                    self.get_items(t_string[key])
                elif isinstance(t_string[key], list):
                    print('is list')
                    self.get_items(t_list=t_string[key])
                else:
                    print('not at all')
        elif t_list:
            for value in t_list:
                print(value)
                if isinstance(value, dict):
                    print('is dict')
                    self.get_items(t_string=value)
                elif isinstance(value, list):
                    print('is list')
                    self.get_items(t_list=value)
                else:
                    print('not at all')
        else:
            for key, value in self.d_string.items():
                print(key, value)
                if isinstance(self.d_string[key], dict):
                    print('is dict')
                    self.get_items(t_string=self.d_string[key])
                elif isinstance(self.d_string[key], list):
                    print('is list')
                    self.get_items(t_list=self.d_string[key])
                else:
                    print('not at all')


if __name__ == "__main__":
    j_string = '''{
	"details": [{
		"_id": "6264b92c023a0e6ffca10c55_13243796852",
		"actual_billsec": 13,
		"ai_recommend_grade": 0,
		"answer": 1650768183000,
		"billsec": 13,
		"business_type": "",
		"call_status": 11,
		"call_time": 1650768176000,
		"can_get_sound_record": 1,
		"cdr_callback_timestamp": 1650768196910,
		"company_id": "5ecb9e2bd2da664d5daa70c1",
		"company_user_id": "612c9b6f824bcc0dc5dbe5cb",
		"contact": "--",
		"duration": "00:00:13",
		"encrypted_contact": "1xfR?(iS;&n",
		"end": 1650768196000,
		"enterprise": "--",
		"export_to_tungee_crm": 1,
		"finish_time": 1650768196910,
		"graph_id": "613721016938c656b15d0a92",
		"graph_name": "bert测试回调",
		"graph_status": 3,
		"graph_version": 1,
		"hangup": "client",
		"has_ai_recommend": 0,
		"intention": "其他",
		"is_op_test": false,
		"is_read": 1,
		"is_valid_conversation": 1,
		"number": "13243796852",
		"original_source": "robot",
		"port_id": "613703bae9e853734763317f",
		"port_type": "vendor",
		"reception_type": 1,
		"result": 1,
		"robot_id": "5ecb9ee37956835bac512c64",
		"robot_name": "电话机器人02",
		"sound_url": "master/recordings/sound/2022-04-24/6264b92c023a0e6ffca10c55_13243796852.10-42-56.13243796852.wav",
		"start": 1650768176000,
		"talk_round": 1,
		"task_id": "6264b92c023a0e6ffca10c55",
		"task_name": "外呼测试",
		"template_id": "tp001_wechat",
		"text_url": "master/recordings/text/2022-04-24/6264b92c023a0e6ffca10c55_13243796852.tsv",
		"tp_id": "",
		"tp_name": "--",
		"tp_source": "robot",
		"transfer_billsec": 0,
		"update_timestamp": 1650976152418,
		"vars": "[]",
		"vendor_line_id": "6101144baec0588a8067332f",
		"vendor_name": "青岛联通",
		"version_id": "613721016938c656b15d0a93",
		"wechat_user_id": null,
		"wechat_user_name": "--"
	}, {
		"_id": "62611499e9e853014e7cabbf_15521061508",
		"actual_billsec": 14,
		"ai_recommend_grade": 0,
		"answer": 1650529498000,
		"billsec": 14,
		"business_type": "",
		"call_status": 11,
		"call_time": 1650529491000,
		"can_get_sound_record": 1,
		"cdr_callback_timestamp": 1650529513525,
		"company_id": "5ecb9e2bd2da664d5daa70c1",
		"company_user_id": "6125088b6eceb92a91ea3420",
		"contact": "石家庄卡农商贸有限公司",
		"doncus_name": "有意向",
		"duration": "00:00:14",
		"encrypted_contact": "1vaO>.raL<$",
		"end": 1650529512000,
		"enterprise": "石家庄卡农商贸有限公司",
		"export_to_tungee_crm": 1,
		"finish_time": 1650529513525,
		"graph_id": "60c2d52e6938c60fd025eda6",
		"graph_name": "Bert测试话术",
		"graph_status": 3,
		"graph_version": 3,
		"hangup": "client",
		"has_ai_recommend": 0,
		"intention": "3s即可",
		"is_op_test": false,
		"is_read": 2,
		"is_valid_conversation": 1,
		"number": "15521061508",
		"original_source": "robot",
		"port_id": "61611318023a0e4ce17694c5",
		"port_type": "vendor",
		"reception_type": 1,
		"remark": "1234",
		"result": 1,
		"robot_id": "5ecb9ee37956835bac512c6b",
		"robot_name": "电话机器人09",
		"sound_url": "master/recordings/sound/2022-04-21/62611499e9e853014e7cabbf_15521061508.16-24-51.15521061508.wav",
		"start": 1650529491000,
		"talk_round": 0,
		"task_id": "62611499e9e853014e7cabbf",
		"task_name": "test直接发起",
		"template_id": "tp001_wechat",
		"text_url": "master/recordings/text/2022-04-21/62611499e9e853014e7cabbf_15521061508.tsv",
		"tp_id": "",
		"tp_name": "--",
		"tp_number_id": null,
		"tp_source": "robot",
		"transfer_billsec": 0,
		"update_timestamp": 1650976152277,
		"vendor_line_id": "61b17c1e8d4c1c74e4550df4",
		"vendor_name": "青岛联通",
		"version_id": "622b6d05e9e85320b5c7eb71",
		"wechat_user_id": null,
		"wechat_user_name": "--"
	}]
}'''
    sh = StringHandler(j_string)
    sh.get_keys()
    sh.get_items()
