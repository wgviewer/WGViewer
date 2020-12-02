# Contribution Guide

To contribute code,

1. start a Python virtual environment
2. install required packages: `pip install -r requirements.txt`
3. make a [pull request](../../pulls) when your code is ready :)

### Packing into executable

To build executable on Windows OS, run

> win_build.bat

To build executable on Unix OS, update `fix_pyinstaller.py` with your directory location, run

> python tools/fix_pyinstaller.py > gui_main.spec  
> pyinstaller --clean gui_main.spec


### Publish New Release

#### Version Naming

WGViewer uses [packaging.version](https://packaging.pypa.io/en/latest/version.html) to test version naming.

- `version` format = `major.minor.micro`
- Valid notations = {a, b, c, r, beta, dev, pre, post, rev}
- Valid notations can appear once and only once in either `minor` or `micro` for the version number to be valid.
- notations are dropped when reading `minor` or `micro` field
  
Some valid example:
``` 
0.0.1
0.0.1a
0.0.1beta
0.0.beta1   # valid but WGViewer does not recommend you to use
0.dev.1
```

The order of the version notation is:

```
(any int) > rev > r > post > c = pre > beta > b > a > dev
```

(If you are curious of how to reach this conclusion, please check this [post by the developer of WGViewer][post].)

[post]: https://blog.yanqing-wu.com/tech/2020/02/15/Determine-Order-Of-Element-From-A-Blackbox/
