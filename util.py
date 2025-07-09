import textwrap
PRIMARY = 'primary'
SECONDARY = 'secondary'
SUCCESS = 'success'
DANGER = 'danger'
INFO = 'info'
WARNING = 'warning'
LINK = 'link'

OUTLINE_INFO = 'info-outline'

INVERSE_INFO = 'info-inverse'





def get_style():
    with open('./style.css', 'r') as file:
        return file.read()

class Colors:
    primary = "#2a9fd6"
    secondary = "#555555"
    success = "#77b300"
    danger = "#cc0000"
    warning = "#ff8800"
    info = "#9933cc"
    dark = "#222222"
    light = "#ADAFAE"
    white = "#ffffff"
    black = "#060606"
    bg = "#060606"
    fg = "#ffffff"
    selectbg = "#454545"
    selectfg = "#ffffff"
    border = "#060606"
    inputfg = "#ffffff"
    inputbg = "#191919"
class TopTitle:
        # background-color: #9933cc;
    # label
    label = textwrap.dedent("""
        color: #ffffff;
        font-weight: 400;
        font-size: 24px;
    """).strip()
    
    # frame
    frame = textwrap.dedent(f'''
        background-color: {Colors.info};
        border-bottom-right-radius: 50px;
        border-bottom-left-radius: 50px;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
          ''').strip()

if __name__ == '__main__':
    print(get_geometry())
