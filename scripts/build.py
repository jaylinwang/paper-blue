"""Build a dependency-free GitHub Pages site and a portable Obsidian demo vault."""
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs'
OUT.mkdir(exist_ok=True)
for path in (ROOT / 'site').iterdir():
    shutil.copy2(path, OUT / path.name)
shutil.copy2(ROOT / 'theme.css', OUT / 'theme.css')
shutil.copytree(ROOT / 'examples', OUT / 'examples', dirs_exist_ok=True)
(OUT / '.nojekyll').touch()
with zipfile.ZipFile(OUT / 'paper-blue-demo.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for path in (ROOT / 'examples').rglob('*'):
        if path.is_file():
            archive.write(path, Path('Paper Blue Demo/examples') / path.relative_to(ROOT / 'examples'))
    for name in ('theme.css', 'manifest.json'):
        archive.write(ROOT / name, 'Paper Blue Demo/.obsidian/themes/Paper Blue/' + name)
    archive.writestr('Paper Blue Demo/.obsidian/appearance.json', '{"cssTheme":"Paper Blue","baseFontSize":17}')
    archive.writestr('Paper Blue Demo/开始阅读.md', '# Paper Blue\n\n打开 [[examples/中文写作与阅读全量样稿]] 开始检查。\n\n请在 Obsidian 设置中开启缩减栏宽。')
print('Built docs/ and portable demo ZIP')
