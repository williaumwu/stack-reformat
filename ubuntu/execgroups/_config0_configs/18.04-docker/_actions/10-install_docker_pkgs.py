def default():
    
    env_vars = []

    shelloutconfigs = []
    shelloutconfigs.append('config0-hub:::ubuntu::install-docker-pkgs')

    task = {'method':'shelloutconfig'}
    task['metadata'] = {'env_vars': env_vars,
                        'shelloutconfigs': shelloutconfigs
                        }

    return task
