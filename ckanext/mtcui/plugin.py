import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


import ckanext.mtcui.views as views
from ckanext.mtcui.logic import (
    action, auth, validators
)

# import ckanext.mtcui.cli as cli
# import ckanext.mtcui.helpers as helpers
# import ckanext.mtcui.views as views
# from ckanext.mtcui.logic import (
#     action, auth, validators
# )

class MtcuiPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "mtcui")
   
    # IAuthFunctions
    def get_auth_functions(self):
        return auth.get_auth_functions()

    # IActions
    def get_actions(self):
        return action.get_actions()

    # IBlueprint
    # def get_blueprint(self):
    #     return views.get_blueprint()

    # IClick
    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers
    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators
    # def get_validators(self):
    #     return validators.get_validators()
    
