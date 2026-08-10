const API_URL = "http://127.0.0.1:6600";


// =========================================================
// HELPERS
// =========================================================

function showError(message) {

    const error = document.getElementById("error");

    error.textContent = message;

    error.classList.remove("hidden");
}


function hideError() {

    document
        .getElementById("error")
        .classList.add("hidden");
}


function setLoading(status) {

    const loading =
        document.getElementById("loading");

    if (status) {

        loading.classList.remove("hidden");

    } else {

        loading.classList.add("hidden");

    }
}


function createList(elementId, items) {

    const element =
        document.getElementById(elementId);

    element.innerHTML = "";

    if (!items || items.length === 0) {

        element.innerHTML =
            "<li>No information available.</li>";

        return;
    }


    items.forEach(item => {

        const li =
            document.createElement("li");

        li.textContent = item;

        element.appendChild(li);

    });
}


function createTags(elementId, items) {

    const element =
        document.getElementById(elementId);

    element.innerHTML = "";

    if (!items || items.length === 0) {

        element.textContent =
            "No information available.";

        return;
    }


    items.forEach(item => {

        const tag =
            document.createElement("span");

        tag.className = "tag";

        tag.textContent = item;

        element.appendChild(tag);

    });
}


// =========================================================
// ANALYZE REPOSITORY
// =========================================================

async function analyzeRepository() {

    const repoUrl =
        document
            .getElementById("repoUrl")
            .value
            .trim();


    if (!repoUrl) {

        showError(
            "Please enter a GitHub repository URL."
        );

        return;
    }


    hideError();

    setLoading(true);


    const button =
        document.getElementById("analyzeBtn");

    button.disabled = true;

    button.textContent =
        "Analyzing...";


    try {

        const response =
            await fetch(
                `${API_URL}/analyze`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        url: repoUrl
                    })
                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Repository analysis failed."
            );

        }


        displayAnalysis(data);


    } catch (error) {

        showError(
            error.message
        );

    } finally {

        setLoading(false);

        button.disabled = false;

        button.textContent =
            "Analyze Repository";

    }

}


// =========================================================
// DISPLAY ANALYSIS
// =========================================================

function displayAnalysis(data) {

    const analysis =
        data.analysis;

    const summary =
        data.summary;

    const review =
        data.review;


    // -----------------------------------------------------
    // Dashboard Metrics
    // -----------------------------------------------------

    document
        .getElementById("projectName")
        .textContent =
        analysis.project_name || "-";


    document
        .getElementById("totalFiles")
        .textContent =
        analysis.total_files ?? "-";


    document
        .getElementById("totalFolders")
        .textContent =
        analysis.total_folders ?? "-";


    document
        .getElementById("projectType")
        .textContent =
        analysis.project_type || "-";


    // -----------------------------------------------------
    // Analysis
    // -----------------------------------------------------

    createTags(
        "languages",
        analysis.programming_languages
    );


    createTags(
        "frameworks",
        analysis.frameworks
    );


    createList(
        "dependencies",
        analysis.dependencies
    );


    createList(
        "entryPoints",
        analysis.entry_points
    );


    createList(
        "importantFiles",
        analysis.important_files
    );


    document
        .getElementById("folderStructure")
        .textContent =
        (analysis.folder_structure || [])
            .join("\n");


    // -----------------------------------------------------
    // Summary
    // -----------------------------------------------------

    document
        .getElementById("purpose")
        .textContent =
        summary.purpose || "";


    document
        .getElementById("projectCategory")
        .textContent =
        summary.project_category || "";


    createList(
        "features",
        summary.key_features
    );


    createTags(
        "techStack",
        summary.tech_stack
    );


    document
        .getElementById("summaryText")
        .textContent =
        summary.summary || "";


    // -----------------------------------------------------
    // Review
    // -----------------------------------------------------

    document
        .getElementById("score")
        .textContent =
        `${review.overall_score}/10`;


    createList(
        "strengths",
        review.strengths
    );


    createList(
        "weaknesses",
        review.weaknesses
    );


    document
        .getElementById("codeQuality")
        .textContent =
        review.code_quality || "";


    document
        .getElementById("documentation")
        .textContent =
        review.documentation_quality || "";


    document
        .getElementById("structure")
        .textContent =
        review.project_structure || "";


    document
        .getElementById("scalability")
        .textContent =
        review.scalability || "";


    document
        .getElementById("maintainability")
        .textContent =
        review.maintainability || "";


    createList(
        "security",
        review.security_issues
    );


    createList(
        "performance",
        review.performance_issues
    );


    createList(
        "suggestions",
        review.suggestions
    );


    document
        .getElementById("finalReview")
        .textContent =
        review.final_review || "";


    // -----------------------------------------------------
    // Show Dashboard
    // -----------------------------------------------------

    document
        .getElementById("dashboard")
        .classList.remove("hidden");


    // Automatically open Analysis tab

    openTab(
        "analysis",
        document.querySelector(".tab")
    );

}


// =========================================================
// TABS
// =========================================================

function openTab(
    tabName,
    button
) {

    const contents =
        document.querySelectorAll(
            ".tab-content"
        );


    const tabs =
        document.querySelectorAll(
            ".tab"
        );


    contents.forEach(content => {

        content.classList.remove(
            "active"
        );

    });


    tabs.forEach(tab => {

        tab.classList.remove(
            "active"
        );

    });


    document
        .getElementById(tabName)
        .classList.add("active");


    if (button) {

        button.classList.add("active");

    }

}


// =========================================================
// CHAT
// =========================================================

async function sendMessage() {

    const input =
        document.getElementById("chatInput");


    const question =
        input.value.trim();


    if (!question) {

        return;

    }


    addMessage(
        question,
        "user"
    );


    input.value = "";


    try {

        const response =
            await fetch(
                `${API_URL}/chat`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        query: question
                    })
                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Chat request failed."
            );

        }


        addMessage(
            data.response,
            "bot"
        );


    } catch (error) {

        addMessage(
            `Error: ${error.message}`,
            "bot"
        );

    }

}


// =========================================================
// ADD CHAT MESSAGE
// =========================================================

function addMessage(
    message,
    type
) {

    const container =
        document.getElementById(
            "chatMessages"
        );


    const div =
        document.createElement("div");


    div.classList.add(
        "message"
    );


    if (type === "user") {

        div.classList.add(
            "user-message"
        );

    } else {

        div.classList.add(
            "bot-message"
        );

    }


    div.textContent =
        message;


    container.appendChild(div);


    container.scrollTop =
        container.scrollHeight;

}


// =========================================================
// ENTER KEY FOR CHAT
// =========================================================

document
    .getElementById("chatInput")
    .addEventListener(
        "keydown",
        function(event) {

            if (event.key === "Enter") {

                sendMessage();

            }

        }
    );