import os
import shutil
import folder_paths
from typing import Dict, Any

class TempCleaner:
    def __init__(self):
        self.default_temp = os.path.join(os.path.dirname(folder_paths.base_path), 'temp')

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "images": ("IMAGE",),
                "temp_folder": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "placeholder": "Leave empty to use default ComfyUI temp folder"
                }),
                "skip_hidden": ("BOOLEAN", {"default": True}),
                "preserve_folders": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "clean_temp"
    CATEGORY = "image/cleanup"
    OUTPUT_NODE = True

    def clean_temp(self, images, temp_folder="", skip_hidden=True, preserve_folders=True):
        # Use default temp folder if none provided
        temp_path = temp_folder.strip() if temp_folder.strip() else self.default_temp
        
        try:
            if not os.path.exists(temp_path):
                print(f"Warning: Temp folder '{temp_path}' does not exist.")
                return (images,)

            files_removed = 0
            for root, dirs, files in os.walk(temp_path, topdown=True):
                # Skip hidden directories if requested
                if skip_hidden:
                    dirs[:] = [d for d in dirs if not d.startswith('.')]
                
                for file in files:
                    # Skip hidden files if requested
                    if skip_hidden and file.startswith('.'):
                        continue
                        
                    file_path = os.path.join(root, file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                            files_removed += 1
                    except Exception as e:
                        print(f"Warning: Could not remove file {file_path}: {str(e)}")

            # Remove empty directories if preserve_folders is False
            if not preserve_folders:
                for root, dirs, files in os.walk(temp_path, topdown=False):
                    for dir_name in dirs:
                        dir_path = os.path.join(root, dir_name)
                        try:
                            if len(os.listdir(dir_path)) == 0:
                                os.rmdir(dir_path)
                        except Exception as e:
                            print(f"Warning: Could not remove directory {dir_path}: {str(e)}")

            print(f"Cleanup completed: {files_removed} files removed from {temp_path}")

        except Exception as e:
            print(f"Error during cleanup: {str(e)}")

        return (images,)

NODE_CLASS_MAPPINGS = {
    "TempCleaner": TempCleaner
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TempCleaner": "Temp Folder Cleaner"
}
