import gradio as gr
from pdf_search import search_pdfs, save_results
import os

def process_search(pdf_files, search_string):
    print(f"接收到 {len(pdf_files)} 个PDF文件")
    for pdf_file in pdf_files:
        print(f"处理文件: {os.path.basename(pdf_file)}")
        print(f"临时文件路径: {pdf_file}")
    
    results = search_pdfs(pdf_files, search_string)
    output_file = "search_results.txt"
    save_results(results, output_file)
    return f"搜索完成。找到 {len(results)} 个匹配的PDF文件。结果已保存到 {output_file}"

iface = gr.Interface(
    fn=process_search,
    inputs=[
        gr.File(file_count="multiple", label="上传PDF文件"),
        gr.Textbox(label="搜索字符串")
    ],
    outputs=gr.Textbox(label="搜索结果"),
    title="PDF文件搜索工具",
    description="上传多个PDF文件并输入要搜索的字符串。结果将保存到本地文件中。"
)

if __name__ == "__main__":
    iface.launch()
