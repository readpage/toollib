"""
@author axiner
@version v1.0.0
@created 2022/2/27 11:31
@abstract
@description
@history
"""
from toollib.tcli import sys_required
from toollib.tcli.base import BaseCmd
from toollib.tcli.option import Options, Arg


class Cmd(BaseCmd):

    def __init__(self):
        super().__init__()

    def add_options(self):
        options = Options(
            name='pyi',
            desc='pip install',
            optional={
                self.pyi: [
                    Arg('pkg', nargs='*', help='安装包'),
                    Arg('-i', '--index', help='下载源'),
                    Arg('-r', '--requirement', help='安装文件'),
                    Arg('-d', '--downloaddir', help='下载包目录'),
                    Arg('-f', '--findlinks', help='离线包目录'),
                ],
            }
        )
        return options

    @sys_required()
    def pyi(self):
        from pip._internal.cli.main import main as pypip
        optional = []
        if self.parse_args.downloaddir:
            optional.extend(['wheel', f'--wheel-dir={self.parse_args.downloaddir}'])
        else:
            optional.append('install')
            if self.parse_args.findlinks:
                optional.extend(['--no-index', f'--find-links={self.parse_args.findlinks}'])
        if self.parse_args.pkg is not False:
            optional.extend(self.parse_args.pkg)
        if self.parse_args.requirement:
            optional.extend(['-r', self.parse_args.requirement])
        optional.extend(self._index_urls(self.parse_args.index))
        pypip(optional)

    @staticmethod
    def _index_urls(index: str = None):
        maps = {
            't': ['-i', 'https://pypi.tuna.tsinghua.edu.cn/simple/'],
            'a': ['-i', 'http://mirrors.aliyun.com/pypi/simple/', '--trusted-host',
                  'mirrors.aliyun.com'],
            'd': ['-i', 'http://pypi.douban.com/simple/', '--trusted-host', 'pypi.douban.com'],
            'u': ['-i', 'http://pypi.mirrors.ustc.edu.cn/simple/', '--trusted-host',
                  'pypi.mirrors.ustc.edu.cn'],
            'pypi': ['-i', 'https://pypi.python.org/simple/'],
        }
        if index is None:
            return maps['t']
        return maps.get(index, maps['pypi'])
