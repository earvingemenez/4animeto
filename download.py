import os
import progressbar
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EP_NAME = "Boruto-Naruto-Next-Generations-Episode-{episode_num}-1080p"

URL = "https://storage.googleapis.com/justawesome-183319.appspot.com/v2.4animu.me/Boruto-Naruto-Next-Generations/{episode_name}.mp4"
SAVE_TO_PATH = os.path.join(BASE_DIR, "downloads", "Boruto")


class ProgressBar(object):
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()



def get_episode(EP):
    return EP_NAME.format(episode_num=EP)

def get_url(EP):
    return URL.format(episode_name=get_episode(EP))


if __name__ == "__main__":

    print("\nInitiating download...\n")

    START_EP = 22
    END_EPISODE = 172

    for i in range(START_EP, END_EPISODE + 1):
        episode_name = get_episode(i)

        print(f"downloading [{episode_name}]")
        urllib.request.urlretrieve(get_url(i), os.path.join(SAVE_TO_PATH, episode_name), ProgressBar())

    print('Done!')

