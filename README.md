# Publish Preflight

## What is this?

Ever wanted to be able to save a draft in wagtail easily, but want lots of required fields for publish?
Of course you have.
This plugin creates some custom model validation that allows for drafts to be saved, but prevents publishing.

It is VERY much in it's infancy and really more of a proof of concept.

## How to use

-   install
-   add to INSTALLED_APPS
-   (atm), include static js or css on the templates where you want the overrides to occur (is there a better way to do this?)

- To specific fields to check, add a 'fields_required_for_publish' tuple to the page model containing the names of the fields to check like so: 
```
    fields_required_for_publish = (
        'first_name',
        'address_1',
        'intro',
    )
```

## TODOs:

-   messages are hidden, becuase at the moment it will create a big ol' list of messages which could get ugly
    -   would love to have a nuanced way to add errors to fields but not show errors in messages at the top
    -   setting different kind of error levels would be great too
    -   this would probably involve a custom message protocol, to either replace or enhance the way wagtail handles messages `add_error`
