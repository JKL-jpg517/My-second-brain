Coding agents are conversational AI models with access to tools such as reading/writing files, web search, and invoking shell commands.
## Key ideas of AI agents

LLM( consume tokens; e.g claude)
$y_{completion}=f(x_{prompt})$     model: a probability distributionof y,x
output$y^$
limited contex window
$\implies$ coverstional chat: 
- turn markers: enable long converstions
	$x_{1}$--->$y_{{1}}$
	$x_{2}$ ,and ($x_{1}$,$y_{{1}}$)---->$y_{2}$
Agent harness(只是个马鞍 e.g: claude code): interpret contex outputs and execute it on the machine(can feed the contents to the LLM again and again to execute; dispach requests to  tools and run them and feed the results to the LLM)
	e.g tools: bash, file read/write........


## Use cases
e.g help u commit on git!
- Implement new features
- fixing error
- Refactoring: rename and make files more in order/beautiful
- code review: see details
- code understanding
- can use it as a shell
- vibe coding

## Advanced agents
advanced features
- resuable prompts(like templates)
- Parallel agents: agents can do work in parallel(as long as it does not work in the same location); if work in the same location: use `git worrktree` and then merge the results


- MCPs: stands for _Model Context Protocol_, is an open protocol that you can use to connect your coding agents with tools. For your coding agents to use more tools
- context management:
	Clear: reduce message history and previous too calls
	
	rewind the conversation: undo steps in the converstion hisotry
	
	compaction:  if the  hitory is too long: compact can enable u to compress the history so that the conversation will not be too long
	llm.txt:  help simplify what the LLM reads from wibsites... 
>[!tip]-
> a proposed [standard](https://llmstxt.org/) location for a document meant for LLMs to use at inference time. Products (e.g., [cursor.com/llms.txt](https://cursor.com/llms.txt)), software libraries (e.g., [ai.pydantic.dev/llms.txt](https://ai.pydantic.dev/llms.txt)), and APIs (e.g., [apify.com/llms.txt](https://apify.com/llms.txt)) might have `llms.txt` files that are handy for development. Such documents are more information dense per token, and so they are more context-efficient than asking your coding agent to fetch and read an HTML page


AGENTS.md: equivilent to README.md to humans; a file that agents read!e.g., Claude Code looks for `CLAUDE.md`

Skills: sometimes AGENTS.md are too long; 
	_Skills_ add one level of indirection to avoid context bloat: you can provide the agent with a list of skills along with descriptions, and the agent can “open” the skill (load it into its context window) as desired
Subagents:  ==coding agents let you define subagents==(e.g form a subagent that filters the fetch of websites), which are agents for task-specific workflows

***CORE: Ease converstion length***



my llm
dclaude







