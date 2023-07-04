export default function ProjectsProvider({ children }) {
  // const project = useFetch(url)
  return (
    <ProjectsProvider.Provider value={ { teste: true } }>
      <div>
        {children}
      </div>
    </ProjectsProvider.Provider>
  );
}

ProjectsProvider.propTypes = {
  children: PropTypes.node.isRequired,
};
