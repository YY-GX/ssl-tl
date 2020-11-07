#!/usr/bin/env bash
nvidia-smi
pip install -r requirements.txt 
# conda env create -f ../environment.yml
# source activate yxy
pip install --upgrade torch torchvision  

# conda env create -f ../environment.yml
# source activate yxy
# python train_pneu.py --transfer-resume '../paths/inat/ssl/1/best.pth.tar' --checkpoint-path '../checkpoints_target/inat/ssl/1/'  --pretrained 'MoCo'

python train_pneu_yxy.py --seed 1 --transfer-resume '../paths/inat/ssl/1/best.pth.tar' --checkpoint-path '../checkpoints_target/inat/ssl/1/1/'  --pretrained 'MoCo'

python train_pneu_yxy.py --seed 10 --transfer-resume '../paths/inat/ssl/1/best.pth.tar' --checkpoint-path '../checkpoints_target/inat/ssl/1/10/'  --pretrained 'MoCo'

python train_pneu_yxy.py --seed 1024 --transfer-resume '../paths/inat/ssl/1/best.pth.tar' --checkpoint-path '../checkpoints_target/inat/ssl/1/1024/'  --pretrained 'MoCo'