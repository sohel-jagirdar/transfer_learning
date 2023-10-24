# Transfer-learning-example

Transfer learning (TL) is a technique in machine learning (ML) in which knowledge learned from a task is re-used in order to boost performance on a related task. For example, for image classification, knowledge gained while learning to recognize cars could be applied when trying to recognize trucks.

Transfer of learning means the use of previously acquired knowledge and skills in new learning or problem-solving situations. Thereby similarities and analogies between previous and actual learning content and processes may play a crucial role

![classifiers-transfer-learning](https://github.com/sohel-jagirdar/transfer_learning/assets/52422511/20cbd98b-7f84-46d3-a9ba-199291e34df5)

## STEPS -
 
### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 06- commit and push the changes to the remote repository

```bash
git init
git remote add origin git@github.com:nunomazer/myrepository.git
git branch -M main
git add .
git commit -m 'feat: My first feature'
git push -u origin main


```
