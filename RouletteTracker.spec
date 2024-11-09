# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/antonyngigge/Downloads/roulette-system/templates', 'templates'), ('/Users/antonyngigge/Downloads/roulette-system/static', 'static'), ('/Users/antonyngigge/Downloads/roulette-system/tracker', 'tracker'), ('/Users/antonyngigge/Downloads/roulette-system/accounts', 'accounts'), ('/Users/antonyngigge/Downloads/roulette-system/roulette_system_tracker', 'roulette_system_tracker'), ('/Users/antonyngigge/Downloads/roulette-system/.env', '.env')],
    hiddenimports=['django', 'django.template.defaulttags', 'django.template.defaultfilters', 'django.template.loader_tags', 'django.templatetags.static', 'django.contrib.messages.storage.fallback', 'django.contrib.staticfiles', 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'rest_framework', 'corsheaders', 'psycopg2', 'drf_yasg', 'packaging'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['runtime_hooks.py'],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='RouletteTracker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='arm64',
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/antonyngigge/Downloads/roulette-system/static/img/favicon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='RouletteTracker',
)
app = BUNDLE(
    coll,
    name='RouletteTracker.app',
    icon='/Users/antonyngigge/Downloads/roulette-system/static/img/favicon.icns',
    bundle_identifier=None,
)
