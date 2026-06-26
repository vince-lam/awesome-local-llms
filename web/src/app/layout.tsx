import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "LLMRepos — Open-Source LLM Projects for Builders",
  description: "Discover the best open-source LLM projects: AI agents, RAG tools, inference engines, eval frameworks, coding agents, and AI devtools — curated for builders, founders, and researchers.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        {/* Prevent dark-mode flash on load */}
        <script
          dangerouslySetInnerHTML={{
            __html: `(function(){try{var m=localStorage.getItem('theme');if(m==='dark'||(m!=='light'&&window.matchMedia('(prefers-color-scheme: dark)').matches)){document.documentElement.classList.add('dark')}}catch(e){}})()`,
          }}
        />
      </head>
      <body className="bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100 antialiased transition-colors">
        {children}
      </body>
    </html>
  );
}
