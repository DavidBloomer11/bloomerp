# ---------------------------------
# The URL patterns for the BloomerpEngine
# This file is responsible for generating the URL patterns for the BloomerpEngine
# ---------------------------------
from django.urls import include, path,  register_converter
from django.contrib.auth import views as auth_views
from django.contrib.contenttypes.models import ContentType
from bloomerp.views.core import (BloomerpForeignRelationshipView)

from bloomerp.views.document_templates import router as document_template_router
from django.db.models import Model
from bloomerp.utils.models import (
    get_attribute_name_for_foreign_key, 
    model_name_plural_underline, 
    model_name_plural_slug,
    get_foreign_occurences_for_model,
    get_model_dashboard_view_url,
    get_bulk_upload_view_url,
    get_base_model_route,
    get_detail_view_url,
    get_create_view_url,
    get_list_view_url,
    get_update_view_url
    )
from bloomerp.utils.api import generate_serializer, generate_model_viewset_class
from bloomerp.views.api import BloomerpModelViewSet
from bloomerp.models import Link
from bloomerp.utils.urls import IntOrUUIDConverter
from rest_framework.routers import DefaultRouter
from bloomerp.utils.router import _get_routers_from_settings, RouteFinder, BloomerpRouterHandler

# Register the custom URL converter
register_converter(IntOrUUIDConverter, 'int_or_uuid') # Register the custom URL converter
drf_router = DefaultRouter()

# Get the base URL from the settings
from django.conf import settings
BASE_URL = settings.BLOOMERP_SETTINGS.get('BASE_URL', '')

# Custom routers
from bloomerp.views.workspace import router as dashboard_router
from bloomerp.views.core import router as core_router
from bloomerp.views.widgets import router as widget_router
from bloomerp.views.auth import router as auth_router
custom_routers = _get_routers_from_settings()


custom_routers.append(document_template_router)
custom_routers.append(dashboard_router)
custom_routers.append(core_router)
custom_routers.append(widget_router)
custom_routers.append(auth_router)


custom_router_handler = BloomerpRouterHandler(custom_routers)
custom_router_handler.generate_links()

# ---------------------------------
# START GENERATION OF URL PATTERNS
#
#           ___/\___
#          |        |
#         /|  O  O  |\      ankers away!
#        / |   ||   | \
#       /  |  ----  |  \
#      |   |  ||||  |   |
#      |  /|  ||||  |\  |
#      \/  |________|  \/
#           |      |
#           |______|
#           |  ||  |
#           |  ||  |
#          /|  ||  |\
#         / |______| \
#         |__________|
#
#           *   *   *
#          *  * * *  *
#         *  *  *  *  *
#        *  *   *   *  *
#       *  *    *    *  *
# ---------------------------------



# ---------------------------------
# Auth related URL patterns
# ---------------------------------
from django.conf import settings

from django.urls import reverse_lazy
urlpatterns = [
    path(settings.LOGIN_URL, auth_views.LoginView.as_view(
            template_name='auth_views/login_view.html',
            next_page=reverse_lazy('bloomerp_home_view')
            ), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
]

# ---------------------------------
# App level routes
# ---------------------------------
app_level_routes = custom_router_handler.get_app_routes()
for route in app_level_routes:
    urlpatterns.append(route.create_urlpattern())


# ---------------------------------
# Model related URL patterns
# ---------------------------------
content_types = ContentType.objects.all()
for content_type in content_types:
    if content_type.model_class():
        # Detail view patterns
        detail_view_patterns = []
        
        # Initialize some variables
        model : Model = content_type.model_class()
        base_model_route = get_base_model_route(model, include_slash=False) # Example: CustomerInvoice -> customer-invoices
        model_name_underline = model_name_plural_underline(model)
        model_name_plural = model._meta.verbose_name_plural
        model_name = model._meta.verbose_name


    	# ---------------------------------
        # Related models
        # ---------------------------------
        for related_model in get_foreign_occurences_for_model(model):
            related_model:Model
            related_model_name_underline = model_name_plural_underline(related_model)
            related_base_model_route = model_name_plural_slug(related_model)
            url_name = f"{model_name_underline}_detail_{related_model_name_underline}"

            # Get application field
            foreign_model_attribute = get_attribute_name_for_foreign_key(related_model, model)

            if foreign_model_attribute:
                # Add related model to the tabs

                urlpatterns.append(
                    path(f"{base_model_route}/<int_or_uuid:pk>/{related_base_model_route}/", 
                        BloomerpForeignRelationshipView.as_view(
                            model=model,
                            foreign_model = related_model,
                            foreign_model_detail_url = f"{related_model_name_underline}_detail",
                            foreign_model_attribute = foreign_model_attribute), 
                        name=url_name))

                Link.objects.get_or_create(
                    content_type=content_type,
                    name=f"{model_name} {related_model._meta.verbose_name_plural}",
                    url=url_name,
                    level = 'DETAIL',
                    is_absolute_url = False,
                    description = f"Related {related_model._meta.verbose_name_plural} view for {model_name}"
                )

        
        # ---------------------------------
        # Custom routes
        # ---------------------------------
        custom_detail_view_routes = custom_router_handler.get_detail_view_routes_for_model(model)
        custom_list_view_routes = custom_router_handler.get_list_view_routes_for_model(model)
            
        for route in custom_detail_view_routes:
            # create the URL pattern
            urlpatterns.append(route.create_urlpattern())


        for route in custom_list_view_routes:
            # create the URL pattern
            urlpatterns.append(route.create_urlpattern())
            

        # ---------------------------------
        # Rest framework URL patterns
        # ---------------------------------
        # Generate the serializer class
        serializer_class = generate_serializer(model)

        # Generate the viewset class
        ApiViewSet = generate_model_viewset_class(
            model=model,
            serializer=serializer_class,
            base_viewset=BloomerpModelViewSet
        )

        drf_router.register(
            prefix = model_name_plural_underline(model), 
            viewset = ApiViewSet, 
            basename=model_name_plural_underline(model)
            )
        
        # ---------------------------------
        # Add the model to the admin dashboard
        # ---------------------------------
        from django.contrib import admin
        from django.contrib.admin.sites import AlreadyRegistered
        try:
            admin.site.register(model)
        except AlreadyRegistered:
            pass


# ---------------------------------
# API URL patterns
# ---------------------------------
urlpatterns += [
    path('api/', include(drf_router.urls))
]

# ---------------------------------
# Route decorator
# ---------------------------------
route_finder = RouteFinder(directory='components', prefix='components/')
urlpatterns += route_finder.generate_urlpatterns()



# ---------------------------------
# Create path
# ---------------------------------

BLOOMERP_URLPATTERNS = path(BASE_URL, include(urlpatterns))
