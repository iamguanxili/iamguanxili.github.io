def generate_nav_html(name):
    names = ["index", "Research", "resume", "courses", "til"]
    idx = -1
    for i, n in enumerate(names):
        if n == name:
            idx = i
    assert idx != -1

    list_items = [
        "<a href=\"https://iamguanxili.github.io/index.html\">About Me</a>",
        "<a href=\"https://iamguanxili.github.io/resume.html\">Resume</a>",
        "<a href=\"https://iamguanxili.github.io/Research.html\">Research</a>",
        "<a href=\"https://iamguanxili.github.io/coursework.html\">Course Work</a>",
        "<a href=\"https://iamguanxili.github.io/til/index.html\">TIL</a>"
    ]
    nav_list_html = ["\n"]
    for i, item in enumerate(list_items):
        if i == idx:
            nav_list_html.append(f"""<li class="current">{item}</li>\n""")
        else:
            nav_list_html.append(f"""<li>{item}</li>\n""")
    return f"""
    <!-- Nav -->
        <nav id="nav">
            <ul>
                {"".join(nav_list_html)}
            </ul>
        </nav>
    """

def generate_logo_html():
    return """
    <!-- Logo -->
        <div id="logo">
            <h1><a href="https://iamguanxili.github.io/index.html">Guanxi Li 李冠曦</a></h1>
        </div>
    """

def generate_header_html(name):
    return f"""
    <!-- Header -->
        <div id="header-wrapper">
            <header id="header" class="container">

                {generate_logo_html()}

                {generate_nav_html(name)}

            </header>
        </div>
    """

def generate_head_html():
    return r"""
    <head>
        <title>Guanxi Li's Website</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="https://iamguanxili.github.io/assets/css/main.css" />
        
        <script type="text/x-mathjax-config">
            MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
        </script>
        <script type="text/javascript"
            src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
        </script>

    </head>
    """

def generate_footer_html():
    return """
    <!-- Footer -->
        <div id="footer-wrapper">
            <footer id="footer" class="container">
                <!-- <div class="row"> -->
                    <div class="col-12">
                        <div id="copyright">
                            <ul class="menu">
                                <li>&copy; 2022 Guanxi Li </li>
                                <li>Hosted on GitHub Pages</li>
                                <li>Design: <a href="http://html5up.net">HTML5 UP (Verti)</a></li>
                            </ul>
                        </div>
                    </div>
                <!-- </div> -->
            </footer>
        </div>
    """

def generate_scripts_html():
    return """
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/jquery.dropotron.min.js"></script>
    <script src="assets/js/browser.min.js"></script>
    <script src="assets/js/breakpoints.min.js"></script>
    <script src="assets/js/util.js"></script>
    <script src="assets/js/main.js"></script>
    """