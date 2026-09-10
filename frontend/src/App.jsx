import { useState } from "react";

import {
  GitBranch,
  Sparkles,
  Loader2,
  AlertCircle,
  Code2,
  FolderTree,
  Package,
  FileCode2,
  CheckCircle2,
  Layers3,
  ShieldCheck,
  Gauge,
} from "lucide-react";

import { analyzeRepository } from "./services/api";

function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAnalyze = async (e) => {
    e.preventDefault();

    if (!repoUrl.trim()) {
      setError("Please enter a GitHub repository URL.");
      return;
    }

    setLoading(true);
    setError("");
    setData(null);

    try {
      const result = await analyzeRepository(repoUrl.trim());

      console.log("Backend response:", result);

      setData(result);
    } catch (err) {
      console.error("Analysis error:", err);

      setError(
        err.message || "Something went wrong while analyzing the repository."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-zinc-950 text-white">
      <Navbar />

      <main className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <Hero
          repoUrl={repoUrl}
          setRepoUrl={setRepoUrl}
          handleAnalyze={handleAnalyze}
          loading={loading}
        />

        {error && <ErrorMessage message={error} />}

        {loading && <LoadingState />}

        {data && !loading && <AnalysisDashboard data={data} />}
      </main>
    </div>
  );
}

/* =========================================================
   NAVBAR
========================================================= */

function Navbar() {
  return (
    <nav className="border-b border-zinc-800 bg-zinc-950/80 backdrop-blur">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
        <div className="flex items-center gap-3">
          <div className="rounded-lg bg-white p-2 text-black">
            <GitBranch size={20} />
          </div>

          <span className="text-lg font-semibold">
            Repo<span className="text-zinc-400">Analyzer</span>
          </span>
        </div>

        <div className="flex items-center gap-2 text-sm text-zinc-400">
          <Sparkles size={16} />
          AI Powered
        </div>
      </div>
    </nav>
  );
}

/* =========================================================
   HERO
========================================================= */

function Hero({
  repoUrl,
  setRepoUrl,
  handleAnalyze,
  loading,
}) {
  return (
    <section className="mx-auto max-w-4xl py-16 text-center">
      <div className="mb-5 inline-flex items-center gap-2 rounded-full border border-zinc-800 bg-zinc-900 px-4 py-2 text-sm text-zinc-300">
        <Sparkles size={15} />
        AI-powered GitHub Repository Analysis
      </div>

      <h1 className="text-4xl font-bold tracking-tight sm:text-6xl">
        Understand any
        <span className="block text-zinc-400">
          GitHub repository.
        </span>
      </h1>

      <p className="mx-auto mt-5 max-w-2xl text-zinc-400">
        Analyze architecture, technologies, dependencies, project
        structure, and get an AI-powered review of the repository.
      </p>

      <form
        onSubmit={handleAnalyze}
        className="mx-auto mt-10 flex max-w-3xl flex-col gap-3 sm:flex-row"
      >
        <input
          type="url"
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)}
          placeholder="https://github.com/username/repository"
          className="h-14 flex-1 rounded-xl border border-zinc-700 bg-zinc-900 px-5 text-sm outline-none transition focus:border-zinc-400"
        />

        <button
          type="submit"
          disabled={loading}
          className="flex h-14 items-center justify-center gap-2 rounded-xl bg-white px-7 font-semibold text-black transition hover:bg-zinc-200 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {loading ? (
            <>
              <Loader2 size={18} className="animate-spin" />
              Analyzing
            </>
          ) : (
            <>
              <Sparkles size={18} />
              Analyze
            </>
          )}
        </button>
      </form>
    </section>
  );
}

/* =========================================================
   DASHBOARD
========================================================= */

