hf jobs uv run \
    --flavor l4x1 \
    --image vllm/vllm-openai \
    -s HF_TOKEN=\
    https://huggingface.co/datasets/freddyaboulton/hf-cli-jobs-uv-run-scripts/resolve/main/02_classify.py \
    freddyaboulton/affordable-housing-conversations \
    freddyaboulton/affordable-housing-conversations-classified \
    --model-id HuggingFaceTB/SmolLM3-3B \
    --temperature 0.7 \
    --messages-column messages \
    --output-column classification \