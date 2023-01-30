import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Auth from "./components/auth/Auth";
import Workspace from "./components/workspace/Workspace";
import { AuthType } from "./types/authtype";

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Workspace />} />
          <Route path="/signin" element={<Auth type={AuthType.SignIn} />} />
          <Route path="/signup" element={<Auth type={AuthType.SignUp} />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
