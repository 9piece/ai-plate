async function generate() {
  const prompt = document.getElementById("prompt").value;
  const res = await fetch("/api/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });

  const data = await res.json();
  if (data.image_url) {
    document.getElementById("image").src = data.image_url;
  } else {
    alert("生成失败：" + (data.error || "未知错误"));
  }
}