# ivansible.dev-jupyter

Installs a jupyter server with ipython backend.

## Requirements

None

## Variables

Available variables are listed below, along with default values.

    jupyter_work_subdir: "jupyter"

A name of subdirectory in the user home directory, where notebooks will be located.

    jupyter_git_repos: []

A list of git repository URLs that will be checked out during install,
e.g. `https://github.com/ivansible/dev-jupyter.git`
or `git@github.com:ivansible/dev-jupyter`.
Leave this blank to skip checkout and leave the work subdirectory empty.
Web server will redirect from home page to the first repository, if any.

    jupyter_password: ""

If this variable is blank, notebooks will be world-open.

    jupyter_nginx_hostname: ""

If you set this to a host name of the jupyter server, ansible will
additionally configure `nginx` on port 80 in front of the jupyter server.
Leave this blank to serve notebooks directly.

    jupyter_port: 8888

This is the port where jupyter will serve notebooks if nginx is not installed.

## Dependencies

None

## Example Playbook

    - hosts: host5
      roles:
        - role: ivansible.dev-jupyter
          jupyter_password: avadakedavra
          jupyter_git_repos:
            - https://github.com/ivandeex/stepik-algos.git
          jupyter_nginx_hostname: host5.example.com

## Testing

    ansible-playbook plays-all/test-role.yml -e role=ivansible.dev-jupyter -l dock2

See settings in `host_vars/dock2/secret/test-role.dev-jupyter.yml`

## License

MIT

## Author Information

Created in 2018 by [IvanSible](https://github.com/ivansible)
