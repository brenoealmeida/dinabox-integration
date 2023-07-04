import Forms from './components/Forms';
import Header from './components/Header';
import ProjectProvider from './context/ProjectProvider';

function App() {
  return (
    <ProjectProvider>
      <Header />
      <Forms />
    </ProjectProvider>
  );
}

export default App;
