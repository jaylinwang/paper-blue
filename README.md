# Paper Blue

为中文写作与长文阅读设计的 Obsidian 主题。默认使用 PingFang SC，支持浅色与深色，无需插件或远程字体。

[在线体验](https://jaylinwang.github.io/paper-blue/) · [下载主题与示例库](https://jaylinwang.github.io/paper-blue/paper-blue-demo.zip)

## 目录

- `theme.css`、`manifest.json`：主题的唯一维护源。
- `examples/`：完整中文样稿、关联笔记、Bases、Canvas、图片、音视频及 PDF。内容均为测试材料。
- `site/`：在线样式展示页源文件，直接使用同一份主题 CSS。
- `scripts/build.py`：生成 `docs/` 网页、附件和便携示例库 ZIP。
- `docs/`：GitHub Pages 发布目录；由构建脚本生成，请勿直接修改。

## 安装与检查

需要 Obsidian **1.14.0 或更新版本**。

下载示例库 ZIP，解压后将 `Paper Blue Demo` 文件夹作为库打开，即可检查全部原生内容。也可将根目录的 `theme.css` 与 `manifest.json` 复制到现有库的 `.obsidian/themes/Paper Blue/`，在「设置 → 外观」启用。

建议开启「编辑器 → 缩减栏宽」，字号 17px 或 18px。主题默认正文与界面优先使用苹方；原生外观设置中的自定义字体会覆盖主题默认值。未安装苹方时回退到本地系统字体，主题不分发字体。

## 本地预览与发布

```sh
python3 scripts/build.py
python3 -m http.server 8080 --directory docs
```

打开 http://localhost:8080。修改主题或示例后重新构建，并将源码及 `docs/` 一起提交。GitHub Pages 使用 `main` 分支的 `/docs` 发布，无需 Node.js 或构建依赖。

网页提供颜色模式、字号、宽度切换，以及常见 Markdown 的阅读排版；它不是 Obsidian 编辑器。实时预览、双链、数学公式、Mermaid、Bases、Canvas 等应在 Obsidian 示例库里检查。尚未提交 Obsidian 社区主题目录。

## 设计与兼容

17px 默认正文、1.8 倍行高、720px 栏宽，零字距、蓝色链接、细引用线与柔和 Callout。2.1 修复 Obsidian 1.14 Callout 颜色变量兼容，移除实时预览重复外框和额外上下间距。

主要在 macOS / Obsidian 1.14.4 浅色阅读视图与实时预览验证。复杂嵌套列表在两种视图中仍可能有缩进差异；移动端及输入法交互尚未全面回归。

中文排版参考 [Apple 中国官网](https://www.apple.com.cn/)，针对笔记和长文重新设计。本项目与 Apple、Obsidian 无隶属关系，不下载或分发其字体与网站素材。

## 反馈与许可

欢迎通过 [Issues](https://github.com/jaylinwang/paper-blue/issues) 提交最小复现样例，请勿包含私人笔记内容。采用 [MIT License](LICENSE)。
