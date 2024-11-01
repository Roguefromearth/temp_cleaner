# ComfyUI Temp Folder Cleaner
workflow cleanup
![Screenshot 2024-11-01 141317](https://github.com/user-attachments/assets/fdb8f019-6794-4e33-b686-405cbc6aeb97)



This custom node implements a temp folder cleaner with the following features:

Takes an image input so it can be added at the end of any workflow
Passes through the image unchanged (allowing for workflow continuation if needed)
Configurable options:

Custom temp folder path.
Option to skip hidden files/folders (default: true).
Option to preserve empty folders (default: true).

Error handling for file operations.
Progress reporting through console output.

To use this node:

Install via Git.
Restart ComfyUI.
Enter you temp folder path.

You can then add the "Temp Folder Cleaner" node at the end of your workflow and connect your image output to it. The node will:

Process any images passed to it.
Clear the specified temp folder.
Pass the images through unchanged.

Configuration options:

**temp_folder**: Path to the temp folder (leave empty to use ComfyUI default)
**skip_hidden**: Whether to skip hidden files/folders (starting with '.')
**preserve_folders**: Whether to keep empty folders after cleanup