function AnalysisDashboard({ data }) {
  const analysis = data?.analysis || {};
  const summary = data?.summary || {};
  const review = data?.review || {};

  return (
    <section className="space-y-6">

      {/* Repository Header */}
      <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-6">
        <div className="flex items-start justify-between gap-4">
          <div className="min-w-0">
            <p className="text-sm text-zinc-500">
              Repository
            </p>

            <h2 className="mt-1 break-words text-2xl font-bold">
              {analysis.project_name || "Repository Analysis"}
            </h2>

            <p className="mt-2 max-w-3xl text-zinc-400">
              {summary.purpose ||
                "AI-powered repository analysis"}
            </p>
          </div>

          <GitBranch
            size={30}
            className="shrink-0 text-zinc-500"
          />
        </div>
      </div>

      {/* Stats */}
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <StatCard
          icon={<Code2 size={22} />}
          title="Languages"
          value={getLength(
            analysis.programming_languages
          )}
        />

        <StatCard
          icon={<FileCode2 size={22} />}
          title="Files"
          value={analysis.total_files ?? 0}
        />

        <StatCard
          icon={<Package size={22} />}
          title="Dependencies"
          value={getLength(
            analysis.dependencies
          )}
        />

        <StatCard
          icon={<CheckCircle2 size={22} />}
          title="Review Score"
          value={
            review.overall_score !== undefined
              ? `${review.overall_score}/10`
              : "—"
          }
        />
      </div>

      {/* Project Information */}
      <div className="grid gap-6 lg:grid-cols-2">

        {/* Summary */}
        <AnalysisSection
          title="Project Summary"
          icon={<Sparkles size={20} />}
        >
          <div className="space-y-5">
            <div>
              <p className="mb-2 text-sm text-zinc-500">
                Purpose
              </p>

              <TextContent
                value={summary.purpose}
                fallback="No project purpose available."
              />
            </div>

            <div>
              <p className="mb-2 text-sm text-zinc-500">
                Summary
              </p>

              <TextContent
                value={summary.summary}
                fallback="No project summary available."
              />
            </div>
          </div>
        </AnalysisSection>

        {/* Project Details */}
        <AnalysisSection
          title="Project Information"
          icon={<Layers3 size={20} />}
        >
          <div className="grid gap-5 sm:grid-cols-2">

            <InfoItem
              label="Project Type"
              value={analysis.project_type}
            />

            <InfoItem
              label="Category"
              value={summary.project_category}
            />

            <InfoItem
              label="Root Directory"
              value={analysis.root_directory}
            />

            <InfoItem
              label="Total Files"
              value={analysis.total_files}
            />

            <InfoItem
              label="Total Folders"
              value={analysis.total_folders}
            />
          </div>
        </AnalysisSection>
      </div>

      {/* Key Features */}
      <ListSection
        title="Key Features"
        items={summary.key_features}
        icon={<Sparkles size={20} />}
      />

      {/* Tech Stack */}
      <ListSection
        title="Tech Stack"
        items={summary.tech_stack}
        icon={<Code2 size={20} />}
      />

      {/* Technical Details */}
      <div className="grid gap-6 lg:grid-cols-2">

        <ListSection
          title="Programming Languages"
          items={analysis.programming_languages}
          icon={<Code2 size={20} />}
        />

        <ListSection
          title="Frameworks"
          items={analysis.frameworks}
          icon={<Layers3 size={20} />}
        />

        <ListSection
          title="Dependencies"
          items={analysis.dependencies}
          icon={<Package size={20} />}
        />

        <ListSection
          title="Entry Points"
          items={analysis.entry_points}
          icon={<FileCode2 size={20} />}
        />

        <ListSection
          title="Important Files"
          items={analysis.important_files}
          icon={<FileCode2 size={20} />}
        />

        <ListSection
          title="Folder Structure"
          items={analysis.folder_structure}
          icon={<FolderTree size={20} />}
        />
      </div>

      {/* AI Review */}
      <ReviewSection review={review} />
    </section>
  );
}

/* =========================================================
   STAT CARD
========================================================= */

function StatCard({ icon, title, value }) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-5">
      <div className="mb-4 text-zinc-500">
        {icon}
      </div>

      <p className="text-sm text-zinc-500">
        {title}
      </p>

      <p className="mt-1 text-2xl font-bold">
        {value}
      </p>
    </div>
  );
}

