# Learning-AI
We will learn about Agents.
- How they are created?
- How they are interacted with LLM?

### Local llm setup

- Get gemm4 model suitable for your system configurations from here https://gemmai4.com/download/#picker

```bash
# macOS / Linux (Sort blobs by size to find the largest file)
ls -lh ~/.ollama/models/blobs/
```
```
# Replace <LARGE_BLOB_HASH> with the hash of the multi-GB file
cp ~/.ollama/models/blobs/sha256-<LARGE_BLOB_HASH> ./models/<your model name>.gguf
```

- Install llama server
```bash
brew install llama.cpp
```
- Verify the installation
```bash
llama-server --help
```
- Run LLM
```bash
llama-server -m ./models/<your model name>.gguf --port 8080 -c 4096 -ngl 99
```