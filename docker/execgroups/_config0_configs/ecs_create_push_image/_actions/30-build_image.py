def default():
    
    task = {}
    env_vars = []
    shelloutconfigs = []

    env_vars.append("config0-hub:::docker::build")
    shelloutconfigs.append('config0-hub:::docker::ecs_build_push_image')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, 
                        'shelloutconfigs': shelloutconfigs 
                        }

    return task
