import argparse
import subprocess
import os
import platform

CWD = os.getcwd()
# npx create-next-app@latest example6 --js --tailwind --eslint --src-dir --no-experimental-app  --import-alias "@/*"
RP_BOT_COMMAND = """npx create-next-app@latest example6 --js --tailwind --eslint --src-dir --no-experimental-app  --import-alias "@/*"""


def command_maker(argument_dict):
    # TODO: classify the essential and non essential arguments to catch errors. 
    # non_esential=["language", ] 
    command = []
    for value in argument_dict.values():
        if value is not None: command.append(value)
    return command

def clean_up(command):
# clean up files in the directory
    with open(f"{command[2]}\\tailwind.config.js","r+") as f:
        print(f.readlines())
    # x = subprocess.Popen(["dir"], shell=True,cwd=os.getcwd(), text=True)


def main():

    parser = argparse.ArgumentParser(
        description='Another unnecessary level of automation.')

    # ProjectName
    parser.add_argument("project_name", type=str,
                        help="Type the name of the nextjs project. This will also be the name of your folder.")
    # Type script or javascript
    parser.add_argument("--typescript", "--ts", type=str, default="--js",
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

    # bootstrapclient arg
    parser.add_argument("--use-pnpm", type=str, default="--use-npm",
                        help="Specify if you WANT Pnpm. Default is npm")

    parser.add_argument("--next-help", type=str, default=None,
                        help="Next JS help")
    args = parser.parse_args()
    # VERSION
    arguments ={
        "package_execution": "npx",
        "create_command": "create-next-app@latest",
        "version": None,
        "project_name":args.project_name,
        "language":args.typescript,
        "tailwind":args.no_tailwind,
        "eslint":args.no_eslint,
        "src_dir" : args.no_src_dir,
        "experimental_app" : args.experimental_app,
        "import_alias" : args.no_import_alias,
        # TODO: Make Alias string customizable
        "alias_string" : "@/*",
        "bootstrap_client" : args.use_pnpm,
        "help_arg" : args.next_help 

    }
    
    command = command_maker(arguments)
    print(" ".join(command))
    x = subprocess.Popen(command, shell=True, text=True)
    x.wait()
    
    # Run clean up function if app was created or else dont
    # TODO override it with another arg
    clean_up(command) if not x.poll() else None
    



if __name__ == '__main__':
    main()
