# ivansible.dev_jupyter

Installs a jupyter server with ipython backend.


## Requirements

None


## Variables

Available variables are listed below, along with default values.

    jupyter_work_subdir: jupyter

Subdirectory in the user home directory, where notebooks will be located.

    jupyter_git_repos: []

A list of git repository URLs that will be checked out during install,
e.g. `https://github.com/ivansible/dev-jupyter.git`
or `git@github.com:ivansible/dev-jupyter`.
Leave this blank to skip checkout and leave the work subdirectory empty.
Web server will redirect from home page to the first repository, if any.

    jupyter_pip_extras: []

Additional python packages to install.

    jupyter_theme: ""

If not blank, the script will configure jupyter theme.
See [jt documentation](https://github.com/dunovank/jupyter-themes).

    jupyter_password: ""

If this variable is blank, notebooks will be world-open.

    jupyter_nginx_hostname: ""

If you set this to a host name of the jupyter server, ansible will
additionally configure `nginx` on port 80 in front of the jupyter server.
Leave this blank to serve notebooks directly.

    jupyter_nginx_ssl_cert: ""
    jupyter_nginx_ssl_pkey: ""

Certificate and private key for SSL access on port 443.
If these are configured, nginx will forcibly redirect port 80 to SSL.

    jupyter_port: 8888

This is the port where jupyter will serve notebooks if nginx is not installed.


## Dependencies

None


## Example Playbook

    - hosts: host5
      roles:
        - role: ivansible.dev_jupyter
          jupyter_password: avadakedavra
          jupyter_git_repos:
            - https://github.com/ivandeex/stepik-algos.git
          jupyter_pip_extras:
            - bs4
          jupyter_theme: "-t gruvboxd -T -cellw 99% -f roboto -fs 10 -ofs 10 -tf robotosans -nf ptsans -nfs 10 -tfs 11 -dfs 10"
          jupyter_nginx_hostname: host5.example.com


## Testing

    ansible-playbook plays-all/run-role.yml -e role=ivansible.dev_jupyter -l vag2

See settings in `host_vars/vag2/secret/test.dev_jupyter.yml`


## License

MIT


## Author Information

Created in 2018 by [IvanSible](https://github.com/ivansible)