/* =========================================================
   INFO ITEM
========================================================= */

function InfoItem({ label, value }) {
  return (
    <div>
      <p className="text-sm text-zinc-500">
        {label}
      </p>

      <p className="mt-1 break-words text-zinc-300">
        {value !== undefined &&
        value !== null &&
        value !== ""
          ? formatValue(value)
          : "Not available"}
      </p>
    </div>
  );
}

/* =========================================================
   ANALYSIS SECTION
========================================================= */

function AnalysisSection({
  title,
  icon,
  children,
}) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-6">
      <div className="mb-5 flex items-center gap-3">
        <div className="text-zinc-400">
          {icon}
        </div>

        <h3 className="text-lg font-semibold">
          {title}
        </h3>
      </div>

      {children}
    </div>
  );
}

/* =========================================================
   LIST SECTION
========================================================= */

function ListSection({
  title,
  items,
  icon = <FileCode2 size={20} />,
}) {
  const normalized = normalizeList(items);

  return (
    <AnalysisSection
      title={title}
      icon={icon}
    >
      {normalized.length === 0 ? (
        <p className="text-sm text-zinc-500">
          No data available.
        </p>
      ) : (
        <div className="flex flex-wrap gap-2">
          {normalized.map((item, index) => (
            <span
              key={`${item}-${index}`}
              className="break-all rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 text-sm text-zinc-300"
            >
              {item}
            </span>
          ))}
        </div>
      )}
    </AnalysisSection>
  );
}

/* =========================================================
   REVIEW SECTION
========================================================= */

