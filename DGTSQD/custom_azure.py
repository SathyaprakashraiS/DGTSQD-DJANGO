from storages.backends.azure_storage import AzureStorage

#class AzureMediaStorage(AzureStorage):
    #account_name = 'dgtsqd' # Must be replaced by your <storage_account_name>
    #account_key = 'ife/0ulHHHuns7puU2KTY06qkO6v2yVfLxW1eeQR/bMzh+tfDMsN86hJbsTRuT26dxJMnQuS73n5ffjzchomlA==' # Must be replaced by your <storage_account_key>
    #azure_container = 'media'
    #expiration_secs = None

#class AzureStaticStorage(AzureStorage):
    #account_name = 'dgtsqd' # Must be replaced by your storage_account_name
    #account_key = 'ife/0ulHHHuns7puU2KTY06qkO6v2yVfLxW1eeQR/bMzh+tfDMsN86hJbsTRuT26dxJMnQuS73n5ffjzchomlA==' # Must be replaced by your <storage_account_key>
    #azure_container = 'static'
    #expiration_secs = None


class AzureMediaStorage(AzureStorage):
    location = 'media'
    file_overwrite = False


class AzureStaticStorage(AzureStorage):
    location = 'static'
    file_overwrite = False