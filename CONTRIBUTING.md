# Contributing to Project Engage

## Things you will need

* Linux, Mac OS X, or Windows.
* git (used for source version control).
* An ssh client (used to authenticate with GitHub).

## Getting the code and configuring your environment

* Ensure all the dependencies described in the previous section are installed.
* Fork `https://github.com/BU-Spark/CS506Spring2021Repository` into your own GitHub account. If
   you already have a fork, and are now installing a development environment on
   a new machine, make sure you've updated your fork so that you don't use stale
   configuration options from long ago.
* If you haven't configured your machine with an SSH key that's known to github, then
   follow [GitHub's directions](https://help.github.com/articles/generating-ssh-keys/)
   to generate an SSH key.
* `git clone git@github.com:<your_name_here>/CS506Spring2021Repository.git`
* `git remote add upstream git@github.com:BU-Spark/CS506Spring2021Repository.git` (So that you
   fetch from the master repository, not your clone, when running `git fetch`
   et al.)

## Contributing code

We gladly accept contributions via GitHub pull requests.

To start working on a patch:

 * `git fetch upstream`
 * `git checkout upstream/master -b <name_of_your_branch>`
 * Hack away.
 * `git commit -a -m "<your informative commit message>"`
 * `git push origin <name_of_your_branch>`

To send us a pull request:

* `git pull-request` (if you are using [Hub](http://github.com/github/hub/)) or
  go to `https://github.com/BU-Spark/CS506Spring2021Repository` and click the
  "Compare & pull request" button

Please make sure all your checkins have detailed commit messages explaining the patch.

Once you've gotten an LGTM from a project maintainer and once your PR has received
the green light from all our automated testing, wait for one the package maintainers
to merge the pull request.
