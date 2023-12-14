def default():
    
    task = {}
    env_vars = []
    shelloutconfigs = []
    shelloutconfigs.append('config0-hub:::docker::cleanup_build')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, 
                        'shelloutconfigs': shelloutconfigs 
                        }

    return task
