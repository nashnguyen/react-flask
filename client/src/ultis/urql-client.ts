import { cacheExchange, Client, dedupExchange, fetchExchange } from 'urql';

const client = new Client({
  url: 'http://localhost:5000/graphql',
  exchanges: [dedupExchange, cacheExchange, fetchExchange]
});

export default client;
