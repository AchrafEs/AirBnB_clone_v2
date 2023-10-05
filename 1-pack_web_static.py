from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        # Create the 'versions' directory if it doesn't exist
        local("mkdir -p versions")

        # Generate the name for the archive
        current_time = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            current_time.year,
            current_time.month,
            current_time.day,
            current_time.hour,
            current_time.minute,
            current_time.second
        )

        # Create the .tgz archive using tar
        local("tar -cvzf versions/{} web_static".format(archive_name), capture=False)

        # Return the path to the archive
        return "versions/{}".format(archive_name)
    except Exception:
        return None
