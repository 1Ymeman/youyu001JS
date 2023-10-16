import tkinter as tk
import execjs
import pyperclip  # 导入 pyperclip 库
#web_scraper
# 创建一个Tkinter窗口
window = tk.Tk()
window.title("JavaScript Execution")

# 创建输入框的标签
input_label = tk.Label(window, text="输入 JavaScript 代码:")
input_label.pack()

# 创建一个按钮，点击后清空输入框内容
def clear_input():
    input_text.delete("1.0", "end")

# 创建一个按钮，点击后清空输入框内容
clear_input_button = tk.Button(window, text="清空输入框内容", command=clear_input)
clear_input_button.pack()


# 创建一个文本框用于接收用户输入
input_text = tk.Text(window, height=10, width=40)
input_text.pack()

# 创建输出框的标签
output_label = tk.Label(window, text="执行结果:")
output_label.pack()

# 创建一个按钮，点击后将剪切板内容复制到输入框
def copy_clipboard_to_input():
    clipboard_content = pyperclip.paste()
    input_text.delete("1.0", "end")
    input_text.insert("1.0", clipboard_content)

copy_to_input_button = tk.Button(window, text="将剪切板内容复制到输入框", command=copy_clipboard_to_input)
copy_to_input_button.pack()

# 创建一个按钮，点击后执行JavaScript代码
# 创建一个按钮，点击后执行JavaScript代码
def execute_js():
    # 从文本框中获取用户输入的JavaScript代码
    user_input = input_text.get("1.0", "end-1c")

    # 提取JavaScript代码
    js = user_input.splitlines()[5][5:-1]

    try:
        # 使用execjs库执行JavaScript代码
        result = execjs.eval(js)

        # 在每个分号后添加换行符
        result = result.replace(';', ';\n')

        # 清空输出文本框
        output_text.delete("1.0", "end")
        # 在输出文本框中显示结果
        output_text.insert("1.0", result)

        # 复制输出框内容到剪切板
        pyperclip.copy(result)
    except Exception as e:
        # 如果发生异常，显示错误消息
        output_text.delete("1.0", "end")
        output_text.insert("1.0", str(e))

# 创建一个按钮，点击后执行JavaScript代码
execute_button = tk.Button(window, text="执行 JavaScript", command=execute_js)
execute_button.pack()


# 创建一个文本框用于显示输出
output_text = tk.Text(window, height=20, width=60, wrap=tk.WORD)  # 使用 tk.WORD 进行自动换行
output_text.pack()

# 创建一个按钮，点击后将输出框内容复制到剪切板
def copy_output_to_clipboard():
    output_content = output_text.get("1.0", "end-1c")
    pyperclip.copy(output_content)

copy_to_clipboard_button = tk.Button(window, text="将输出框内容复制到剪切板", command=copy_output_to_clipboard)
copy_to_clipboard_button.pack()

# 启动Tkinter主循环
window.mainloop()
