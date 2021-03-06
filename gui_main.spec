# -*- mode: python ; coding: utf-8 -*-
import sys
block_cipher = None
a = Analysis(['gui_main.py'],
             pathex=['D:\\github\\WGViewer'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('assets/favicon.ico','D:\\github\\WGViewer\\assets\\favicon.ico','DATA'),
('assets/data/exp_data.csv','D:\\github\\WGViewer\\assets\\data\\exp_data.csv','DATA'),
('assets/fonts/Consolas.ttf','D:\\github\\WGViewer\\assets\\fonts\\Consolas.ttf','DATA'),
('assets/icons/collect_16.png','D:\\github\\WGViewer\\assets\\icons\\collect_16.png','DATA'),
('assets/icons/equip_16.png','D:\\github\\WGViewer\\assets\\icons\\equip_16.png','DATA'),
('assets/icons/lock_64.png','D:\\github\\WGViewer\\assets\\icons\\lock_64.png','DATA'),
('assets/icons/pants_32.png','D:\\github\\WGViewer\\assets\\icons\\pants_32.png','DATA'),
('assets/icons/ring_60.png','D:\\github\\WGViewer\\assets\\icons\\ring_60.png','DATA'),
('assets/icons/ship_16.png','D:\\github\\WGViewer\\assets\\icons\\ship_16.png','DATA'),
('assets/icons/ship_32.png','D:\\github\\WGViewer\\assets\\icons\\ship_32.png','DATA'),
('assets/icons/sign_16.png','D:\\github\\WGViewer\\assets\\icons\\sign_16.png','DATA'),
('assets/icons/unlock_64.png','D:\\github\\WGViewer\\assets\\icons\\unlock_64.png','DATA'),
('assets/items/ammo.png','D:\\github\\WGViewer\\assets\\items\\ammo.png','DATA'),
('assets/items/bauxite.png','D:\\github\\WGViewer\\assets\\items\\bauxite.png','DATA'),
('assets/items/BB.png','D:\\github\\WGViewer\\assets\\items\\BB.png','DATA'),
('assets/items/blueprint_construct.png','D:\\github\\WGViewer\\assets\\items\\blueprint_construct.png','DATA'),
('assets/items/blueprint_dev.png','D:\\github\\WGViewer\\assets\\items\\blueprint_dev.png','DATA'),
('assets/items/CA.png','D:\\github\\WGViewer\\assets\\items\\CA.png','DATA'),
('assets/items/CV.png','D:\\github\\WGViewer\\assets\\items\\CV.png','DATA'),
('assets/items/DD.png','D:\\github\\WGViewer\\assets\\items\\DD.png','DATA'),
('assets/items/fuel.png','D:\\github\\WGViewer\\assets\\items\\fuel.png','DATA'),
('assets/items/gold.png','D:\\github\\WGViewer\\assets\\items\\gold.png','DATA'),
('assets/items/instant_build.png','D:\\github\\WGViewer\\assets\\items\\instant_build.png','DATA'),
('assets/items/instant_repair.png','D:\\github\\WGViewer\\assets\\items\\instant_repair.png','DATA'),
('assets/items/revive.png','D:\\github\\WGViewer\\assets\\items\\revive.png','DATA'),
('assets/items/SS.png','D:\\github\\WGViewer\\assets\\items\\SS.png','DATA'),
('assets/items/steel.png','D:\\github\\WGViewer\\assets\\items\\steel.png','DATA'),
]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Warship Girls Viewer' + ('.exe' if sys.platform == 'win32' else ''),
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='assets/favicon.ico'
          )

