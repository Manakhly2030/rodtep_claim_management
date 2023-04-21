from . import __version__ as app_version

app_name = "rodtep_claim_management"
app_title = "Rodtep Claim Management"
app_publisher = "FinByz"
app_description = "Rodtep Claim Management"
app_email = "info@finbyz.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rodtep_claim_management/css/rodtep_claim_management.css"
# app_include_js = "/assets/rodtep_claim_management/js/rodtep_claim_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/rodtep_claim_management/css/rodtep_claim_management.css"
# web_include_js = "/assets/rodtep_claim_management/js/rodtep_claim_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rodtep_claim_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "rodtep_claim_management.utils.jinja_methods",
#	"filters": "rodtep_claim_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rodtep_claim_management.install.before_install"
# after_install = "rodtep_claim_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rodtep_claim_management.uninstall.before_uninstall"
# after_uninstall = "rodtep_claim_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rodtep_claim_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events={
    "Rodtep Claimed Management":{
        "on_submit":"rodtep_claim_management.rodtep_claim_management.doctype.rodtep_claimed_management.rodtep_claimed_management.create_jv_on_submit"
    },
    "Duty DrawBack Claim Management":{
        "on_submit":"rodtep_claim_management.rodtep_claim_management.doctype.duty_drawback_claim_management.duty_drawback_claim_management.create_jv_on_submit"
    },
    "Sales Invoice":{
    "validate":"rodtep_claim_management.rodtep_claim_management.doc_events.sales_invoice.validate",
    "on_submit": "rodtep_claim_management.rodtep_claim_management.api.si_on_submit",
	"on_cancel": "rodtep_claim_management.rodtep_claim_management.api.si_on_cancel"}
}

doctype_js = {
	"Sales Invoice" : "public/js/sales_invoice.js",
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"rodtep_claim_management.tasks.all"
#	],
#	"daily": [
#		"rodtep_claim_management.tasks.daily"
#	],
#	"hourly": [
#		"rodtep_claim_management.tasks.hourly"
#	],
#	"weekly": [
#		"rodtep_claim_management.tasks.weekly"
#	],
#	"monthly": [
#		"rodtep_claim_management.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "rodtep_claim_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "rodtep_claim_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "rodtep_claim_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["rodtep_claim_management.utils.before_request"]
# after_request = ["rodtep_claim_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["rodtep_claim_management.utils.before_job"]
# after_job = ["rodtep_claim_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"rodtep_claim_management.auth.validate"
# ]

fixtures = [
       {
        "dt": "Custom Field", 
        "filters":[["name","in",['Sales Invoice Item-fob_value','Sales Invoice Item-meis_rate','Sales Invoice Item-meis_value','Journal Entry-voucher_type','Company-meis_receivable_account','Company-meis_income_account','Sales Invoice-total_fob_value','Sales Invoice-total_meis','Sales Invoice-meis_jv','Sales Invoice-duty_drawback_','Sales Invoice-rodtep_jv','Company-meis_cost_center']]]
      },
]