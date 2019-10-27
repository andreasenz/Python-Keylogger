# Python-Keylogger
<p>A simple keylogger in python working in Linux. Is not difficult creating a keylogger for Windows OS.</p>
<h1>What we need</h1>
<ul>
  <li>First, we need <a href="https://github.com/JeffHoogland/pyxhook/blob/master/pyxhook.py">this</a> library to emulate some of the PyHook library on linux.</li>
  <li>The library need python-xlib to work fine. You can install it using <code>sudo apt-get install python-xlib</code></li>
</ul>
<h1>Structure of the project</h1>
<p>This is a simple and dumb example of keylogger that logs every single key pressed in a log file and every character is followed by a <code>/n</code>. To make everything working, create a directory and put inside the <code>keylogger.py</code> file and the <code>pyxhook.py</code> file downloaded from github.<br>Inside <code>keylogger.py</code> there is a macro named <code>PATH</code> that identify the place where the log file is saved; feel free to change this location as you prefer. Feel free to change everything you want and have fun! <h4>No root privileges are needed</h4></p>
<h1>References</h1>
<ul>
  <li><a href="https://en.wikipedia.org/wiki/Keystroke_logging">Wikipedia</a></li>
</ul>

<h1>Disclaimer<h1>
  <p>I'm not responsible for your use of the information contained in this document. This is only for learning purpose. Keylogging is not legal.</p>
