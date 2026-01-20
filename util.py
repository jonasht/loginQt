import textwrap


from style import Color


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
        background-color: {Color.INFO};
        border-bottom-right-radius: 50px;
        border-bottom-left-radius: 50px;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
          ''').strip()

if __name__ == '__main__':
    pass 
