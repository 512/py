import os
import shutil

"""
Get all directories.
For each directory
  get numerical prefix (01)
  get all files in that directory
  for each file:
    rename file from X to 01-X



./08 Album/01 - song.flac

"""

for (root, dirs, files) in os.walk("."):
    for n in files:
        orig = os.path.join(root, n)
        print("orig: %s" % orig)
        if not orig.endswith(".flac"):
            continue
        parts = orig.split("/")
        if len(parts) >= 3:
            dir = parts[1]
            nth = dir[:2]
            file = parts[2]

            """
            # special case to fix earlier bug
            pieces = file.split(" ")
            fp = pieces[0]
            numbers = fp.split("-")
            if len(numbers) > 2:
                last_two = numbers[-2:]
                np = "-".join(last_two)
                remainder = " ".join(pieces[1:])
                new_file = "%s %s" % (np, remainder)
                src = os.path.join(root, file)
                dest = os.path.join(root, new_file)
                print("FIX %s to %s" % (src, dest))
                shutil.move(src, dest)

            """

            if nth.isdigit() and not file.startswith("."):
                new_file = "%s-%s" % (nth, file)
                print("rename %s to %s" % (file, new_file))
                src = os.path.join(root, file)
                dest = os.path.join(root, new_file)
                already = "%s-" % nth
                if new_file.startswith(already):
                    continue
                shutil.move(src, dest)

