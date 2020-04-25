import os
data = {
    ".c": "c语言",
    ".cpp": "c++",
    ".py": "python",
    ".pyw": "python",
    ".css": "css",
    ".html": "html",
    ".vue": "vue",
    ".go": "golang",
    ".json": "Json",
    ".js": "Javascript",
    ".dart": "Dart"
}
linecount, charcount, filecount = {}, {}, 0
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        ext = '.'+name.split('.')[-1]
        path = os.path.join(root, name)
        if ext in data.keys():
            filecount += 1
            print("发现代码:", path)
            lang = data[ext]
            if not linecount.get(lang):
                linecount[lang] = 0
            if not charcount.get(lang):
                charcount[lang] = 0
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    code = f.read()
            except:
                try:
                    with open(path, 'r', encoding='gbk') as f:
                        code = f.read()
                except:
                    continue
            linecount[lang] += len(code.split('\n'))
            charcount[lang] += len(code)
print("共发现", filecount, "个文件")
print("其中明细如下:")
for i in linecount.keys():
    print('\t', i, linecount[i], '行, ', charcount[i], '个字符')

input()
