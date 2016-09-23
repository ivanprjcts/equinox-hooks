
import requests
import logging
import re

__logger__ = logging.getLogger(__name__)

HOOK_ID = "id"
HOOK_LATCH_STATUS = "latch_status"
HOOK_REQUEST = "request"
HOOK_REQUEST_METHOD = "method"
HOOK_REQUEST_HEADERS = "headers"
HOOK_REQUEST_BODY = "body"
HOOK_REQUEST_URL = "url"
HOOK_REGEX_ENABLE = "regex_enable"
HOOK_REGEX = "regex"
HOOK_RESPONSE_ENABLE = "response_enable"

LATCH_STATUS_ON = "on"
LATCH_STATUS_OFF = "off"


def get_raw_headers(header_list):
    full_response_raw = ""
    for header in header_list:
        full_response_raw += "{key}: {value}\n".format(key=header, value=header_list[header])

    return full_response_raw


def execute_hook(hook_list, status):
    for hook in hook_list:
        if hook[HOOK_LATCH_STATUS] == status:
            request_data = hook
            print ("Executing request: %s" % request_data)
            response = requests.request(method=request_data[HOOK_REQUEST_METHOD],
                                        url=request_data[HOOK_REQUEST_URL],
                                        data=request_data[HOOK_REQUEST_BODY],
                                        #headers=request_data[HOOK_REQUEST_HEADERS],
                                        verify=False)
            print ("> Response status: \n%s" % response.status_code)
            print ("> Response headers: \n%s" % response.headers)
            print ("> Response body: \n%s" % response.text)

            full_response_raw = get_raw_headers(response.headers)
            full_response_raw += response.text

            print ("> Full response: \n%s" % full_response_raw)

            """
            if hook[HOOK_RESPONSE_ENABLE]:
                # Save response into BD > full_response_raw
                pass
            elif hook[HOOK_REGEX_ENABLE]:
                # Save response into BD after matching Regex
                match_result_list = re.findall("Content-Type: (.*)", full_response_raw)
                print "Match list:", match_result_list
                if match_result_list:
                    match_result_list_raw = ""
                    for match_result in match_result_list:
                        match_result_list_raw += match_result + "\n"
                    print ("Match: %s" % match_result_list_raw)
                else:
                    print ("no matching")
            """

if __name__ == '__main__':

    hook_list = [
        {
            "id": 1,
            "latch_status": "ON",
            "request": {
                "method": "POST",
                "url": "http://demo8299546.mockable.io/test1",
                "headers": {"Content-Type": "application/json", "Token": "lalalala"},
                "body": " {\"\"} "
            },
            "response_enable": False,
            "regex_enable": True,
            "regex": "Content-Type: (.*)"
        },
        {
            "id": 2,
            "latch_status": "OFF",
            "request": {
                "method": "POST",
                "url": "http://demo8299546.mockable.io/test1",
                "headers": {"Content-Type": "application/json", "Token": "lalalala"},
                "body": " {\"\"} "
            },
            "response_enable": True,
            "regex_enable": True,
            "regex": "{}"
        },
        {
            "id": 3,
            "latch_status": "OFF",
            "request": {
                "method": "POST",
                "url": "http://demo8299546.mockable.io/test1",
                "headers": {"Content-Type": "application/json", "Token": "lalalala"},
                "body": " {\"\"} "
            },
            "response_enable": True,
            "regex_enable": True,
            "regex": "{}"
        }
    ]

    execute_hook(hook_list, LATCH_STATUS_ON)
