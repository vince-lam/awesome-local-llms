import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Trending AI Repos",
  description: "Track daily star growth across curated AI/LLM GitHub repositories",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-white text-gray-900 antialiased">{children}</body>
    </html>
  );
}
