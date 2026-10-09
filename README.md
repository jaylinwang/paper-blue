# Paper Blue

**一个专注优化中文体验的 Obsidian 主题。**

Paper Blue 围绕中文写作、中英文混排和长文阅读调整字体、行距、栏宽与内容层级，让日记、读书笔记和技术文档更容易书写与重读。默认使用 PingFang SC（苹方），支持浅色与深色，无需插件或远程字体，采用 **MIT 开源协议**。

A Chinese-first Obsidian theme for comfortable writing, mixed Chinese–English typography, and long-form reading. Free and open source under the MIT License.

[在线体验](https://jaylinwang.github.io/paper-blue/) · [下载主题与示例库](https://jaylinwang.github.io/paper-blue/paper-blue-demo.zip)

## 为中文体验做了哪些优化

- **中文字体优先**：正文与界面默认使用 PingFang SC，缺失时回退到系统字体、微软雅黑等；代码保留等宽字体。
- **适合长文的阅读节奏**：默认 17px 正文、1.8 倍行高与 720px 栏宽，配合段落留白，方便连续阅读和寻找下一行。
- **自然的中英文混排**：保持零字距与左对齐，使用严格的中文标点换行规则，让汉字、英文、数字和行内代码共同出现时更协调。主题不修改原文，也不自动插入中英文空格。
- **清晰的标题与强调**：通过字号、600 字重和间距区分内容层级，蓝色链接与柔和高亮便于识别。
- **更舒展的列表**：调整符号与正文之间的距离、列表缩进及嵌套间距，兼顾长条目折行后的可读性。
- **克制的引用与 Callout**：细引用线、浅色背景和轻边框；针对 Obsidian 1.14 修复 Callout 颜色，并减少实时预览中的重复外框与额外间距。
- **兼顾阅读与写作**：适配阅读视图与实时预览，源码模式保持紧凑；字号仍可通过 Obsidian 原生设置调整。

适合以中文为主的日记、知识笔记、读书记录，以及包含英文术语和代码的技术文档。实际字体与排版表现会随操作系统、字体安装情况及 Obsidian 设置变化。

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

## 反馈

欢迎通过 [Issues](https://github.com/jaylinwang/paper-blue/issues) 反馈中文排版问题。请提供 Obsidian 版本、操作系统、阅读或编辑模式，以及不含私人内容的最小 Markdown 样例。

## 开源协议

Paper Blue 使用 [MIT License](LICENSE)。主题源码、展示网页和本仓库原创示例按该协议开放；完整许可条款见根目录 `LICENSE` 文件。

Copyright (c) 2026 jaylinwang.
