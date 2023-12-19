def default():
    
    task = {}
    env_vars = []
    shelloutconfigs = []

    env_vars.append('config0-hub:::ansible::create')
    shelloutconfigs.append('config0-hub:::ansible::resource_wrapper')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars,
                        'shelloutconfigs': shelloutconfigs
                        }

    return task

