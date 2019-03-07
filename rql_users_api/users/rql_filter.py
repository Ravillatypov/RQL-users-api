from django.db.models import Q
from rest_framework.filters import BaseFilterBackend
from pyrql.parser import Parser

class RQLFilterBackend(BaseFilterBackend):
    """
    RQL filter backend class for DRF
    implement filter functions: `eq, in, and, or`
    """
    filterset_fields = ()
    query_name = 'q'
    _functions = ('in', 'eq', 'and', 'or')

    def get_filterset_fields(self, view):
        """
        get filterset_fields from view
        """
        self.filterset_fields = getattr(view, 'filterset_fields', ())
        return self.filterset_fields
    
    def get_conditions(self, args):
        """
        method `get_conditions` parse function name and arguments
        if function is implemented, call with arguments.
        return `django.db.models.Q` object 
        """
        func_name = args.get('name', '')
        if func_name not in self._functions:
            return NotImplementedError(f"Bad query: function {func_name} is not implemented")
        func = getattr(self, '_' + func_name, None)
        func_args = args.get('args', None)
        if isinstance(func_args, list) and len(func_args) > 1 and func_args[0] in self.filterset_fields:
            return func(func_args)
        return Q()

    def _in(self, args):
        return Q(**{args[0] + '__in': args[1:]})

    def _eq(self, args):
        if len(args) == 2:
            return Q(**{args[0]: args[1]})
        return Q()

    def _and(self, args):
        result = Q()
        for a in args:
            result = result & self.get_conditions(a)
        return result

    def _or(self, args):
        result = Q()
        for a in args:
            result = result | self.get_conditions(a)
        return result

    def filter_queryset(self, request, queryset, view):
        self.get_filterset_fields(view)
        parser = Parser()
        try:
            self.rql = parser.parse(request.GET.get(self.query_name))
        except:
            return queryset
        conditions = self.get_conditions(self.rql)
        try:
            filtered = queryset.filter(conditions)
        except:
            filtered = queryset
        return filtered
