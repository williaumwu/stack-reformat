def default():

    task = {'method': 'shelloutconfig',
            'metadata': {'env_vars': ['config0-hub:::ansible::ssh_key'],
                         'shelloutconfigs': ['config0-hub:::ansible::resource_wrapper']}}

    return task
