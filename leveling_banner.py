from PIL import Image, ImageFont, ImageDraw, ImageColor, ImageEnhance
from typing import Optional, Tuple
import uuid, textwrap

class BannerLevel:
    fontfold = "assets/font"
    imgfold = "assets/image"
    sticker = [f"{imgfold}/af7754b21494ef6c12f7c2216d39e72c.jpg", f"{imgfold}/9481fd376c9972838658358bfcb03ddb.jpg"]
    fonts = f"{fontfold}/Chocolate Covered Raindrops BOLD.ttf"

    def __init__(self, username:Optional[str], name:Optional[str], is_prem:Optional[bool], frame:Optional[str]) -> None:
        self.username = username
        self.name = name
        self.is_prem = is_prem
        self.frame = frame
        self.__image = Image.open(f"{self.imgfold}/nacho_neko_nekoha_shizuku_gray_hair_blue_hair_cat_girl_blush_long_hair_food-1857595.jpg")

    def set_background(self, impath):
        self.__image = Image.open(impath)

    def set_brightness(self, rate:float):
        self.__image = ImageEnhance.Brightness(self.__image).enhance(rate)

    def add_dark_bg(self):
        w,h = self.__image.size
        im = Image.new("RGB", (w,h), (0,0,0))
        im = im.copy()
        self.__image.paste(im, (int(w-2), int(h-2)))

    def add_sticker(self, sname, tpl:tuple):
        simg = Image.open(sname)
        self.__image.paste(simg, (tpl[0], tpl[1]))

    def add_name(self):
        font = ImageFont.truetype(self.fonts, size=100)
        wrapper = textwrap.TextWrapper(width=30) 
        word_list = wrapper.wrap(text=self.name)
        capt = '\n'.join(line.center(80) for line in word_list)
        draw = ImageDraw.Draw(self.__image)
        wt, ht = draw.textsize(capt, font)
        draw.text((int((1200-wt)/5),int((1200-ht)/2)), capt, fill='rgb(255, 255, 255)', font=font)

    def create_all(self, sticker=False):
        self.set_brightness(0.7)
        self.add_dark_bg()
        if sticker:
            self.add_sticker(self.sticker[1], (int((100-200)/2), int((50-20)/2)))
            self.add_sticker(self.sticker[0], (int((200-100)/2), int((50-30)/2)))
        self.add_name()

    def save(self, saveAs:str):
        if saveAs == "" or not saveAs or saveAs is None:
            saveAs = uuid.uuid(4)
        savefile = f"{saveAs}{'' if saveAs.endswith('.png') or saveAs.endswith('.jpg') else '.png'}"
        self.__image.save(savefile)
        return savefile

banner = BannerLevel("nekoha", "Kee", True, "395aebb5f536f65d7817d38f0d1c1925.jpg")
banner.create_all()
banner.save("gatau.png")