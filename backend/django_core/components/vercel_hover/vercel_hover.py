from django_components import component


@component.register("vercel_hover")
class VercelHover(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "vercel_hover/vercel_hover.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, icons):
        """"""

    class Media:
        css = "vercel_hover/vercel_hover.css"
        js = "vercel_hover/vercel_hover.js"
