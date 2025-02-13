import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import nb_file_util as nb


def main(argv=sys.argv):
    if 2 <= len(argv):
        path = argv[1]
    else:
        path = nb.get_upper_folder()

    for root, filename in nb.one_level_ipynb_path_file(path):
        full_path = os.path.join(root, filename)
        nodes = nb.read_nodes_from_ipynb(full_path)

        nb.remove_cell_id_from_nodes(nodes)

        if "colab" in nodes["metadata"]:
            del nodes["metadata"]["colab"]

        nb.write_nodes_to_ipynb(full_path, nodes)


def get_google_colab_import_cell(folder_name:str, repo_name:str="nmisp") -> str:
    code = (
        "# This cell is for the Google Colaboratory\n"
        "# https://stackoverflow.com/a/63519730\n"
        "if 'google.colab' in str(get_ipython()):\n"
        "  # https://colab.research.google.com/notebooks/io.ipynb\n"
        "  import google.colab.drive as gcdrive\n"
        "  # may need to visit a link for the Google Colab authorization code\n"
        '''  gcdrive.mount("/content/drive/")\n'''
        "  import sys\n"
        f'''  sys.path.insert(0,"/content/drive/My Drive/Colab Notebooks/{repo_name}/{folder_name}")\n'''
    )
    return code


if "__main__" == __name__:
    main(sys.argv)
