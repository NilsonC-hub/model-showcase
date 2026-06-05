# AI 建模 · 学生 3D 作品展示网页

把学生用 AI 生成的 3D 模型放进网页，做成可浏览、可分享的作品展示站。

## 关键文件与目录

```
AI 建模/
├── student-showcase-lite.html        # 登录页（NEXBOT 机器人 + 终端输入姓名）
├── model-showcase-ninja2.html        # 赛博忍者 MK-II — 黄歧        01/04
├── model-showcase-predator-new.html  # 外骨骼捕食者 — 杨琪帆        02/04
├── model-showcase-capsule.html       # 胶囊仓库 — 亢知行             03/04
├── model-showcase-jazz.html          # 变形金刚·爵士 — 朱梓彧       04/04
├── model-showcase-denied.html        # 陌生姓名 → ACCESS DENIED 页
├── model-viewer.min.js               # Google model-viewer 3.5.0（本地化）
├── draco/                            # Draco 解码器（本地化，解决 gstatic 不可达）
├── 模型GLB_optimized/web/            # 已压缩 GLB（Draco + WebP 2048）
│   ├── 赛博忍者2-黄歧.glb
│   ├── 外骨骼捕食者-杨琪帆.glb
│   ├── 胶囊仓库-亢知行.glb
│   └── 变形金刚-爵士-朱.glb
└── 模型GLB/学生作品/                  # 原始学生模型（待处理的 9 个）
```

## 已定的架构决策（别重走弯路）

### 整体架构：A 方案（跳转式）
- 登录页（Spline WebGL）和展示页（model-viewer）物理隔离，防双 Three.js 冲突
- 登录成功 → `window.location.href` 跳转对应 HTML → MODEL VAULT loading 屏 → 展示界面
- 展示页底部导航条 `← 上一件 / 01/04 / 下一件 →` 循环浏览 4 件作品

### 姓名→页面映射（在 student-showcase-lite.html 的 WORKS_MAP）
```js
const WORKS_MAP = {
  "黄歧":  "model-showcase-ninja2.html",
  "杨琪帆": "model-showcase-predator-new.html",
  "亢知行": "model-showcase-capsule.html",
  "朱梓彧": "model-showcase-jazz.html"
};
// 名字不在列表 → model-showcase-denied.html
```

### 设计系统（MODEL VAULT）
- **品牌名**：MODEL VAULT（不是 ARMORY NEXUS）
- **主色**：柠檬绿 `#caff38`（登录页同款）
- **强调色**：橙 `#ff8a1f`（作者名）
- **正文**：米白 `#f4f1e8`
- **Logo**：SVG 双层六边形 + chevron
- 不用 `<select>` 下拉（改用拨动开关）
- 灯光：有阴影 / 无阴影 两档拨动
- 3D 控制：ROTATE / ZOOM / RESET 三键
- 自动旋转默认关闭

### model-viewer 配置约定
```html
camera-controls rotation-per-second="6deg"
disable-pan interaction-prompt="none"
environment-image="neutral" exposure="1"
shadow-intensity="0.6" shadow-softness="0.8"
min-field-of-view="30deg" max-field-of-view="52deg"
min-camera-orbit="auto 75deg auto" max-camera-orbit="auto 75deg auto"
camera-orbit="-25deg 75deg auto"
```
- `min-field-of-view="30deg"`：限制手动最近缩放，防止纹理过近显示粗糙

### GLB 压缩规范（交给其他模型执行）
```bash
npx gltf-transform optimize <输入.glb> <输出.glb> \
  --compress draco \
  --texture-compress webp \
  --texture-size 2048 \
  --simplify true \
  --simplify-ratio 0.5~0.75
```
- **禁止** `--compress meshopt`（model-viewer 解不了）
- 输出放到 `模型GLB_optimized/web/`

## 部署

- **GitHub Pages**：https://nilsonc-hub.github.io/model-showcase/
- **仓库**：https://github.com/NilsonC-hub/model-showcase（公开，main 分支）
- **入口**：https://nilsonc-hub.github.io/model-showcase/student-showcase-lite.html
- 本地开发：`python -m http.server 8097`（在本目录起）
- **必须用 http 服务器**，不能 `file://` 打开（GLB 加载失败）
- 改完推送：`git add <文件> && git commit -m "..." && git push origin HEAD:main`

## 已知限制

- 登录页 Spline WebGL 在普通浏览器有卡顿，是固有成本，用户已接受
- GLB 纹理 2048px，不建议缩放太近（min-field-of-view 已限制）
- Zoom 按钮（30deg）和手动滚轮之间状态不同步，属已知行为，不修
- 多作者作品（如狮子铠甲 3 人）：任意一名学生输入自己姓名都能进入

## 本地运行

```
python -m http.server 8097
# 访问 http://127.0.0.1:8097/student-showcase-lite.html
```