function ReviewSection({ review }) {
  if (!review || Object.keys(review).length === 0) {
    return (
      <AnalysisSection
        title="AI Code Review"
        icon={<CheckCircle2 size={20} />}
      >
        <p className="text-zinc-500">
          No review available.
        </p>
      </AnalysisSection>
    );
  }

  return (
    <AnalysisSection
      title="AI Code Review"
      icon={<CheckCircle2 size={20} />}
    >
      <div className="space-y-6">

        {/* Score */}
        {review.overall_score !== undefined && (
          <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
            <div className="flex items-center gap-4">
              <CheckCircle2
                size={32}
                className="text-zinc-400"
              />

              <div>
                <p className="text-sm text-zinc-500">
                  Overall Score
                </p>

                <p className="text-4xl font-bold">
                  {review.overall_score}
                  <span className="text-lg text-zinc-500">
                    /10
                  </span>
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Quality Metrics */}
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">

          <ReviewMetric
            title="Code Quality"
            value={review.code_quality}
            icon={<Code2 size={20} />}
          />

          <ReviewMetric
            title="Documentation"
            value={review.documentation_quality}
            icon={<FileCode2 size={20} />}
          />

          <ReviewMetric
            title="Project Structure"
            value={review.project_structure}
            icon={<FolderTree size={20} />}
          />

          <ReviewMetric
            title="Scalability"
            value={review.scalability}
            icon={<Gauge size={20} />}
          />

          <ReviewMetric
            title="Maintainability"
            value={review.maintainability}
            icon={<Layers3 size={20} />}
          />
        </div>

        {/* Strengths */}
        <ReviewList
          title="Strengths"
          items={review.strengths}
        />

        {/* Weaknesses */}
        <ReviewList
          title="Weaknesses"
          items={review.weaknesses}
        />

        {/* Security */}
        <ReviewList
          title="Security Issues"
          items={review.security_issues}
          icon={<ShieldCheck size={20} />}
        />

        {/* Performance */}
        <ReviewList
          title="Performance Issues"
          items={review.performance_issues}
          icon={<Gauge size={20} />}
        />

        {/* Suggestions */}
        <ReviewList
          title="Suggestions"
          items={review.suggestions}
        />

        {/* Final Review */}
        {review.final_review && (
          <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
            <h4 className="mb-3 text-lg font-semibold">
              Final Review
            </h4>

            <p className="whitespace-pre-wrap leading-7 text-zinc-400">
              {review.final_review}
            </p>
          </div>
        )}
      </div>
    </AnalysisSection>
  );
}

/* =========================================================
   REVIEW METRIC
========================================================= */

function ReviewMetric({
  title,
  value,
  icon,
}) {
  return (
    <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">
      <div className="mb-3 flex items-center gap-2 text-zinc-500">
        {icon}

        <span className="text-sm">
          {title}
        </span>
      </div>

      <p className="whitespace-pre-wrap text-sm leading-6 text-zinc-300">
        {value || "Not available"}
      </p>
    </div>
  );
}

/* =========================================================
   REVIEW LIST
========================================================= */

function ReviewList({
  title,
  items,
  icon = <CheckCircle2 size={20} />,
}) {
  const normalized = normalizeList(items);

  return (
    <div>
      <div className="mb-3 flex items-center gap-2">
        <div className="text-zinc-500">
          {icon}
        </div>

        <h4 className="font-semibold">
          {title}
        </h4>
      </div>

      {normalized.length === 0 ? (
        <p className="text-sm text-zinc-500">
          None reported.
        </p>
      ) : (
        <ul className="space-y-2">
          {normalized.map((item, index) => (
            <li
              key={index}
              className="rounded-xl border border-zinc-800 bg-zinc-950 p-4 text-sm leading-6 text-zinc-400"
            >
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

/* =========================================================
   TEXT CONTENT
========================================================= */

function TextContent({
  value,
  fallback,
}) {
  if (
    value === undefined ||
    value === null ||
    value === ""
  ) {
    return (
      <p className="text-zinc-500">
        {fallback}
      </p>
    );
  }

  return (
    <p className="whitespace-pre-wrap leading-7 text-zinc-400">
      {formatValue(value)}
    </p>
  );
}

/* =========================================================
   FORMAT VALUE
========================================================= */

function formatValue(value) {
  if (typeof value === "string") {
    return value;
  }

  if (Array.isArray(value)) {
    return value.join(", ");
  }

  if (
    typeof value === "object" &&
    value !== null
  ) {
    return JSON.stringify(value, null, 2);
  }

  return String(value);
}

/* =========================================================
   NORMALIZE LIST
========================================================= */

function normalizeList(value) {
  if (!value) {
    return [];
  }

  if (Array.isArray(value)) {
    return value.map((item) => {
      if (typeof item === "string") {
        return item;
      }

      if (
        typeof item === "object" &&
        item !== null
      ) {
        return (
          item.name ||
          item.path ||
          item.language ||
          JSON.stringify(item)
        );
      }

      return String(item);
    });
  }

  if (typeof value === "object") {
    return Object.entries(value).map(
      ([key, val]) => `${key}: ${val}`
    );
  }

  return [String(value)];
}

/* =========================================================
   GET LENGTH
========================================================= */

function getLength(value) {
  if (!value) {
    return 0;
  }

  if (Array.isArray(value)) {
    return value.length;
  }

  if (typeof value === "object") {
    return Object.keys(value).length;
  }

  return "—";
}

/* =========================================================
   LOADING
========================================================= */

function LoadingState() {
  return (
    <div className="mx-auto max-w-4xl py-16 text-center">
      <Loader2
        size={42}
        className="mx-auto animate-spin text-zinc-500"
      />

      <h2 className="mt-5 text-xl font-semibold">
        Analyzing repository...
      </h2>

      <p className="mt-2 text-sm text-zinc-500">
        Cloning, indexing and analyzing the repository.
      </p>
    </div>
  );
}

/* =========================================================
   ERROR
========================================================= */

function ErrorMessage({ message }) {
  return (
    <div className="mx-auto mb-8 flex max-w-3xl items-start gap-3 rounded-xl border border-red-900/50 bg-red-950/30 p-4 text-red-300">
      <AlertCircle
        className="mt-0.5 shrink-0"
        size={20}
      />

      <div>
        <p className="font-semibold">
          Analysis failed
        </p>

        <p className="mt-1 break-words text-sm text-red-400">
          {message}
        </p>
      </div>
    </div>
  );
}

export default App;

