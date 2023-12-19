def default():
    
    task = {}
    env_vars = []
    shelloutconfigs = []

    env_vars.append("config0-hub:::docker::build")
    # We used to create the Dockerfile through environmental variables
    # but we just let the user specify where the "DOCKER_REPO" that includes
    # <REPO_NAME:TAG> format
    #shelloutconfigs.append('config0-hub:::docker::create_dockerfile')
    shelloutconfigs.append('config0-hub:::docker::build-docker-image')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, 
                        'shelloutconfigs': shelloutconfigs 
                        }

    return task

