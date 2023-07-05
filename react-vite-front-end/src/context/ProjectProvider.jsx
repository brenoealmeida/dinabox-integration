import { useMemo, useState } from 'react';
import ProjectsContext from './ProjectsContext';

export default function ProjectProvider({ children }) {
  const [user, setUser] = useState({
    email: '',
    password: '',
  });

  const contextValue = useMemo(() => ({
    user,
    setUser,
  }), [
    user,
    setUser,
  ]);

  return (
    <ProjectsContext.Provider value={ contextValue }>
      {children}
    </ProjectsContext.Provider>
  );
}

ProjectProvider.propTypes = {
  children: PropTypes.node.isRequired,
};
