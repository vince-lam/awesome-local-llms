import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "(awesome local) llm repos",
  description: "Curated AI & LLM GitHub repositories tracked daily — sorted by stars, filterable by category",
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
