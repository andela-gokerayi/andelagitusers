import requests
import pprint
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

# Create your views here.
class HomepageView(TemplateView):
    template_name = "gitusers.html"

    def get(self, request):
        args = dict()
        userlist = dict()
        api_res = self.get_api_results()
        userlist["val"] = api_res
        args["users"] = userlist["val"]
        return render(request, self.template_name, args)

    @staticmethod
    def get_api_results():
        try:
            res = requests.get("https://api.github.com/orgs/andela/members?since=135")

            if res.status_code != 200:
                return "Something must be wrong somewhere"
            else:
                org = res.json()
                user = [users["url"]for users in org]

        except requests.ConnectionError as error:
            return error

        return user

class CommitView(TemplateView):
    template_name = "commit.html"

    def get(self, request):
        args = dict()
        user_url = request.GET.get('filter','')
        commit_msg = self.commits(user_url)
        args["commits"] = commit_msg
        return render(request, self.template_name, args)

    @staticmethod
    def commits(url):
        msg = []
        fellow_event = requests.get(url).json()
        event_url = fellow_event["events_url"]
        real_url = event_url[:-10]
        req = requests.get(real_url).json()

        [i for i in req if i !=0]
        user_payload = i["payload"]

        if "commits" in user_payload:
            cmmt_msg = user_payload["commits"][0]["message"]
            msg.append(cmmt_msg)

        if len(msg) == 0:
            message = ("User hasn't committed any code in a while.")
            msg.append(message)
            return msg
        else:
            return msg
