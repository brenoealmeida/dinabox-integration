import { Route, Routes } from 'react-router-dom';
// @ts-ignore
import ProjectProvider from './context/ProjectProvider';
import Login from './pages/Login';
import Pricing from './pages/Pricing';
import Proposal from './pages/Proposal';

function App() {
  return (
    <ProjectProvider>
      <Routes>
        <Route path="/" element={ <Login /> } />
        <Route path="/pricing" element={ <Pricing /> } />
        <Route path="/proposal" element={ <Proposal /> } />
      </Routes>
    </ProjectProvider>
  );
}

export default App;
