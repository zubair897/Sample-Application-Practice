import subprocess
import time

def run(cmd):
    print(f"▶ {cmd}")
    return subprocess.call(cmd, shell=True)

def git_pull():
    run("git pull origin main")

def build():
    run("docker build -t ai-app .")

def load_to_k8s():
    run("minikube image load ai-app")

def deploy():
    run("kubectl apply -f k8s/")
    run("kubectl rollout restart deployment ai-app")

def health_check():
    time.sleep(5)
    return run("curl -f http://localhost:3000") == 0

def rollback():
    print("🔁 Rolling back...")
    run("kubectl rollout undo deployment ai-app")

def pipeline():
    git_pull()
    build()
    load_to_k8s()
    deploy()

    if health_check():
        print("✅ Deployment successful")
    else:
        print("❌ Deployment failed")
        rollback()

if __name__ == "__main__":
    pipeline()
