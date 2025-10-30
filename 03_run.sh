hf jobs uv run \
    --flavor l4x1 \
    --image vllm/vllm-openai \
    --secrets-file secrets.txt \
    https://huggingface.co/datasets/gnovoa26/hfscripts/resolve/main/classify.py \
    --max-model-len 45000 \
    princeton-hf-workshop/affordable-housing-conversations \
    princeton-hf-workshop/affordable-housing-conversations-classified \
    --model-id Qwen/Qwen3-VL-4B-Instruct \
    --temperature 0.7 \
    --messages-column messages \
    --output-column classification