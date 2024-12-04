import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import Component from "./Component.tsx";
import "./index.css";

createRoot(document.getElementById("counter")!).render(
  <StrictMode>
    <Component />
  </StrictMode>
);
