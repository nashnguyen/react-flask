import { useSalariesQuery } from '../../graphql/generated/graphql';

const Home = () => {
  const [salariesResult, _] = useSalariesQuery();
  const { data, fetching, error } = salariesResult;

  if (fetching) return <h3>Loading ....</h3>;

  if (error)
    return <h3 style={{ color: 'red' }}>Error: {JSON.stringify(error)}</h3>;

  return (
    <ul>
      {data?.salaries?.map(item => (
        <li>{item?.player}</li>
      ))}
    </ul>
  );
};

export default Home;
