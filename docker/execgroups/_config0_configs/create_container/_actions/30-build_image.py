def default():

    task = {'method': 'shelloutconfig',
            'metadata': {'env_vars': ["config0-hub:::docker::build"],
                         'shelloutconfigs': ['config0-hub:::docker::build-docker-image']}}

    return task
