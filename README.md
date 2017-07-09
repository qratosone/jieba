# jieba
NLP demo using jieba

### 使用方法

```bash
python main.py [-h] [-r] [-o OUTPUT] [-f] [-l] [-p] filename
```
`filename`为输入文件名
`-o OUTPUT`为输出文件名，目前支持输出文本格式
`-r`为处理目录——开启该参数，会将`filename`作为目录处理，递归地处理目录下的所有文件与子目录
`-f -l -p`分别对应jieba提供的统计词频，切词，关键词抽取功能，可以叠加使用