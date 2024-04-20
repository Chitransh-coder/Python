import git

# Kaggle repo
K_repo = git.Repo(path='d:/Projects/Kaggle')

# ML repo
ML_repo = git.Repo(path='d:/Projects/ML')

# Python repo
P_repo = git.Repo(path='d:/Projects/Python')

# TensorFlow repo
TF_repo = git.Repo(path='d:/Projects/Tensorflow')

# Fassal repo
F_repo = git.Repo(path='d:/Projects/Earth Engine App')

# MAUI repo
M_repo = git.Repo(path='d:/Projects/C#/MAUI')

# REST API repo
R_repo = git.Repo(path='d:/Projects/REST API/Study')

# Difference
diff_k = K_repo.git.diff(K_repo.head.commit.tree)
diff_ml = ML_repo.git.diff(ML_repo.head.commit.tree)
diff_p = P_repo.git.diff(P_repo.head.commit.tree)
diff_tf = TF_repo.git.diff(TF_repo.head.commit.tree)
diff_f = F_repo.git.diff(F_repo.head.commit.tree)
diff_m = M_repo.git.diff(M_repo.head.commit.tree)
diff_r = R_repo.git.diff(R_repo.head.commit.tree)

# Extract file names from the diff output
files_k = [line.split('\t')[1] for line in diff_k.split('\n') if line.startswith('diff --git')]
files_ml = [line.split('\t')[1] for line in diff_ml.split('\n') if line.startswith('diff --git')]
files_p = [line.split('\t')[1] for line in diff_p.split('\n') if line.startswith('diff --git')]
files_tf = [line.split('\t')[1] for line in diff_tf.split('\n') if line.startswith('diff --git')]
files_f = [line.split('\t')[1] for line in diff_f.split('\n') if line.startswith('diff --git')]
files_m = [line.split('\t')[1] for line in diff_m.split('\n') if line.startswith('diff --git')]
files_r = [line.split('\t')[1] for line in diff_r.split('\n') if line.startswith('diff --git')]

print("Files changed in Kaggle repo:", files_k)
print("Files changed in ML repo:", files_ml)
print("Files changed in Python repo:", files_p)
print("Files changed in TensorFlow repo:", files_tf)
print("Files changed in Fassal repo:", files_f)
print("Files changed in MAUI repo:", files_m)
print("Files changed in REST API repo:", files_r)
