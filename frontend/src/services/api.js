const API_URL ="http://127.0.0.1:8000";

export async function analyzeRepository(url) {
  const response = await fetch(`${API_URL}/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url,
    }),
  });

  const text = await response.text();

  console.log("API STATUS:", response.status);
  console.log("API CONTENT TYPE:", response.headers.get("content-type"));
  console.log("API RAW RESPONSE:", text);

  if (!response.ok) {
    let message = `Request failed with status ${response.status}`;

    try {
      const errorData = JSON.parse(text);

      if (errorData.detail) {
        message =
          typeof errorData.detail === "string"
            ? errorData.detail
            : JSON.stringify(errorData.detail);
      }
    } catch {
      if (text) {
        message = text;
      }
    }

    throw new Error(message);
  }

  if (!text.trim()) {
    throw new Error(
      "Backend returned an empty response."
    );
  }

  try {
    return JSON.parse(text);
  } catch (error) {
    console.error("Invalid JSON from backend:", text);

    throw new Error(
      "Backend returned invalid JSON."
    );
  }
}