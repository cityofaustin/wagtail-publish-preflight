from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.core.models import Page, PageRevision
from django.core.exceptions import ValidationError
from wagtail.admin import messages
import logging
import traceback


class PublishPreflightForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        """
        ways to limit scope:
        changed fields,
        then exclude fields that are required

        self.changed_data = list of fields changed

        self[field_name].data or as_text (might be useful for streamfields)
        looks like this is working, atm tho it just wont let you publish any empty fields :-D
        """
        def check_for_empties(*args):
            """
            adds an error to each field if it is empty
            """
            errors_for_empties = {
                field_name: try_adding_error_to_field(field_name, field_value)
                for (field_name, field_value) in self.data.items()
                if len(field_value) == 0
            }

            # [
            #     try_adding_error_to_field(i, self.data.get(i))
            #     for i in fields
            #     if not self.data.get(i)
            # ]

            # [
            # try_adding_error_to_field(i, self.data.get(i))
            # for i in fields_required_for_publish
            # if i not in self.data  or not self.data.get(i)
            # ]

        def try_adding_error_to_field(field_name, field_value):
            # import pdb
            # pdb.set_trace()
            print(field_name, field_value)
            try:
                self.add_error(field_name, f'{field_name} is empty!')
            except ValueError as e:
                logging.error(e)
                # try:
                #     import pdb
                #     pdb.set_trace()
                #     self.formsets[field_name].form.add_error(
                #         None, f'{field_name} is empty!')
                # except Exception as e:
                #     logging.error(e)
                #     print(traceback.format_exc())
                #     pass

                try:
                    self.formsets[field_name].non_form_errors().append(
                        f'{field_name} not selected!')
                    self.add_error(None, f'{field_name} is missing!')
                except AttributeError as e:
                    logging.error(e)
                    pass
                pass

        # may have handled this above
        def check_for_missing_relations():
            relations = self.formsets
            # relation_value.cleaned_data
            errors_for_missing_relations = {
                relation_name: try_adding_error_to_field(
                    relation_name, relation_value)
                for (relation_name, relation_value) in relations.items()
                if not relation_value.forms
            }

        cleaned_data = super().clean()

        if 'action-publish' in self.data:
            # TODO: we'll probably want a good way to check a managed subset
            # something like getattr(self.instance, {related_links}) if we want to check
            # for fields in the tuple provided that don't actually exist on the model
            all_keys = self._meta.fields + list(self.formsets.keys())
            if hasattr(self.instance, 'fields_required_for_publish'):
                fields_required = self.instance.fields_required_for_publish
                check_all = check_for_empties()
            else:
                check_all = check_for_empties()
            # missing_relations = check_for_missing_relations()

        return cleaned_data
