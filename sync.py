import os
import sys
import rmcl


def writeout(doc, path):
    fn = "%s/%s.pdf" % (path, doc.name)
    print(fn)
    with open(fn, "wb") as fh:
        fh.write(doc.annotated_s().read())


def copy_filetree(folder_obj, path="./rmfiles"):
    if not os.path.isdir(path):
        if os.path.exists(path):
            raise Exception()
        os.mkdir(path)
    for child in folder_obj.children:
        if isinstance(child, rmcl.Document):
            writeout(child, path)
        elif isinstance(child, rmcl.Folder):
            child_path = os.path.join(path, child.name)
            copy_filetree(child, child_path)


def main(path):
    root = rmcl.Item.get_by_id_s('')
    copy_filetree(root, path)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: %s <dest>" % sys.argv[0])
        sys.exit(1)
    path = sys.argv[1]
    main(path)
