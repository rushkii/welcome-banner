from banner.editor import WelcomeBanner

banner = WelcomeBanner(
    name="Kee",
    message="Welcome to Anime Grup Indonesia",
    frame=None,
    use_sticker=True
)

banner.save() # Save your banner, using path.
# banner.show() # Show the banner, I think this function wouldn't work on virtual server.