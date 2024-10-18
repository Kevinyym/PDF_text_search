# PDF文件搜索工具

这是一个简单而强大的PDF文件搜索工具，允许用户在多个PDF文件中搜索特定字符串。

## 功能特点

- 支持批量PDF文件上传
- 在PDF文件中搜索指定字符串
- 将搜索结果保存到本地文本文件
- 用户友好的图形界面

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/your-username/pdf-search-tool.git
   cd pdf-search-tool
   ```

2. 创建并激活虚拟环境（可选但推荐）：
   ```
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. 运行程序：
   ```
   python ui.py
   ```

2. 在浏览器中打开显示的本地URL（通常是 http://127.0.0.1:7860）

3. 使用界面上传PDF文件，输入搜索字符串，然后点击"提交"按钮

4. 查看搜索结果，结果也会保存在本地的 `search_results.txt` 文件中

## 文件结构

- `ui.py`: 包含Gradio用户界面的代码
- `pdf_search.py`: 包含PDF搜索和处理逻辑的主要功能
- `requirements.txt`: 列出项目依赖

## 依赖

- gradio
- PyPDF2

## 注意事项

- 确保您有足够的权限来读取上传的PDF文件和写入结果文件
- 大型PDF文件或大量文件可能需要较长的处理时间

## 贡献

欢迎提交问题报告和拉取请求。对于重大更改，请先开issue讨论您想要改变的内容。

## 许可证

[MIT](https://choosealicense.com/licenses/mit/)
