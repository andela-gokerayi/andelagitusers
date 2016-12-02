import requests
import pprint
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomepageView(TemplateView):
    template_name = "gitusers.html"

    def get(self, request):
        args = dict()
        userlist = []
        api_res = self.get_api_results()
        for val in api_res:
            userlist.append(val)
        args["users"] = userlist
        return render(request, self.template_name, args)

    @staticmethod
    def get_api_results():
        pp = pprint.PrettyPrinter(indent=4)
        try:
            res = requests.get("https://api.github.com/orgs/andela/members")

            if res.status_code != 200:
                return "Something must be wrong somewhere"
            else:
                org = res.json()
                user = [users["url"]for users in org]
                user_id = [users["events_url"]for users in org]
                # print(user_id)
                for urls in user_id:
                    base_url = urls
                req = requests.get(base_url)
                print(req)
        except requests.ConnectionError as error:
            return error

        return user
