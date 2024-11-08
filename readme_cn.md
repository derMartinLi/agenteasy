# Agenteasy

Agenteasy 是一个人工智能库，旨在简化人类创建和管理人工智能应用的过程。它极易使用和扩展，减轻了开发人工智能解决方案通常伴随的负担。

创建 Agenteasy 的动机源于市场上现有人工智能工具的复杂性和扩展难度。这些工具要么过于复杂，要么难以为特定需求定制。Agenteasy 旨在通过提供一个简化而强大的基础，作为更高级人工智能功能的基础，来解决这些问题。

使用 Agenteasy，开发者可以利用 ai_template 语法来定义人工智能流程的模板。这种语法使用基本格式：System:xxx||User:xxx||Assistant:xxx||。关键词 System、User 和 Assistant 表示消息流中的不同角色，它们可以以任何顺序出现。ai_template 解析这些关键词和 || 之间的文本，以生成结构化消息。

## 特性
**简单性**：直观的设计和界面使其适合初学者和有经验的开发者。

**可扩展性**：轻松扩展库以满足特定项目需求。

**效率**：简化构建人工智能应用的过程，让开发者专注于应用逻辑而非技术细节。

## 安装
要使用 agenteasy 库，你首先需要安装它。假设它在 PyPI 上可用，你可以通过 pip 安装它：
```
pip install agenteasy
```

## 基本使用示例
让我们通过一个简单的例子来了解如何使用 Agenteasy 进行语言翻译：
``` python
# 从 agenteasy 导入必要的模块
import agenteasy
from agenteasy.promptools import ai_template

# 定义人工智能任务的模板
@ai_template
def plain_translate(*, content: str, target: str, source: str | None = None):
    """System: {% if source is defined %}源语言: {{source}}{% endif %}
    任务：将用户提供的内容翻译成 {{target}}。只返回翻译结果。||
    用户：{{content}}"""
    ...

# 使用 GPT 模型初始化人工智能代理
agent = agenteasy.AIAgent(agenteasy.GPT())

# 生成翻译
print(
    agent.generate(
        messages=plain_translate(
            content="这是一个平凡的早晨",
            target="English",
        )
    )
)
```
### 解释
**定义翻译任务**：使用 @ai_template 装饰器定义将给定内容翻译成目标语言的主要任务。这利用了 ai_template 语法进行结构化通信。

**创建人工智能代理**：AIAgent 使用语言模型（本例中为 GPT）初始化以执行操作。

**调用翻译**：在代理上调用 generate 方法执行翻译，并打印结果。

### 扩展 Agenteasy
Agenteasy 的设计允许开发者在其核心功能上进行构建。创建新模板或修改现有模板以适应你的应用的独特需求。

## 贡献
欢迎对 Agenteasy 做出贡献！如果你遇到任何问题或有改进建议，请在项目的 GitHub 仓库上创建一个拉取请求或打开一个 issue。

## 许可证
Agenteasy 根据 GNU 通用公共许可证第 3 版（LGPLv3）授权。更多信息，请参见 LICENSE 文件。这意味着 Agenteasy 可以自由使用、修改和在开源项目中重新分发，根据 LGPLv3 的条款。

Agenteasy 使构建人工智能应用变得轻松，赋予开发者专注于最重要的事情——创造智能、变革性的解决方案。
