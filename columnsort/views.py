import operator
from functools import reduce

from django.db.models import Q
from django.views import generic

from .models import AddressList


class Address(generic.ListView):
    paginate_by = 100
    model = AddressList
    context_object_name = "address_list"

    def get_queryset(self, *args, **kwargs):

        address_list = super().get_queryset()

        q_query = []
        sort_order = "first"

        if self.request.GET.get("search_first"):
            q_query.append(Q(first__icontains=self.request.GET.get("search_first")))

        if self.request.GET.get("search_last"):
            q_query.append(Q(last__icontains=self.request.GET.get("search_last")))

        if self.request.GET.get("search_address"):
            q_query.append(Q(address__icontains=self.request.GET.get("search_address")))

        if self.request.GET.get("search_city"):
            q_query.append(Q(city__icontains=self.request.GET.get("search_city")))

        if self.request.GET.get("search_state"):
            q_query.append(Q(state__icontains=self.request.GET.get("search_state")))

        if self.request.GET.get("search_zip"):
            q_query.append(Q(zip__icontains=self.request.GET.get("search_zip")))

        if self.request.GET.get("sort_order"):
            sort_order = self.request.GET.get("sort_order")

        if q_query:
            address_list = address_list.filter(reduce(operator.and_, q_query)).order_by(
                sort_order
            )

            return address_list

        else:
            return AddressList.objects.all().order_by(sort_order)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_count"] = AddressList.objects.all().count()
        context["search_count"] = self.get_queryset().count()

        if self.request.GET.get("search_first"):
            context["search_first"] = self.request.GET["search_first"]

        if self.request.GET.get("search_last"):
            context["search_last"] = self.request.GET["search_last"]

        if self.request.GET.get("search_address"):
            context["search_address"] = self.request.GET["search_address"]

        if self.request.GET.get("search_city"):
            context["search_city"] = self.request.GET["search_city"]

        if self.request.GET.get("search_state"):
            context["search_state"] = self.request.GET["search_state"]

        if self.request.GET.get("search_zip"):
            context["search_zip"] = self.request.GET["search_zip"]

        if self.request.GET.get("sort_order"):
            context["sort_order"] = self.request.GET["sort_order"]

        return context

    def get_template_names(self):
        if self.request.htmx:
            return "columnsort/partials/address_list_partial.html"
        return "columnsort/address_list.html"
