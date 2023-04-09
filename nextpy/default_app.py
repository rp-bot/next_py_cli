import argparse
import subprocess

# npx create-next-app@latest example6 --js --tailwind --eslint --src-dir --no-experimental-app  --import-alias "@/*"
RP_BOT_COMMAND = """npx create-next-app@latest example6 --js --tailwind --eslint --src-dir --no-experimental-app  --import-alias "@/*"""


def command_maker(project_name, lang_name, tailwind, eslint, experimental_app, src_dir, import_alias, alias_string, bootstrap_client, help, create_command="create-next-app@latest", version=None):
    if version != None:
        create_command = "create-next-app"
    command = ["npx",
               create_command,
               version,
               project_name,
               lang_name,
               tailwind,
               eslint,
               experimental_app,
               src_dir,
               import_alias,
               alias_string,
               bootstrap_client,
               help]
    return command


def main():

    parser = argparse.ArgumentParser(
        description='Another unnecessary level of automation.')
    args = parser.parse_args()
    # ProjectName
    parser.add_argument("project_name", type=str,
                        help="Type the name of the nextjs project. This will also be the name of your folder.")
    # Type script or javascript
    parser.add_argument("--ts", "--typescript", type=str, default="--js",
                        help="Specify if you WANT typescript. Default is javascript")

    # Tailwind or no Tailwind
    parser.add_argument("--no-tailwind", type=str, default="--tailwind",
                        help="Specify if you DON'T WANT tailwind. Default is WITH tailwind")

    # ESLint or no
    parser.add_argument("--no-eslint", type=str, default="--eslint",
                        help="Specify if you DON'T WANT eslint. Default is WITH eslint")
    # src dir or no
    parser.add_argument("--no-src-dir", type=str, default="--src-dir",
                        help="Specify if you DON'T WANT the src-dir. Default is WITH src-dir")

    # experimental app or no
    parser.add_argument("--experimental-app", type=str, default="--no-experimental-app",
                        help="Specify if you WANT the experimental-app. Default is WITHOUT experimental-app")

    # import alias or nah
    parser.add_argument("--no-import-alias", type=str, default="--import-alias",
                        help="Specify if you DON'T WANT the import alias. Default is it imports alias")
    # Alias string
    # TODO: Do a condition statement to check whether alias is selected or not.
    alias_string_arg = None
    if args.no_import_alias == "--import-alias":
        parser.add_argument("alias_string_arg", type=str, default="@/*",
                            help="Specify if you DON'T WANT the import alias. Default is it imports alias")

    # bootstrapclient arg
    parser.add_argument("--use-pnpm", type=str, default="--use-npm",
                        help="Specify if you WANT Pnpm. Default is npm")

    parser.add_argument("--next-help", type=str, default=None,
                        help="Next JS help")

    # VERSION

    project_name = args.project_name
    language = args.typescript
    tailwind = args.no_tailwind
    eslint = args.no_eslint
    src_dir = args.no_src_dir
    experimental_app = args.experimental_app
    import_alias = args.no_import_alias
    alias_string = args.alias_string_arg
    bootstrap_client = args.use_pnpm
    help_arg = args.next_help  # needs to be converted to --help from --next-help
    command_maker(project_name, language, tailwind, eslint, src_dir,
                  experimental_app, import_alias, alias_string, bootstrap_client, help_arg, )
    x = subprocess.Popen([],
                         shell=True, text=True)
    x.wait()


if __name__ == '__main__':
    main()
