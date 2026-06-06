import gdown

# ID của folder
folder_id = "16KgVsnVzcnsE-iUlly_99VlbGGMfrlCC"
output_dir = "app/model/weights/"  # ví dụ: "./du_lieu/"

gdown.download_folder(id=folder_id, output=output_dir, quiet=False, use_cookies=False)